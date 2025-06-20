from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from summarizer import PDFSummarizer
import tempfile
import os

app = FastAPI(title="PDF Summarizer", version="1.0")

@app.post("/summarize", response_class=JSONResponse)
async def summarize_pdf(file: UploadFile):
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(400, "Only PDF files accepted")
    
    try:
        # Save temp file
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(await file.read())
            tmp_path = tmp.name
        
        # Process
        text = PDFSummarizer.extract_text(tmp_path)
        if not text:
            raise HTTPException(422, "No extractable text found")
        
        summary = PDFSummarizer.basic_summary(text)
        
        return {
            "filename": file.filename,
            "page_count": len(text.split('\f')) if '\f' in text else 1,
            "summary": summary,
            "char_count": len(summary)
        }
        
    finally:
        if 'tmp_path' in locals() and os.path.exists(tmp_path):
            os.unlink(tmp_path)  # Clean up