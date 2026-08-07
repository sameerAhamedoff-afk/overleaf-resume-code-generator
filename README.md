# Overleaf Resume Code Generator 🚀

An Antigravity-driven workspace designed to take existing LaTeX resume templates and generate customized, ATS-aligned resumes tailored to specific job descriptions in seconds. Ready to copy and paste directly into **Overleaf**!

---

## 📂 Project Structure

- **`.agents/`**: Core Antigravity configuration directory.
  - **`AGENTS.md`**: Contains rules and constraints for generating and formatting LaTeX code (balancing braces, escaping special characters, ATS best practices).
  - **`skills/`**: Custom Antigravity capabilities.
    - **`tailor_resume/`**: Centralized resume tailoring workflow that parses JDs, compares them with the master profile, performs ATS optimization, saves outputs, and updates tracking log.
    - **`manage_templates/`**: Commands for managing (listing, viewing, adding) LaTeX templates.
- **`templates/`**: Directory containing LaTeX templates.
  - `template-1-Image.tex`: Layout containing contact info and minipage image blocks.
  - `template-2.tex`: Optimized AI Engineer resume layout.
  - `template-3(Fullstack).tex`: Optimized AI and Fullstack Developer resume layout.
- **`profile.md`**: Consolidated master profile (contact info, full skills inventory, all projects, and experience bullets).
- **`job_tracker.md`**: Markdown table tracking all JDs posted and resumes generated.

---

## 🛠️ Custom Antigravity CLI Skills

These skills are automatically discovered by Antigravity in this workspace. You can run them by talking to the agent naturally or prompting specific trigger phrases:

### 1. Tailor Resume Skill
**Triggers**: `tailor resume`, `generate resume`, `customize resume`, `resume for job`

**How to Use**:
1. Run the skill by saying `tailor resume` or `tailor my resume for a job`.
2. Provide a **Job Description**:
   - Paste the job description text directly.
   - **OR** Paste a URL to the job posting (e.g., LinkedIn, Greenhouse, Lever, etc.).
3. Choose your base template (e.g. `templates/template-2.tex` for AI or `templates/template-3(Fullstack).tex` for Fullstack).
4. The agent will:
   - Load the user's master experience from `profile.md`.
   - Ingest and analyze the JD (fetching it online if a URL is provided).
   - Perform an **ATS Gap Analysis** comparing the JD to `profile.md` to identify missing keywords.
   - Save the tailored code to a separate directory inside the outputs folder: `outputs/<Username>-<Company_Name>-<Role_Name>/resume.tex` (e.g., `outputs/Sameer-Google-AI_Engineer/resume.tex`).
   - Generate a professional cover letter as a Microsoft Word document (.docx) matching the tailored achievements, saving it to `outputs/<Username>-<Company_Name>-<Role_Name>/cover_letter.docx`.
   - Log the application details in `job_tracker.md`.
   - Output the calculated Job Match Rates, the ATS Keywords Table, and links to both files in the terminal response. Suppression of raw code and text output ensures clean CLI operation.

### 2. Manage Templates Skill
**Triggers**: `list templates`, `view template <name>`, `add resume template`

**How to Use**:
- List all available resume designs: `list templates`
- Show the content of a template: `view template template-2`
- Add a new layout: `add resume template` (and supply the LaTeX code)

---

## 📝 LaTeX Character Escaping Reference
When modifying your resume content manually, remember that LaTeX requires escaping specific characters:
- `&` ➡️ `\&` (e.g., `Node.js \& React`)
- `%` ➡️ `\%` (e.g., `increased efficiency by 30\%`)
- `_` ➡️ `\_` (e.g., `sighti\_evals`)
- `$` ➡️ `\$`
- `#` ➡️ `\#`
- `{` / `}` ➡️ `\{` / `\}`
