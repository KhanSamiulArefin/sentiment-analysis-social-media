# app/utils.py
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
nltk.download('stopwords')

# Stopwords removal
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"@\S+", "", text)     # Remove @mentions
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # Remove special characters
    text = text.lower()  # Convert to lowercase
    
    words = word_tokenize(text)
    filtered_text = [word for word in words if word not in stop_words]  # Remove stopwords
    return ' '.join(filtered_text)