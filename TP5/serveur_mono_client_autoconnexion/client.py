import os, sys

MAXLINE = 1000


def client(readfd, writefd):
    """
    readfed : file descriptor of client fifo , recieves bytes from server
    writefd : file descripor of server fifo, recieves bytes from client

    """
    global MAXLINE
    # Récuper le texte sur  l'entrée standard et l'envoyer au serveur
    while True:
        text = input("> ")

        if text == "exit":
            os.write(1, b"Exiting ...\n")
            break
        os.write(writefd, text.encode("utf-8"))

        # Récuper le text recue depuis le serveur
        buff = os.read(readfd, MAXLINE)

        os.write(1, buff)  # écrire contenu du tube sur la sortie standard
        os.write(1, b"\n")
