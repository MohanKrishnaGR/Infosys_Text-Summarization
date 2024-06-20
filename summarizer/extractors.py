import requests
from bs4 import BeautifulSoup
import fitz  # PyMuPDF
from docx import Document

def extract_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    paragraphs = soup.find_all('p')
    text = ' '.join([para.get_text() for para in paragraphs])
    return text

def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)
    text = ''
    for page in document:
        text += page.get_text()
    return text

def extract_text_from_docx(docx_path):
    document = Document(docx_path)
    text = ' '.join([para.text for para in document.paragraphs])
    return text
