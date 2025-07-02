def clean_text(text):
    # Function to clean Vietnamese text by removing unwanted characters and normalizing whitespace
    import re
    text = re.sub(r'\s+', ' ', text)  # Normalize whitespace
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text.strip()

def tokenize_text(text):
    # Function to tokenize Vietnamese text into words
    from vncorenlp import VnCoreNLP
    tokenizer = VnCoreNLP("http://127.0.0.1:9000")  # Ensure VnCoreNLP server is running
    tokens = tokenizer.tokenize(text)
    return [word for sentence in tokens for word in sentence]

def preprocess_text(text):
    # Function to preprocess Vietnamese text for summarization
    cleaned_text = clean_text(text)
    tokens = tokenize_text(cleaned_text)
    return tokens

def extract_keywords(text, num_keywords=10):
    # Function to extract keywords from Vietnamese text using a simple frequency-based approach
    from collections import Counter
    tokens = preprocess_text(text)
    keyword_freq = Counter(tokens)
    return keyword_freq.most_common(num_keywords)