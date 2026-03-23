import socket, sys, os

MAXBYTES = 4096
host = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
port = sys.argv[2] if len(sys.argv) > 2 else "2000"

sockadress = (host, int(port))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(
    sockadress
)  # Cette appel est bloquante, elle retourne seulement si la connexion est établie
print("Connected to server: ", sockadress)
while True:
    line = os.read(0, MAXBYTES)
    if len(line) == 0:
        client_socket.shutdown(socket.SHUT_WR)
        break

    client_socket.send(line)

    data = client_socket.recv(MAXBYTES)
    if len(data) == 0:
        break
    os.write(1, data)

client_socket.close()
