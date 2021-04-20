import ktrain
import tensorflow as tf
import random
import serial
import cv2
import numpy as np
import serial
from time import sleep
from playsound import playsound
from ProcessSpeech import play_prompt, reaction, listen_for
from DetectPlay import play_game


def main():
    # denote start of initialization
    # play init prompt
    play_prompt("audio\\init.mp3")
    # arduino = serial.Serial(port='COM7', baudrate=9600, timeout=.1)
    # send byte that will activate on off flashing of LED for arduino
    # load emo model
    emo_predictor = ktrain.load_predictor("tf_model.h5")
    # load rps model
    rps_predict = tf.keras.models.load_model("rock_paper_scissors_cnn.h5")
    shape_to_label = {b'r':np.array([1.,0.,0.]), b'p':np.array([0.,1.,0.]), b's':np.array([0.,0.,1.])}
    arr_to_shape = {np.argmax(shape_to_label[x]):x for x in shape_to_label.keys()}

    # initialization complete
    play_prompt("audio\\initcomp.mp3")
    # send byte that shall make LED full color

    # run emotional prompts
    emo_prompt = "audio\\emoprompt.mp3"
    reaction(emo_predictor, emo_prompt)

    # prompt user to play game
    game_prompt = "audio\\game_prompt.mp3"
    reject_prompt = "audio\\no.mp3"
    # force user to say yes
    listen_for(["yes", "yeah", "sure", "yup"], game_prompt, reject_prompt)

    # tell about game
    play_prompt("audio\\yes.mp3")

    # play the game
    play_game(rps_predict)


if __name__ == "__main__":
    main()
