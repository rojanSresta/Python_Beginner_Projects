import pyttsx3 #-->this is a library that makes the computer speak

engine = pyttsx3.init() #-->initialigizing the pyttsx3

# Seeing the available voices
# for voice in voices:
#     print("ID:", voice.id, "Name:", voice.name, "Lang:", voice.languages)

def get_voice():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) 

def speak(text):
    get_voice()
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    print("\n\t\t\t*** Welcome, Press q and hit enter to quit the talking ***\n")
    while True:
        if(user_input := input("Enter what to say: ")) == 'q': #-->used walrus operator
            speak("Robo Speaker Quitted \n")
            break
        speak(user_input)