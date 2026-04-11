import os

MAXLINE = 1000


def server(readfd, writefd):
    global MAXLINE
    buff = os.read(readfd, MAXLINE)

    try:
        # On attend de recevoir un nom de fichier par le client
        print(buff.decode("utf-8"))
        fd = os.open(buff.decode("utf-8"), os.O_RDONLY)

    # La mnaière la plus safe pour gérer ca et OSError parceque c'est plus générique
    except FileNotFoundError:
        os.write(writefd, b"error: can't open " + buff + b"\n")
    else:
        # ouverture réussie
        buff = os.read(fd, MAXLINE)
        while len(buff) > 0:
            # écrire au client le contenue du fichier et lire du fichier
            os.write(writefd, buff)
            buff = os.read(fd, MAXLINE)
        os.close(fd)
