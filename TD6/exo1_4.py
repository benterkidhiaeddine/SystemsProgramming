import os
import sys

fd = os.open("toto.txt", os.O_RDONLY)
pid = os.fork()
if pid == 0:
    c = os.read(fd, 1)
    sys.exit(0)
os.wait()
c = os.read(fd, 1)
print(c)
sys.exit(0)

# Le programme va afficher 'z' parcque le fils hérite le déscripteur de fichier du père , et avec ce dernier
# il hérite aussi la position pointeur dans le fichier
