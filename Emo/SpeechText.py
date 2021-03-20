import speech_recognition as sr
from playsound import playsound


r = sr.Recognizer()

# play_prompt plays the audio prompt (How are you doing today)
def play_prompt():
    opening_prompt = "C:\\Users\\tyxia\\Documents\\Pomona\\Classes\\2nd\\s2\\electronics128\\PythonCode\\prompt.wav"
    playsound(opening_prompt)


# open_mic plays the prompt and stores and returns the response
def open_mic():
    play_prompt()
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time over, thanks")
        
        try:
            # using google speech recognition
            speech = r.recognize_google(audio_text)
            print("Text: " + speech)
            return speech
        except:
            print("Sorry, I did not get that")