import pdfplumber
from typing import Optional

class PDFSummarizer:
    @staticmethod
    def extract_text(pdf_path: str) -> Optional[str]:
        """Extract raw text from PDF"""
        try:
            with pdfplumber.open(pdf_path) as pdf:
                return " ".join(page.extract_text() for page in pdf.pages if page.extract_text())
        except Exception as e:
            print(f"Extraction error: {e}")
            return None

    @staticmethod
    def basic_summary(text: str, sentences: int = 5) -> str:
        """Return first N sentences as basic summary"""
        if not text:
            return ""
        
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        return '. '.join(sentences[:sentences]) + '.' if sentences else ""