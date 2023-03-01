import openai
import os
import sys

import speech_recognition as sr
from typing import Text
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()
# Set up the OpenAI API client
openai.api_key = ("API--here")

def speak_chatgpt_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)
    engine.say(text)
    engine.runAndWait()
    

def ask_chatgpt(my_prompt):
    chat_gpt3_model_engine = "text-davinci-003"
    results = []
    # Generate a streamed response
    completions = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = my_prompt,
        max_tokens = 512,
        n = 1,
        stop = None,
        temperature=0.5,
    )
    results = completions.choices[0].text
    print(results)
    return "".join(results)

def main():
    while True:
        try:
# use the microphone as source for input.
            with sr.Microphone() as source2:
                print("Microphone is open now say your prompt...")
                r.adjust_for_ambient_noise(source2, duration=0.5)
                audio2 = r.listen(source2)
                my_prompt = r.recognize_wit(audio2,key="API-key-here")
                

                print("Did you say :", my_prompt)
                prompt_resp_text = ask_chatgpt(my_prompt)
                speak_chatgpt_text(prompt_resp_text)
        except Exception as e:
            print(e)
            print("Could not request results; {0}".format(e))

if __name__ == "__main__":
    main()

