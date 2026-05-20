import streamlit as st

from groq import Groq
from dotenv import load_dotenv

import os
import json

from tools import (
    get_time,
    add,
    multiply
)

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

tools = {

    "get_time": get_time,

    "add": add,

    "multiply": multiply
}

system_prompt = """
You are a Tool Calling AI Agent.

Rules:
- Always respond in JSON
- If user asks time → use get_time
- If user asks addition → use add
- If user asks multiplication → use multiply

Examples:

{
  "tool": "get_time",
  "args": {}
}

{
  "tool": "add",
  "args": {
    "a": 5,
    "b": 10
  }
}
"""

st.set_page_config(
    page_title="Tool Calling AI Agent",
    page_icon="🤖"
)

st.title("🤖 Tool Calling AI Agent")

user_input = st.text_input(
    "Enter Your Prompt"
)

if st.button("Run Agent"):

    try:

        response = client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        )

        content = response.choices[0].message.content

        data = json.loads(content)

        tool_name = data["tool"]

        args = data["args"]

        if tool_name in tools:

            result = tools[tool_name](**args)

            st.success("Task Completed ✅")

            st.json(result)

        else:

            st.error("Unknown Tool")

    except Exception as e:

        st.error(str(e))