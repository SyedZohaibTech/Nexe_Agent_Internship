from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def ask_agent(role, task):

    prompt = f"""
    You are a {role}.

    Task:
    {task}

    Give clear and professional response.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


def run_multi_agent_system(topic):

    # Research Agent
    research = ask_agent(
        "Research Agent",
        f"Research about: {topic}"
    )

    # Planning Agent
    planning = ask_agent(
        "Planning Agent",
        f"""
        Based on this research:

        {research}

        Create step-by-step plan.
        """
    )

    # Content Agent
    final_output = ask_agent(
        "Content Agent",
        f"""
        Research:
        {research}

        Plan:
        {planning}

        Generate final professional report.
        """
    )

    return {
        "research": research,
        "planning": planning,
        "final_output": final_output
    }