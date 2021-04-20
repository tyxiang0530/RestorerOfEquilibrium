import ktrain
import tensorflow as tf
import random
import serial
import speech_recognition as sr
from playsound import playsound

# arduino = serial.Serial(port='COM7', baudrate=9600, timeout=.1)
# denote model loading


# going from emotions to bytes for arduino serial sending
trans_table = {
    "sadness": b'a',
    "joy": b'b',
    "fear": b'c',
    "neutral": b'd',
    "anger": b'e'
}

# going from emotions to audio files
sad_paths = ["audio\\sadcounter.mp3"]
anger_paths = ["audio\\angercounter.mp3"]
joy_paths = ["audio\\joycounter.mp3"]
fear_paths = ["audio\\fearcounter.mp3"]
neutral_paths = ["audio\\neutralcounter.mp3"]

path_trans = {
    b'a': sad_paths,
    b'b': joy_paths,
    b'c': fear_paths,
    b'd': neutral_paths,
    b'e': anger_paths
}

r = sr.Recognizer()


# "C:\\Users\\tyxia\\Documents\\Pomona\\Classes\\2nd\\s2\\electronics128\\PythonCode\\prompt.wav"
# play_prompt plays the audio prompt (How are you doing today)
def play_prompt(path):
    opening_prompt = path
    playsound(opening_prompt)


# open_mic plays the prompt and stores and returns the response
def open_mic(prompt_path):
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        play_prompt(prompt_path)
        print("Talk")
        audio_text = r.record(source, duration = 5)
        # audio_text = r.listen(source, timeout = 1, phrase_time_limit=5
        print("Time over, thanks")

        try:
            # using google speech recognition
            speech = r.recognize_google(audio_text)
            print("Text: " + speech)
            return speech

        except:
            print("Sorry, I did not get that")


# have our classifier make a prediction
def predict_emotion(model_in, emo_prompt):
    prediction = model_in.predict(open_mic(emo_prompt))
    print(prediction)
    return trans_table[prediction]


# play the audio clip and send the right byte
def reaction(model_in, emo_prompt):
    emo_byte = predict_emotion(model_in, emo_prompt)
    play_prompt(random.choice(path_trans[emo_byte]))
    # arduino.write(emo_byte)


# function will only exit if keyword is found in speech
def listen_for(keyword, game_prompt, reject_prompt):
    play_prompt(game_prompt)
    exit_cond = True
    while exit_cond:
        with sr.Microphone() as source:
            print("listening")
            audio_text = r.record(source, duration=3)

        print("recognizing")

        try:
            text = r.recognize_google(audio_text)
            print(text)
            if any(word in text for word in keyword):
                print('found')
                exit_cond = False

            else:
                play_prompt(reject_prompt)
                play_prompt(game_prompt)

        except Exception as e:
            print(e)
            play_prompt(reject_prompt)

