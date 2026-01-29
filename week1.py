import streamlit as st

def run_week1():
    st.header("📅 Week 1: Rule-Based FAQ Responder")
    st.write("This bot answers fixed questions using exact pattern matching.")

    # 1. Define the FAQ Dictionary
    faq_data = {
        "timings": "The institute operates from 9:00 AM to 5:00 PM, Monday to Friday.",
        "fees": "The tuition fee for the CSE program is ₹1,50,000 per year.",
        "contact": "You can reach the administration at admin@institute.edu or +91-1234567890.",
        "admission": "Admissions are open from May to July based on entrance exam scores.",
        "hostel": "Separate hostels for boys and girls are available within the campus.",
        "location": "The campus is located in the North Education Hub, Sector 42."
    }

    # 2. User Input
    user_query = st.text_input("Ask a question (e.g., timings, fees, contact):").lower().strip()

    # 3. Logic: Pattern Matching
    if user_query:
        found = False
        for key in faq_data:
            if key in user_query: # Check if the keyword exists in the user's sentence
                st.success(f"**Bot:** {faq_data[key]}")
                found = True
                break
        
        if not found:
            st.error("**Bot:** I'm sorry, I don't have information on that topic yet.")

    # Show the "Database" on the website so the user knows what to ask
    with st.expander("View Supported Keywords"):
        st.write(list(faq_data.keys()))

if __name__ == "__main__":
    run_week1()