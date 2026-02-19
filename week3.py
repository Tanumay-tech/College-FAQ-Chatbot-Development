import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
import string

nltk.download('punkt')

st.title("📅 Week 3: Synonym-Aware FAQ Bot")

synonym_map = {
    "fees": ["tuition", "payment", "cost", "billing", "charges"],
    "hostel": ["accommodation", "dorm", "residence", "stay"],
    "timings": ["hours", "schedule", "open", "close"],
    "contact": ["phone", "email", "address", "reach"]
}

def get_master_keyword(token):
    for master, synonyms in synonym_map.items():
        if token == master or token in synonyms:
            return master
    return token

query = st.text_input("Ask a question (e.g., 'What is the tuition cost?'):").lower()

if query:
    clean_query = query.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(clean_query)
    
    mapped_tokens = [get_master_keyword(t) for t in tokens]
    
    st.write(f"**Tokens Found:** {tokens}")
    st.success(f"**Mapped to Keywords:** {mapped_tokens}")
    
    if "fees" in mapped_tokens:
        st.info("Bot: The tuition fee is ₹1,50,000 per year.")
    elif "hostel" in mapped_tokens:
        st.info("Bot: The hostel is located behind the academic block.")