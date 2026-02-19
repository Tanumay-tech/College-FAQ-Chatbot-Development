import streamlit as st

st.title("📅 Week 5: Intent Classification & Routing")

# 1. Define Intent Buckets
intents = {
    "Admissions": ["apply", "admission", "enroll", "criteria"],
    "Exams": ["exam", "test", "results", "schedule", "timetable"],
    "Hostel": ["room", "dorm", "hostel", "accommodation", "stay"],
    "Scholarships": ["financial aid", "scholarship", "discount", "stipend"]
}

def classify_intent(query):
    query = query.lower()
    for intent, keywords in intents.items():
        if any(keyword in query for keyword in keywords):
            return intent
    return "Unknown"

user_query = st.text_input("Enter your query to route it to an intent (e.g., 'When is the exam?'):")

if user_query:
    intent = classify_intent(user_query)
    
    st.write(f"**Detected Intent:** :blue[{intent}]")
    
    # Routing Logic
    if intent == "Admissions":
        st.info("Routing to Admissions Desk: Visit the main portal to fill out the application.")
    elif intent == "Exams":
        st.info("Routing to Examination Cell: The mid-term schedule will be released next Monday.")
    elif intent == "Hostel":
        st.info("Routing to Warden's Office: Hostel registration is currently open for first-year students.")
    elif intent == "Scholarships":
        st.info("Routing to Accounts Office: Merit-based scholarships are available for scores above 90%.")
    else:
        st.warning("Intent not recognized. Redirecting to General Inquiry...")