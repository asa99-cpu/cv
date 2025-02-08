import streamlit as st
import json
import docx
from io import BytesIO
from jinja2 import Template
from weasyprint import HTML

# Load CV data from JSON file
with open("data/cv_data.json", "r") as file:
    cv_data = json.load(file)

# Function to generate Word CV dynamically
def create_word_cv(data):
    doc = docx.Document()

    # Title
    doc.add_heading(data["name"], level=1)

    # Contact Information
    doc.add_paragraph(f"📞 Phone: {data['phone']}")
    doc.add_paragraph(f"📧 Email: {data['email']}")
    doc.add_paragraph(f"🎂 Date of Birth: {data['dob']}")
    doc.add_paragraph(f"🏠 Nationality: {data['nationality']}")

    # Education
    doc.add_heading("Education", level=2)
    doc.add_paragraph(data["education"])

    # Skills
    doc.add_heading("Skills", level=2)
    for skill in data["skills"]:
        doc.add_paragraph(f"• {skill}")

    # Languages
    doc.add_heading("Languages", level=2)
    for language in data["languages"]:
        doc.add_paragraph(f"• {language}")

    # Internships
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
    pdf_buffer = BytesIO()
    HTML(string=html_content).write_pdf(pdf_buffer)
    pdf_buffer.seek(0)
    return pdf_buffer

# Streamlit App
st.title("📄 CV Generator")

# Show CV details
st.subheader(cv_data["name"])
st.write(f"📞 **Phone:** {cv_data['phone']}")
st.write(f"📧 **Email:** {cv_data['email']}")
st.write(f"🎂 **Date of Birth:** {cv_data['dob']}")
st.write(f"🏠 **Nationality:** {cv_data['nationality']}")

st.subheader("Education")
st.write(cv_data["education"])

st.subheader("Skills")
st.write(", ".join(cv_data["skills"]))

st.subheader("Languages")
st.write(", ".join(cv_data["languages"]))

st.subheader("Internships")
for internship in cv_data["internships"]:
    st.write(f"- {internship}")

# Download buttons
st.subheader("Download CV")
word_buffer = create_word_cv(cv_data)
st.download_button("📥 Download as Word", word_buffer, file_name="cv.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")

pdf_buffer = create_pdf_cv(cv_data)
st.download_button("📥 Download as PDF", pdf_buffer, file_name="cv.pdf", mime="application/pdf")
