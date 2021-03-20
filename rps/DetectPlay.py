import tensorflow as tf
import cv2
import numpy as np
import serial
from time import sleep
from playsound import playsound


cap = cv2.VideoCapture(1, cv2.CAP_DSHOW) #captureDevice = camera
rps_predict = tf.keras.models.load_model("C:\\Users\\tyxia\\Documents\\elec\\rps\\rock_paper_scissors_cnn.h5")
rps_predict.summary()
shape_to_label = {b'r':np.array([1.,0.,0.]), b'p':np.array([0.,1.,0.]), b's':np.array([0.,0.,1.])}
arr_to_shape = {np.argmax(shape_to_label[x]):x for x in shape_to_label.keys()}
arduino = serial.Serial(port='COM7', baudrate=9600, timeout=.1)


# def preprocess(image):
#     # Make image color values to be float.
#     image = tf.cast(image, tf.float32)
#     # Make image color values to be in [0..1] range.
#     image = image / 255.q
#     # Make sure that image has a right size
#     image = tf.image.resize(image, [INPUT_IMG_SIZE, INPUT_IMG_SIZE])
#     return image

def play_prompt(path):
    opening_prompt = path
    playsound(opening_prompt)


def preprocess(path):
    return cv2.resize(path,(150,150)).reshape(1,150,150,3)


def play_game():
    pred = ""
    font = cv2.FONT_HERSHEY_SIMPLEX
    exit_cond = 0
    playing_cond = 0

    while(True):
        ret, frame = cap.read()
        if exit_cond == 0:
            arduino.write(b'1')
            play_prompt("C:\\Users\\tyxia\\Documents\\elec\\rps\\rock.mp3")
            sleep(0.5)
            arduino.write(b'2')
            play_prompt("C:\\Users\\tyxia\\Documents\\elec\\rps\\paper.mp3")
            sleep(0.5)
            arduino.write(b'3')
            play_prompt("C:\\Users\\tyxia\\Documents\\elec\\rps\\scissors.mp3")

        exit_cond = 1
        
        frame = cv2.putText(frame, "", (400,400), font, 1, (250,250,0), 2, cv2.LINE_AA)
        
        if playing_cond == 0:
            pred = arr_to_shape[np.argmax(rps_predict.predict(preprocess(frame[50:350,100:400])))]
            arduino.write(pred)

            cv2.rectangle(frame, (0, 0), (500, 500), (255, 255, 255), 2)
            frame = cv2.putText(frame, str(pred), (400,400), font, 1, (250,250,0), 2, cv2.LINE_AA)

            playing_cond == 1

        cv2.imshow('Rock Paper Scissor',frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break


play_game()
