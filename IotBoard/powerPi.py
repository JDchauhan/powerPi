import machine
import json

threshold = 75

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
    for switch in range (0,7):
        if (data[str(switch)] == 0):
            pins[switch].low()
        else:
            pins[switch].high()


# def operate(num, msg):
#     with open("switches.json", "r") as jsonFile:
#         data = json.load(jsonFile)

#     if(msg == 'ON'):
#         data[str(num)] = 1
#         pins[num].high()

#     if(msg == 'OFF'):
#         pins[num].low()
#         data[str(num)] = 0

#     data = json.dumps(data)

#     print(data)
#     f = open('switches.json', "w")
#     f.write(data)
#     f.close()

#     print(num, msg)

def operate(switch, isCharging, charge):
    with open("switches.json", "r") as jsonFile:
        data = json.load(jsonFile)
    print(switch, isCharging, charge)
    if charge == 100:
        #battery full then disconnect
        print("case 1")
        pins[switch].low()
        data[str(switch)] = 0
    
    elif charge > threshold:
        #battery > threshold 
        print("case 2")
    
    elif data[str(switch)] == 1:
        # battery < threshold && socket = ON
        print("case 3")
        if isCharging == 0:
            print("case 4") 
            data[str(switch)] = 0
            pins[switch].low()    

    else:
        #battery < threshold && socket = OFF
        print("case 5")
        data[str(switch)] = 1
        pins[switch].high()        
    

    data = json.dumps(data)

    print(data)
    f = open('switches.json', "w")
    f.write(data)
    f.close()
