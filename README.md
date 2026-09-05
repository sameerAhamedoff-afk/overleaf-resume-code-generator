# Antigravity AI Resume Architect & ATS Optimization Engine 🚀

An autonomous, agentic workspace powered by Google Antigravity designed to decode Job Descriptions (JDs), eliminate ATS keyword gaps, and generate interview-winning, multi-format resumes (**LaTeX / Overleaf**, **Word .docx**, and **PDF**) alongside customized cover letters in seconds.

---

## 🌟 Key Features & Philosophy

- **Veteran Hiring Manager Philosophy**: Decodes unspoken engineering requirements (System Design, Async Processing, Event-Driven Architecture, Observability) and eliminates recruiter exclusion filters by aligning conventional corporate target titles.
- **Product-Style Storytelling & Explicit Tech Stack**: Bullet points follow the **What-How-Why (Google XYZ)** formula, leading with bold product/platform names (e.g., `**Beeha DevSecOps Agent:**`, `**DocuShield PII Redactor:**`, `**Sentinel Observability Suite:**`) and explicitly highlighting concrete technologies (LangChain, LangGraph, FastAPI, Pinecone, Docker, AWS, etc.).
- **Multi-Format Output Generation**:
  - **LaTeX / Overleaf**: Pixel-perfect `.tex` files with character escaping (`\&`, `\%`, `\_`, `\$`, `\#`, `\{`, `\}`).
  - **Microsoft Word (.docx)**: Clean ATS-compliant layout generated via `python-docx` with custom indentations and bullet hierarchies.
  - **Compiled PDF**: Automated conversion to `Sameer_<role_name>.pdf` via Word headless automation.
  - **Cover Letters**: Tailored, professional Word documents (`cover_letter.docx`).
- **Strict ATS Optimization Engine**:
  - **Enforced Section Sequence**: `PROFESSIONAL SUMMARY` ➡️ `PROFESSIONAL EXPERIENCE` ➡️ `TECHNICAL SKILLS` ➡️ `EDUCATION`.
  - **No Pipe-Delimited Walls**: Formats technical skills as clean, comma-separated category blocks to preserve linear ATS parser indexing.
  - **Emoji-Free Headers**: Clean text contact lines without icons or emojis that fail corporate parsing engines.
- **Automated ATS Gap Analysis & Match Scoring**: Computes pre- and post-tailoring match percentages using `.agents/scripts/rate_resume.py`.
- **Application Tracking**: Automatically records tailored applications, implemented keywords, and generated artifact paths in `job_tracker.md`.

---

## 📂 Project Structure

```text
├── .agents/
│   ├── AGENTS.md                  # Core rules: Hiring manager principles, ATS constraints, LaTeX escaping
│   ├── scripts/
│   │   ├── rate_resume.py          # TF-IDF & keyword ATS match rate scoring engine
│   │   ├── generate_docx_resume.py # Programmatic Word (.docx) and PDF resume compiler
│   │   └── generate_docx.py        # Tailored Word cover letter generator
│   └── skills/
│       ├── tailor_resume/          # Primary tailoring skill workflow & instructions
│       └── manage_templates/       # Template management skill (list, inspect, add)
├── templates/
│   ├── template-1-Image.tex        # LaTeX layout with minipage header and photo placeholder
│   ├── template-2.tex              # AI Engineer & GenAI developer LaTeX layout
│   ├── template-3(Fullstack).tex   # AI & Fullstack developer LaTeX layout
│   └── Template-4.docx             # Clean Word ATS reference layout
├── outputs/                        # Generated resumes, cover letters, and reports per job
│   └── <Candidate>-<Company>-<Role>/
│       ├── resume.tex              # Overleaf-ready LaTeX code (if requested)
│       ├── resume.docx             # ATS-formatted Word document
│       ├── Sameer_<role>.pdf       # Compiled PDF resume
│       ├── cover_letter.docx       # Tailored Word cover letter
│       └── rating_report.md        # Detailed ATS match & gap analysis report
├── profile.md                      # Consolidated master candidate profile & experience base
├── job_tracker.md                  # Application history and keyword log
└── README.md                       # Workspace documentation
```

---

## 🛠️ Antigravity CLI Skills

These skills are natively discovered by Antigravity in this workspace:

### 1. Tailor Resume Skill
**Triggers**: `tailor resume`, `generate resume`, `customize resume`, `resume for job`

**Workflow**:
1. Ingests Job Description from raw text or live URL (LinkedIn, Greenhouse, Lever, etc.).
2. Conducts ATS Gap Analysis against `profile.md` using `rate_resume.py`.
3. Synthesizes tailored experience bullets using product-style bold subtitles and explicit tech stack disclosures.
4. Generates output artifacts in `outputs/<Candidate>-<Company>-<Role>/`:
   - `resume.tex` (LaTeX) or `resume.docx` & `Sameer_<role>.pdf` (Word/PDF).
   - `cover_letter.docx` (Cover letter).
5. Automatically updates `job_tracker.md`.
6. Reports the match rate progression (Before vs. After) and a summary table of integrated ATS keywords.

### 2. Manage Templates Skill
**Triggers**: `list templates`, `view template <name>`, `add resume template`

**Usage**:
- List all available templates: `list templates`
- Inspect a specific template: `view template template-2`
- Add a new layout: `add resume template`

---

## 📝 LaTeX Character Escaping Quick Reference
When modifying templates or LaTeX resumes manually, ensure all reserved characters are escaped:
- `&` ➡️ `\&` (e.g., `Node.js \& React`)
- `%` ➡️ `\%` (e.g., `reduced latency by 45\%`)
- `_` ➡️ `\_` (e.g., `sighti\_evals`)
- `$` ➡️ `\$`
- `#` ➡️ `\#`
- `{` / `}` ➡️ `\{` / `\}`
