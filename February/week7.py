import streamlit as st
from nlp_utils import extract_course_info

def run_week7():
    st.header("📅 Week 7: Multi-Turn Conversations")
    st.write("This module uses session state to remember context across multiple messages.")

    # 1. Initialize session state for memory
    # We use a specific key 'w7_context' so it doesn't interfere with other weeks
    if "w7_context" not in st.session_state:
        st.session_state.w7_context = {"intent": None, "semester": None, "course_code": None}

    # A simple mock database to demonstrate the final output
    faq_db = {
        "exam": "The exams for {course} Semester {sem} are scheduled for next month.",
        "fees": "The fees for {course} Semester {sem} are ₹75,000."
    }

    st.info("Try typing this sequence one by one:\n1. 'When is the exam?'\n2. 'For CS'\n3. 'Semester 5'\n4. 'Clear'")

    # Chat interface
    user_query = st.text_input("Talk to the bot:", key="w7_input").lower()

    if user_query:
        # 2. Detect Intent (Mocking Week 5 logic for simplicity)
        if "exam" in user_query:
            st.session_state.w7_context["intent"] = "exam"
        elif "fee" in user_query or "fees" in user_query:
            st.session_state.w7_context["intent"] = "fees"
        elif "reset" in user_query or "clear" in user_query:
            # Allow the user to wipe the memory
            st.session_state.w7_context = {"intent": None, "semester": None, "course_code": None}
            st.success("Memory cleared! Start a new topic.")
            return

        # 3. Extract Entities using the utility file we built in Week 6
        entities = extract_course_info(user_query)
        
        # 4. Update Memory ONLY if new entities are found
        # If the user says "For CS", the semester stays exactly as it was.
        if entities["semester"]:
            st.session_state.w7_context["semester"] = entities["semester"]
        if entities["course_code"]:
            st.session_state.w7_context["course_code"] = entities["course_code"]

        # 5. Fetch variables for readability
        intent = st.session_state.w7_context["intent"]
        sem = st.session_state.w7_context["semester"]
        course = st.session_state.w7_context["course_code"]

        # Display the bot's internal brain so you can see it working
        st.write("### 🧠 Bot's Current Memory:")
        st.json(st.session_state.w7_context)

        st.write("### 🤖 Bot Response:")
        
        # 6. Decision Logic based on combined state
        if not intent:
            st.warning("How can I help you today? (Try asking about exams or fees)")
            
        elif intent and not (sem and course):
            # We know what they want, but missing details! Ask for them.
            missing = []
            if not course: missing.append("branch (e.g., CS or IT)")
            if not sem: missing.append("semester (1-8)")
            st.info(f"I can help with {intent}s! But I need to know your {' and '.join(missing)}.")
            
        elif intent and sem and course:
            # Multi-turn success! We have all the pieces.
            response = faq_db[intent].format(course=course, sem=sem)
            st.success(response)

if __name__ == "__main__":
    run_week7()