#!/usr/bin/env python3
"""Markdown to PDF converter using WeasyPrint.

The PDF output uses the same design as resume.html:
- Blue color scheme (#1e40af, #2563eb)
- Clean professional layout on white background
- Matching typography and section styles
"""

import sys
import argparse
import markdown
from weasyprint import HTML, CSS

# CSS matching the design of resume.html / resume-ja.html
STYLE = """
@page {
    margin: 18mm 18mm 18mm 18mm;
    size: A4;
}

* {
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, 'DejaVu Sans', 'Noto Sans', sans-serif;
    font-size: 10pt;
    line-height: 1.6;
    color: #333;
    background: white;
}

/* ---- Name / Title (h1) ---- */
h1 {
    font-size: 22pt;
    color: #1e40af;
    text-align: center;
    margin: 0 0 4px 0;
    padding: 0;
}

/* First paragraph after h1 = subtitle + contact line */
h1 + p {
    text-align: center;
    color: #555;
    font-size: 10pt;
    margin: 0 0 6px 0;
}

/* Horizontal rule beneath header */
hr {
    border: none;
    border-top: 3px solid #2563eb;
    margin: 8px 0 14px 0;
}

/* ---- Section headings ---- */
h2 {
    font-size: 13pt;
    color: #1e40af;
    border-bottom: 2px solid #e5e7eb;
    padding-bottom: 4px;
    margin-top: 18px;
    margin-bottom: 8px;
}

h3 {
    font-size: 11pt;
    color: #334155;
    margin-top: 10px;
    margin-bottom: 3px;
}

h4 {
    font-size: 10pt;
    color: #1e40af;
    margin-top: 8px;
    margin-bottom: 2px;
}

/* ---- Body text ---- */
p {
    margin: 4px 0 6px 0;
    font-size: 10pt;
}

/* Summary block: first blockquote = styled summary */
blockquote {
    background: #f8fafc;
    border-left: 4px solid #2563eb;
    margin: 8px 0 12px 0;
    padding: 10px 14px;
    font-size: 9.5pt;
    color: #334155;
    line-height: 1.7;
}

blockquote p {
    margin: 0;
}

/* ---- Lists ---- */
ul, ol {
    margin: 4px 0 8px 0;
    padding-left: 20px;
}

li {
    margin-bottom: 4px;
    line-height: 1.6;
    font-size: 10pt;
}

/* ---- Links ---- */
a {
    color: #2563eb;
    text-decoration: none;
}

/* ---- Strong / emphasis ---- */
strong {
    color: #1a1a1a;
}

em {
    color: #475569;
}

/* ---- Code (tech stack lines) ---- */
code {
    background: #f1f5f9;
    color: #334155;
    padding: 1px 5px;
    border-radius: 3px;
    font-size: 9pt;
}

pre {
    background: #f1f5f9;
    padding: 8px 12px;
    border-radius: 4px;
    font-size: 9pt;
    margin: 6px 0;
    white-space: pre-wrap;
}

/* ---- Tables ---- */
table {
    border-collapse: collapse;
    width: 100%;
    margin: 8px 0;
    font-size: 9.5pt;
}

th {
    background-color: #e8f0fa;
    border: 1px solid #ccc;
    padding: 5px 9px;
    text-align: left;
    color: #1e40af;
}

td {
    border: 1px solid #ddd;
    padding: 4px 9px;
}

tr:nth-child(even) td {
    background: #f8fafc;
}

/* ---- Page break hints ---- */
h2 {
    page-break-after: avoid;
}

li, tr {
    page-break-inside: avoid;
}
"""


def build_html(md_text: str) -> str:
    html_body = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "nl2br"],
    )
    return (
        "<!DOCTYPE html>"
        "<html><head><meta charset='utf-8'></head>"
        f"<body>{html_body}</body></html>"
    )


def convert(input_path: str, output_path: str) -> None:
    ext = input_path.rsplit(".", 1)[-1].lower()

    if ext in ("html", "htm"):
        # Use the HTML file's own styles as-is; do not apply the Markdown STYLE
        # so the page design, colors, and layout are preserved exactly.
        HTML(filename=input_path).write_pdf(output_path)
    else:
        with open(input_path, encoding="utf-8") as f:
            md_text = f.read()
        html = build_html(md_text)
        HTML(string=html).write_pdf(output_path, stylesheets=[CSS(string=STYLE)])

    print(f"Generated: {output_path}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert Markdown (or HTML) to PDF matching resume.html design"
    )
    parser.add_argument("input", help="Input .md or .html file")
    parser.add_argument(
        "-o",
        "--output",
        help="Output PDF file (default: same name as input with .pdf extension)",
    )
    args = parser.parse_args()

    output = args.output or args.input.rsplit(".", 1)[0] + ".pdf"
    convert(args.input, output)


if __name__ == "__main__":
    main()
