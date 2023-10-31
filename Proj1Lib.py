# CMSC 481 Project 1 -- Proj1Lib.py
# Nathan Woodell & Sean Arfa Russo

# This file contains all of the various library files, used to format the messages sent
# over the network, into an easily readable/transmittable format. This library is meant
# to be used on both the server, and the client.

# Import Statements
import socket
import string

'''
GenSuccess(ptkID, token, code, data="")
This function generates the success message, and returns it as a
properly defined string (or set of strings). This function takes
three arguements, and an optional data argument. If this is not
defined in the function call, the data section will default to
an empty string.'''

def GenSuccess(pktID, token, code, data=""):
    pktID = str(pktID)
    return "SUCCESS" + "&" + pktID + "&" + token + "&" + code + "&" + data + "//E"


'''
GenIdentify(pktID, user_ID)
This function generates the Identify message. This should be 
sent by the client to the server. This is the only message that
doesn't fit the traditional pktID-token format. '''
def GenIdentify(pktID, user_ID):
    pktID = str(pktID)
    return "IDENTIFY" + "&" + pktID + "&" + user_ID + "//E"


'''
GenAdd(pktID, token, name, date, loc="", desc="")
This function creates a ADD message. This function takes the
standard set of inputs, and a few data fields. The name, and
date field are required, while the loc and desc fields are 
optional. Note that the name="all" message is reserved.'''
def GenAdd(pktID, token, name, date, loc="", desc=""):
    pktID = str(pktID)
    return "ADD" + "&" + pktID + "&" + token + "&" + name + "&" + date + "&" + loc + "&" + desc + "//E"


'''
GenRem(pktID, token, name)
This function creates a REM message. This function will take the
standard set of inputs, and the name data field. This function
will then return the formed remove message.'''
def GenRem(pktID, token, name):
    pktID = str(pktID)
    return "REM" + "&" + pktID + "&" + token + "&" + name + "//E"


'''
GenGet(pktID, token, name="ALL")
This function creates a GET message, and accepts the following
fields: pktID, token, and name. This function will return the
a properly formatted string.'''
def GenGet(pktID, token, name):
    pktID = str(pktID)
    return "GET" + "&" + pktID + "&" + token + "&" + name + "//E"

'''
GenEnd(pktID, token)
This function creates a END message, and accepts the following
fields: pktID and token. This function will return the correctly
formatted array, which will be used to end the connection.'''
def GenEnd(pktID, token):
    pktID = str(pktID)
    return "END" + "&" + pktID + "&" + token + "//E"



# ---------- Handle Data Issues ----------

'''
DigestPacket(pktstring)
This function recieves the packet's string, and breaks it down
following the specified method. This function will return an
array to the user.'''
def DigestPacket(pktstring):
    packetdigest = pktstring.split("&")
    if packetdigest[0] == "IDENTIFY":                           # handle IDENTIFY messages
        print("Handling IDENTIFY Message")
        packetdigest[2].replace("//E", "")
        return [packetdigest[0], packetdigest[1], packetdigest[2]]

    elif packetdigest[0] == "ADD":                              # handle ADD messages
        print("Handling ADD Message")
        packetdigest[6].replace("//E", "")
        return [packetdigest[0], packetdigest[1], packetdigest[2], packetdigest[3], packetdigest[4], packetdigest[5], packetdigest[6]]
    
    elif packetdigest[0] == "REM":                              # handle REM messages
        print("Handling REM Message")
        packetdigest[3].replace("//E", "")
        return [packetdigest[0], packetdigest[1], packetdigest[2], packetdigest[3]]
    
    elif packetdigest[0] == "GET":                              # handle GET messages
        print("Handling GET Message")
        packetdigest[3].replace("//E", "")
        return [packetdigest[0], packetdigest[1], packetdigest[2], packetdigest[3]]
    
    elif packetdigest[0] == "END":                              # handle END messages
        print("Handling END Message")
        packetdigest[2].replace("//E", "")
        return [packetdigest[0], packetdigest[1], packetdigest[2]]
    
    elif packetdigest[0] == "SUCCESS":                          # handle SUCCESS messages
        print("Handling SUCCESS Message")
        packetdigest[4].replace("//E", "")
        return [packetdigest[0], packetdigest[1], packetdigest[2], packetdigest[3], packetdigest[4]]
    else:
        return 0
    

'''
handleSUC(successArr)
This function is responsible for responding to the SUCCESS 
message recieved by the client from the server. This function
takes two arguments, the array from the success message, and a
string holding the last message type sent.'''
def handleSUC(successArr, Lastsent):
    if successArr[0] != "SUCCESS":
        print("Non-Success array fed to function")
        return 0

    if Lastsent == "IDENTIFY":
        # Handle The Success array
        return 1 # Placeholder
    
    elif Lastsent == "ADD":
        # Handle The Success array
        return 2 # Placeholder
    
    elif Lastsent == "REM":
        # Handle The Success array
        return 3 # Placeholder
    
    elif Lastsent == "GET":
        # Handle The Success array
        return 4 # Placeholder
    
    else:
        print("Bad-Packet-Type")
        return 0 # Placeholder
