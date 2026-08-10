import argparse
import os
import json
import subprocess
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def add_bottom_border(paragraph, border_type="single", sz="18", space="1", color="0070c0"):
    """Adds a bottom border to a paragraph using OpenXML."""
    pPr = paragraph._p.get_or_add_pPr()
    pBdr = parse_xml(r'<w:pBdr %s><w:bottom w:val="%s" w:sz="%s" w:space="%s" w:color="%s"/></w:pBdr>' % (nsdecls('w'), border_type, sz, space, color))
    pPr.append(pBdr)

def add_hyperlink(paragraph, url, text, color="0000ff", underline=True):
    """Adds a real hyperlink element to a paragraph."""
    part = paragraph.part
    r_id = part.relate_to(url, docx.opc.constants.RELATIONSHIP_TYPE.HYPERLINK, is_external=True)

    hyperlink = parse_xml(r'<w:hyperlink %s xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" r:id="%s"/>' % (nsdecls('w'), r_id))
    new_run = parse_xml(r'<w:r %s/>' % nsdecls('w'))
    text_node = parse_xml(r'<w:t %s>%s</w:t>' % (nsdecls('w'), text))
    new_run.append(text_node)

    rPr = parse_xml(r'<w:rPr %s/>' % nsdecls('w'))
    rFonts = parse_xml(r'<w:rFonts %s w:ascii="Calibri" w:hAnsi="Calibri" w:cs="Calibri"/>' % nsdecls('w'))
    rPr.append(rFonts)

    b = parse_xml(r'<w:b %s w:val="1"/>' % nsdecls('w'))
    rPr.append(b)

    sz = parse_xml(r'<w:sz %s w:val="20"/>' % nsdecls('w'))
    rPr.append(sz)

    c = parse_xml(r'<w:color %s w:val="%s"/>' % (nsdecls('w'), color))
    rPr.append(c)

    if underline:
        u = parse_xml(r'<w:u %s w:val="single"/>' % nsdecls('w'))
        rPr.append(u)

    new_run.append(rPr)
    hyperlink.append(new_run)
    paragraph._p.append(hyperlink)
    return hyperlink

def clean_project_name(name, company_name):
    """Strips the company name prefix from the project title."""
    for sep in [" — ", " – ", " - ", " | "]:
        if sep in name:
            parts = name.split(sep, 1)
            company_words = set(w.lower() for w in company_name.split() if len(w) > 2)
            left_words = set(w.lower() for w in parts[0].split())
            if company_words.intersection(left_words):
                return parts[1].strip()
    
    clean = name
    if company_name.lower() in clean.lower():
        idx = clean.lower().find(company_name.lower())
        clean = clean[idx + len(company_name):].strip()
        clean = clean.lstrip(" -–—|:").strip()
    return clean

