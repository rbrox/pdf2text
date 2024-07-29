import streamlit as st
import fitz
from io import BytesIO
from preprocess import preprocess_text
from apiCalls import fetchData

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
    
    
    # read entire PDF
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    
    # preprocess the text
    st.write(full_text[:10000])
    preprocessed_text = preprocess_text(full_text)
    del full_text
    
    # 
    data = fetchData(preprocessed_text[:10000])
    del preprocessed_text
    st.write("Data from GPT-3:")
    st.json(data)
    