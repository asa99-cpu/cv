import streamlit as st
import json
from jinja2 import Template

# Load the CV data from JSON file
with open('data/cv_data.json', 'r') as f:
    cv_data = json.load(f)

# Set the profile image path
profile_image = 'assets/profile.jpg'  # Add your actual profile image path

# Create the HTML template
with open('templates/cv_template.html', 'r') as f:
    template_content = f.read()

# Render the CV using Jinja2
template = Template(template_content)
cv_html = template.render(
    name=cv_data['personal_details']['name'],
    email=cv_data['personal_details']['email'],
    phone=cv_data['personal_details']['phone'],
    dob=cv_data['personal_details']['dob'],
    gender=cv_data['personal_details']['gender'],
    nationality=cv_data['personal_details']['nationality'],
    profile_image=profile_image,
    education=cv_data['education'],
    skills=cv_data['skills'],
    languages=cv_data['personal_details']['languages'],
    internships=cv_data['internships']
)

# Display the CV in Streamlit
st.markdown(cv_html, unsafe_allow_html=True)

# Option to download the CV as a Word document (using python-docx or other libraries)
st.download_button(
    label="Download CV as Word Document",
    data="Word document content goes here",  # Add your method to generate Word file here
    file_name="cv.docx",
    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
)

# Option to download the CV as a PDF (if you want)
st.download_button(
    label="Download CV as PDF",
    data="PDF content goes here",  # Add your method to generate PDF here
    file_name="cv.pdf",
    mime="application/pdf"
)
