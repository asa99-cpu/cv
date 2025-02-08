import streamlit as st
import json
import jinja2
from docx import Document
import pdfkit
from io import BytesIO

# Load CV data
with open('data/cv_data.json', 'r') as f:
    cv_data = json.load(f)

# Set up the Streamlit layout
st.title(f"CV of {cv_data['name']}")

# Load and render the CV template with Jinja2
template_loader = jinja2.FileSystemLoader(searchpath="templates")
template_env = jinja2.Environment(loader=template_loader)
template = template_env.get_template("cv_template.html")

html_content = template.render(
    name=cv_data['name'],
    email=cv_data['email'],
    phone=cv_data['phone'],
    dob=cv_data['dob'],
    gender=cv_data['gender'],
    education=cv_data['education'],
    languages=", ".join(cv_data['languages']),
    internship=cv_data['internship'],
    skills=cv_data['skills']
)

# Display the CV in Streamlit
st.markdown(html_content, unsafe_allow_html=True)

# Function to generate Word document
def generate_word():
    doc = Document()
    doc.add_heading(cv_data['name'], 0)
    doc.add_paragraph(f"Email: {cv_data['email']}")
    doc.add_paragraph(f"Phone: {cv_data['phone']}")
    doc.add_paragraph(f"Date of Birth: {cv_data['dob']}")
    doc.add_paragraph(f"Gender: {cv_data['gender']}")
    doc.add_paragraph(f"Education: {cv_data['education']}")
    doc.add_paragraph(f"Languages: {', '.join(cv_data['languages'])}")
    doc.add_paragraph(f"Internship: {cv_data['internship']}")
    doc.add_heading("Skills", level=1)
    for skill in cv_data['skills']:
        doc.add_paragraph(skill)
    
    # Save to a BytesIO object for download
    doc_io = BytesIO()
    doc.save(doc_io)
    doc_io.seek(0)
    return doc_io

# Function to generate PDF
def generate_pdf(html_content):
    pdf = pdfkit.from_string(html_content, False)
    return BytesIO(pdf)

# Add download buttons
st.download_button(
    label="Download CV as Word",
    data=generate_word(),
    file_name="cv.docx",
    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
)

st.download_button(
    label="Download CV as PDF",
    data=generate_pdf(html_content),
    file_name="cv.pdf",
    mime="application/pdf"
)
