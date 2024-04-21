import speech_recognition as sr
import pyttsx3
import webbrowser

# Initialize speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Define function for speech recognition
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return None
    except sr.RequestError:
        print("Sorry, there was an error connecting to Google Speech Recognition.")
        return None

# Define function for text-to-speech conversion
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define function to perform a Google search and open the search results page
def google_search(query):
    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    speak(f"Opening Google search results for {query} in your web browser.")
    webbrowser.open(search_url)

# Main loop for interacting with the user
def main():
    speak("Hello! What would you like to search for on Google?")

    while True:
        user_input = listen()

        if user_input:
            if "search for" in user_input:
                query = user_input.replace("search for", "").strip()
                google_search(query)
                break
            elif "exit" in user_input or "quit" in user_input:
                speak("Goodbye!")
                break
            else:
                speak("Sorry, I'm not sure how to help with that.")

if __name__ == "__main__":
    main()
