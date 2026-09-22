import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
MODEL = os.getenv("MODEL")

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=API_KEY
)