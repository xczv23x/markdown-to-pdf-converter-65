import markdown
from xhtml2pdf import pisa
import sys

def convert_md_to_pdf(source_file, output_file):
    """
    Converts a Markdown file to a PDF document using markdown and xhtml2pdf.
    Requires: pip install markdown xhtml2pdf
    """
    try:
        with open(source_file, 'r', encoding='utf-8') as f:
            text = f.read()
        
        # Convert markdown to basic HTML structure
        html_body = markdown.markdown(text)
        html_content = f'<html><head><style>body {{ font-family: Helvetica, sans-serif; margin: 40px; }}</style></head><body>{html_body}</body></html>'
        
        # Convert HTML to PDF
        with open(output_file, 'wb') as f:
            pisa_status = pisa.CreatePDF(html_content, dest=f)
            
        if pisa_status.err:
            print('Error: Conversion process failed.')
        else:
            print(f'Success: Generated {output_file}')
            
    except FileNotFoundError:
        print(f'Error: The file {source_file} was not found.')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print('Usage: python converter.py <input.md> <output.pdf>')
    else:
        convert_md_to_pdf(sys.argv[1], sys.argv[2])