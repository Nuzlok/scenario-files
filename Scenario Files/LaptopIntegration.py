################################################
#
# REMOTE PULL CONDITION
#
# Global Variable Legend:
# 
# Robot:        Milo - 0        Nao - 1 
# Trust:        Reliable - 0    Unreliable - 1
# Scenario:     One - 0         Two - 1
#
###############################################

from naoqi import ALProxy
import socket

# UNIVERSAL GLOBAL VARIABLES -- CHANGE AS NEEDED
ROBOT = 1
TRUST = 0
SCENARIO = 1
MILOIP = "172.29.60.143"
NAOIP = "172.29.107.164"
key = ""


###############################
#
# MILO SPEECH FUNCTIONS
#
###############################

#Scenario 1 Reliable

def MR11(sock):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    sock.send("Speak Obstacle quarter mile ahead.\n")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    sock.send("Speak Detected by front cameras.\n")
    key = ""

    return 0

def MR12(sock):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    sock.send("Speak It is expected to swerve in 1000 feet.\n")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    sock.send("Speak Detected by prediction program.\n")
    key = ""

    return 0

def MR13(sock):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    sock.send("Speak System Error.\n")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    sock.send("Speak Detected in system's decison code.\n")
    key = ""

    return 0

def MR14(sock):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    sock.send("Speak Based on the pedestrian's trajectory, the vehicle will brake and move to the left lane.\n")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    sock.send("Speak Detected by front right sensors.\n")
    key = ""

    return 0

def MR15(sock):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    sock.send("Speak Heavy fog ahead.\n")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    sock.send("Speak Detected by vehicle's light sensors.\n")
    key = ""

    return 0

#Scenario 2 Reliable

def MR21(sock):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    sock.send("Speak Obstacle 700 feet ahead.\n")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    sock.send("Speak Detected by vehicle's front cameras.\n")
    key = ""

    return 0

def MR22(sock):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    sock.send("Speak Sensor malfunction.\n")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    sock.send("Speak Detected in system's test code.\n")
    key = ""

    return 0

def MR23(sock):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    sock.send("Speak Based on the animal's trajectory, the vehicle will brake and move to the left lane.\n")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    sock.send("Speak Detected by front cameras.\n")
    key = ""

    return 0

def MR24(sock):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    sock.send("Speak Heavy rain ahead.\n")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    sock.send("Speak Detected by vehicle's moisture sensors.\n")
    key = ""

    return 0

def MR25(sock):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    sock.send("Speak The vehicle is positioned on your left.\n")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    sock.send("Speak Detected in system's decision model.\n")
    key = ""

    return 0

#Scenario 1 Unreliable

def MU11(sock):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    sock.send("Speak Obstacle 3 miles ahead.\n")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    sock.send("Speak Detected by front cameras.\n")
    key = ""

    return 0

def MU12(sock):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    sock.send("Speak It is expected to swerve in 2 miles.\n")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    sock.send("Speak Detected by prediction program.\n")
    key = ""

    return 0

def MU13(sock):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    sock.send("Speak System Error.\n")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    sock.send("Speak Detected in system's decison code.\n")
    key = ""

    return 0

def MU14(sock):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    sock.send("Speak Based on the animal's trajectory, the vehicle will brake and move to the left lane.\n")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    sock.send("Speak Detected by front right sensors.\n")
    key = ""

    return 0

def MU15(sock):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    sock.send("Speak Heavy rain ahead.\n")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    sock.send("Speak Detected by vehicle's moisture sensors.\n")
    key = ""

    return 0

#Scenario 2 Unreliable

def MU21(sock):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    sock.send("Speak Obstacle 2 miles ahead.\n")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    sock.send("Speak Detected by vehicle's front cameras.\n")
    key = ""

    return 0

def MU22(sock):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    sock.send("Speak Sensor Malfunction.\n")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    sock.send("Speak Detected in system's test code.\n")
    key = ""

    return 0

def MU23(sock):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    sock.send("Speak Based on their trajectory, the vehicle will brake and move to the left lane.\n")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    sock.send("Speak Detected by front cameras.\n")
    key = ""

    return 0

def MU24(sock):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    sock.send("Speak Heavy fog ahead.\n")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    sock.send("Speak Detected by vehicle's light sensors.\n")
    key = ""

    return 0

def MU25(sock):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    sock.send("Speak The vehicle is positioned on your right.\n")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    sock.send("Speak Detected in system's decision model.\n")
    key = ""

    return 0


###############################
#
# NAO SPEECH FUNCTIONS
#
###############################

#Scenario 1 Reliable

def NR11(tts):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    tts.say("Obstacle quarter mile ahead.")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    tts.say("Detected by front cameras.")
    key = ""

    return 0

def NR12(tts):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    tts.say("It is expected to swerve in 1000 feet.")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    tts.say("Detected by prediction program.")
    key = ""

    return 0

def NR13(tts):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    tts.say("System Error.")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    tts.say("Detected in system's decison code.")
    key = ""

    return 0

