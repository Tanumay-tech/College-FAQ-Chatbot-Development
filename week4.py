import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("📅 Week 4: Retrieval-Based Chatbot (TF-IDF)")

# The FAQ Dataset
faq_data = {
    "What are the institute timings?": "The institute operates from 9:00 AM to 5:00 PM, Monday to Friday.",
    "How much is the tuition fee?": "The tuition fee for the CSE program is ₹1,50,000 per year.",
    "How can I contact the administration?": "You can reach us at admin@institute.edu or +91-1234567890.",
    "Is there a hostel facility?": "Separate hostels for boys and girls are available within the campus.",
    "Where is the campus located?": "The campus is located in the North Education Hub, Sector 42."
}

questions = list(faq_data.keys())

user_query = st.text_input("Ask the bot anything about the institute:")

if user_query:
    # 1. Initialize TF-IDF Vectorizer
    vectorizer = TfidfVectorizer()
    
    # 2. Fit and transform the FAQ questions + user query
    tfidf_matrix = vectorizer.fit_transform(questions + [user_query])
    
    # 3. Calculate Cosine Similarity between user query and all FAQ questions
    # The user query is the last item in the matrix
    similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    
    # 4. Find the index of the most similar question
    best_match_idx = similarities.argmax()
    confidence = similarities[0][best_match_idx]

    if confidence > 0.2: # Threshold to ensure it's a decent match
        matched_question = questions[best_match_idx]
        st.success(f"**Matched Question:** {matched_question}")
        st.info(f"**Bot:** {faq_data[matched_question]}")
    else:
        st.error("Bot: I'm sorry, I couldn't find a relevant answer.")