'''
   =======================================================================
   
   Copyright 2024 Mohan Krishna G R

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

   =======================================================================
'''

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
