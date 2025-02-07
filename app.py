import streamlit as st
import pytesseract
from PIL import Image

st.title("CV Image to Text Converter")

# Upload CV image
uploaded_file = st.file_uploader("Upload your CV image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded CV", use_column_width=True)

    # Extract text
    extracted_text = pytesseract.image_to_string(image)

    # Display extracted text
    st.subheader("Extracted Text")
    st.text_area("CV Text", extracted_text, height=300)

    # Save extracted text as a file
    with open("cv_text.txt", "w", encoding="utf-8") as f:
        f.write(extracted_text)

    st.success("Text extraction complete! Download the extracted text below.")
    st.download_button("Download Extracted Text", extracted_text, file_name="cv_text.txt")
