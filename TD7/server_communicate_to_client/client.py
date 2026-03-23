import os, sys, select, socket


MAXBYTES = 4096
HOST = sys.argv[1]
PORT = int(sys.argv[2])


sockadrr = (HOST, PORT)


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(sockadrr)


fd_list = [client_socket, 0]
while True:
    readables, _, _ = select.select(fd_list, [], [])
    for fd in readables:
        if fd == 0:

            line = os.read(0, MAXBYTES)
            if len(line) == 0:
                client_socket.shutdown(socket.SHUT_WR)
                break
            client_socket.send(line)
        else:

            recv_line = client_socket.recv(MAXBYTES)
            os.write(1, recv_line)
