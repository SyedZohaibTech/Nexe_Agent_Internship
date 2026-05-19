from groq import Groq
from dotenv import load_dotenv

import os


load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def run_agent(user_goal):

    prompt = f"""
    You are an Autonomous Business Agent.

    User Goal:
    {user_goal}

    Your task:
    1. Analyze the business idea
    2. Create step-by-step plan
    3. Suggest marketing strategy
    4. Estimate budget
    5. Generate execution logs

    Give professional response.
    """

    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.7
    )

    return response.choices[0].message.content