import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import pyaudio
import setuptools

recognizer = sr.Recognizer()

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't get that. Please try again.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an issue with the request. Please try again later.")
        return ""

def assistant():
    speak("Hello! I'm your voice assistant. How can I help you today?")

    while True:
        query = listen()
        
        if "hello" in query:
            speak("Hello! How are you.?")
        
        elif "time" in query:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}")
        
        elif "date" in query:
            current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
            speak(f"Today's date is {current_date}")
        
        elif "search" in query:
            speak("What would you like me to search for?")
            search_query = listen()
            if search_query:
                url = f"https://www.google.com/search?q={search_query}"
                webbrowser.open(url)
                speak(f"Here is what I found for {search_query}.")
        
        elif "exit" in query or "bye" in query:
            speak("Goodbye!")
            break
        
        else:
            speak("Sorry, I'm not sure how to help with that. Could you please try something else?")

if __name__ == "__main__":
    assistant()
