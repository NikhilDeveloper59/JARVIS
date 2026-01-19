# -------------------- ai_chat.py --------------------
import os
from dotenv import load_dotenv
from openai import OpenAI

# step 1: Load API Key from .env file
load_dotenv()   # reads .env file
API_KEY = os.getenv("OPENAI_API_KEY")

# Step 2: Create OpenAI client
client = OpenAI(api_key=API_KEY)

# Step 3: Jarvis memory (chat history)
# This helps Jarvis remember previous messages
chat_history = [
    {"role": "system", "content": "You are Jarvis, a helpful voice assistant."}
]

# Step 4: Function to talk with AI
def chat_with_ai(user_text):
    
    # Add user message into memory
    chat_history.append({"role": "user", "content": user_text})

    # Send chat history to OpenAI
    response = client.chat.completions.create(
        model="gpt-4o-mini",   #This selects which AI model to use. 
        messages=chat_history, # send the full chat_history to OpenAI so that gives memory to Jarvis.
        temperature=0.7        # 0.7 → balanced (BEST for Jarvis, Jarvis will reply naturally, friendly, and smart.)
    )


    # Get AI reply from response
    # response contains:choices ,tokens usage ,model info ,response content 
    ai_reply = response.choices[0].message.content.strip() # to get actual content


    # Add AI reply into memory
    chat_history.append({"role": "assistant", "content": ai_reply})

    return ai_reply
