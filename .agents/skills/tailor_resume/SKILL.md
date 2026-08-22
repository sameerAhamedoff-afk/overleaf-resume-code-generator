---
name: Tailor Resume
description: centralizes the resume tailoring workflow using a master profile (profile.md), JDs (text/URL), ATS keyword gap mapping, templates, and job application tracking.
---

# Skill: Tailor Resume (ATS-Optimized & Tracked)

Use this skill when the user wants to generate a highly customized, ATS-aligned LaTeX resume for a specific job application, while logging the request in the tracking history.

## inputs & setup
Before starting, ensure you have:
1. **Job Description (JD)**: The user will paste raw text or provide a job posting URL.
2. **Master Profile**: The master experience database at `profile.md` in the workspace root.
3. **Templates**: LaTeX layouts stored in the `templates/` folder (e.g. `template-2.tex` for AI-focused, `template-3(Fullstack).tex` for Fullstack-focused, `template-1-Image.tex`).

---

## Tailoring Workflow

### Step 1: Ingest and Analyze the Job Description (JD)
- **If a Job URL is provided**:
  - Fetch page contents using `read_url_content` or `browser_subagent`.
  - Extract the Job Title, Company Name, Job Posting Link, and the full job description.
- **If raw text is provided**:
  - Extract/infer Job Title, Company Name (ask the user for these if not clearly visible in the text).
- Summarize the top 5-10 core skills, technologies, and methodologies required by this JD.

### Step 2: Read the Master Profile
- Read `profile.md` in the workspace root. If it is missing, check `templates/template-2.tex` or `templates/template-3(Fullstack).tex` to reconstruct it, write it to `profile.md`, and then read it.
- Retrieve Sameer's contact details, skills, experiences, and project history.

### Step 3: Perform ATS Gap Analysis & Calculate Initial Match Rate
- Save the Job Description content to a temporary text file (e.g. `temp_jd.txt`).
- Calculate the initial match rate before tailoring by running the rating script against the master profile:
  `python .agents/scripts/rate_resume.py --resume profile.md --jd temp_jd.txt`
- Compare the JD requirements with the skills and achievements listed in `profile.md`.
- Identify key ATS keywords (languages, frameworks, tools, methodologies, action verbs) that are:
  - **Required by the JD** but **missing or under-represented** in the master profile.
  - Target these keywords for inclusion in the tailored resume.

### Step 4: Choose Template & Tailor Resume Code
- Select the best template layout from `templates/` (e.g., `template-2.tex` for AI/ML roles, `template-3(Fullstack).tex` for React/Node/Fullstack roles, or `Template-4.docx` for Word/PDF resume output).
- Replace the profile summary, skills list, work experiences, and projects in the template with tailored versions from `profile.md`:
  - Incorporate the missing or underrepresented ATS keywords naturally into the summary, skills list, and experience bullet points.
  - If using LaTeX templates, maintain the template's LaTeX preamble, formatting commands, columns, and packages exactly and escape special characters (`&` ➡️ `\&`, `%` ➡️ `\%`, `_` ➡️ `\_`, etc.).
  - If using the Template 4 layout, prepare a structured JSON object to feed into the Word resume generator.

### Step 5: Log the Entry in `job_tracker.md`
- Append a new row to the table in `job_tracker.md`.
- Record:
  - Date & Time
  - Company Name
  - Job Title / Role
  - Job Posting Link (or "Pasted Text")
  - Path of the output file: `outputs/<Username>-<Company_Name>-<Role_Name>/resume.tex` (e.g., `outputs/Sameer-Google-AI_Engineer/resume.tex`)
  - Implemented keywords & key ATS points

### Step 6: Save the File
- Create the separate subfolder within `outputs/` (e.g., `outputs/Sameer-<Company_Name>-<Role_Name>/`).
- **If a LaTeX template (1, 2, 3) is requested**: Save the final LaTeX code as `resume.tex` inside it.
- **If Template 4 layout is explicitly requested**: Skip `.tex` file generation entirely.

### Step 6b: Generate Word & PDF Resume (if Template-4.docx layout is requested or as secondary formats)
- Create a structured JSON file `temp_resume.json` containing the tailored contact details, summary, key skills, tools & technologies, roles, projects, education, and certifications.
- Run the python script to generate the Word resume and compile the PDF, ensuring the PDF file is named `Sameer_<role_name>.pdf` (with spaces replaced by underscores, e.g. `Sameer_AI_Engineer.pdf`):
  `python .agents/scripts/generate_docx_resume.py --json temp_resume.json --output "outputs/Sameer-<Company_Name>-<Role_Name>/resume.docx" --pdf "outputs/Sameer-<Company_Name>-<Role_Name>/Sameer_<role_name>.pdf"`
