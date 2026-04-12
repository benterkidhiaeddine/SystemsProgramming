"""
1. Écrire un programme Python qui crée 3 fils, chacun des fils créant 2 petits-fils. Le
programme et chacun des fils ou petits-fils affichent leur rang dans la fratrie, leur
PID et se terminent.
2. Modifier le programme pour que les nombres de fils et de petits-fils qu’il crée soient
reçus en arguments de la ligne de commande

"""

import os
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} nombre_fils nombre_petit_fils")
        sys.exit(1)

    nombre_fils = int(sys.argv[1])
    nombre_petit_fils = int(sys.argv[2])

    for i in range(1, nombre_fils + 1):
        try:
            child_pid = os.fork()
        except OSError:
            print("Error forking")
            sys.exit(1)

        if child_pid == 0:
            for j in range(1, nombre_petit_fils + 1):
                try:
                    grand_child_pid = os.fork()
                except OSError:
                    print("Error forking")
                    sys.exit(1)

                if grand_child_pid == 0:
                    print(f"pid = {os.getpid()} , petit_fils = {i}.{j}")
                    sys.exit(0)

            # Après avoir créer ces peit fils il peut se terminer
            print(f"pid = {os.getpid()} , fils {i}")

            for j in range(1, nombre_petit_fils + 1):
                # attend la fin de ces deux petit fils après il peut se terminer
                os.wait()
            sys.exit(0)

    for i in range(1, nombre_fils + 1):
        os.wait()

    sys.exit(0)
