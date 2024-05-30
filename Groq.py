import os
#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
from groq import Groq

from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)