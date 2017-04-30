import paho.mqtt.client as mqtt
# import RPi.GPIO as GPIO

def lightOn():

    GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
    GPIO.setup(10, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
    GPIO.output(10,True) ## Turn on GPIO pin 7

def driveForward():

    pass

def driveBackward():

    pass

def turnLeft():

    pass

def turnRight():

    pass

def lightOff():

    pass


broker = 'broker.shiftr.io'
subscribedTopic = 'test'

def onConnect(client, userdata, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(subscribedTopic)

def whenMessageRecieved(client, userdata, msg):
    # print(msg.topic + str(msg.payload))

    payload = str(msg.payload)
    print(payload)

    if payload == "#PAYLOADSIZED":
        print("ah")
        lightOn()


client = mqtt.Client()
client.on_connect = onConnect
client.on_message = whenMessageRecieved

client.username_pw_set('####SHIFTR.IO USR####', '####SHIFTR.IO USR####')

client.connect(broker)

client.loop_forever()

