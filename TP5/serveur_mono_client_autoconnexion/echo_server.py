import os, sys, atexit
import server


MAXBYTES = 4096

# Créer le fifo de serveur
pid = os.getpid()
server_fifo_path = f"/tmp/{pid}server.fifo"
print(f"Mon fifo est à : {server_fifo_path}")
os.mkfifo(server_fifo_path)


# Ouvrir le fifo de serveur en lecture
fd_r = os.open(server_fifo_path, os.O_RDONLY)

# Récupérer le path de fifo du client
client_fifo_path = os.read(fd_r, MAXBYTES)

os.write(1, b"connected to client fifo :" + client_fifo_path + b"\n")

# Ouvir le fifo du client en écriture
fd_w = os.open(client_fifo_path, os.O_WRONLY)

server.server(fd_r, fd_w)


def cleanup():
    global server_fifo_path
    global fd_r
    # Ferme sa propre fifo
    os.write(1, b"Closing server fifo\n")
    os.close(fd_r)
    os.write(1, b"Removing server fifo\n")
    os.remove(server_fifo_path)


atexit.register(cleanup)


sys.exit(0)
