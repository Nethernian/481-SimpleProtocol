# CMSC 481 Project 1 -- Proj1Lib.py
# Nathan Woodell & Sean Arfa Russo

# This file contains the majority of the code for CMSC 481's project 1.
# For this project we must develop a Application Layer web protocol, which we
# will simulate using the UMBC cyberrange, and the python sockets package. The
# requirements for the project are outlined in the file "ProjectDocument.pdf".

# Import Statements
import socket

'''
GenSuccess(ptkID, token, code, data="")
This function generates the success message, and returns it as a
properly defined string (or set of strings). This function takes
three arguements, and an optional data argument. If this is not
defined in the function call, the data section will default to
an empty string.'''

def GenSuccess(pktID, token, code, data=""):
    return 0


'''
GenIdentify(pktID, user_ID)
This function generates the Identify message. This should be 
sent by the client to the server. This is the only message that
doesn't fit the traditional pktID-token format. '''
def GenIdentify(pktID, user_ID):
    return 0


'''
GenAdd(pktID, token, name, date, loc="", desc="")
This function creates a ADD message. This function takes the
standard set of inputs, and a few data fields. The name, and
date field are required, while the loc and desc fields are 
optional. Note that the name="all" message is reserved.'''
def GenAdd(pkdID, token, name, date, loc="", desc=""):
    return 0


'''
GenRem(pktID, token, name)
This function creates a REM message. This function will take the
standard set of inputs, and the name data field. This function
will then return the formed remove message.'''
def GenRem(pktID, token, name):
    return 0


'''
GenGet(pktID, token, name="ALL")
This function creates a GET message, and accepts the following
fields: pktID, token, and name. This function will return the
a properly formatted string.'''
def GenGet(pktID, token, name):
    return 0

'''
GenEnd(pktID, token)
This function creates a END message, and accepts the following
fields: pktID and token. This function will return the correctly
formatted array, which will be used to end the connection.'''
def GenEnd(pktID, token):
    return 0