- Delete the temporary JSON file: `Remove-Item -Force temp_resume.json`.

### Step 7: Generate Cover Letter (Word Format)
- Based on the tailored resume and the target Job Description, write a compelling and professional 3-4 paragraph cover letter.
- Save the paragraphs of the cover letter separated by double newlines into a temporary text file named `temp_cover_letter.txt` in the root workspace.
- Run the python script to format and compile the cover letter into a Word document (.docx):
  `python .agents/scripts/generate_docx.py --output "outputs/<Username>-<Company_Name>-<Role_Name>/cover_letter.docx" --name "Sameer Ahamed A" --email "sameerahamedoff3@gmail.com" --phone "+91-9080861209" --linkedin "https://www.linkedin.com/in/sameer-ahamed-338558310/" --company "<Company_Name>" --role "<Role_Name>" --content_file temp_cover_letter.txt`
- Delete the temporary file `temp_cover_letter.txt` by running a powershell command: `Remove-Item -Force temp_cover_letter.txt`.

### Step 7b: Calculate Tailored Match Rate & Save Report
- Evaluate the tailored resume against the JD to calculate the final match rate and generate the rating reports:
  - **For LaTeX resumes:**
    `python .agents/scripts/rate_resume.py --resume "outputs/Sameer-<Company_Name>-<Role_Name>/resume.tex" --jd temp_jd.txt --markdown-output "outputs/Sameer-<Company_Name>-<Role_Name>/rating_report.md" --json-output "outputs/Sameer-<Company_Name>-<Role_Name>/rating_report.json"`
  - **For Word resumes:**
    `python .agents/scripts/rate_resume.py --resume "outputs/Sameer-<Company_Name>-<Role_Name>/resume.docx" --jd temp_jd.txt --markdown-output "outputs/Sameer-<Company_Name>-<Role_Name>/rating_report.md" --json-output "outputs/Sameer-<Company_Name>-<Role_Name>/rating_report.json"`
- Clean up the temporary JD file: `Remove-Item -Force temp_jd.txt`.

### Step 8: Present Results to User
Deliver the output in a clear, formatted presentation:
1. **Job Match Rate**: Show the calculated match rate percentage of the JD to the profile before tailoring vs. after tailoring (using output from `rate_resume.py`).
2. **ATS Keywords Table**:
   - Provide a table detailing:
     - **Required Keyword / Skill** (from JD)
     - **Status** (Already Present / Added during tailoring)
     - **Implementation Detail** (where it was integrated in the resume)
3. **Generated Files Locations**:
   - Clickable link to the saved tailored LaTeX file (if compiled): `[resume.tex](file:///c:/Users/user/Desktop/job-ai/overleaf-resume-code-generator/outputs/Sameer-Google-AI_Engineer/resume.tex)`
   - Clickable link to the saved tailored Word resume: `[resume.docx](file:///c:/Users/user/Desktop/job-ai/overleaf-resume-code-generator/outputs/Sameer-Google-AI_Engineer/resume.docx)`
   - Clickable link to the saved tailored PDF resume: `[Sameer_AI_Engineer.pdf](file:///c:/Users/user/Desktop/job-ai/overleaf-resume-code-generator/outputs/Sameer-Google-AI_Engineer/Sameer_AI_Engineer.pdf)` (replacing `AI_Engineer` with the tailored role name).
   - Clickable link to the saved tailored Word cover letter file: `[cover_letter.docx](file:///c:/Users/user/Desktop/job-ai/overleaf-resume-code-generator/outputs/Sameer-Google-AI_Engineer/cover_letter.docx)`
   - Clickable link to the generated rating report: `[rating_report.md](file:///c:/Users/user/Desktop/job-ai/overleaf-resume-code-generator/outputs/Sameer-Google-AI_Engineer/rating_report.md)`
4. **DO NOT output the full LaTeX code block or the cover letter text in the terminal.** They are already saved to the paths above.


---

## Token Efficiency Guidelines (Reduced Token Usage)
- **JD Scrape Optimizations**: When reading job description URLs, filter out and extract only the relevant job title, company name, required skills, and core responsibilities. Discard HTML tags, header navigation, scripts, and footer content before processing.
- **One-Time Context Load**: Load the master profile `profile.md` and template code once. Reuse these details from your active context instead of repeatedly reading the files.
- **Single-Pass File Writing**: Finalize the resume details entirely in memory first, then write the finished LaTeX code to `outputs/<Username>-<Company_Name>-<Role_Name>/resume.tex` in a single write operation rather than multiple incremental edits.
