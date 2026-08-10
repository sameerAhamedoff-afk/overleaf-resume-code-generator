# Resume Generator Agent Rules

This workspace is designed to help the user generate and tailor resumes using LaTeX templates for Overleaf. When working in this workspace, you must adhere to the following rules:

## 1. LaTeX Preamble & Style Integrity
- **Do not modify the preamble** (packages, spacing commands, margins, custom macro definitions like `\resumeSubheading`) of the template unless explicitly requested by the user.
- Maintain the visual hierarchy, margins, font settings, and structural commands defined in the source template (e.g., `templates/templat-1.tex` or `templates/jake_resume.tex`).

## 2. LaTeX Syntax & Character Escaping
- **CRITICAL**: When tailoring bullet points or text, always check for LaTeX special characters and escape them properly to prevent compile errors on Overleaf:
  - `&` must be escaped as `\&` (especially in tech lists, company names, or job titles).
  - `%` must be escaped as `\%` (common in metrics).
  - `_` must be escaped as `\_` (common in file names, variables, or URLs).
  - `$` must be escaped as `\$`.
  - `#` must be escaped as `\#`.
  - `{` and `}` must be escaped as `\{` and `\}`.
- Ensure all open brackets/braces have corresponding matching closing brackets/braces.

## 3. Resume Tailoring Philosophy
- **ATS Alignment**: Focus on identifying key technical keywords, hard skills, soft skills, and verbs from the Job Description (JD) and integrating them naturally.
- **Action-Oriented Bullet Points**: Use strong action verbs at the start of each bullet point. Apply the **STAR methodology** (Situation, Task, Action, Result) or Google's **XYZ formula** (Accomplished X, as measured by Y, by doing Z).
- **No Keyword Stuffing**: Integrate keywords logically into real experiences. Do not fabricate experience.
- **Maintain Contact Details**: Do not alter or lose the user's phone, email, LinkedIn, GitHub, or location unless specifically instructed.

## 4. UI/UX and Delivery
- Always write/save the generated code to a separate directory inside the outputs folder: `outputs/<Username>-<Company_Name>-<Role_Name>/resume.tex` (e.g., `outputs/Sameer-Google-AI_Engineer/resume.tex`).
- If generating Word and PDF resumes, save them to the same output folder. The Word document must be named `resume.docx` and the PDF resume must be named `Sameer_<role_name>.pdf` (where spaces in the role name are replaced by underscores, e.g. `Sameer_AI_Engineer.pdf`).
- **Do not print the complete LaTeX code block, JSON payloads, or cover letter text in the terminal response**.
- In the final response, only present:
  1. Clickable links to the generated files: `resume.tex` (if generated), `resume.docx`, `Sameer_<role_name>.pdf`, and `cover_letter.docx`.
  2. The job match rate (%) compared to your profile (both before and after tailoring).
  3. A structured table displaying key keywords used/implemented for this JD.

## 5. Token Efficiency & Cost Optimization (Reduced Token Usage)
- **Use Chunk Edits**: Avoid replacing or rewriting entire files when making changes. Instead, make precise edits to targeted lines using `replace_file_content` or `multi_replace_file_content`.
- **Targeted Reading**: When viewing files, do not read the entire file if you only need a specific portion. Specify precise line ranges in `view_file` to conserve input tokens.
- **Scrape Filtering**: When fetching job descriptions from URLs, extract only the text relevant to the job requirements (title, company, skills, responsibilities). Filter out headers, footers, HTML scripts, and navigation links.
- **Concise Reasoning & Chat Output**: Eliminate conversational filler, pleasantries, and redundancy in your thoughts and responses. Provide the requested information directly.
- **Prevent Execution Loops**: Set a hard limit on steps and verify progress at each step to prevent infinite thinking loops or redundant tool calls. Stop and ask for clarification if stuck.
