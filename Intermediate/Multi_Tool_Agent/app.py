import streamlit as st

from agent import (
    web_search,
    ai_response
)

from database import (
    save_search,
    get_history
)

from email_sender import send_email

st.set_page_config(
    page_title="Multi Tool AI Agent",
    page_icon="🤖"
)

st.title("🤖 Multi Tool AI Agent")

tool = st.sidebar.selectbox(

    "Select Tool",

    [
        "Web Search",
        "AI Chat",
        "Send Email",
        "History"
    ]
)

# WEB SEARCH
if tool == "Web Search":

    query = st.text_input(
        "Enter Search Query"
    )

    if st.button("Search"):

        result = web_search(query)

        save_search(query, result)

        st.success("Search Completed ✅")

        st.write(result)

# AI CHAT
elif tool == "AI Chat":

    prompt = st.text_area(
        "Ask AI Anything"
    )

    if st.button("Generate"):

        response = ai_response(prompt)

        st.success("Response Generated ✅")

        st.write(response)

# SEND EMAIL
elif tool == "Send Email":

    receiver = st.text_input(
        "Receiver Email"
    )

    subject = st.text_input(
        "Subject"
    )

    body = st.text_area(
        "Message"
    )

    if st.button("Send"):

        result = send_email(
            receiver,
            subject,
            body
        )

        st.success(result)

# HISTORY
elif tool == "History":

    history = get_history()

    st.subheader("📜 Search History")

    for item in history:

        st.write(f"🔍 {item[0]}")

        st.write(item[1])

        st.divider()