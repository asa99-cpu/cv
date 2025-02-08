import streamlit as st
from sections import introduction, education, experience, skills, contact

st.markdown(f'<style>{open("static/styles.css").read()}</style>', unsafe_allow_html=True)

def main():
    st.title("Derin Najmadin Mahamd - CV")

    # Display Profile Image
    st.image("assets/profile_image.jpg", width=150)
    st.subheader("Personal Information")
    st.write("**Name:** Derin Najmadin Mahamd")
    st.write("**Email:** deman.najmadin¢0@gmail.com")
    st.write("**Phone:** 0750 710 40 32")
    st.write("**Date of Birth:** September 9, 1995")
    st.write("**Gender:** Female")
    st.write("**Nationality:** Kurdish")
    st.write("**Languages:** Kurdish, Arabic, English, Persian")

    # Call different sections of the CV
    introduction.show()
    education.show()
    experience.show()
    skills.show()
    contact.show()

if __name__ == "__main__":
    main()
