"""
1. Écrire un programme Python qui affiche son PID, puis crée deux fils. Ils affichent
leur PID et leur filiation et se terminent.
"""
import os , sys




if __name__ == "__main__":
    print(f"mon ppid : {os.getpid()} , mon pere {os.getppid()}")

    fork_result = os.fork()

    if fork_result == 0:
        print(f"je suis le fils: mon ppid : {os.getpid()} , mon pere {os.getppid()}")
        fork_res_2 = os.fork()

        if fork_res_2 == 0:
            print(f"je suis le petit fils: mon ppid : {os.getpid()} , mon pere {os.getppid()}")
            exit(0)# Sortie de petit fils

        exit(0) # Sortie de fils
        
    exit(0) # Sortie de  père
            



    