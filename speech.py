import speech_recognition as sr
AUDIO_FILE=("sound.wav")

r=sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio=r.record(source)

try:
    print("audio file contains"+r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google speech recognition could not understand audio")
except sr.RequestError:
    print("Could not get the results from google")


