import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
import string

def run_week3():
    st.header("📅 Week 3: Synonym-Aware FAQ Bot")
    nltk.download('punkt')

    synonym_map = {
        "fees": ["tuition", "payment", "cost", "billing"],
        "hostel": ["accommodation", "dorm", "residence"],
        "timings": ["hours", "schedule", "open"],
        "contact": ["phone", "email", "reach"]
    }

    def get_master_keyword(token):
        for master, synonyms in synonym_map.items():
            if token == master or token in synonyms:
                return master
        return token

    query = st.text_input("Ask a question:", key="w3_input").lower()

    if query:
        clean_query = query.translate(str.maketrans('', '', string.punctuation))
        tokens = word_tokenize(clean_query)
        mapped_tokens = [get_master_keyword(t) for t in tokens]
        
        st.write(f"**Tokens Found:** {tokens}")
        st.success(f"**Mapped to Keywords:** {mapped_tokens}")
