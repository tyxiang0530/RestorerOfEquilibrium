import cv2
import serial
import numpy as np
from time import sleep
from playsound import playsound
import tensorflow as tf


# set some initial parameters
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW) #captureDevice = camera
shape_to_label = {b'r': np.array([1.,0.,0.]), b'p': np.array([0.,1.,0.]), b's': np.array([0.,0.,1.])}
arr_to_shape = {np.argmax(shape_to_label[x]):x for x in shape_to_label.keys()}
arduino = serial.Serial(port ='COM5', baudrate=9600, timeout=.1)
rps_predict = tf.keras.models.load_model("rock_paper_scissors_cnn.h5")
arduino.setDTR(False)
sleep(1)
# toss any data already received, see\
arduino.flushInput()
arduino.setDTR(True)



def play_prompt(path):
    """
    plays the designated prompt
    :param path: the path where your prompt is stored
    :return:
    """
    opening_prompt = path
    playsound(opening_prompt)


def preprocess(path):
    """
    resizes the image to match dimensionality for the CNN
    :param path: the path of your image
    :return: the resized image
    """
    return cv2.resize(path,(150, 150)).reshape(1, 150, 150, 3)


# play the game
def play_game():
    """
    main loop of the RPS player
    :param
    :return:
    """

    # read the frame
    ret, frame = cap.read()
    # play audio to indicate start of game
    play_prompt("audio\\rock.mp3")
    sleep(0.5)
    play_prompt("audio\\paper.mp3")
    # set a longer delay before final scissors to stunt player
    sleep(0.5)
    play_prompt("audio\\scissors.mp3")

    # pass sentinal variable

    # write the answer to arduino
    # predict what the player plays
    pred = arr_to_shape[np.argmax(rps_predict.predict(preprocess(frame[100:400,100:400])))]

    arduino.write(pred)
    print(pred)
    arduino.write(b'p')
    # a flushing byte to prevent bleedthrough
