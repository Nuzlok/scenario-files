################################################
#
#
# AUDIO EVENT FILE MASTER
#
# Value Legend:
# 
# Robot:        Milo - 0        Nao - 1
# Condition:    Pull - 0        Push - 1
# Trust:        Reliable - 0    Unreliable - 1
#
###############################################

from naoqi import ALProxy
import socket
import mice # Exclusive to the Driving Simulator


def main():

    robot = mice.variables["Robot"]
    cond = mice.variables["Info"]
    trust = mice.variables["Trust"]

    miloIP = "127.0.0.1" # Change this as needed

    naoIP = "127.0.0.1" # Change this as needed

    if(robot == 0):

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((miloIP, 4001))

        if(cond == 0):
            if(trust == 0):    
                sock.send("Speak Milo Reliable Pull")  
            else:
                sock.send("Speak Milo Unreliable Pull")
        else:
            if(trust == 0):    
                sock.send("Speak Milo Reliable Push")  
            else:
                sock.send("Speak Milo Unreliable Push")

        sock.close()

    else:

        tts = ALProxy("ALTextToSpeech", naoIP, 9559);

        if(cond == 0):
            if(trust == 0):    
                tts.say("Nao Reliable Pull") 
            else:
                tts.say("Nao Unreliable Pull")
        else:
            if(trust == 0):    
                tts.say("Nao Reliable Push")  
            else:
                tts.say("Nao Unreliable Push")

    return 0.0