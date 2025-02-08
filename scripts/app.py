import streamlit as st
from scripts.components import display_cv

# Page Configuration
st.set_page_config(page_title="Derin Najmadin Mahamd - CV", page_icon="📄", layout="wide")

# Apply custom CSS
with open("styles/styles.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

# Load CV data
with open("data/cv_text.txt", "r", encoding="utf-8") as file:
    cv_text = file.read()

# Display CV
display_cv(cv_text)
