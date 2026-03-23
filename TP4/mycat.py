import os, sys


args = sys.argv
MAXBUFFER = 1024
STDIN = 0


def read_and_print(fd):
    octets = os.read(fd, MAXBUFFER)
    while octets:
        os.write(1, octets)
        octets = os.read(fd, MAXBUFFER)


# Comportement fichihers Fichier_n -> STDOUT
if len(args) >= 2:
    for filename in args[1:]:
        fd = os.open(filename, os.O_RDONLY, 0o644)
        read_and_print(fd)
        os.close(fd)

# Comportement sans fichihers STDIN -> STDOUT
else:
    read_and_print(STDIN)
