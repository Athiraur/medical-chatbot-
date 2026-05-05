import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv() #to load env file

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def medical_response(user_input: str):

    system_prompt = """
    You are strictly a medical assistant.
    You must ONLY answer health-related questions.
    If the user asks anything unrelated to health,
    respond with:
    'I am a medical chatbot. Please ask health-related questions only.'
    Never answer non-medical questions.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        temperature=0.5 #creativity of AI responses(balanced)
    )

    return response.choices[0].message.content