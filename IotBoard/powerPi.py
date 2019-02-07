import machine
import json

d0 = 16 # wake
d1 = 5
d2 = 4
d3 = 0 #flash
d4 = 2
d5 = 14
d6 = 12
d7 = 13
d8 = 15
d9 = 3
d10 = 1


pins = [
    # machine.Pin(d0, machine.Pin.OUT), 
    machine.Pin(d1, machine.Pin.OUT), 
    machine.Pin(d2, machine.Pin.OUT), 
    # machine.Pin(d3, machine.Pin.OUT),
    machine.Pin(d4, machine.Pin.OUT), 
    machine.Pin(d5, machine.Pin.OUT), 
    machine.Pin(d6, machine.Pin.OUT), 
    machine.Pin(d7, machine.Pin.OUT), 
    machine.Pin(d8, machine.Pin.OUT), 
    # machine.Pin(d9, machine.Pin.OUT), 
    # machine.Pin(d10, machine.Pin.OUT)
]

for pin in pins:
    pin.low()

with open("switches.json", "r") as jsonFile:
    data = json.load(jsonFile)
    for i in range (0,7):
        if (data[str(i)] == 0):
            pins[i].low()
        else:
            pins[i].high()


def operate(num, msg):
    with open("switches.json", "r") as jsonFile:
        data = json.load(jsonFile)

    if(msg == 'ON'):
        data[str(num)] = 1
        pins[num].high()

    if(msg == 'OFF'):
        pins[num].low()
        data[str(num)] = 0

    data = json.dumps(data)

    print(data)
    f = open('switches.json', "w")
    f.write(data)
    f.close()

    print(num, msg)
