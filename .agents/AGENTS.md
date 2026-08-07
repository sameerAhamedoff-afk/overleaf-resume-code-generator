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
- Always write/save the generated code to a separate directory inside the outputs folder: `outputs/<Username>-<Company_Name>-<Role_Name>/resume.tex` (e.g., `outputs/Sameer-Google-AI_Engineer/resume.tex`). Do not write it to a generic `tailored_resume.tex` file in the root.
- Present the final LaTeX code in a clean, copyable Markdown code block.
