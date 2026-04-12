import select
import socket
import sys

HOST = "127.0.0.1"  # or 'localhost' or '' - Standard loopback interface address
PORT = 2003  # Port to listen on (non-privileged ports are > 1023)
MAXBYTES = 4096
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((HOST, PORT))
serversocket.listen()


# Sockets objects are treated like file descriptors , that's why we put the
# stdin file descriptor in the socket list
socketlist = [serversocket, sys.stdin]

running = True
while running:
    # select basicaly selects the file descriptors that are ready for reading , writing or for whome some exceptional
    # condition appliy
    # In our case we will only use the readable list to accept client sockets
    (readable, _, _) = select.select(socketlist, [], [])
    for fd in readable:
        if fd == serversocket:  # serversocket receives a connection
            (clientsocket, (addr, port)) = fd.accept()
            print("connection from:", addr, port)
            socketlist.append(clientsocket)
        elif fd == sys.stdin:  # keyboard input
            _ = sys.stdin.readline()
            running = False
        else:  # data is sent from given client
            data = fd.recv(MAXBYTES)
            if len(data) > 0:
                fd.sendall(data)
            else:  # client has disconnected
                socketlist.remove(fd)
                fd.close()
# Close all client connections

for c in socketlist:
    c.close()

serversocket.close()
