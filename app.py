import weasyprint
from jinja2 import Template
from io import BytesIO

def create_pdf_cv(data):
    # Load HTML template
    with open("templates/cv_template.html", "r") as file:
        template = Template(file.read())

    # Render the HTML content with provided data
    html_content = template.render(data)

    # Convert HTML to PDF using WeasyPrint
    pdf_buffer = BytesIO()
    weasyprint.HTML(string=html_content).write_pdf(pdf_buffer)
    pdf_buffer.seek(0)
    return pdf_buffer

# (The rest of your app code goes here.)
