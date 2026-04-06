import atexit
import os
import sys

import server

MAXBYTES = 4096
clients = {}


# Créer le fifo de serveur
pid = os.getpid()
server_fifo_path = f"/tmp/{pid}server.fifo"
print(f"Mon fifo est à : {server_fifo_path}")
os.mkfifo(server_fifo_path)


# Ouvrir le fifo de serveur en lecture
fd_r = os.open(server_fifo_path, os.O_RDONLY)

# Chaque client va continuer à envoyer son identifiant au début de message avec l'encodage id#Message
# Récupérer le path de fifo du client


# Manière plus simple de faire ca c'est de vérifier es que le message c'est tout simplement une demande de connextion
while True:
    client_buff = os.read(fd_r, MAXBYTES)
    client_decoded_buff = client_buff.decode("utf-8")
    client_identifiant = client_decoded_buff.split("#")[0]
    client_message = client_decoded_buff.split("#")[1]

    try:
        client_fd = os.open(client_message, os.O_WRONLY)
        if client_identifiant not in clients:
            os.write(
                1,
                b"connected to client fifo :"
                + client_identifiant.encode("utf-8")
                + b"\n",
            )
            clients[client_identifiant] = client_fd

    except:  # message n'est pas une demande de connexion
        if client_identifiant in clients:
            server.server(fd_r, clients[client_identifiant])


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
