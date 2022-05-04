import sys
import speech_recognition
from datetime import date
from datetime import time



#SYSTEM DATE AND TIME
today = date.today()
strTextToday = today.strftime("%B %d %Y")
print(strTextToday)


#VOICE INPUT
voice = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print("Listening...")
    audio = voice .listen(mic)
try:
    input_text =  voice.recognition_google(audio)
except:
    input_text = "I do not understand"
print(input_text)

#VOICE OUTPUT
while input_text != "Thank you Monica":
output_text = ""
if input_text == "Hey Morica"
    output = "Hello Master, how can I help you"
elif input_text == "What date is today":
    output = "Today is " + strTextToday
else:
    output = "Sorry I do not understand, can you say it again"
    continue
else

engine =  pyttsx3.init()
engine.say("I hear " + input_text)
engine.runAndWait()

