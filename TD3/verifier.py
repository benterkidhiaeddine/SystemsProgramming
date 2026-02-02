#! /usr/bin/env python3
import os , sys
try:
    filename = sys.argv[1]
    argv = sys.argv[1:]
except IndexError:
    print(f"Usage {sys.argv[0]} com arg1 .. argn")
    sys.exit(1)


# Create child process to execute
try:
    pid = os.fork()
except OSError:
    print("Un problème est survenue lors du fork")
if pid == 0: # fils
    try:
        # On choisit execvp pour qu'on puisse seulemnt passer le nom de la commande 
        # et pas nécessairement le chemain absolue 
        os.execvp(filename, argv)
    # Trois types d'erreurs peuvent arriver lors de l'éxecution de exec
    except (PermissionError, FileNotFoundError , OSError) as e:
        print(f"Une erreur est survenue lors de l'execution de la commande {e}")
        sys.exit(1)
else: # père
    (pid , status ) = os.waitpid(-1 , 0)
    if not os.WIFEXITED(status):
        print("La commande s'est termninée avant de pouvoir rendre un code de sortie ")
    exit_code = os.WEXITSTATUS(status)
    if exit_code == 0:
        print("La commande a terminé avec succès")
    else:
        print(f"La commande s'est terminé avbec echec code :{ exit_code}")
    sys.exit(0)
