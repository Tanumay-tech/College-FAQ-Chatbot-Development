import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Download necessary data for NLP
nltk.download('punkt')
nltk.download('stopwords')

st.title("📅 Week 2: NLP Preprocessing Pipeline")

def preprocess_text(text):
    # Transformation steps:
    text = text.lower() # 1. Lowercasing
    text = text.translate(str.maketrans('', '', string.punctuation)) # 2. Punctuation
    tokens = word_tokenize(text) # 3. Tokenization
    
    stop_words = set(stopwords.words('english')) # 4. Stopword removal
    filtered_tokens = [w for w in tokens if not w in stop_words]
    
    return tokens, filtered_tokens

user_input = st.text_input("Enter a query to see the preprocessing (e.g., 'What are the FEES??'):")

if user_input:
    raw_tokens, clean_tokens = preprocess_text(user_input)
    
    st.subheader("Results:")
    st.write(f"**Original Tokens:** {raw_tokens}")
    st.write(f"**Cleaned Keywords:** {clean_tokens}")