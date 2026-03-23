# logger.py
import os


# Récupérer la commande de l'utilsiateur
cmd = input("commande? ")
# Ouvrir un fichier "log.txt" , s'il n'existe pas crée le
fd = os.open("log.txt", os.O_WRONLY | os.O_CREAT | os.O_APPEND)

# Copie le descripteur de fichier de log.txt vers la sortie standard , ce qui fait
# que la sortie standard va etre rederigé vers log.txt
os.dup2(fd, 1)

# Femer le fichiher pour eviter la perte de mémoire
os.close(fd)  # <- bonne pratique


# Déviser le inputs en commande et arguments de commandes
args = cmd.split(" ")
# éxecuter la commande
os.execvp(args[0], args)

# La sortie standard de la commande va etre rederigé vers log.txt
