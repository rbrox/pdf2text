import streamlit as st
import fitz
from io import BytesIO
from preprocess import preprocess_text

# Streamlit app layout
st.title("PDF Processing Pipeline")

# File uploader
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    st.success(f"Uploaded file: {uploaded_file.name}")
    st.write(f"File size: {uploaded_file.size} bytes")
    st.write(f"File type: {uploaded_file.type}")
    file_bytes = BytesIO(uploaded_file.read())
    
    # Open the PDF using PyMuPDF from the in-memory file
    doc = fitz.open(stream=file_bytes, filetype="pdf")
    
    # Extract text from the first page (for demo purposes)
    first_page = doc.load_page(0)
    first_page_text = first_page.get_text()
    
    
    st.write("Text from the first page:")
    st.write(first_page_text[:1000])  # Display the first 1000 characters
    
    # read entire PDF
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    
    # preprocess the text
    
    preprocessed_text = preprocess_text(full_text)
    del full_text
    
    st.write("Preprocessed text:" + preprocessed_text[:1000])
    