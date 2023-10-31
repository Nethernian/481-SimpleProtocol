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

# ---------- HELPER FUNCTIONS ---------- #



# ---------- MAIN CODE BASE ---------- #

# define variables
packetnum = 0
server_addr = "127.0.0.1"                                       # Address of the server (currently set to loopback address)
server_port = 4200                                              # port of the server (generally unused port, must be reflected by the server)
recieve_size = 2048                                             # Size of the buffer for recieving responses
loop_ctrl = True

# Establish Socket for sending - port number and IP assignment
client_sock = socket(AF_INET, SOCK_STREAM)                      # Despite our protocol having many of the sequencing, and loss features of TCP we use a TCP socket anyway.
client_sock.connect((server_addr, server_port))                   # Open a TCP connection with the server (using the provided address)
client_sock.setblocking(0)                                      # Insists that the new socket uses stream data instead of block data


user_ID = input("Please Input your User ID: ")
IDmsg = Proj1Lib.GenIdentify(packetnum, user_ID)
user_tkn = user_ID

while True:
    #try:
        #ID_resp = client_sock.recv()
    break

# A loop to listen, and establish a connection.
while loop_ctrl == True:
    packetnum += 1
    print("Please Select the Function you wish to perform: \n1. ADD \n2. GET\n3. REM\n4. BYE")
    choice = input("Please Make your Selection from above (1-4): ")

    # build the message or prompt the user
    if choice == "1" or choice == "ADD":
        print("---------- ADD Method Employed ----------")
        ev_name = input("Event Name: ")
        ev_date = input("Event Date: ")
        ev_loc = input("Event Location: ")
        ev_desc = input("Event Description: ")
        ADmsg = Proj1Lib.GenAdd(packetnum, user_tkn, ev_name, ev_date, ev_loc, ev_desc)

    elif choice == "2" or choice == "GET":
        print("---------- GET Method Employed ----------")

    elif choice == "3" or choice == "REM":
        print("---------- REM Method Employed ----------")

    elif choice == "4" or choice == "BYE":
        print("---------- BYE Method Employed ----------")
        #client_sock.close()
        break

    else:
        print("Invalid Message Type - Try Again")


