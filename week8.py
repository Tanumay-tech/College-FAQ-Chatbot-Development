import streamlit as st

def main():
    st.set_page_config(page_title="Fallback & Handover Demo", page_icon="🤖")
    st.title("🤖 Chatbot: Fallbacks & Handover")
    st.markdown("---")

    
    faq_data = {
        "timings": "The institute operates from 9:00 AM to 5:00 PM, Monday to Friday.",
        "fees": "The tuition fee for the CSE program is ₹1,50,000 per year.",
        "contact": "You can reach the administration at admin@institute.edu.",
    }

    user_query = st.text_input("Ask me about timings, fees, or contact:").lower().strip()

    if user_query:
        found = False
        for key, response in faq_data.items():
            if key in user_query:
                st.success(f"**Bot:** {response}")
                found = True
                break
        

        if not found:
            
            st.warning("**Bot:** I'm sorry, I don't have information on that topic yet.")
            st.info("💡 **Try searching for:** 'fees', 'timings', or 'contact'.")
            
            
            st.markdown("---")
            st.subheader("Still need help? Speak to an advisor")
            col1, col2 = st.columns(2)
            with col1:
                st.link_button("📧 Email Support", "mailto:admin@institute.edu")
            with col2:
                st.link_button("📞 Call Admin Desk", "tel:+911234567890")

if __name__ == "__main__":
    main()