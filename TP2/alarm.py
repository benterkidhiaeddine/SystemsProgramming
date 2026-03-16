import os, time, sys, signal


STD_IN = 0
STD_OUT = 1


def ALRM_handler(sig_num, frame):
    signal.alarm(1)
    try:
        os.kill(os.getppid(), 0)
    except OSError:
        os.write(STD_OUT, "mon père a terminé".encode("utf-8"))
        sys.exit(0)


pid = os.fork()
if pid == 0:  # fils
    print(
        f"Fils : {os.getpid()}",
    )
    signal.signal(signal.SIGALRM, ALRM_handler)
    signal.alarm(1)
    while True:
        pass


counter = 1

# Trouver un moyen de continuer à lire de l'entrée standard jusqà un charactère de nouvelle ligne ou EOF
b = os.read(STD_IN, 1)
while len(b) != 0:
    os.write(STD_OUT, b)
    b = os.read(STD_IN, 1)


sys.exit(0)
