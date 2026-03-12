import streamlit as st

def run_week8():
    st.header("📅 Week 8: Fallbacks & Human Handover")
    st.write("This module handles unclear or out-of-scope questions by asking for clarification, offering suggestions, or routing to a human advisor.")

    # A mock list of topics the bot actually understands
    known_topics = ["exam", "fees", "hostel", "admission"]

    st.info("Try asking a known topic like 'exams', then try an out-of-scope question like 'What is the cafeteria menu?', and finally type 'I want to speak to a human'.")

    user_query = st.text_input("Ask the bot a question:", key="w8_input").lower()

    if user_query:
        # 1. Check for explicit human handover request
        if any(word in user_query for word in ["human", "person", "advisor", "contact", "help desk"]):
            st.warning("🤖 **Bot:** It looks like you need specialized help. Let me connect you with a human advisor.")
            st.markdown("### 📞 Human Handover:")
            st.markdown("* **Email:** [support@institute.edu](mailto:support@institute.edu)")
            st.markdown("* **Live Desk:** Room 104, Main Admin Block (9 AM - 4 PM)")
            return # Stop processing further

        # 2. Check if the query matches our known topics
        intent_found = False
        for topic in known_topics:
            if topic in user_query:
                intent_found = True
                st.success(f"🤖 **Bot:** You are asking about **{topic}**. Here is the information you need...")
                # In a real scenario, you'd fetch the answer here
                break

        # 3. Fallback Strategy for Out-of-Scope or Unclear Questions
        if not intent_found:
            st.error("🤖 **Bot:** I'm not entirely sure I understand your question.")
            
            # Offer suggestions (Clarification)
            st.write("**Did you mean to ask about one of these topics?**")
            cols = st.columns(len(known_topics))
            for i, topic in enumerate(known_topics):
                if cols[i].button(topic.capitalize(), key=f"btn_{topic}"):
                    st.success(f"🤖 **Bot:** Ah, you want to know about **{topic}**. Let me get that for you!")
            
            # Provide the safety net (Handover)
            st.divider()
            st.info("Still can't find what you're looking for? You can always reach out to our [Human Help Desk](mailto:support@institute.edu).")

if __name__ == "__main__":
    run_week8()