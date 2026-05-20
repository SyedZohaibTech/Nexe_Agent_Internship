import streamlit as st

from groq import Groq
from dotenv import load_dotenv

import os
import json

from calculator import (
    add,
    subtract,
    multiply,
    divide,
    show_memory
)

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

tools = {

    "add": add,

    "subtract": subtract,

    "multiply": multiply,

    "divide": divide,

    "memory": show_memory
}

system_prompt = """
You are an AI Calculator Agent.

Rules:
- Always respond in JSON.
- Use calculator tools only.
- If user asks addition → use add
- subtraction → subtract
- multiplication → multiply
- division → divide
- memory/history → memory

Examples:

{
  "tool": "add",
  "args": {
    "a": 5,
    "b": 10
  }
}

{
  "tool": "memory",
  "args": {}
}
"""

st.set_page_config(
    page_title="AI Calculator Agent",
    page_icon="🧮"
)

st.title("🧮 AI Calculator Agent")

user_input = st.text_input(
    "Enter Your Math Prompt"
)

if st.button("Calculate"):

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

            st.success("Calculation Completed ✅")

            st.json(result)

        else:

            st.error("Unknown Tool")

    except Exception as e:

        st.error(str(e))