from time import sleep
from ProcessSpeech import play_prompt, reaction, listen_for
from DetectPlay import play_game
import serial


def main():
    # denote start of initialization
    # play init prompt
    play_prompt("audio\\init.mp3")
    arduino = serial.Serial(port='COM7', baudrate=9600, timeout=.1)
    arduino.setDTR(False)
    sleep(1)
    # toss any data already received
    arduino.flushInput()
    arduino.setDTR(True)
    arduino.write(b'z')

    # initialization complete
    play_prompt("audio\\initcomp.mp3")
    # send byte that shall make LED full color

    # run emotional prompts
    emo_prompt = "audio\\emoprompt.mp3"
    reaction(emo_prompt, arduino)

    sleep(2)
    # prompt user to play game
    game_prompt = "audio\\game_prompt.mp3"
    reject_prompt = "audio\\no.mp3"
    # force user to say yes
    listen_for(["yes", "yeah", "sure", "yup"], game_prompt, reject_prompt)

    # tell about game
    play_prompt("audio\\yes.mp3")

    sleep(3)
    # play the game
    play_game(arduino)


if __name__ == "__main__":
    main()
