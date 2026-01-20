import openai
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
def summarize_policy(policy_text: str):
    try:
        prompt = f"""
You are an Indian public policy expert.

Summarize the Union Budget in simple language.

Tasks:
1. Summarize key focus areas (max 120 words)
2. Mention benefits for students, middle-income earners, and seniors

Return ONLY valid JSON.

Policy Text:
{policy_text}
"""

        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )

        return response.choices[0].message.content

    except Exception as e:
        print("OPENAI ERROR:", e)
        return "Error generating summary"
