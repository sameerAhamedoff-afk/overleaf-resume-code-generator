---
name: Tailor Resume
description: centralizes the resume tailoring workflow using a master profile (profile.md), JDs (text/URL), ATS keyword gap mapping, templates, and job application tracking.
---

# Skill: Tailor Resume (Veteran Hiring Manager Review & ATS Optimization)

In this skill, you act as a **Veteran Technical Hiring Manager & Principal Engineering Screener** reviewing job applications for Tier-1 companies and high-growth AI teams. Your objective is not merely mechanical keyword matching, but critically dissecting the Job Description (JD), decoding the hiring team's unspoken technical requirements, strategically bridging keyword gaps from the candidate's master profile (`profile.md`), and producing an elite, ATS-optimized resume.

## Inputs & Setup
Before starting, ensure you have:
1. **Job Description (JD)**: Raw text or a job posting URL.
2. **Master Profile**: The master experience database at `profile.md` in the workspace root.
3. **Templates**: LaTeX layouts in `templates/` (e.g. `template-2.tex` for AI-focused, `template-3(Fullstack).tex` for Fullstack-focused, `template-1-Image.tex`) or `Template-4.docx` for Word/PDF.

---

## Tailoring Workflow

### Step 1: Ingest & Deconstruct the Job Description (The Hiring Manager's Technical Breakdown)
- **If a Job URL is provided**:
  - Fetch page contents using `read_url_content` or `browser_subagent`.
  - Extract the Job Title, Company Name, Job Posting Link, and core job text.
- **If raw text is provided**:
  - Extract/infer Job Title and Company Name (ask if ambiguous).
- **Hiring Manager Technical Deconstruction**:
  - **Core Problem Domain**: What is the engineering team actually trying to ship? (e.g., autonomous agents, enterprise RAG, high-throughput document extraction, real-time CV, event-driven microservices).
  - **Trendy vs. Foundational Balance**: Highlight flashy frameworks (LangGraph, Bedrock, OpenAI) *AND* pull out the unspoken foundational requirements (System Design, Asynchronous Processing, Database Optimization, Observability, Uptime).
  - **Strategic Corporate Target Title**: Formulate a conventional, high-search-volume corporate headline (e.g., `Agentic AI Engineer | Generative AI Developer`, `AI Engineer`) that avoids recruiter exclusion filters.

### Step 2: Read the Master Profile
- Read `profile.md` in the workspace root. If missing, check `templates/template-2.tex` or `templates/template-3(Fullstack).tex` to reconstruct it.
- Audit Sameer's contact details, technical skills, production experiences, and project history.

### Step 3: ATS Gap Analysis & Hiring Manager Keyword Curation
- Save the Job Description content to a temporary text file (e.g. `temp_jd.txt`).
- Calculate the initial match rate before tailoring:
  `python .agents/scripts/rate_resume.py --resume profile.md --jd temp_jd.txt`
- **Hiring Manager Keyword Strategy**:
  - Group required keywords into four strategic buckets:
    1. **Agentic & Generative AI**: LangGraph, LangChain, AWS Bedrock, RAG, Semantic Search, Re-ranking, Structured Outputs, Tool Calling, Hallucination Guardrails.
    2. **Backend & Architecture Foundations**: System Design, Asynchronous Processing, Python (FastAPI), Node.js, REST APIs, Microsoft Graph API, Event-Driven Architecture, SQL, PostgreSQL, MongoDB.
    3. **Cloud, Infrastructure & DevOps**: AWS (ECS/Fargate, Lambda, SQS, SNS, S3, SES), Docker, Git, CI/CD (GitHub Actions), Linux/Unix.
    4. **Observability, Testing & Metrics**: Prometheus, Grafana, AI Evaluation Frameworks, TDD, 99.9% Uptime.
  - Map which skills are missing or under-represented in `profile.md` and target them for organic, truthful inclusion.

### Step 4: Craft the Tailored Resume (Hiring Manager Precision)
- Select the best template layout from `templates/` (e.g., `template-2.tex`, `template-3(Fullstack).tex`, or Template 4 layout).
- **Section Order Requirement**:
  - Resumes must strictly position `PROFESSIONAL EXPERIENCE` before `TECHNICAL SKILLS`.
  - Hierarchy: `PROFESSIONAL SUMMARY` ➡️ `PROFESSIONAL EXPERIENCE` ➡️ `TECHNICAL SKILLS` ➡️ `EDUCATION` (followed by `PROJECTS` and `CERTIFICATIONS`).
- **Professional Summary**:
  - Craft a 3-4 sentence high-impact summary. Lead with candidate's years of experience, core production focus, architecture patterns (e.g., event-driven microservices, RAG, autonomous agents), and verified metrics (e.g., 99.9% uptime).
