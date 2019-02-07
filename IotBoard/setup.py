import network
import json
import time
import machine


def initialize():
    with open("config.json", "r") as jsonFile:
        data = json.load(jsonFile)
    return data


def networkConnect(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        print(ssid, password)
        wlan.connect(ssid, password)
        ledSignals.connecting()
        time.sleep(5)
    else:
        print("already connected")
        ledSignals.save()

