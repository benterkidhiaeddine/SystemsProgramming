import os
import sys

# programme générique client-serveur
# Les deux modules suivants doivent être écrits
# ils sont supposés fournir les deux méthodes
# client.client()
# server.server()
import client
import server

if __name__ == "__main__":
    childpid = os.fork()

    # Create the fifos if they don't exist:
    try:
        os.mkfifo("child_to_father.fifo", 0o644)
        os.mkfifo("father_to_child.fifo", 0o644)
    except FileExistsError:
        os.write(1, b"Fifos already exists, continue Execution\n")

    if childpid == 0:  # child == server
        # Le serveur a besoin du flot de lecture de tube du père vers le fils et le flot d'écriture du fils vers le père seulement
        w_child_to_father = os.open("child_to_father.fifo", os.O_WRONLY)
        r_father_to_child = os.open("father_to_child.fifo", os.O_RDONLY)

        server.server(r_father_to_child, w_child_to_father)  # fils éxecute serveur

    else:  # father
        # Le client a besoin du flot de lecture de tube du fils vers le père et le flot d'écriture du père vers le fils seulement
        r_child_to_father = os.open("child_to_father.fifo", os.O_RDONLY)
        w_father_to_child = os.open("father_to_child.fifo", os.O_WRONLY)

        client.client(r_child_to_father, w_father_to_child)  # père exécute client

        os.waitpid(childpid, 0)  # attendre fin fils
    sys.exit(0)
