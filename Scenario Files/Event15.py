################################################
#
#
# AUDIO SCENARIO 1 EVENT 5 FILE
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
                sock.send("Speak Please take over.\n")
            else:
                sock.send("Speak Please take over.\n")
        else:
            if(trust == 0):    
                sock.send("Speak Please take over. The vehicle's light sensors detect heavy fog ahead.\n")
            else:
                sock.send("Speak Please take over. The vehicle's moisture sensors detect heavy rain ahead.\n")

        sock.close()

    else:

        tts = ALProxy("ALTextToSpeech", naoIP, 9559);

        if(cond == 0):
            if(trust == 0):    
                tts.say("Please take over.") 
            else:
                tts.say("Please take over.")
        else:
            if(trust == 0):    
                tts.say("Please take over. The vehicle's light sensors detect heavy fog ahead.")  
            else:
                tts.say("Please take over. The vehicle's moisture sensors detect heavy rain ahead.")
    return 0.0



