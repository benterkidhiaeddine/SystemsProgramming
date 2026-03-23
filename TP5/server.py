import os, sys

MAXLINE = 1000


def server(readfd, writefd):
    """


    Args:
        readfd (_type_): fd of server fifo for reading
        writefd (_type_): fd of client for writing
    """
    global MAXLINE
    buff = os.read(readfd, MAXLINE)

    # Renvoyer au client le texte recue
    while len(buff) > 0:
        os.write(writefd, buff)
        buff = os.read(readfd, MAXLINE)
