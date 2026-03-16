import os, sys

"""
méthode standard
ch = input()
print(ch)
"""


BUFFSIZE = 1024

# Lire sur l'entrée standard dans un buffer
b = os.read(0, BUFFSIZE)

# Ecrire ce qui a été lu dans le buffer b dans la sortie standard
os.write(1, b)
