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

### Step 3: Perform ATS Gap Analysis
- Compare the JD requirements with the skills and achievements listed in `profile.md`.
- Identify key ATS keywords (languages, frameworks, tools, methodologies, action verbs) that are:
  - **Required by the JD** but **missing or under-represented** in the master profile.
  - Target these keywords for inclusion in the tailored resume.

### Step 4: Choose Template & Tailor LaTeX Code
- Select the best template layout from `templates/` (e.g., `template-2.tex` for AI/ML roles, `template-3(Fullstack).tex` for React/Node/Fullstack roles).
- Replace the profile summary, skills list, work experiences, and projects in the template with tailored versions from `profile.md`:
  - Incorporate the missing or underrepresented ATS keywords naturally into the summary, skills list, and experience bullet points.
  - Maintain the template's LaTeX preamble, formatting commands, columns, and packages exactly.
  - **CRITICAL**: Escape all special characters (`&` ➡️ `\&`, `%` ➡️ `\%`, `_` ➡️ `\_`, `$` ➡️ `\$`, `#` ➡️ `\#`, `{`/`}` ➡️ `\{`/`\}`) to prevent Overleaf compilation errors.

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
- Create the separate subfolder within `outputs/` (e.g., `outputs/Sameer-<Company_Name>-<Role_Name>/`) and save the final LaTeX code as `resume.tex` inside it.

### Step 7: Present Results to User
Deliver the output in a clear, formatted presentation:
1. **Job Match Rate**: Show the calculated match rate percentage of the JD to the profile before tailoring vs. after tailoring (e.g. "Initial Match Rate: 65% | Tailored Match Rate: 98%").
2. **ATS Keywords Table**:
   - Provide a table detailing:
     - **Required Keyword / Skill** (from JD)
     - **Status** (Already Present / Added during tailoring)
     - **Implementation Detail** (where it was integrated in the resume)
3. **Resume Location**: Show a clickable file link to the saved tailored LaTeX file (e.g. `[resume.tex](file:///c:/Users/user/Desktop/job-ai/overleaf-resume-code-generator/outputs/Sameer-Google-AI_Engineer/resume.tex)`).
4. **DO NOT output the full LaTeX code block in the terminal.** It is already saved to the path above.

---

## Token Efficiency Guidelines (Reduced Token Usage)
- **JD Scrape Optimizations**: When reading job description URLs, filter out and extract only the relevant job title, company name, required skills, and core responsibilities. Discard HTML tags, header navigation, scripts, and footer content before processing.
- **One-Time Context Load**: Load the master profile `profile.md` and template code once. Reuse these details from your active context instead of repeatedly reading the files.
- **Single-Pass File Writing**: Finalize the resume details entirely in memory first, then write the finished LaTeX code to `outputs/<Username>-<Company_Name>-<Role_Name>/resume.tex` in a single write operation rather than multiple incremental edits.
