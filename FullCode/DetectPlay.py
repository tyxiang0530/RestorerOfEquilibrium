import cv2
import numpy as np
from time import sleep
from playsound import playsound


# set some initial parameters
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #captureDevice = camera
shape_to_label = {b'r': np.array([1.,0.,0.]), b'p': np.array([0.,1.,0.]), b's': np.array([0.,0.,1.])}
arr_to_shape = {np.argmax(shape_to_label[x]):x for x in shape_to_label.keys()}
# arduino = serial.Serial(port  ='COM7', baudrate=9600, timeout=.1)


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
def play_game(model_in):
    """
    main loop of the RPS player
    :param model_in:
    :return:
    """
    font = cv2.FONT_HERSHEY_SIMPLEX
    exit_cond = 0
    playing_cond = 0

    # read the frame
    while True:
        ret, frame = cap.read()
        if exit_cond == 0:
            # play audio to indicate start of game
            play_prompt("audio\\rock.mp3")
            sleep(0.5)
            play_prompt("audio\\paper.mp3")
            # set a longer delay before final scissors to stunt player
            sleep(0.75)
            play_prompt("audio\\scissors.mp3")

        # pass sentinal variable
        exit_cond = 1

        frame = cv2.putText(frame, "", (400,400), font, 1, (250,250,0), 2, cv2.LINE_AA)

        if playing_cond == 0:
            # write the answer to arduino
            # predict what the player plays
            pred = arr_to_shape[np.argmax(model_in.predict(preprocess(frame[100:400,100:400])))]
            # arduino.write(pred)

            cv2.rectangle(frame, (0, 0), (500, 500), (255, 255, 255), 2)
            frame = cv2.putText(frame, str(pred), (400,400), font, 1, (250,250,0), 2, cv2.LINE_AA)

            playing_cond == 1

        # pop the frame up (this is only for clarity in testing)
        cv2.imshow('Rock Paper Scissor', frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
