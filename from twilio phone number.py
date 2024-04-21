from twilio.rest import Client
import speech_recognition as sr
import pyttsx3

# Twilio credentials
account_sid = 'US789ff89948bdb470503a0701206b80c2'
auth_token = 'YOUR_AUTH_TOKEN'
twilio_phone_number = '+919850090117'
recipient_phone_number = '+919850039617'

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

# Define function to make a phone call
def make_phone_call():
    client = Client(account_sid, auth_token)

    try:
        call = client.calls.create(
            twiml='<Response><Say>Hello! This is your personal voice assistant calling.</Say></Response>',
            to=recipient_phone_number,
            from_=twilio_phone_number
        )
        print("Phone call initiated. Call SID:", call.sid)
        speak("Phone call initiated.")
    except Exception as e:
        print("An error occurred:", e)
        speak("Sorry, I couldn't make the phone call.")

# Main loop for interacting with the user
def main():
    speak("Hello! Would you like me to make a phone call for you?")

    while True:
        user_input = listen()

        if user_input:
            if "yes" in user_input:
                make_phone_call()
                break
            elif "no" in user_input:
                speak("Okay, let me know if you change your mind.")
                break
            else:
                speak("Sorry, I'm not sure how to help with that.")

if __name__ == "__main__":
    main()