import serial
import time
from ProcessSpeech import predict_emotion


arduino = serial.Serial(port='COM5', baudrate=9600, timeout=.1)

def write_read():
    arduino.write(predict_emotion())


if __name__ == '__main__':
    write_read(predict_emotion())