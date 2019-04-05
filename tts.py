import pyttsx3
import subprocess

# def speak(input):
#     subprocess.call('echo '+input+'|festival --tts', shell=True)

def speak(input):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    rate = engine.getProperty('rate')
    # for voice in voices:
    #     engine.setProperty('voice', voice.id)
    #     print(voice.id)
    #     engine.say(input)
    engine.setProperty('voice', 'english-us')
    engine.setProperty('rate', rate-40)
    engine.say(input)
    engine.runAndWait()
