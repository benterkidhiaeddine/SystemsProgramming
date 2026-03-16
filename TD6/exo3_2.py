import os, sys

BUFFSIZE = 1024


fd = os.open("input.txt", os.O_RDONLY)

# Lorsque on a copié le pointeur de descripteur de input.txt vers le pointeur de l'entrée standard
# on a rederigé l'entrée standard pour qu'elle pointe au fichier input.txt
# Donc  on est entrain de lire de input.txt à la place de l'entrée standard normal


# Résumé : Redireger a vers b == copier le descripteur de b à a
os.dup2(fd, 0)

b = os.read(0, BUFFSIZE)  # 0 = input.txt , Il entrain de lire directement de input.txt

nb_octets_effectivements_écrits = os.write(1, b)
os.write(2, f"{nb_octets_effectivements_écrits} octets écrits \n".encode("utf-8"))


os.close(fd)


# Une autre manière de faire cet exercice et de feremer le descripteur de fichiher de l'entrée s
# standard via os.close(0)
# le premier fd = 0 va etre libéré
# lorsque on fait fd = os.open("input.txt", os.O_RDONLY) il va etre mis dans le 0

# sinon on utilise la primitive os.dup(fd) après os.close(0) qui copie fd dans  le premier
# descripteur libre
