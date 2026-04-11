import os
import sys

import server

if __name__ == "__main__":
    # Le serveur a besoin du flot de lecture de tube du père vers le fils et le flot d'écriture du fils vers le père seulement
    try:
        w_child_to_father = os.open("child_to_father.fifo", os.O_WRONLY)
        r_father_to_child = os.open("father_to_child.fifo", os.O_RDONLY)

    except FileNotFoundError:
        os.write("The fifos don't exist try to create them first \n")
        sys.exit(1)
    server.server(r_father_to_child, w_child_to_father)  # fils éxecute serveur
