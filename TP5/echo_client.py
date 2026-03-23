import os, sys, atexit
import client


MAXBYTES = 4096

# Récupérer le path de la fifo du serveur de la ligne de commande
server_fifo_path = sys.argv[1]

# Créer le fifo unique du client
pid = os.getpid()
client_fifo_path = f"/tmp/{pid}client.fifo"
os.mkfifo(client_fifo_path)


#  Ouvrir le fifo de serveur en mode écriture
fd_w = os.open(server_fifo_path, os.O_WRONLY)

# Envoyer le chemin de fifo de client (L'envoyer pour le serveur)
os.write(fd_w, client_fifo_path.encode("utf-8"))

# Ouvrir le fifo de client en mode lecture
fd_r = os.open(client_fifo_path, os.O_RDONLY)

client.client(fd_r, fd_w)


def cleanup():
    global client_fifo_path
    global fd_r
    # Ferme sa propre fifo

    os.write(1, b"closing client fifo\n")
    os.close(fd_r)
    os.write(1, b"removing client fifo\n")
    os.remove(client_fifo_path)


atexit.register(cleanup)
sys.exit(0)
