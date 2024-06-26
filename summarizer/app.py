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

from fastapi import FastAPI, UploadFile, File, Form, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from extractors import extract_text_from_url, extract_text_from_pdf, extract_text_from_docx
from transformers import BartForConditionalGeneration, BartTokenizer
from extractive_summary import generate_summary as generate_extractive_summary

app = FastAPI()

templates = Jinja2Templates(directory="templates")

model = BartForConditionalGeneration.from_pretrained('saved_model', local_files_only=True, trust_remote_code=True)
tokenizer = BartTokenizer.from_pretrained('saved_model', local_files_only=True)

def summarize_text(text):
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)
    summary_ids = model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/summarize-url")
async def summarize_url(url: str = Form(...)):
    text = extract_text_from_url(url)
    abstractive_summary = summarize_text(text)
    extractive_summary = generate_extractive_summary(text)
    return JSONResponse(content={"abstractive_summary": abstractive_summary, "extractive_summary": extractive_summary})

@app.post("/summarize-file")
async def summarize_file(file: UploadFile = File(...)):
    if file.filename.endswith('.pdf'):
        with open(file.filename, 'wb') as f:
            f.write(await file.read())
        text = extract_text_from_pdf(file.filename)
    elif file.filename.endswith('.docx'):
        with open(file.filename, 'wb') as f:
            f.write(await file.read())
        text = extract_text_from_docx(file.filename)
    else:
        return JSONResponse(content={"error": "Unsupported file type"}, status_code=400)

    abstractive_summary = summarize_text(text)
    extractive_summary = generate_extractive_summary(text)
    return JSONResponse(content={"abstractive_summary": abstractive_summary, "extractive_summary": extractive_summary})

@app.post("/summarize-text")
async def summarize_text_direct(text: str = Form(...)):
    abstractive_summary = summarize_text(text)
    extractive_summary = generate_extractive_summary(text)
    return JSONResponse(content={"abstractive_summary": abstractive_summary, "extractive_summary": extractive_summary})

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
