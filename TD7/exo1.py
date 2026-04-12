import socket

HOST = "127.0.0.1"  # or 'localhost' or '' - Standard loopback interface address
PORT = 2000  # Port to listen on (non-privileged ports are > 1023)
MAXBYTES = 4096
# create socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serversocket:
    # AF_INET: IPv4
    # SOCK_STREAM: TCP
    serversocket.bind((HOST, PORT))  # bind this socket to specific port on host
    serversocket.listen()  # make the socket a listening one

    # We add an infinit while loop here to make sure the server dosen't terminate when the first client disconnects
    while True:
        (
            clientsocket,
            (
                addr,
                port,
            ),
        ) = serversocket.accept()  # blocking; returns if a client connects.
        with clientsocket:
            print(f"Connected by application: {port} on machine: {addr}")
            data = clientsocket.recv(MAXBYTES)
            while (
                len(data) > 0
            ):  # otherwise means a disconnection from the client side.
                clientsocket.sendall(data)
                data = clientsocket.recv(MAXBYTES)
