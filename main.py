'''
Author: Mihretab Nigatu
Date: 2023-05-18 19:56:10
LastEditTime: 2023-05-20 03:33:45
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Description: Wikipedia-based Voice Assistant for Everyday Information Retrieva.
'''
import speech_recognition as sr
import pyttsx3
import wikipedia

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        print("Listening...")
        audio = recognizer.listen(source, phrase_time_limit=5)  # Limit the listening time to 5 seconds
        

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        return ""
    except sr.RequestError:
        print("Sorry, I encountered an error while processing your request.")
        return ""

def search_wikipedia(query):
    try:
        page = wikipedia.page(query)
        return page.summary
    except wikipedia.exceptions.PageError:
        return "I'm sorry, but I couldn't find any information on that topic."
    except wikipedia.exceptions.DisambiguationError as e:
        options = e.options[:5]  # Limit the number of options to display
        options_text = ", ".join(options)
        return f"Please be more specific. Did you mean one of these: {options_text}?"

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)  # Adjust the speech rate as desired
    engine.setProperty("voice", "english+f3")  # Set voice to a more human-like tone
    engine.say(text)
    engine.runAndWait()

def ai_talking_friend():
    speak("Hello! I'm MTAB, your Personal Voice Assistant for everyday Wikipedia searches. How may I assist you today? I'm all ears!")
    speak("Beeppp")

    while True:
        user_query = listen()

        if user_query.lower() == "bye":
            speak("Goodbye! It was nice talking to you.")
            print("Goodbye! It was nice talking to you.")
            break

        response = search_wikipedia(user_query)

        speak(response)
        print(response)
        speak("Is there anything else I can help you with?")

ai_talking_friend()