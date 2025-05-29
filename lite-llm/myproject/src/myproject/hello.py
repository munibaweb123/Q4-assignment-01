from dotenv import load_dotenv
from litellm import completion
import os

load_dotenv()  


def openai():
    response = completion(
        model="openai/gpt-4o",
        messages=[{ "content": "Hello, how are you?","role": "user"}]
    )

    print(response)

def gemini():
    response = completion(
        model="gemini/gemini-1.5-flash",
        messages=[{ "content": "Hello, how are you?","role": "user"}]
    )

    print(response)

def gemini2():
    response = completion(
        model="gemini/gemini-2.0-flash-exp",
        messages=[{ "content": "Hello, how are you?","role": "user"}]
    )

    print(response)