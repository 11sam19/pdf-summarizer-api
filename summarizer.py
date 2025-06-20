import pdfplumber
from typing import Optional, List

class PDFSummarizer:
    @staticmethod
    def extract_text(pdf_path: str) -> Optional[str]:
        """Extract raw text from PDF"""
        try:
            with pdfplumber.open(pdf_path) as pdf:
                return " ".join(
                    page.extract_text() 
                    for page in pdf.pages 
                    if page.extract_text()  # Only process pages with text
                )
        except Exception as e:
            print(f"Extraction error: {e}")
            return None

    @staticmethod
    def basic_summary(text: str, sentence_count: int = 5) -> str:
        """Return first N sentences as basic summary
        
        Args:
            text: Input text to summarize
            sentence_count: Number of sentences to return (default: 5)
            
        Returns:
            str: Summary ending with a period
        """
        if not text:
            return ""
        
        # Split into sentences and clean empty strings
        sentences: List[str] = [
            s.strip() 
            for s in text.split('.') 
            if s.strip()
        ]
        
        # Join first N sentences and ensure proper punctuation
        summary = '. '.join(sentences[:sentence_count])
        return f"{summary}." if summary else ""