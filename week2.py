import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

def run_week2():
    st.header("📅 Week 2: NLP Preprocessing Pipeline")
    
    nltk.download('punkt')
    nltk.download('stopwords')

    def preprocess_text(text):
        text = text.lower() 
        text = text.translate(str.maketrans('', '', string.punctuation)) 
        tokens = word_tokenize(text) 
        stop_words = set(stopwords.words('english')) 
        filtered_tokens = [w for w in tokens if not w in stop_words]
        return tokens, filtered_tokens

    user_input = st.text_input("Enter a query to see the preprocessing:", key="w2_input")

    if user_input:
        raw_tokens, clean_tokens = preprocess_text(user_input)
        st.write(f"**Original Tokens:** {raw_tokens}")
        st.write(f"**Cleaned Keywords:** {clean_tokens}")
