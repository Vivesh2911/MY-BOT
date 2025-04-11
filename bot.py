import speech_recognition as sr
import pyttsx3
import random

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
  
    with sr.Microphone() as source:
        print("Listening for your message...")
        recognizer.adjust_for_ambient_noise(source)  
        audio = recognizer.listen(source)  
        try:
            message = recognizer.recognize_google(audio)  
            print(f"You said: {message}")
            return message
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return None
        except sr.RequestError:
            print("Sorry, I'm having trouble with the speech service.")
            return None

# Main chatbot function
def chatbot():
    jokes = ["Why don’t skeletons fight each other? They don’t have the guts.", 
             "I told my wife she was drawing her eyebrows too high. She looked surprised."]
    weather_tips = ["It's sunny today, don’t forget your sunglasses!", 
                    "It looks like it might rain, better take an umbrella."]
    
    speak("Hello! I am your friendly bot. How can I help you today?")

    while True:
        user_message = listen()  # Listen to the user's message
        
        if user_message:
            user_message = user_message.lower()

            if "joke" in user_message:
                joke = random.choice(jokes)
                speak(joke)
            
            elif "weather" in user_message:
                weather = random.choice(weather_tips)
                speak(weather)
            
            elif "bye" in user_message:
                speak("Goodbye! Have a great day.")
                break

            else:
                speak("I'm not sure about that. Please ask something else.")
        else:
            speak("Can you please repeat that?")

# Start the chatbot
if __name__ == "__main__":
    chatbot()
