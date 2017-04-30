import paho.mqtt.client as mqtt
# import RPi.GPIO as GPIO
import time
count = 0
GPIO.setmode(GPIO.BOARD) ## Use board pin numbering


gpio1 = 19 #GPIO 10 pin 5 on 3pi 
gpio2 = 21 #GPIO 09 pin 1 on 3pi 

GPIO.setup(gpio1, GPIO.OUT)
GPIO.setup(gpio2, GPIO.OUT)
GPIO.setup(gpio3, GPIO.OUT)

off = GPIO.LOW 
on = GPIO.HIGH

def lightOn():

    GPIO.output(19,GPIO.HIGH) ## Turn on GPIO pin 7

# Pin 1 and 2 on 
def driveForward(gpio1, gpio2):
    print("forward")
    GPIO.output(gpio1, on)
    GPIO.output(gpio2, on)
    time.sleep(2)
    GPIO.output(gpio1, off)
    GPIO.output(gpio2, off)
    
# Pin 1 on 
def turnLeft(gpio1, gpio2):
    GPIO.output(gpio1, on)
    GPIO.output(gpio2, off)
    time.sleep(2)
    GPIO.output(gpio1, off)

# Pins 2 on 
def turnRight(gpio1, gpio2):
    GPIO.output(gpio1, off)
    GPIO.output(gpio2, on)
    time.sleep(2)
    GPIO.output(gpio1, off)
    GPIO.output(gpio2, off)

# all off
def idle(gpio1, gpio2):

    GPIO.output(gpio1, off)
    GPIO.output(gpio2, off)



def lightOff():

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(19, GPIO.OUT)
    GPIO.output(19, GPIO.LOW)


broker = 'broker.shiftr.io'
subscribedTopic = 'vect'

def onConnect(client, userdata, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(subscribedTopic)

def whenMessageRecieved(client, userdata, msg):
    # print(msg.topic + str(msg.payload))

    payload = str(msg.payload)
    print(payload)

    if payload == "b\'hello\'":
        global count
        count += 1
        if count % 2 == 0:
            lightOn()
        else: 
            lightOff()

    elif payload == "b\'left'\'":
        turnLeft()
    
    elif payload == "b\'right\'":
        turnRight()
    
    elif payload == "b\'forward\'":
        driveForward()
    
    elif payload == "b\'backward\'":
        driveForward()
    else:
        idle()


client = mqtt.Client()
client.on_connect = onConnect
client.on_message = whenMessageRecieved

client.username_pw_set('####SHIFTR.IO USR####', '####SHIFTR.IO USR####')

client.connect(broker)

client.loop_forever()

