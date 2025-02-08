import os
import pdfkit
from jinja2 import Template
from io import BytesIO
import subprocess

# Try to find the path of wkhtmltopdf in the environment
def find_wkhtmltopdf():
    try:
        # Check if wkhtmltopdf is installed in the environment
        result = subprocess.run(['which', 'wkhtmltopdf'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode().strip()  # Return the path
    except Exception as e:
        return None

wkhtmltopdf_path = find_wkhtmltopdf()

if not wkhtmltopdf_path:
    raise Exception("wkhtmltopdf is not installed in the environment")

# Manually set the wkhtmltopdf path for pdfkit
PDFKIT_CONFIG = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

def create_pdf_cv(data):
    # Load HTML template
    with open("templates/cv_template.html", "r") as file:
        template = Template(file.read())

    # Render the HTML content with provided data
    html_content = template.render(data)

    # Convert HTML to PDF
    pdf_buffer = BytesIO()
    pdfkit.from_string(html_content, "cv.pdf", configuration=PDFKIT_CONFIG)
    with open("cv.pdf", "rb") as f:
        pdf_buffer.write(f.read())
    pdf_buffer.seek(0)
    return pdf_buffer
