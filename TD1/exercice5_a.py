"""
1. Écrire un programme Python qui affiche son PID, puis crée deux fils. Ils affichent
leur PID et leur filiation et se terminent.
"""
import os , sys




if __name__ == "__main__":
    print(f"mon ppid : {os.getpid()} , mon pere {os.getppid()}")
    numero_fils = 0
    for i in range(2):
        try:
            fork_result = os.fork()
        except OSError:
            exit(1)
        numero_fils += 1
        if fork_result == 0:
            print(f"Je suis fils numéro {numero_fils} ,mon ppid : {os.getpid()} , mon pere {os.getppid()}")
            exit(0)
    
    exit(0)
            



    