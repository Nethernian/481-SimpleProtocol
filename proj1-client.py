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
client_sock.connect((server_addr, server_port))                 # Open a TCP connection with the server (using the provided address)
client_sock.setblocking(0)                                      # Insists that the new socket uses stream data instead of block data


user_ID = input("Please Input your User ID: ")                  # Prompt the user for an ID
IDmsg = Proj1Lib.GenIdentify(packetnum, user_ID)                # Generate an IDENTIFY message
client_sock.send(IDmsg.encode())                                # Send an Identity message
time.sleep(0.1)                                                 # Await Server Response

while True:
    try:
        success = client_sock.recv(recieve_size)
        user_tkn = Proj1Lib.DigestPacket(success.decode())[2]
        break
    except error as e:
        if e.errno == errno.EWOULDBLOCK:
            break
        else:
            exit(1)

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

        # Format our ADD message
        ADDmsg = Proj1Lib.GenAdd(packetnum, user_tkn, ev_name, ev_date, ev_loc, ev_desc)
        client_sock.send(ADDmsg.encode())                       # Send our ADD message
        time.sleep(0.1)                                         # Await Server Feedback

        # Wait for server Success message
        while True:                                             
            try:
                success = client_sock.recv(recieve_size)
                # TEMP needs to be customized success handling
                print (Proj1Lib.DigestPacket(success.decode()))
                break
            except error as e:                                  # MAGIC
                if e.errno == errno.EWOULDBLOCK:
                    break
                else:
                    exit(1)

    elif choice == "2" or choice == "GET":
        print("---------- GET Method Employed ----------")
        ev_name = input("Enter the Event Name: ")

        # Format GET message
        GETmsg = Proj1Lib.GenGet(packetnum, user_tkn, ev_name)
        client_sock.send(ADDmsg.encode())                       # Send our ADD message
        time.sleep(0.1)                                         # Await Server Feedback

        # Wait for server Success message
        while True:                                             
            try:
                success = client_sock.recv(recieve_size)
                # TEMP needs to be customized success handling
                print (Proj1Lib.DigestPacket(success.decode()))
                break
            except error as e:                                  # MAGIC
                if e.errno == errno.EWOULDBLOCK:
                    break
                else:
                    exit(1)

    elif choice == "3" or choice == "REM":
        print("---------- REM Method Employed ----------")
        ev_name = input("Enter the Event Name: ")

        # Format REM message
        GETmsg = Proj1Lib.GenGet(packetnum, user_tkn, ev_name)
        client_sock.send(ADDmsg.encode())                       # Send our ADD message
        time.sleep(0.1)                                         # Await Server Feedback

        # Wait for server Success message
        while True:                                             
            try:
                success = client_sock.recv(recieve_size)
                # TEMP needs to be customized success handling
                print (Proj1Lib.DigestPacket(success.decode()))
                break
            except error as e:                                  # MAGIC
                if e.errno == errno.EWOULDBLOCK:
                    break
                else:
                    exit(1)

    elif choice == "4" or choice == "BYE":
        print("---------- BYE Method Employed ----------")
        client_sock.close()
        break

    else:
        print("Invalid Message Type - Try Again")


