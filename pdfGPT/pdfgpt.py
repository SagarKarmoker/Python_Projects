import requests
import streamlit as st
from dotenv import load_dotenv
import fitz  # PyMuPDF
import os

load_dotenv()
API= os.getenv('API')

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": API}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	

# Streamlit app header
st.title("pdfGPT: PDF Text to summarised PDF Text")

# File upload widget
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

# Display PDF content if a file is uploaded
if uploaded_file is not None:
    # Check if an uploaded file exists and is of PDF type
    
    # Read PDF file as bytes
    pdf_bytes = uploaded_file.read()

    # Create a PyMuPDF document object
    pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")
    
    # Extract text from each page
    pdf_text = ""
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        pdf_text += page.get_text()

    # Close the PyMuPDF document object
    pdf_document.close()

    # Display the extracted PDF text
    st.write("PDF summarised Text:")
    output = query({
	"inputs": pdf_text
    })

    summary_text = output[0]['summary_text']
    st.write(summary_text)



