# LaTeX Template Converter

When I provide you with a text file or content, convert it into a professional LaTeX document using the Template-LaTex structure.

## Instructions:

1. **Read the provided file/content**
2. **Extract key information** (title, author, content sections)
3. **Apply the LaTeX template structure** from `/workspaces/Presentations/Archive/Template-LaTex/Template-LaTex.tex`
4. **Generate a complete LaTeX document** with proper formatting

## Template Structure to Follow:

### Document Setup:
- Use `\documentclass[11pt,letterpaper]{article}`
- Include all required packages from the template
- Set up custom commands: `\milestone{}`, `\metric{}`, `\risk{}`, `\mitigation{}`, `\techterm{}`, `\code{}`

### Template Variables to Replace:
- `\projectname{}` - Extract from content or use "Document Title"
- `\projectsubtitle{}` - Extract subtitle or use "Generated Document"
- `\authorteam{}` - Extract author or use "Document Author"
- `\documentversion{}` - Use "1.0"
- `\documentdate{}` - Use "\today"
- `\documentstatus{}` - Use "Draft"

### Content Structure:
1. **Title and Abstract** (if applicable)
2. **Introduction** - Background and objectives
3. **Main Content** - Organize into logical sections
4. **Methodology** (if technical content)
5. **Results/Analysis** (if applicable)
6. **Conclusion** - Summary and findings
7. **References** (if citations exist)

### Formatting Guidelines:
- Use `\section{}`, `\subsection{}`, `\subsubsection{}` for hierarchy
- Apply `\label{}` for cross-references
- Use `\begin{itemize}` and `\begin{enumerate}` for lists
- Convert tables to LaTeX table format with `\begin{table}` and `\begin{tabular}`
- Use `\begin{equation}` for mathematical content
- Apply custom commands for emphasis: `\textbf{}`, `\textit{}`, `\texttt{}`

### Output Requirements:
- Generate complete LaTeX code ready for compilation
- Include all necessary packages and commands
- Maintain professional academic formatting
- Ensure proper LaTeX syntax
- Add comments for section organization

## Example Usage:
When I say "Apply LaTeX template to [filename]", you should:
1. Read the specified file
2. Analyze its content structure
3. Generate a complete LaTeX document following the template
4. Provide the ready-to-compile LaTeX code

The output should be a complete `.tex` file that can be compiled with `pdflatex` to produce a professional PDF document.