- **Professional Experience (What-How-Why Storytelling & Google XYZ Formula)**:
  - **Bold Product-Style Subtitle Requirement**: Every bullet point must lead with a concise **bold subtitle formatted like a product, system, engine, or platform name** (e.g. `**FinTax Copilot:**`, `**Beeha DevSecOps Agent:**`, `**DocuShield PII Redactor:**`, `**Sighti Vision Heatmaps:**`, `**Omnisense Telemetry Gateway:**`, `**Sentinel Observability Suite:**` in Markdown/DOCX, or `\item \textbf{Beeha DevSecOps Agent:}...` in LaTeX). Avoid generic labels (e.g. "Monitoring setup", "Data Processing", "RAG Pipeline"); brand each bullet as a concrete shipped product, service, or tool.
  - Focus each bullet point strictly on business value, engineering scale, and tangible outcomes rather than simple daily tasks or passive responsibility lists.
  - **Explicit Technology Informing**: When detailing the implementation, always explicitly name and highlight the concrete technologies and frameworks used (e.g., LangChain, LangGraph, FastAPI, Pinecone, Docker, AWS Bedrock, PostgreSQL) within the "How" and narrative description.
  - Structure every bullet point using the **What-How-Why** storytelling framework synthesized with Google's **XYZ formula** (*Accomplished [X] as measured by [Y] by doing [Z]*):
    - **What**: The specific engineering action, product, or system capability delivered (initiating with a decisive active verb like *Architected, Engineered, Deployed, Streamlined, Spearheaded*).
    - **How**: The explicit tools, frameworks, architectural patterns, algorithms, or methodologies used (e.g., *built using LangChain and LangGraph for multi-agent state orchestration, async FastAPI workers, Docker, Pinecone vector indexing, hybrid RAG*). Always inform the exact tech stack utilized.
    - **Why**: The measurable result, business impact, cost/latency reduction, reliability metric, or the "so what?" answering why the work mattered (e.g., *slashing latency by 45%, eliminating manual overhead by 60%, maintaining 99.9% production uptime*).
  - Weave target keywords naturally into production realities (e.g., integrating OCR, vector search, or Fargate microservices).
- **Technical Skills (Eliminate Key-Value Walls)**:
  - Organize strictly under `TECHNICAL SKILLS` (positioned after Professional Experience).
  - Format each category as `<Category Name>: Item 1, Item 2, Item 3` (comma-separated, strictly NO pipeline `|` dividers inside skills).
- **LaTeX Integrity & Character Escaping**:
  - If compiling LaTeX: preserve preamble, escape special characters (`\&`, `\%`, `\_`, `\$`, `\#`, `\{`, `\}`).
- If using Template 4 (Word/PDF): prepare the clean ATS JSON payload.

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
- Create a structured JSON file `temp_resume.json` adhering to strict ATS formatting guidelines:
  - **No Key-Value Walls**: Do not use pipelines (`|`) to join skills. Use `technical_skills` mapping each category to a comma-separated list of items (e.g. `"AI Frameworks": "LangGraph, LangChain, OpenAI..."`).
  - **Clean Contact Info**: No unicode emojis or icons (`phone`, `email`, `location`, `linkedin`, `github`).
  - **Roles with Bullets**: Supply `"bullets": [...]` directly on each role object in `"roles"`.
  - **Sections**: Include `"name"`, `"headline"` (or `"role"`), `"phone"`, `"email"`, `"location"`, `"linkedin"`, `"summary"`, `"technical_skills"`, `"roles"`, `"education"`, and optional `"certifications"` (or `"include_certifications": false`).
- Run the python script to generate the Word resume and compile the PDF, ensuring the PDF file is named `Sameer_<role_name>.pdf` (with spaces replaced by underscores, e.g. `Sameer_AI_Engineer.pdf`):
  `python .agents/scripts/generate_docx_resume.py --json temp_resume.json --output "outputs/Sameer-<Company_Name>-<Role_Name>/resume.docx" --pdf "outputs/Sameer-<Company_Name>-<Role_Name>/Sameer_<role_name>.pdf"`
  *(Use `--no-certifications` / `--exclude-certifications` to avoid mentioning certificates, or `--include-certifications` / `--certifications` to explicitly include them).*
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
2. **Hiring Manager Keyword & Positioning Table**:
   - Provide a structured table detailing:
     - **Required / High-Yield Keyword** (from JD & Hiring Manager Analysis)
     - **Engineering Category** (e.g. Core AI/Agents, Backend & System Design, Cloud/DevOps, Observability)
     - **Status** (Already Present / Added during tailoring)
     - **Strategic Implementation** (where and how it was integrated into Summary, Technical Skills, or Experience bullets using What-How-Why / XYZ storytelling format)
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