def generate_resume(data_path, output_path):
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    doc = Document()

    # Section Setup - Page margins & size (A4)
    section = doc.sections[0]
    section.page_width = Inches(8.27)
    section.page_height = Inches(11.69)
    section.top_margin = Inches(0.375)
    section.bottom_margin = Inches(0.20)
    section.left_margin = Inches(0.394)
    section.right_margin = Inches(0.487)

    # Styles Setup (Calibri, 10pt standard)
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Calibri'
    font.size = Pt(10)

    # 1. Document Header (Name and Role)
    p_header = doc.add_paragraph()
    p_header.paragraph_format.space_before = Pt(0)
    p_header.paragraph_format.space_after = Pt(0)
    p_header.paragraph_format.line_spacing = 1.0

    run_name = p_header.add_run(data["name"].upper() + " – ")
    run_name.font.name = 'Calibri'
    run_name.font.size = Pt(18)
    run_name.bold = True

    run_role = p_header.add_run(data["role"].upper())
    run_role.font.name = 'Calibri'
    run_role.font.size = Pt(14)
    run_role.bold = True

    add_bottom_border(p_header, "dotted", "4", "1", "00000a")

    # Spacing paragraph
    p_space = doc.add_paragraph()
    p_space.paragraph_format.space_before = Pt(0)
    p_space.paragraph_format.space_after = Pt(2)
    p_space.paragraph_format.line_spacing = 1.0

    # 2. Contact Details
    p_contact = doc.add_paragraph()
    p_contact.paragraph_format.space_before = Pt(0)
    p_contact.paragraph_format.space_after = Pt(4)
    p_contact.paragraph_format.line_spacing = 1.0

    contact_str = f"☎: {data['phone']} | 🖂: {data['email']} | 📍 {data['location']} | "
    run_contact = p_contact.add_run(contact_str)
    run_contact.font.name = 'Calibri'
    run_contact.font.size = Pt(10)
    run_contact.font.bold = True
    run_contact.font.color.rgb = RGBColor(0x00, 0x70, 0xC0) # 0070c0 blue

    add_hyperlink(p_contact, data["linkedin"], "LinkedIn", color="0000ff", underline=True)
    add_bottom_border(p_contact, "dotted", "4", "1", "00000a")

    # Spacing paragraph
    p_space2 = doc.add_paragraph()
    p_space2.paragraph_format.space_before = Pt(0)
    p_space2.paragraph_format.space_after = Pt(2)
    p_space2.paragraph_format.line_spacing = 1.0

    # 3. Professional Summary
    p_summary = doc.add_paragraph()
    p_summary.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_summary.paragraph_format.space_before = Pt(0)
    p_summary.paragraph_format.space_after = Pt(4)
    p_summary.paragraph_format.line_spacing = 1.1
    run_summary = p_summary.add_run(data["summary"])
    run_summary.font.name = 'Calibri'
    run_summary.font.size = Pt(10)

    def add_section_heading(text):
        p_head = doc.add_paragraph()
        p_head.paragraph_format.space_before = Pt(8)
        p_head.paragraph_format.space_after = Pt(3)
        p_head.paragraph_format.line_spacing = 1.1
        run_head = p_head.add_run(text.upper())
        run_head.font.name = 'Calibri'
        run_head.font.size = Pt(11)
        run_head.bold = True
        run_head.font.color.rgb = RGBColor(0x00, 0x70, 0xC0)
        add_bottom_border(p_head, "single", "18", "1", "0070c0")
        return p_head

    # 4. Key Skills
    add_section_heading("KEY SKILLS")
    p_skills = doc.add_paragraph()
    p_skills.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_skills.paragraph_format.space_before = Pt(0)
    p_skills.paragraph_format.space_after = Pt(4)
    p_skills.paragraph_format.line_spacing = 1.1
    skills_text = " | ".join(data["skills"])
    run_skills = p_skills.add_run(skills_text)
    run_skills.font.name = 'Calibri'
    run_skills.font.size = Pt(10)

    # 5. Tools & Technologies
    add_section_heading("TOOLS & TECHNOLOGIES")
    for key, val in data["tools"].items():
        p_tool = doc.add_paragraph()
        p_tool.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p_tool.paragraph_format.space_before = Pt(0)
        p_tool.paragraph_format.space_after = Pt(2)
        p_tool.paragraph_format.line_spacing = 1.1

        run_cat = p_tool.add_run(f"{key}: ")
        run_cat.font.name = 'Calibri'
        run_cat.font.size = Pt(10)
        run_cat.bold = True

        run_val = p_tool.add_run(val)
        run_val.font.name = 'Calibri'
        run_val.font.size = Pt(10)

    # 6. Professional Experience
    add_section_heading("PROFESSIONAL EXPERIENCE")
    
    # Associate projects to roles dynamically using multi-stage matching
    role_projects = {role['company']: [] for role in data["roles"]}
    unassigned_projects = []
    
    for proj in data["projects"]:
        assigned = False
        
        proj_name_lower = proj['name'].lower()
        proj_company_lower = proj.get("company", "").lower()
        bullets_text_lower = " ".join(proj.get("bullets", [])).lower()
        
        # Normalize common typos (like tios -> trios)
        if "tios" in proj_name_lower:
            proj_name_lower = proj_name_lower.replace("tios", "trios")
        if "tios" in proj_company_lower:
            proj_company_lower = proj_company_lower.replace("tios", "trios")
        if "tios" in bullets_text_lower:
            bullets_text_lower = bullets_text_lower.replace("tios", "trios")

        for role in data["roles"]:
            role_company_lower = role['company'].lower()
            if "tios" in role_company_lower:
                role_company_lower = role_company_lower.replace("tios", "trios")
                
            # Stage 1: Explicit company field matching
            if proj_company_lower and (proj_company_lower in role_company_lower or role_company_lower in proj_company_lower):
                role_projects[role['company']].append(proj)
                assigned = True
                break
                
            # Stage 2: Company name words in project name (ignoring common company suffixes)
            company_words = [w.lower() for w in role['company'].replace("tios", "trios").split() if len(w) > 2 and w.lower() not in ["pvt", "ltd"]]
            if company_words and any(w in proj_name_lower for w in company_words):
                role_projects[role['company']].append(proj)
                assigned = True
                break
                
            # Stage 3: Company name words in project bullets/achievements
            if company_words and any(w in bullets_text_lower for w in company_words):
                role_projects[role['company']].append(proj)
                assigned = True
                break
                
        if not assigned:
            unassigned_projects.append(proj)
            
    # Default unassigned to the first role
    if unassigned_projects and data["roles"]:
        role_projects[data["roles"][0]['company']].extend(unassigned_projects)

    for role in data["roles"]:
        # Write role header
        p_role = doc.add_paragraph()
        p_role.paragraph_format.space_before = Pt(6)
        p_role.paragraph_format.space_after = Pt(2)
        p_role.paragraph_format.line_spacing = 1.2
        p_role.paragraph_format.tab_stops.add_tab_stop(Inches(7.25), WD_TAB_ALIGNMENT.RIGHT)

        left_text = f"{role['title']} | {role['company']}"
        right_text = f"{role['location']} | {role['timeline']}"

        p_role.text = ""
        run_role_left = p_role.add_run(f"{left_text}\t{role['location']} | ")
        run_role_left.font.name = 'Calibri'
        run_role_left.font.size = Pt(10)
        run_role_left.bold = True
        
        # Split out "Present" if present to draw in red
        timeline_part = role['timeline']
        if "Present" in timeline_part:
            pre_present = timeline_part.split("Present")[0]
            run_time = p_role.add_run(pre_present)
            run_time.font.name = 'Calibri'
            run_time.font.size = Pt(10)
            run_time.bold = True
            
            run_pres = p_role.add_run("Present")
            run_pres.font.name = 'Calibri'
            run_pres.font.size = Pt(10)
            run_pres.font.color.rgb = RGBColor(0xFF, 0x00, 0x00) # Red Present
            run_pres.bold = True
        else:
            run_time = p_role.add_run(timeline_part)
            run_time.font.name = 'Calibri'
            run_time.font.size = Pt(10)
            run_time.bold = True

        # Write experience projects/domains under this company
        projects_for_role = role_projects.get(role['company'], [])
        for proj in projects_for_role:
            p_title = doc.add_paragraph()
            p_title.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p_title.paragraph_format.space_before = Pt(4)
            p_title.paragraph_format.space_after = Pt(2)
            p_title.paragraph_format.line_spacing = 1.1

            # Strip company name from the project/domain heading
            clean_name = clean_project_name(proj["name"], role['company'])
            run_title = p_title.add_run(clean_name)
            run_title.font.name = 'Calibri'
            run_title.font.size = Pt(10)
            run_title.bold = True

            for bullet in proj["bullets"]:
                p_bullet = doc.add_paragraph()
                p_bullet.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                p_bullet.paragraph_format.left_indent = Inches(0.25)
                p_bullet.paragraph_format.first_line_indent = Inches(-0.25)
                p_bullet.paragraph_format.space_before = Pt(0)
                p_bullet.paragraph_format.space_after = Pt(0)
                p_bullet.paragraph_format.line_spacing = 1.1

                pPr = p_bullet._p.get_or_add_pPr()
                numPr = parse_xml(r'<w:numPr %s><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>' % nsdecls('w'))
                pPr.append(numPr)

                run_bullet = p_bullet.add_run(bullet)
                run_bullet.font.name = 'Calibri'
                run_bullet.font.size = Pt(10)

    # 7. Education
    add_section_heading("EDUCATION")
    for edu in data["education"]:
        p_edu = doc.add_paragraph()
        p_edu.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p_edu.paragraph_format.space_before = Pt(0)
        p_edu.paragraph_format.space_after = Pt(2)
        p_edu.paragraph_format.line_spacing = 1.1

        run_deg = p_edu.add_run(edu["degree"])
        run_deg.font.name = 'Calibri'
        run_deg.font.size = Pt(10)
        run_deg.bold = True
        run_deg.font.color.rgb = RGBColor(0x00, 0xB0, 0xF0) # 00b0f0 light blue

        rest_text = f" | {edu['institution']} | {edu['timeline']}"
        run_rest = p_edu.add_run(rest_text)
        run_rest.font.name = 'Calibri'
        run_rest.font.size = Pt(10)

    # 8. Certifications
    add_section_heading("CERTIFICATIONS")
    for cert in data["certifications"]:
        p_cert = doc.add_paragraph()
        p_cert.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p_cert.paragraph_format.left_indent = Inches(0.25)
        p_cert.paragraph_format.first_line_indent = Inches(-0.25)
        p_cert.paragraph_format.space_before = Pt(0)
        p_cert.paragraph_format.space_after = Pt(0)
        p_cert.paragraph_format.line_spacing = 1.1

        pPr = p_cert._p.get_or_add_pPr()
        numPr = parse_xml(r'<w:numPr %s><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>' % nsdecls('w'))
        pPr.append(numPr)

        run_cname = p_cert.add_run(cert["name"])
        run_cname.font.name = 'Calibri'
        run_cname.font.size = Pt(10)
        run_cname.bold = True
        run_cname.font.color.rgb = RGBColor(0x00, 0xB0, 0xF0) # 00b0f0 light blue

        run_corg = p_cert.add_run(f" | {cert['org']}")
        run_corg.font.name = 'Calibri'
        run_corg.font.size = Pt(10)

    # Save DOCX
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    doc.save(output_path)
    print(f"Word resume successfully generated at: {output_path}")

