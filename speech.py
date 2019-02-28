import speech_recognition as SR

r = SR.Recognizer()

with SR.Microphone() as source:
    print('Say Something')
    audio = r.listen(source)

try:
    print('You said: \n' + r.recognize_google(audio))

except:
    pass