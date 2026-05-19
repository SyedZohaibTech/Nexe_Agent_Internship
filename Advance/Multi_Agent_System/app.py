import streamlit as st
from agents import run_multi_agent_system

st.set_page_config(
    page_title="Multi-Agent AI System",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Multi-Agent AI System")

topic = st.text_area(
    "Enter Topic",
    placeholder="Example: Build an AI Startup"
)

if st.button("Run Multi-Agent System"):

    if topic.strip() == "":
        st.warning("Please enter a topic")
    else:

        with st.spinner("Agents Working..."):

            result = run_multi_agent_system(topic)

        st.success("Task Completed ✅")

        st.subheader("🔍 Research Agent")
        st.write(result["research"])

        st.subheader("📌 Planning Agent")
        st.write(result["planning"])

        st.subheader("🧠 Content Agent")
        st.write(result["final_output"])