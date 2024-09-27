import os
import openai 
from openai import OpenAIError

openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_me():
    print ("Hi there! You can chat with me, and type 'exit' to end our conversation.")
    convo_history = [{"role":"system", "content":"You are helpful and knowledgeable assistant."}]
    
    while True:
        user_input = input ("You:  ")
        
        if user_input.lower() == "exit":
            print ("Chatbot: Goodbye!")
            break 
        convo_history.append({"role":"user", "content": user_input})
        
        try:
            response = openai.chat.completions.create(
                model = "gpt-3.5-turbo",
                messages= convo_history)
                    
            bot_message = response.choices[0].message.content
            print (f"Chatbot: {bot_message}")
        
            convo_history.append({"role":"assistant", "content": bot_message})
        except OpenAIError as e: 
            print(f"Error communicating with OPENAI: {e}")
            break

if __name__ == "__main__":
    chat_with_me()
