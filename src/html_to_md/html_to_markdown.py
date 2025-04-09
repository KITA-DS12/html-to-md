import os
from pathlib import Path
from markdownify import markdownify as md

def convert_html_to_markdown(base_dir: str | Path) -> None:
    """
    Convert HTML files in the html directory to Markdown files in the markdown directory.
    
    Args:
        base_dir (str | Path): Base directory containing html and markdown directories
    """
    base_dir = Path(base_dir)
    html_dir = base_dir / "html"
    markdown_dir = base_dir / "markdown"
    
    # Create markdown directory if it doesn't exist
    markdown_dir.mkdir(exist_ok=True)
    
    # Get all HTML files
    html_files = list(html_dir.glob("*.html"))
    
    for html_file in html_files:
        # Read HTML content
        with open(html_file, "r", encoding="utf-8") as f:
            html_content = f.read()
        
        # Convert to Markdown
        markdown_content = md(html_content)
        
        # Create markdown file path
        markdown_file = markdown_dir / html_file.with_suffix(".md").name
        
        # Write markdown content
        with open(markdown_file, "w", encoding="utf-8") as f:
            f.write(markdown_content)
            
        print(f"Converted {html_file.name} to {markdown_file.name}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python html_to_markdown.py <base_directory>")
        sys.exit(1)
        
    base_dir = sys.argv[1]
    convert_html_to_markdown(base_dir) 