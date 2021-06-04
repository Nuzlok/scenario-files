################################################
#
#
# AUDIO SCENARIO 1 EVENT 2 FILE
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

    naoIP = "172.29.107.164" # Change this as needed

    if(robot == 0):

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((miloIP, 4001))

        if(cond == 0):
            if(trust == 0):    
                sock.send("Speak The car ahead of you is expected to swerve into your lane.\n")
            else:
                sock.send("Speak The car ahead of you is expected to swerve into your lane.\n")
        else:
            if(trust == 0):    
                sock.send("Speak The car in front of you is expected to swerve into your ")
                sock.send("lane in X yards based on the system's prediction program.\n")
            else:
                sock.send("Speak The car in front of you is expected to swerve into your ")
                sock.send("lane in Y yards based on the system's prediction program.\n")

        sock.close()

    else:

        tts = ALProxy("ALTextToSpeech", naoIP, 9559);

        if(cond == 0):
            if(trust == 0):    
                tts.say("The car ahead of you is expected to swerve into your lane.") 
            else:
                tts.say("The car ahead of you is expected to swerve into your lane.")
        else:
            if(trust == 0):    
                tts.say("The car in front of you is expected to swerve into your lane in X yards based on the system's prediction program.")  
            else:
                tts.say("The car in front of you is expected to swerve into your lane in Y yards based on the system's prediction program.")
    return 0.0