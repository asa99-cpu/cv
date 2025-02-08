import pdfkit
from jinja2 import Template
from io import BytesIO

# Manually set wkhtmltopdf path for Streamlit Cloud
PDFKIT_CONFIG = pdfkit.configuration(wkhtmltopdf="/usr/bin/wkhtmltopdf")

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
