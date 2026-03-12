import streamlit as st
from nlp_utils import extract_course_info, extract_dates

def run_week6():
    st.header("📅 Week 6: Entity Recognition")
    st.write("This module extracts specific details (entities) like semesters, course codes, and dates from the user's query.")
    
    # Example prompts to guide the user
    st.info("Try asking: 'When is the SEM 5 CS exam next Monday?' or 'Tell me the timetable for IT semester 3 tomorrow.'")

    user_query = st.text_input("Enter your query:", key="w6_input")

    if user_query:
        # Process the input through our utility functions
        course_entities = extract_course_info(user_query)
        time_entities = extract_dates(user_query)
        
        st.write("### 🔍 Extraction Results:")
        
        # Display the results neatly
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(label="Semester", value=course_entities["semester"] if course_entities["semester"] else "None")
            
        with col2:
            st.metric(label="Course Code", value=course_entities["course_code"] if course_entities["course_code"] else "None")
            
        with col3:
            # Join multiple dates if found, otherwise show "None"
            dates_found = ", ".join(time_entities["dates"]) if time_entities["dates"] else "None"
            st.metric(label="Date/Time", value=dates_found)
            
        # Show how this helps the bot
        st.divider()
        st.write("### 🤖 How the bot sees this:")
        if course_entities["semester"] and course_entities["course_code"]:
            st.success(f"**Bot Internal Logic:** I need to search the database for `{course_entities['course_code']}` department, specifically for Semester `{course_entities['semester']}`.")
        else:
            st.warning("**Bot Internal Logic:** I understand the general question, but I might need to ask the user for their specific semester or branch to give an accurate answer.")

if __name__ == "__main__":
    run_week6()
