import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def summarize_policy(policy_text: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a policy analyst."},
            {"role": "user", "content": f"Summarize this policy:\n{policy_text}"}
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content
