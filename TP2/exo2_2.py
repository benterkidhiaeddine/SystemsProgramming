import os, signal, sys, time


def handler(sig, ignore):
    global counter
    pid = 1  # pour amorcer la boucle while
    try:
        #  On utilise une boucle dans le handler parceque c'est possible que plusieurs fils envoie un SIGCHLD au meme temps
        while pid > 0 and counter > 0:
            # On test le pid supérieur a 0 parceque si jamais le père attend encore , et aucun fils existe waitpid retourne 0
            pid, status = os.waitpid(-1, os.WNOHANG)
            if pid > 0:
                # Pour corriger le probleme avec print qui un appel non réentrant : cad il y a un risque de collision avec les
                # signaux

                os.write(1, "père: fils {} terminé\n".format(pid).encode("utf-8"))
                # print("père: fils {} terminé\n".format(pid))
                counter -= 1
                os.write(
                    1, "Nombre de fils restants: {}\n".format(counter).encode("utf-8")
                )
    except OSError:
        pass


if __name__ == "__main__":
    signal.signal(signal.SIGCHLD, handler)
    counter = max_fils = 5
    # compte le nombre de fils restant
    # boucle de 0 a max_fils-1
    for i in range(max_fils):
        if os.fork() == 0:
            # le fils i
            print("fils {} (pid={}) terminé".format(i, os.getpid()))
            sys.exit(0)
    # ici le père peut travailler sur autre chose sans se soucier
    # de ses fils. Il fait semblant en faisant une boucle vide.
    while counter > 0:
        pass
    print("père: Tous mes fils sont terminés.")
    sys.exit(0)
    # Attention, petite faiblesse de python par raport à C:
    # vous risquez d'avoir lors de certaines exécutions:
    # RuntimeError: reentrant call inside <_io.BufferedWriter name='<stdout>'>
    # Cela provient des print() du handler qui ne sont pas réentrant.
    # i.e. un print() n'est pas terminé, alors que le handler est appelé de nouveau
    # ce qui provoque un print() au milieu d'un print().
    # Il faut trouver un astuce pour ne pas faire de print() dans les handlers.
