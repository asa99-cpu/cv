import streamlit as st
from sections import introduction, education, experience, skills, contact

def main():
    st.title("My CV")

    # Display profile image
    st.image("assets/profile_image.jpg", width=150)

    # Call different sections of the CV
    introduction.show()
    education.show()
    experience.show()
    skills.show()
    contact.show()

if __name__ == "__main__":
    main()
