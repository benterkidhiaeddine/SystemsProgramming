import os

MAXLINE = 1000


def client(readfd, writefd):
    nomfic = input("entrez un nom de fichier : ")
    os.write(
        writefd, nomfic.encode("utf-8")
    )  # envoyer nom fichier sur tube vers serveur
    buff = os.read(readfd, MAXLINE)  # lire contenu du fichier sur tube depuis serveur
    while len(buff) > 0:
        os.write(1, buff)  # écrire contenu du tube sur la sortie standard
        buff = os.read(readfd, MAXLINE)
