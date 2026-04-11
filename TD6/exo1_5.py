import os
import sys

fd1 = os.open("titi.txt", os.O_RDONLY)
fd2 = os.open("titi.txt", os.O_RDONLY)
c = os.read(fd2, 1)
# dup2 copie le descripteur de fichier fd2 dans le descripteur de fichiher fd1
os.dup2(fd2, fd1)
c = os.read(fd1, 1)
# fd1 pointe desormais vers le curseur de fd1 qui étais dans le premier octect,
# on l'avance d'un autre otctet et on lit le deuxième octect dans le texte
os.close(fd1)
os.close(fd2)
print(c)  # affiche b'a'
sys.exit(0)
