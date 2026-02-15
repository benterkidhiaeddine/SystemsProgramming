"""
Écrire un programme qui réalise une chaîne de n sous-processus, où n est passée en paramètre de 
lexécution de la commande (par exemple, n = 3 sur la figure ci-dessus). Faire
imprimer le numéro de chaque processus et celui de son père. Même question avec la struc￾ture en arbre.
"""
import os ,sys

def arbre_processus(n):
    for i in range(n):
        try:
            fork_result = os.fork()
        except OSError as e:
            exit(1)
        if fork_result == 0:#child
            print(f"le pid de père est {os.getppid()} et mon pid est {os.getpid()}")
        else:
            exit(0)
        
            



if __name__ == "__main__":
    n = int(sys.argv[1])
    l = len(sys.argv)
    if l != 2:
        print(f"Usage exercice4_a n")
        exit(1)
    print(f"le pid de père est {os.getppid()} et mon pid est {os.getpid()}")
    arbre_processus(n)
    exit(0)