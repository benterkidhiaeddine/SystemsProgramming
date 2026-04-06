import os
import socket
import string
import sys

MAXBYTES = 4096
if len(sys.argv) != 3:
    print("Usage:", sys.argv[0], "hote port")
    sys.exit(1)

HOST = sys.argv[1]
PORT = int(sys.argv[2])

sockaddr = (HOST, PORT)

pid = os.getpid()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4, TCP
s.connect(sockaddr)
print("connected to:", sockaddr)

connection_accepted = False
command_list = ["@tous", "@leave"]


# The client chooses his pseudo
pseudo = input("What is your pseudo")
if pseudo in command_list:
    print("choose another client name")
    print("Existing ...")
    sys.exit(1)


for c in pseudo:
    if c in string.punctuation:
        print(f"the username can't have {string.punctuation}")
        print("Existing ...")
        sys.exit(1)


# Protocol :
"""
liste_clients : client_1,client_2,...client3\n
message_serveur : message_serveur\n
connection_accpeted : boolean vaariable to check if we did a first connection with the server
available_commands : list of commands that contains all available client as well as @tous that make it possible to send message to all
other clients , and disconnect
"""
retries = 0
while True:
    # First time we enter the while loop we establish connection and get client list to show to
    # the connected clients
    if not connection_accepted:
        # envoyer le pseudo
        message = pseudo.encode("utf-8") + b"#"

        data = s.recv(MAXBYTES)  # attention, si le serveur n'envoie rien on est bloqué.

        # Si le serveur accept il va renvoyer OK
        if len(data) == 0:
            break

        # Parse the server message to get connected clients
        message_list = data.decode("utf-8").split("#")

        confirmation = message_list[1]
        if confirmation == "OK":
            connection_accepted = True
        else:
            if retries < 3:
                retries += 1

    else:
        # If we are already connected show to the client list of available commands
        os.write(1, "Choose an action")
        for i, value in enumerate(command_list):
            message = f"{i}: {value}".encode("utf-8")
            os.write(1, message)

        line = os.read(0, MAXBYTES)
        if len(line) == 0:
            s.shutdown(socket.SHUT_WR)
            break

        # Creation du message avec l'identifiant
        message = pseudo.encode("utf-8") + line
        s.send(message)
        data = s.recv(MAXBYTES)  # attention, si le serveur n'envoie rien on est bloqué.

        if len(data) == 0:
            break

        # Parse the server message to get connected clients
        message = data.decode("utf-8")

        client_list = message.split("\n")[0].split(",")

        # Check if the client name is not already taken
        if pseudo in client_list:
            os.write(1, b"client name is already taken\n")
            os.write(1, b"Exiting ... \n")
            sys.exit(1)

        server_message = message.split("\n")[1]

        os.write(1, data)

s.close()
