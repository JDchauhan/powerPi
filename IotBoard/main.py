import time
import network
import machine

from lib.umqttRobust import MQTTClient

import setup
import powerPi

isBroker = True

wlan = network.WLAN(network.STA_IF)
data = setup.initialize()


def sub_cb(topic, msg):
    topic = topic.decode("utf-8")
    msg = msg.decode("utf-8")
    device = topic.split('/')[1]

    device = (int) (device)
    powerPi.operate(device, msg)

    client.check_msg()


client = MQTTClient(
    client_id = data["client_id"],
    server = data["server"], 
    port = data["port"], 
    user = data["user"], 
    password = data["pass"]
)

client.set_callback(sub_cb)

while not wlan.isconnected():

    print("connectin to network...")
    setup.networkConnect(data["ssid"], data["password"])


while True:
    try:
        client.connect()
        break
    except :
        print("error connecting broker")
        pass    

client.subscribe(topic= data["id"] + "/#")    

while True:
    # 5.5
    if not wlan.isconnected():
        isBroker = False
        print("connecting...")
        setup.networkConnect(data["ssid"], data["password"])
    else:

        for _ in range(3): 
            try:
                client.publish(topic="test", msg="testing")
                if not isBroker:
                    client.subscribe(topic= data["id"] + "/#")                     
                # print("connected")
                client.check_msg()
                time.sleep(0.5)
            except:
                isBroker = False
                print("broker disconnected")
                time.sleep(2)
                break
