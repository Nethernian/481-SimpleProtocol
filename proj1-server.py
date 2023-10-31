# CMSC 481 Project 1 -- driver.py
# Nathan Woodell & Sean Arfa Russo

# This project will serve as a basic driver file for CMSC 481's Project 1.
# We have been tasked with creating a Simple Application Protocol - the outline
# for this project is contained in the file titled "ProjectDocument.pdf". The
# code used by this driver is contained in the file "Proj1Lib.py"

# Import Statements
import Proj1Lib
from socket import *
import errno
import time

# define variables
server_port = 4200                                              # generally unused port that the server can listen on.
recieve_sze = 2048                                              # size of buffer to recieve packets

# define data structures to contain server objects


# bind listener
server_sock = socket(AF_INET, SOCK_STREAM)                      # Create the socket in stream mode
server_sock.bind((('', server_port)))                           # bind the socket to the port specified above
server_sock.listen(1)                                           # Listen on the aforementioned port
print("Server Listening on Port: ", server_port)

# loop to recieve from the client on specified port **
while True:
    # accept a new connection
    cli_sck, cli_addr = server_sock.accept()
    print("Accepted Connection From: ", cli_addr)
    cli_sck.setblocking(0)

    while True:
        try:
            # handle incoming packet
            incmsg = cli_sck.recv(recieve_sze)
            incmsg = incmsg.decode()
            if (len(incmsg) > 0):
                print(incmsg)
                successmsg = incmsg # NEED TO BE UPDATED SOON
                # send correct SUCCESS packet to the user
                cli_sck.send(successmsg.encode())
                continue
            else:
                break
        except error as e:
            if e.errno == errno.EWOULDBLOCK:
                time.sleep(0.1)
                continue
            else:
                break
    cli_sck.close()
    # end loop and await new packet **
    