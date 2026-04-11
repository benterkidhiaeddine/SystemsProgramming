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
    rfd1, wfd1 = os.pipe()  # tube père vers fils
    rfd2, wfd2 = os.pipe()  # tube fils vers père
    childpid = os.fork()
    if childpid == 0:  # child == server
        # Le serveur a besoin du flot de lecture de tube du père vers le fils et le flot d'écriture du fils vers le père seulement
        os.close(wfd1)
        os.close(rfd2)
        server.server(rfd1, wfd2)  # fils éxecute serveur

    else:  # father
        # Le client a besoin du flot de lecture de tube du fils vers le père et le flot d'écriture du père vers le fils seulement
        os.close(rfd1)
        os.close(wfd2)
        client.client(rfd2, wfd1)  # père exécute client
        os.waitpid(childpid, 0)  # attendre fin fils
    sys.exit(0)
