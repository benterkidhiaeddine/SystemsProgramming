import os
import socket
import sys

MAXBYTES = 4096
host = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
port = sys.argv[2] if len(sys.argv) > 2 else "2000"

sockadress = (host, int(port))

# Create a client socket IPv4 and TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client socket to the server socket
client_socket.connect(
    sockadress
)  # Cette appel est bloquante, elle retourne seulement si la connexion est établie
print("Connected to server: ", sockadress)
while True:
    # Read lines from stdin
    line = os.read(0, MAXBYTES)
    if len(line) == 0:
        client_socket.shutdown(socket.SHUT_WR)
        break
    # Send the line to the server
    client_socket.send(line)

    # Recieve data from the server
    data = client_socket.recv(MAXBYTES)
    if len(data) == 0:
        break

    # Write it to stdout
    os.write(1, data)

client_socket.close()