def NR14(tts):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    tts.say("Based on the pedestrian's trajectory, the vehicle will brake and move to the left lane.")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    tts.say("Detected by front right sensors.")
    key = ""

    return 0

def NR15(tts):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    tts.say("Heavy fog ahead.")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    tts.say("Detected by vehicle's light sensors.")
    key = ""

    return 0

#Scenario 2 Reliable

def NR21(tts):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    tts.say("Obstacle 700 feet ahead.")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    tts.say("Detected by vehicle's front cameras.")
    key = ""

    return 0

def NR22(tts):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    tts.say("Sensor malfunction.")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    tts.say("Detected in system's test code.")
    key = ""

    return 0

def NR23(tts):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    tts.say("Based on the animal's trajectory, the vehicle will brake and move to the left lane.")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    tts.say("Detected by front cameras.")
    key = ""

    return 0

def NR24(tts):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    tts.say("Heavy rain ahead.")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    tts.say("Detected by vehicle's moisture sensors.")
    key = ""

    return 0

def NR25(tts):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    tts.say("The vehicle is positioned on your left.")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    tts.say("Detected in system's decision model.")
    key = ""

    return 0

#Scenario 1 Unreliable

def NU11(tts):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    tts.say("Obstacle 3 miles ahead.")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    tts.say("Detected by front cameras.")
    key = ""

    return 0

def NU12(tts):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    tts.say("It is expected to swerve in 2 miles.")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    tts.say("Detected by prediction program.")
    key = ""

    return 0

def NU13(tts):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    tts.say("System Error.")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    tts.say("Detected in system's decison code.")
    key = ""

    return 0

def NU14(tts):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    tts.say("Based on the animal's trajectory, the vehicle will brake and move to the left lane.")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    tts.say("Detected by front right sensors.")
    key = ""

    return 0

def NU15(tts):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    tts.say("Heavy rain ahead.")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    tts.say("Detected by vehicle's moisture sensors.")
    key = ""

    return 0

#Scenario 2 Unreliable

def NU21(tts):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    tts.say("Obstacle 2 miles ahead.")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    tts.say("Detected by vehicle's front cameras.")
    key = ""

    return 0

def NU22(tts):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    tts.say("Sensor Malfunction.")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    tts.say("Detected in system's test code.")
    key = ""

    return 0

def NU23(tts):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    tts.say("Based on their trajectory, the vehicle will brake and move to the left lane.")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    tts.say("Detected by front cameras.")
    key = ""

    return 0

def NU24(tts):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    tts.say("Heavy fog ahead.")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    tts.say("Detected by vehicle's light sensors.")
    key = ""

    return 0

def NU25(tts):

    key = raw_input("press b to break")
    if(key == "b"):
        return 0
    
    tts.say("The vehicle is positioned on your right.")
    key = ""

    key = raw_input("press b to break")
    if(key == "b"):
        return 0

    tts.say("Detected in system's decision model.")
    key = ""

    return 0


#############################
#
# MILO OVERARCHING FUNCTIONS
#
#############################

def MiloReliable1(sock):

    MR11(sock)
    MR12(sock)
    MR13(sock)
    MR14(sock)
    MR15(sock)

    return 0;

def MiloReliable2(sock):

    MR21(sock)
    MR22(sock)
    MR23(sock)
    MR24(sock)
    MR25(sock)

    return 0;

def MiloUnreliable1(sock):

    MU11(sock)
    MU12(sock)
    MU13(sock)
    MU14(sock)
    MU15(sock)

    return 0;

def MiloUnreliable2(sock):

    MU21(sock)
    MU22(sock)
    MU23(sock)
    MU24(sock)
    MU25(sock)

    return 0;


#############################
#
# NAO OVERARCHING FUNCTIONS
#
#############################

def NaoReliable1(tts):

    NR11(tts)
    NR12(tts)
    NR13(tts)
    NR14(tts)
    NR15(tts)

    return 0;

def NaoReliable2(tts):

    NR21(tts)
    NR22(tts)
    NR23(tts)
    NR24(tts)
    NR25(tts)

    return 0;

def NaoUnreliable1(tts):

    NU11(tts)
    NU12(tts)
    NU13(tts)
    NU14(tts)
    NU15(tts)

    return 0;

def NaoUnreliable2(tts):

    NU21(tts)
    NU22(tts)
    NU23(tts)
    NU24(tts)
    NU25(tts)

    return 0;


#####################
#
# MAIN FUNCTION
#
#####################

if(ROBOT == 0):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((MILOIP, 4001))

    if(TRUST == 0):

        if(SCENARIO == 0):
            MiloReliable1(sock)

        else:
            MiloReliable2(sock)

    else:
        if(SCENARIO == 0):
            MiloUnreliable1(sock)

        else:
            MiloUnreliable2(sock)

    sock.close()

else:

    tts = ALProxy("ALTextToSpeech", NAOIP, 9559);

    if(TRUST == 0):

        if(SCENARIO == 0):
            NaoReliable1(tts)

        else:
            NaoReliable2(tts)

    else:
        if(SCENARIO == 0):
            NaoUnreliable1(tts)

        else:
            NaoUnreliable2(tts)