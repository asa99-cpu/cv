import streamlit as st
import json
import docx
from io import BytesIO
from jinja2 import Template
import pdfkit  # Replacing WeasyPrint

# Load CV data from JSON file
with open("data/cv_data.json", "r") as file:
    cv_data = json.load(file)

# Function to generate Word CV dynamically
def create_word_cv(data):
    doc = docx.Document()
    
    doc.add_heading(data["name"], level=1)
    doc.add_paragraph(f"📞 Phone: {data['phone']}")
    doc.add_paragraph(f"📧 Email: {data['email']}")
    doc.add_paragraph(f"🎂 Date of Birth: {data['dob']}")
    doc.add_paragraph(f"🏠 Nationality: {data['nationality']}")

    doc.add_heading("Education", level=2)
    doc.add_paragraph(data["education"])

    doc.add_heading("Skills", level=2)
    for skill in data["skills"]:
        doc.add_paragraph(f"• {skill}")

    doc.add_heading("Languages", level=2)
    for language in data["languages"]:
        doc.add_paragraph(f"• {language}")

    doc.add_heading("Internships", level=2)
    for internship in data["internships"]:
        doc.add_paragraph(f"• {internship}")

    # Save to memory
    buffer = BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    return buffer

# Function to generate PDF CV dynamically
def create_pdf_cv(data):
    with open("templates/cv_template.html", "r") as file:
        template = Template(file.read())

    html_content = template.render(data)

    # Convert HTML to PDF using pdfkit
    pdf_buffer = BytesIO()
    pdfkit.from_string(html_content, pdf_buffer)
    pdf_buffer.seek(0)
    return pdf_buffer

# Streamlit App
st.title("📄 CV Generator")

st.subheader(cv_data["name"])
st.write(f"📞 **Phone:** {cv_data['phone']}")
st.write(f"📧 **Email:** {cv_data['email']}")
st.write(f"🎂 **Date of Birth:** {cv_data['dob']}")
st.write(f"🏠 **Nationality:** {cv_data['nationality']}")

st.subheader("Education")
s
