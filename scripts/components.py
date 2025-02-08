import streamlit as st

def display_cv(cv_text):
    st.image("assets/cv_image.jpg", caption="Derin Najmadin Mahamd", use_column_width=True)
    
    sections = parse_cv_text(cv_text)

    st.markdown("## Personal Details")
    st.write(sections.get("Personal details", "N/A"))

    st.markdown("## Skills")
    st.write(sections.get("Skills", "N/A"))

    st.markdown("## Education")
    st.write(sections.get("Education", "N/A"))

    st.markdown("## Languages")
    st.write(sections.get("Languages", "N/A"))

    st.markdown("## Internships")
    st.write(sections.get("Internships", "N/A"))

def parse_cv_text(cv_text):
    sections = {}
    lines = cv_text.split("\n")
    current_section = None

    for line in lines:
        line = line.strip()
        if line.endswith(")"):
            current_section = line.strip("()")
            sections[current_section] = ""
        elif current_section:
            sections[current_section] += line + "\n"

    return sections

