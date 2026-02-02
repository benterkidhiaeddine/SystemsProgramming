import os 
# va causer une erreur
argv = ["ls", "-lt", "/"]
try:
    os.execv("/bin/ls", argv)
except OSError as e:
    print("There was an error",  e)

# Cette ligne ne veut pas etre executé parceque la commande exec remplace le code du processus en éxecution par 
# le code de l'excutable passé
print("this will not execute in case of the execution of ls")