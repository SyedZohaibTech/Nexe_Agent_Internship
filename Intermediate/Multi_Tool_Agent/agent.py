from groq import Groq
from dotenv import load_dotenv
import os
import requests

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def web_search(query):

    return f"""
Google Search:
https://www.google.com/search?q={query}

Wikipedia:
https://en.wikipedia.org/wiki/{query.replace(" ", "_")}

YouTube:
https://www.youtube.com/results?search_query={query}
"""


def ai_response(prompt):

    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content