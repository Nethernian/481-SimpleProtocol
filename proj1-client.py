# CMSC 481 Project 1 -- proj1-client.py
# Nathan Woodell & Sean Arfa Russo

# This file contains the client program for our custom network protocol.
# This program requires the file Proj1Lib.py to function correctly.
# For this project it is necessary to run 

# Import Statements
import Proj1Lib
from socket import *
import errno
import time

# define variables
packetnum = 0
server_addr = "127.0.0.1"                                       # Address of the server (currently set to loopback address)
server_port = 4200                                              # port of the server (generally unused port, must be reflected by the server)
recieve_size = 1024                                             # Size of the buffer for recieving responses

# Establish Socket for sending - port number and IP assignment
client_sock = socket(AF_INET, SOCK_STREAM)                      # Despite our protocol having many of the sequencing, and loss features of TCP we use a TCP socket anyway.
client_sock.connect(server_addr, server_port)                   # Open a TCP connection with the server (using the provided address)
client_sock.setblocking(0)                                      # Insists that the new socket uses stream data instead of block data

# Send an Identify message to the user
user_id = input("Please enter your user ID: ")
IDmessage = Proj1Lib.GenIdentify(packetnum, user_id)            # generate the IDENTIFY message for the connection

# Await response from the server

# Loop to prompt the user for desired message type **

# prompt the user

# send the message over socket

# Handle return message

# End of Loop / Loop back **

# send goodbye message


# ----- Helper Functions -----

'''
formData()
This function is responsible for requesting the various data
types from the user, and formatting them into an appropriate
data format. This function takes no arguments, and instead
requests input from the user. '''
def formData():
    r_name = input("Please enter the name of your new event: ")
    r_date = input("Please enter the event date as follows: dd/mm/yyyy: ")
    r_date.append(" - " + input("Please enter the time of the event as follows: 00:00:00: "))
    r_loc = input("Please enter the location of the event (optional): ")
    r_desc = input("Please enter an event description: ")
    return [r_name, r_date, r_loc, r_desc]


'''
handleSUC(successArr)
This function is responsible for responding to the SUCCESS 
message recieved by the client from the server. This function
takes two arguments, the array from the success message, and a
string holding the last message type sent.'''
def handleSUC(successArr, Lastsent):
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
        # Handle The Success array
        return 0 # Placeholder
