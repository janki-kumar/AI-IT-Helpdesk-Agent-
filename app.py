import streamlit as st

st.set_page_config(page_title="AI IT Helpdesk Agent", page_icon="🤖")

st.title("🤖 AI-IT-Helpdesk-Agent")
st.write("AI-powered IT support assistant for automated issue classification")

issue = st.text_area("Apna IT Issue Likho:", placeholder="Ex: My laptop is not connecting to WiFi")

if st.button("Submit Issue"):
    if issue:
        # Simple AI Logic
        issue_lower = issue.lower()
        if "wifi" in issue_lower or "network" in issue_lower or "internet" in issue_lower:
            category = "Network Issue"
            solution = "1. Router restart karo\n2. Network settings check karo\n3. Forget and Reconnect karo"
            priority = "High"
        elif "password" in issue_lower or "login" in issue_lower or "access" in issue_lower:
            category = "Access Issue"
            solution = "1. Password reset link pe jao\n2. IT admin se contact karo"
            priority = "Medium"
        elif "slow" in issue_lower or "hang" in issue_lower or "software" in issue_lower:
            category = "Software Issue"
            solution = "1. System restart karo\n2. Task Manager se extra apps band karo"
            priority = "Medium"
        else:
            category = "Hardware Issue"
            solution = "Ticket has been created. IT Team will contact you soon."
            priority = "Low"

        st.success(f"Ticket Created Successfully!")
        st.write(f"**Category:** {category}")
        st.write(f"**Priority:** {priority}")
        st.write(f"**Suggested Solution:**")
        st.code(solution)
    else:
        st.warning("Please enter your issue first!")

st.markdown("---")
st.caption("Made by Janki Kumar | B.Tech Project")
