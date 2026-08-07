---
name: Manage Templates
description: Lists available LaTeX resume templates, displays their details, or adds new templates.
---

# Skill: Manage Templates

Use this skill when the user wants to list, view, add, or customize the available LaTeX resume templates in this repository.

## Commands & Workflows

### 1. List Templates
- **Trigger**: "list templates", "show templates", "what templates do you have?"
- **Action**: 
  - List the contents of the `templates/` directory using `list_dir`.
  - Present the templates to the user with a description of their layouts (e.g. "Jake's Resume - Classic SWE single-column", "templat-1 - Modern AI & Fullstack layout").

### 2. View Template Content
- **Trigger**: "view template <name>", "show template <name>", "view templates/<name>"
- **Action**:
  - Read the specified template file using `view_file`.
  - Display the structure and explain its main design elements (e.g., custom commands, fonts, spacing).

### 3. Add New Template
- **Trigger**: "add template", "create template"
- **Action**:
  - Prompt the user for the name and the LaTeX source code of the new template.
  - Write the LaTeX code into `templates/<name>.tex` using `write_to_file` (set `overwrite=true` if updating an existing one).
  - Verify that the template is well-formed.

---

## Standard Template Directory
All templates must be stored under the `templates/` folder in the root of the workspace.
- `templates/jake_resume.tex` (Classic single-column software engineer template)
- `templates/templat-1.tex` (Sameer's customized AI and full-stack developer template)
