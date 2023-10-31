# CMSC 481 Project 1 -- driver.py
# Nathan Woodell & Sean Arfa Russo

# This project will serve as a basic driver file for CMSC 481's Project 1.
# We have been tasked with creating a Simple Application Protocol - the outline
# for this project is contained in the file titled "ProjectDocument.pdf". The
# code used by this driver is contained in the file "Proj1Lib.py"

# Import Statements
from socket import *
import errno, time, random, Proj1Lib


# define variables
server_port = 4200                                              # generally unused port that the server can listen on.
recieve_sze = 2048                                              # size of buffer to recieve packets

# define data structures to contain server objects
#dict(user_id = "Bobby", token = "", )

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
            inc_msg = cli_sck.recv(recieve_sze)
            inc_msg = inc_msg.decode()
            print("Accepted packet: ", inc_msg)
            

            if (len(inc_msg) > 0):
                inc_arr = Proj1Lib.DigestPacket(inc_msg)
                
                if inc_arr[0] == "IDENTIFY":                    # Handle based on index [0]
                    ret_tkn = str(hash(inc_arr[2]+str(random.randint(0,1000))))
                    # NEED TO DETERMINE CORRECT <code> field
                    success_rtn = Proj1Lib.GenSuccess(inc_arr[1], ret_tkn, "ok", inc_arr[0])
                    print("sending: ", success_rtn, "to address: ", cli_addr)

                elif inc_arr[0] == "GET":                       # Handle based on index [0]
                    # NEED TO DETERMINE CORRECT <code> and <data> fields
                    success_rtn = Proj1Lib.GenSuccess(inc_arr[1], inc_arr[2], "ok", inc_arr[0])

                elif inc_arr[0] == "REM":                       # Handle based on index [0]
                    # NEED TO DETERMINE CORRECT <code> field
                    success_rtn = Proj1Lib.GenSuccess(inc_arr[1], inc_arr[2], "ok", inc_arr[0])

                elif inc_arr[0] == "ADD":                       # Handle based on index [0]
                    # Validate incoming token
                    # Check for event name in user's calendar
                    # Add or deny
                    # send Success message # PLACEHOLDER -- Needs Edits
                    success_rtn = Proj1Lib.GenSuccess(inc_arr[1], inc_arr[2], "ok", inc_arr[0])

                elif inc_arr[0] == "END":                       # Handle based on index [0]
                    # Set the user token to '' in the database - end the session
                    break # Placeholder
                
                cli_sck.send(success_rtn.encode())
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
    