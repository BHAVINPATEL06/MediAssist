# First File

# Step 1: Setup GROQ API key
import os
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")  # Fetching API form .env file in variable named GROQ_API_KEY


# Step 2: Convert Image to required text
import base64   # converts bits into string  # using this because data should't not be corrupt from one system to another Use for encoding and decoding


# image_path = "acne.jpeg"
def encoded_image(image_path):
    image_file = open(image_path, "rb")   # rb means read file in binary format
    return base64.b64encode(image_file.read()).decode("utf-8")  # fiile reads in utf-8 format and then it will be decoded and then it will encoded into base64 format  


# Step 3: Setup MultiModal LLM Model (GROQ)
from groq import Groq

model = "meta-llama/llama-4-scout-17b-16e-instruct" # GROQ model name
query = "Is there something wrong with my face?"

def analyze_image_with_query(query,model,encoded_image):
# This is a format of message that we need to send to the GROQ Model
    client = Groq()   # Creating client object of Groq class 

    messages = [
        {
            "role": "user",
            "content": [
                {
                    #input 1 This is text input
                    "type": "text",
                    "text": query
                },
                {  
                    #input 2 This is image input
                    "type": "image_url",
                    "image_url" : {
                        "url" : f"data:image/jpeg;base64,{encoded_image}",  # encoded image in base64 format 
                    },
                },
            ],
        }]

    #API Call to GROQ LLM Model
    chat_completion = client.chat.completions.create(
        messages = messages,  # messages to be sent to the model
        model = model   # model name
    )

    return chat_completion.choices[0].message.content  # print the output from the model


