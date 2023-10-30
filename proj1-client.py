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


# define variables
packetnum = 0
server_addr = "127.0.0.1"                                       # Address of the server (currently set to loopback address)
server_port = 4200                                              # port of the server (generally unused port, must be reflected by the server)
recieve_size = 1024                                             # Size of the buffer for recieving responses
loop_ctrl = True

# Establish Socket for sending - port number and IP assignment
client_sock = socket(AF_INET, SOCK_STREAM)                      # Despite our protocol having many of the sequencing, and loss features of TCP we use a TCP socket anyway.
client_sock.connect(server_addr, server_port)                   # Open a TCP connection with the server (using the provided address)
client_sock.setblocking(0)                                      # Insists that the new socket uses stream data instead of block data

# Send an Identify message to the user 
user_id = input("Please enter your user ID: ")
IDmessage = Proj1Lib.GenIdentify(packetnum, user_id)            # generate the IDENTIFY message for the connection
client_sock.send(IDmessage.encode())                            # Encode the message to be sent

# Await response from the server

# Loop to prompt the user for desired message type **
while loop_ctrl:
    packetnum += 1                                              # Increment the packet ID
    
    print("What operation would you like to perform?\n1. GET\n2. ADD\n3. REM\n4. END\n")
    userchoice = input("Please make your choice: ")             # prompt the user

    # Handle Different Message Options
    if userchoice == 1 or userchoice == "GET":                  # Handle GET messages
        msg_name = input("Please enter the name of the event you wish to get the info for: ")
        SendMessage = Proj1Lib.GenGet(packetnum, token, msg_name)
        client_sock.send(SendMessage.encode())
    elif userchoice == 2 or userchoice == "ADD":                # Handle ADD messages
        messagedata = formData()
        SendMessage = Proj1Lib.GenAdd(packetnum, token, messagedata[0], messagedata[1], messagedata[2], messagedata[3])
        client_sock.send(SendMessage.encode())
    elif userchoice == 3 or userchoice == "REM":                # Handle REM messages
        msg_name = input("Please enter the name of the message you want to remove: ")
        SendMessage = Proj1Lib.GenRem(packetnum, token, msg_name)
        client_sock.send(SendMessage.encode())
    elif userchoice == 4 or userchoice == "END":                # Handle END messages
        SendMessage = Proj1Lib.GenEnd(packetnum, token)
        client_sock.send(SendMessage.encode())                  
        loop_ctrl = False                                       # End the user input loop
    else:
        print("Please Select a Valid option.")
    # send the message over socket

    # Handle return message

    # End of Loop / Loop back **
    break

# send goodbye message


