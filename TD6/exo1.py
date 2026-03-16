import os, sys


fd1 = os.open("toto.txt", os.O_RDONLY)
print(fd1)
os.close(fd1)


fd2 = os.open("titi.txt", os.O_RDONLY)
print(fd2)


fd3 = os.open("titi.txt", os.O_RDONLY)
print(fd3)
os.close(fd2)
os.close(fd3)

# Le comportement de ce programme c'est afficher 3 3 4
# Parceque le processus prend le premier descripteur de fichier qui est libre , 0 1 2 sont pris respectivement par stdin, stdout et
# stderr


# On peut remarquer aussi qu'un meme fichier peut etre ouvert par deux descripteurs de fichiers
