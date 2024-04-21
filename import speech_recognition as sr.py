import speech_recognition as sr
import pyttsx3
import datetime

# Initialize the speech recognition engine and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to take voice input and process commands
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            command = command.lower()
            print("You said:", command)
            return command
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an error with the request. Please try again later.")
        return ""

# Function to handle different commands
def handle_command(command):
    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}")
    elif "thank you" in command:
        speak("You're welcome!")
    elif "goodbye" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I'm sorry, I didn't understand that.")

# Main function to continuously listen for commands
def main():
    speak("Hello! I'm your voice assistant. How can I help you?")
    while True:
        command = take_command()
        handle_command(command)

if __name__ == "__main__":
    main()