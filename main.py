from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from summarizer import PDFSummarizer
import tempfile
import os

app = FastAPI(
    title="PDF Summarizer API",
    version="1.0",
    description="Extracts and summarizes text from PDF files"
)

@app.post("/summarize", response_class=JSONResponse)
async def summarize_pdf(file: UploadFile):
    """Endpoint for PDF text extraction and summarization"""
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files accepted")
    
    try:
        # Save temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp:
            content = await file.read()
            tmp.write(content)
            tmp_path = tmp.name
        
        # Process PDF
        text = PDFSummarizer.extract_text(tmp_path)
        if not text:
            raise HTTPException(
                status_code=422,
                detail="No extractable text found (may be scanned PDF)"
            )
        
        summary = PDFSummarizer.basic_summary(text)
        
        return {
            "filename": file.filename,
            "page_count": text.count('\f') + 1,  # More accurate page count
            "summary": summary,
            "char_count": len(summary),
            "status": "success"
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Processing failed: {str(e)}"
        )
        
    finally:
        if 'tmp_path' in locals() and os.path.exists(tmp_path):
            try:
                os.unlink(tmp_path)
            except:
                pass  # Silent cleanup