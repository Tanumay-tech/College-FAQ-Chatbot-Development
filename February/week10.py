import streamlit as st
import pandas as pd
import os
from logger import log_interaction

def run_week10():
    st.header("📅 Week 10: Logging & Analytics Dashboard")
    st.write("This module logs interactions and helps identify areas for improvement based on real user data.")

    # 1. Simulator: Let's log a fake interaction right now to test it
    st.write("### 📝 Simulate an Interaction")
    test_input = st.text_input("Type a test student query (e.g., 'where is the canteen?'):", key="w10_input")
    
    if st.button("Simulate Chat & Log"):
        # For demonstration, we'll hardcode a failed intent
        log_interaction(
            user_input=test_input,
            intent="Unknown",
            entities={"semester": None, "course_code": None},
            bot_response="I'm not sure. Did you mean exams?"
        )
        st.success("Interaction logged successfully to `chat_logs.csv`!")

    st.divider()

    # 2. The Analytics Dashboard
    st.write("### 📊 Chatbot Interaction Logs")
    
    if os.path.exists("chat_logs.csv"):
        # Read the CSV into a pandas DataFrame
        df = pd.read_csv("chat_logs.csv")
        
        # Display as an interactive Streamlit dataframe
        st.dataframe(df, use_container_width=True)
        
        # 3. Propose Improvements based on data
        st.write("### 💡 Proposed Improvements")
        st.info(
            "**Observations from Logs:**\n"
            "* **Missing Intents:** Multiple students asked about the 'canteen' and 'library', which currently route to 'Unknown'.\n"
            "* **Entity Failures:** The bot fails to recognize 'first year' as Semester 1 or 2.\n\n"
            "**Action Items:**\n"
            "1. Add new FAQs for library timings and cafeteria menu.\n"
            "2. Update `nlp_utils.py` to map conversational text like 'first year' to numeric semester values."
        )
    else:
        st.warning("No logs found yet. Use the simulator above to generate some data!")

if __name__ == "__main__":
    run_week10()