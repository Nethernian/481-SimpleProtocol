# CMSC 481 Project 1 -- Proj1Lib.py
# Nathan Woodell & Sean Arfa Russo

# This file contains the majority of the code for CMSC 481's project 1.
# For this project we must develop a Application Layer web protocol, which we
# will simulate using the UMBC cyberrange, and the python sockets package. The
# requirements for the project are outlined in the file "ProjectDocument.pdf".

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
    return "SUCCESS" + "&" + pktID + "&" + token + "&" + code + "&" + data


'''
GenIdentify(pktID, user_ID)
This function generates the Identify message. This should be 
sent by the client to the server. This is the only message that
doesn't fit the traditional pktID-token format. '''
def GenIdentify(pktID, user_ID):
    return "IDENTIFY" + "&" + pktID + "&" + user_ID


'''
GenAdd(pktID, token, name, date, loc="", desc="")
This function creates a ADD message. This function takes the
standard set of inputs, and a few data fields. The name, and
date field are required, while the loc and desc fields are 
optional. Note that the name="all" message is reserved.'''
def GenAdd(pkdID, token, name, date, loc="", desc=""):
    return "ADD" + "&" + pkdID + "&" + token + "&" + name + "&" + date + "&" + loc + "&" + desc


'''
GenRem(pktID, token, name)
This function creates a REM message. This function will take the
standard set of inputs, and the name data field. This function
will then return the formed remove message.'''
def GenRem(pktID, token, name):
    return "REM" + "&" + pktID + "&" + token + "&" + name


'''
GenGet(pktID, token, name="ALL")
This function creates a GET message, and accepts the following
fields: pktID, token, and name. This function will return the
a properly formatted string.'''
def GenGet(pktID, token, name):
    return "GET" + "&" + pktID + "&" + token + "&" + name

'''
GenEnd(pktID, token)
This function creates a END message, and accepts the following
fields: pktID and token. This function will return the correctly
formatted array, which will be used to end the connection.'''
def GenEnd(pktID, token):
    return "END" + "&" + pktID + "&" + token


'''
DigestPacket(pktstring)
This function recieves the packet's string, and breaks it down
following the specified method. This function will return an
array to the user.'''
def DigestPacket(pktstring):
    packetdigest = pktstring.split("&")
    if packetdigest[0] == "IDENTIFY":
        return 0
    elif packetdigest[0] == "ADD":
        return 1
    elif packetdigest[0] == "REM":
        return 2
    elif packetdigest[0] == "GET":
        return 3
    elif packetdigest[0] == "END":
        return 4
    elif packetdigest[0] == "SUCCESS":
        return 5