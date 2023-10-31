# Send an Identify message to the user 
user_id = input("Please enter your user ID: ")
IDmessage = Proj1Lib.GenIdentify(packetnum, user_id)            # generate the IDENTIFY message for the connection
client_sock.send(IDmessage.encode())                            # Encode the message to be sent
time.sleep(0.1)
while True:
    try:
        inc_msg = client_sock.recv(recieve_size)
    except error as e:
        if e.errno == errno.EWOULDBLOCK:
            break
        else:
            client_sock.close()                                 # close the socket
            exit(1)                                             # A major error end the program
    

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
        client_sock.close()                                     # close the client socket.

    else:                                                       # Handle any errors in data
        print("Please Select a Valid option.")
    # send the message over socket

    # Handle return message

    # End of Loop / Loop back **
    break

# send goodbye message