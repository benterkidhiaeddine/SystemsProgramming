import os
import select
import socket
import sys

HOST = "127.0.0.1"  # or 'localhost' or '' - Standard loopback interface address
PORT = 2005  # Port to listen on (non-privileged ports are > 1023)
MAXBYTES = 4096

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4, TCP
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind((HOST, PORT))

serversocket.listen()
print("server listening on port:", PORT)

nb_open = 0
# Create list of potential active sockets and place server socket in
# first position
socketlist = [serversocket]

# On the first iteration of the loop we take into account the server socket to accept our first connexion
# On subsequent iteration we only take into account the number of connected clients
# If no more clients are connected we close the server
first = True
while first or nb_open > 0:
    first = False
    (activesockets, _, _) = select.select(socketlist, [], [])
    for s in activesockets:
        if s == serversocket:
            (clientsocket, (addr, port)) = serversocket.accept()
            socketlist.append(clientsocket)
            print(f"Incoming connection from {addr} on port {port}...")
            nb_open += 1
        else:  # client socket
            msg = s.recv(MAXBYTES)
            if len(msg) == 0:
                print("NULL message. Closing connection...")
                s.close()
                # Remove the closed connection from potential active sockets
                socketlist.remove(s)
                nb_open -= 1
            else:
                msg = msg.decode("utf-8")
                argv = msg.split()
                if len(argv) >= 1:
                    # Get the client socket file descriptor
                    socket_dno = s.fileno()

                    # rederict stdout to the client file descriptor
                    os.dup2(socket_dno, 1)
                    os.dup2(socket_dno, 2)
                    try:
                        pid = os.fork()
                    except OSError:
                        os.write(2, b"Probleme forking process\n")
                        sys.exit(1)

                    if pid == 0:  # child
                        cmd = argv[0]
                        try:
                            os.execvp(cmd, argv)
                        except OSError:
                            os.write(
                                2, argv[0].encode("utf-8") + b": No such command\n"
                            )
                            sys.exit(1)

                    #  To avoid zombie processes
                    os.wait()

                else:
                    s.send(b": No such command \n")


serversocket.close()
print("Last connection closed. Bye!")
sys.exit(0)
