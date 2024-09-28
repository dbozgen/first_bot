import os
from openai import OpenAI

client= OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

chat_completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role":"user", "content":"Hi, how are you?"}
    ]   
)

print (chat_completion.choices[0].message.content)