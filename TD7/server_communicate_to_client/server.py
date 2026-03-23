import os, sys, socket, select

MAXBYTES = 4069

HOST = "127.0.0.1"
PORT = 2000

# Create the server socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
serversocket.bind((HOST, PORT))

fd_list = [serversocket, 0]

while len(fd_list) > 0:
    (readables, _, _) = select.select(fd_list, [], [])
    for fd in readables:
        if fd == 0:
            line = os.read(0, MAXBYTES)
            if len(line) == 0:
                
