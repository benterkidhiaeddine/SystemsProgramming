import os
import sys

import client

if __name__ == "__main__":
    # Le client a besoin du flot de lecture de tube du fils vers le père et le flot d'écriture du père vers le fils seulement
    try:
        r_child_to_father = os.open("child_to_father.fifo", os.O_RDONLY)
        w_father_to_child = os.open("father_to_child.fifo", os.O_WRONLY)
    except FileNotFoundError:
        os.write(1, "The fifos don't exist \n")
        sys.exit(1)

    client.client(r_child_to_father, w_father_to_child)
