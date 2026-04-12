"""
Écrire un programme qui réalise une chaîne de n sous-processus, où n est passée en paramètre de
lexécution de la commande (par exemple, n = 3 sur la figure ci-dessus). Faire
imprimer le numéro de chaque processus et celui de son père. Même question avec la struc￾ture en arbre.
"""

import os
import sys


def arbre_processus(n):
    for i in range(n):
        try:
            fork_result = os.fork()
        except OSError:
            exit(1)
        if fork_result == 0:  # fils
            print(f"le pid de père est {os.getppid()} et mon pid est {os.getpid()}")
        else:  # père meurt
            sys.exit(0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <number_of_processes: int>")
        sys.exit(1)

    n = int(sys.argv[1])

    # Le père affiche d'abbord
    print(f"le pid de père est {os.getppid()} et mon pid est {os.getpid()}")

    arbre_processus(n)
    exit(0)
