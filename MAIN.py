import pyttsx3
import speech_recognition as sr
import webbrowser
from datetime import datetime  


recognizer = sr.Recognizer() 
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
      

    
    elif "date" in c.lower():
        today = datetime.now().strftime("%A, %B %d, %Y")  
        speak(f"Today is {today}.")
    

if __name__ == "__main__":

    speak("Initializing Roxy.... , SAY THE CODE")
    while True:
        r = sr.Recognizer()

        print("Recognizing...")

        try:
            with sr.Microphone() as source:
                print("listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=3)
            word = r.recognize_google(audio)
            if word.lower() == "roxy":
                speak("Yes")

                with sr.Microphone() as source:
                    print("roxy active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processcommand(command)

        except Exception as e:
            print(f"Error: {e}")
