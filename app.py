import streamlit as st
from jinja2 import Template
import json

# Load the CV data from JSON file
with open('data/cv_data.json') as f:
    cv_data = json.load(f)

# Load the CV template HTML file
with open('templates/cv_template.html', 'r') as f:
    template_content = f.read()

# Create a Jinja2 Template object
template = Template(template_content)

# Render the HTML template with the dynamic data
rendered_html = template.render(
    name=cv_data['name'],
    profile_image='assets/profile.jpg',  # Image path
    email=cv_data['email'],
    phone=cv_data['phone'],
    dob=cv_data['dob'],
    gender=cv_data['gender'],
    nationality=cv_data['nationality'],
    education=cv_data['education'],
    skills=cv_data['skills'],
    languages=cv_data['languages'],
    internships=cv_data['internships']
)

# Display the rendered HTML in the Streamlit app
st.markdown(rendered_html, unsafe_allow_html=True)
