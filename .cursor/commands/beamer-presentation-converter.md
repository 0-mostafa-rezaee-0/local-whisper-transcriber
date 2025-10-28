# Beamer Presentation Template Converter

When I provide you with a text file or content, convert it into a professional Beamer presentation using the Template-Presentations structure.

## Instructions:

1. **Read the provided file/content**
2. **Extract key information** (title, presenter, content sections)
3. **Apply the Beamer template structure** from `/workspaces/Presentations/Archive/Template-Presentations/Template-presentation.tex`
4. **Generate a complete Beamer presentation** with proper formatting

## Template Structure to Follow:

### Document Setup:
- Use `\documentclass[aspectratio=169]{beamer}`
- Include all required packages from the template
- Set up Madrid theme with custom color scheme
- Configure custom commands: `\highlight{}`, `\metric{}`, `\risk{}`, `\mitigation{}`, `\techterm{}`, `\code{}`

### Template Variables to Replace:
- `\presentationtitle{}` - Extract from content or use "Presentation Title"
- `\presentationsubtitle{}` - Extract subtitle or use "Generated Presentation"
- `\presentername{}` - Extract presenter or use "Presenter Name"
- `\presenteraffiliation{}` - Extract affiliation or use "Organization"
- `\presentationdate{}` - Use "\today"
- `\presentationversion{}` - Use "1.0"

### Presentation Structure:
1. **Title Slide** - Title, subtitle, presenter, affiliation, date
2. **Outline/Agenda** - Table of contents slide
3. **Introduction** - Background and objectives
4. **Main Content** - Organize into logical sections with frames
5. **Methodology** (if technical content)
6. **Results/Analysis** (if applicable)
7. **Conclusion** - Summary and key takeaways
8. **References** (if citations exist)

### Frame Formatting Guidelines:
- Use `\begin{frame}` and `\end{frame}` for each slide
- Apply `\frametitle{}` for slide titles
- Use `\begin{itemize}` and `\begin{enumerate}` for lists
- Convert tables to LaTeX table format with `\begin{table}` and `\begin{tabular}`
- Use `\begin{equation}` for mathematical content
- Apply custom commands for emphasis: `\textbf{}`, `\textit{}`, `\texttt{}`
- Use `\pause` for slide transitions
- Apply `\alert{}` for highlighting important points

### Visual Elements:
- Use TikZ for diagrams and flowcharts
- Apply custom colors: `myblue`, `myred`, `mygreen`, `mypurple`, `myorange`
- Use `\begin{block}{}` environments for callouts
- Apply `\begin{columns}` for multi-column layouts

### Output Requirements:
- Generate complete Beamer LaTeX code ready for compilation
- Include all necessary packages and commands
- Maintain professional presentation formatting
- Ensure proper LaTeX syntax
- Add comments for section organization
- Use appropriate frame breaks for readability

## Example Usage:
When I say "Apply Beamer template to [filename]", you should:
1. Read the specified file
2. Analyze its content structure
3. Generate a complete Beamer presentation following the template
4. Provide the ready-to-compile LaTeX code

The output should be a complete `.tex` file that can be compiled with `pdflatex` to produce a professional PDF presentation.

## Key Differences from Document Template:
- Uses `beamer` document class instead of `article`
- Organizes content into frames instead of sections
- Includes slide transitions and visual effects
- Optimized for 16:9 aspect ratio
- Focuses on visual presentation rather than detailed text
