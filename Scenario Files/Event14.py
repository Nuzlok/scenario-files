################################################
#
#
# AUDIO SCENARIO 1 EVENT 4 FILE
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
import mice  # Exclusive to the Driving Simulator

def main():

    robot = mice.variables["Robot"]
    cond = mice.variables["Info"]
    trust = mice.variables["Trust"]

    miloIP = "127.0.0.1" # Change this as needed

    naoIP = "172.29.107.164" # Change this as needed

    if(robot == 0):

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((miloIP, 4001))

        if(cond == 0):
            if(trust == 0):    
                sock.send("Speak Pedestrian on road ahead.\n")
            else:
                sock.send("Speak Animal crossing road ahead.\n")
        else:
            if(trust == 0):    
                sock.send("Speak The vehicle's front right sensors detect a pedestrian ahead who is walking into the street.")
                sock.send("Based on their trajectory the vehicle will brake and move to the left lane.\n")
            else:
                sock.send("Speak The vehicle's front right sensors detect a large animal crossing the road ahead. ")
                sock.send("Based on its trajectory the vehicle will brake and move to the left lane.\n")

        sock.close()

    else:

        tts = ALProxy("ALTextToSpeech", naoIP, 9559);

        if(cond == 0):
            if(trust == 0):    
                tts.say("Pedestrian on road ahead.") 
            else:
                tts.say("Animal crossing road ahead.")
        else:
            if(trust == 0):    
                tts.say("The vehicle's front right sensors detect a pedestrian ahead who is walking into the street.")
                tts.say("Based on their trajectory the vehicle will brake and move to the left lane.")
            else:
                tts.say("The vehicle's front right sensors detect a large animal crossing the road ahead.")
                tts.say("Based on its trajectory the vehicle will brake and move to the left lane.")
    return 0.0


