import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")


def generate_description(obj) -> str:
    response = model.generate_content(f"""
    {obj} use keywords in this object and write description in plain text string in 3-5 lines
    """)
    return response.text
