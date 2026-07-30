# utils/preprocessing.py
import re

def clean_text(text):
    text = text.lower()
    
    # remove urls
    text = re.sub(r"http\S+", "", text)
    
    # remove mentions
    text = re.sub(r"@\w+", "", text)
    
    # remove hashtags symbol only
    text = re.sub(r"#", "", text)
    
    # remove special characters
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    
    # remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()
    
    return text 