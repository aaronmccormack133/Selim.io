#!/usr/bin/python3
import speech_recognition as SR
import pyaudio

# If the device is not picking up your voice, uncomment this function to find the correct device index. 
# Use that number in line 16 for the microphone to pick up properly.

# p = pyaudio.PyAudio()
# for i in range(p.get_device_count()):
#     info = p.get_device_info_by_index(i)
#     print(info['index'], info['name'])

r = SR.Recognizer()

def speech():
    with SR.Microphone(device_index=2) as source:
        print('Input beginning')
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        print('done listening')

    try:
        print("you said: " + r.recognize_google(audio))
        return(r.recognize_google(audio))
    except Exception as e:
        print(e)
        return(e)