# alexandra.py
# my artificial intelligence
# Samuel Winkens, 2023

from datetime import time
from revChatGPT.V1 import Chatbot
import pyttsx3

# initializing the tts engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)
engine.setProperty('voice', voices[1].id)

# creating Alexandra object with my account configuration
alexandra = Chatbot(config={
    'email':<Insert Email>,
    'password':<Insert Password>
})

# creating greeting for user
greeting = 'Hello! My name is Alexandra.'
print(greeting)
engine.say(greeting)
engine.runAndWait()
engine.stop()

# creating while loop to wait for user input and give response
while True:
    print('') # spacing
    prompt = input('Question? ')
    response = ''
    for data in alexandra.ask(prompt):
        response = data['message']
    print('\n' + response)
    engine.say(response)
    engine.runAndWait()
    engine.stop()
    if prompt.strip() == 'quit':
        break
