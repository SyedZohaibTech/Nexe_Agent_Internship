import streamlit as st

from agent import run_agent


st.set_page_config(
    page_title="Autonomous Business Agent",
    page_icon="🤖"
)

st.title("🤖 Autonomous Business Agent")


goal = st.text_area(
    "Enter Your Business Goal"
)


if st.button("Run Agent"):

    if goal.strip() == "":

        st.warning("Please enter a goal")

    else:

        with st.spinner("AI Agent is thinking..."):

            result = run_agent(goal)

        st.success("Task Completed ✅")

        st.markdown(result)