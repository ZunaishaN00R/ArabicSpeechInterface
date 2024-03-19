# ###### NEW MODEL
import speech_recognition as sr
import pyttsx3


def speak(text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")

    # Select an Arabic voice
    for i, voice in enumerate(voices):
        if "ar-SA" in voice.id:
            engine.setProperty("voice", voices[i].id)
            break

    engine.setProperty("rate", 200)  # Adjust the rate as needed

    print(f"My Model: {text}")
    engine.say(text)
    engine.runAndWait()
def listen_and_speak():
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = r.listen(source, phrase_time_limit=5)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="ar-SA")
            print(f"You: {query}")
            speak(query)
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand your request.")
        except sr.RequestError as e:
            print(f"Recognition request error: {e}")


if __name__ == '__main__':
    while True:
        listen_and_speak()