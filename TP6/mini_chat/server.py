import os
import select
import socket

HOST = "127.0.0.1"  # or 'localhost' or '' - Standard loopback interface address
PORT = 2003  # Port to listen on (non-privileged ports are > 1023)
MAXBYTES = 4096

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((HOST, PORT))
serversocket.listen()
os.write(
    1,
    b"Listnening on host:"
    + HOST.encode("utf-8")
    + b" port:"
    + str(PORT).encode("utf-8")
    + b"\n",
)

socketlist = [serversocket]
socket_dict = {"@serveur": serversocket}


while len(socket_dict.values()) > 0:
    (readable, _, _) = select.select(socketlist, [], [])

    for s in readable:
        if s == serversocket:
            # serversocket receives a connection
            (clientsocket, (addr, port)) = s.accept()
            print("connection from:", addr, port)
            socketlist.append(clientsocket)
        else:
            # data is sent from given client
            data = s.recv(MAXBYTES)

            # Si le client est dèja connecté
            data = data.decode("utf-8").split("#")
            client_id = data[0]
            client_message = data[1]
            # Assocaite the client id with it's socket
            if s not in socketlist:
                socket_dict[client_id] = s

            if len(data) > 0:
                s.sendall(data)
            else:
                # client has disconnected
                s.close()
                socketlist.remove(s)

serversocket.close()
