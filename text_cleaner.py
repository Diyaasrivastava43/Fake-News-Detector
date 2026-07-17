import re

# Pre-compile the regex patterns outside the function so they only compile ONCE
HTML_CLEANER = re.compile(r'<[^>]*>')
URL_CLEANER = re.compile(r'https?://\S+|www\.\S+')
CHAR_CLEANER = re.compile(r'[^a-zA-Z\s]')
SPACE_CLEANER = re.compile(r'\s+')

def clean_news_text(text):
    """
    Highly optimized string sanitization pipeline for large Pandas datasets.
    """
    if not isinstance(text, str):
        return ""
    
    text = text.lower()
    text = HTML_CLEANER.sub('', text)
    text = URL_CLEANER.sub('', text)
    text = CHAR_CLEANER.sub('', text)
    text = SPACE_CLEANER.sub(' ', text).strip()
    
    return text