from pygame import mixer
import RPi.GPIO as GPIO
import time
from bottle import route, run, template

mixer.init() #Initialize mixer
mixer.music.load('/home/pi/GeorgeMichael/CarelessWhisper.wav') #Change to location of your wav file

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, GPIO.LOW) #GPIO OFF


@route('/')
def index():
    return 'Hi!'
@route('/relay/:relay')
def relay(relaynum=0):
    if relaynum == 0:
        return 'No relay'
    elif relaynum =='1': 
        time.sleep(2)             #used to give enough time for google home to reply before starting music
        mixer.music.play()        #PLAY MUSIC
        time.sleep(13)
        GPIO.output(17,GPIO.HIGH) #GPIO ON
        time.sleep(25)
        GPIO.output(17,GPIO.LOW)  #GPIO OFF
        return 'TIme to feel sexy'

run(host='IP ADDRESS OF PI', port=1234) #Change to your IP address