def convert_docx_to_pdf(docx_path, pdf_path):
    """Converts a DOCX file to PDF using Microsoft Word COM interface via PowerShell."""
    docx_path = os.path.abspath(docx_path)
    pdf_path = os.path.abspath(pdf_path)

    # Temporary ps1 file path
    temp_dir = os.path.dirname(pdf_path)
    ps1_path = os.path.join(temp_dir, "temp_convert_pdf.ps1")

    ps1_content = f"""
    $clean_path = "{docx_path}"
    $pdf_path = "{pdf_path}"

    try {{
        $word = New-Object -ComObject Word.Application
        $word.DisplayAlerts = 0
        $word.Visible = $false
        $doc = $word.Documents.Open($clean_path, $false, $true, $false)
        $doc.SaveAs($pdf_path, 17)
        $doc.Close()
        $word.Quit()
        [System.Runtime.InteropServices.Marshal]::ReleaseComObject($word) | Out-Null
        [System.GC]::Collect()
        [System.GC]::WaitForPendingFinalizers()
    }} catch {{
        Write-Error $_.Exception.Message
    }}
    """

    with open(ps1_path, 'w', encoding='utf-8') as f:
        f.write(ps1_content)

    print("Running PDF compilation via background PowerShell script...")
    result = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", ps1_path], capture_output=True, text=True)

    if os.path.exists(ps1_path):
        try:
            os.remove(ps1_path)
        except Exception:
            pass

    if os.path.exists(pdf_path):
        print(f"PDF resume successfully generated at: {pdf_path}")
    else:
        print(f"Failed to generate PDF! PowerShell Error: {result.stderr}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate Word & PDF Resume (Template-4 Layout)")
    parser.add_argument("--json", required=True, help="Path to JSON file containing resume data")
    parser.add_argument("--output", required=True, help="Output .docx file path")
    parser.add_argument("--pdf", required=False, help="Optional output .pdf file path")

    args = parser.parse_args()
    generate_resume(args.json, args.output)

    if args.pdf:
        with open(args.json, 'r', encoding='utf-8') as f:
            data = json.load(f)
        role = data.get("role", "resume")
        role_clean = role.replace(" ", "_").replace("/", "_").replace("-", "_")
        role_clean = "".join(c for c in role_clean if c.isalnum() or c == "_")
        while "__" in role_clean:
            role_clean = role_clean.replace("__", "_")
        
        pdf_dir = os.path.dirname(args.pdf)
        pdf_path = os.path.join(pdf_dir, f"Sameer_{role_clean}.pdf")
        
        # Clean up any generic resume.pdf that might be left over
        old_pdf = os.path.join(pdf_dir, "resume.pdf")
        if os.path.exists(old_pdf) and os.path.abspath(old_pdf) != os.path.abspath(pdf_path):
            try:
                os.remove(old_pdf)
            except Exception:
                pass
                
        convert_docx_to_pdf(args.output, pdf_path)
