#!/usr/bin/python3
import pyttsx3
import subprocess

# Input: Using the input received from the query
# Output: Synthesized voice speaking the contents of input
def speak(input):
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    rate = engine.getProperty('rate')
    # Loops through the voices that are installed in the system. Uncomment to find one if you would like to replace the standard.
    # for voice in voices:
    #     engine.setProperty('voice', voice.id)
    #     print(voice.id)
    #     engine.say(input)
    engine.setProperty('voice', 'english-us')
    engine.setProperty('rate', rate-40)
    engine.say(input)
    engine.runAndWait()