import streamlit as st
from sections import introduction, skills, education, languages, internships, contact

def main():
    st.title("Derin Najmadin Mahamd's CV")

    # Display profile image
    st.image("assets/profile_image.jpg", width=150)

    # Call different sections of the CV
    introduction.show()
    skills.show()
    education.show()
    languages.show()
    internships.show()
    contact.show()

if __name__ == "__main__":
    main()
