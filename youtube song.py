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

# Define function to play a song on YouTube
def play_song(song_name):
    url = f"https://www.youtube.com/results?search_query={song_name.replace(' ', '+')}"
    webbrowser.open(url)

# Main loop for interacting with the user
def main():
    speak("Hello! What song would you like to listen to?")

    while True:
        user_input = listen()

        if user_input:
            if "play" in user_input:
                song_name = user_input.replace("play", "").strip()
                play_song(song_name)
                speak(f"Playing {song_name} on YouTube. Enjoy!")
                break
            elif "exit" in user_input or "quit" in user_input:
                speak("Goodbye!")
                break
            else:
                speak("Sorry, I'm not sure how to help with that.")

if __name__ == "__main__":
    main()