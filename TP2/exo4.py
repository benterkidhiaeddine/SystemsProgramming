import os, sys, signal, time


if len(sys.argv) != 2:
    print("Usage exo4.py [n:int]")
    sys.exit(0)
try:
    n = int(sys.argv[1])
except ValueError:
    print("Usage exo4.py [n:int]")
    sys.exit(0)


try:
    pid = os.fork()
except OSError as e:
    print("Error :", e)
    sys.exit(1)


if pid == 0:  # Fils
    ppid = os.getppid()
    while n > 0:
        os.kill(ppid, signal.SIGUSR1)
        n -= 1
    sys.exit(0)

compteur = 0


# Père
def SIGUSR1_handler(sig_num, frame):
    global compteur
    compteur += 1


signal.signal(signal.SIGUSR1, SIGUSR1_handler)
os.wait()
print("Nombre de signal recues est", compteur)
sys.exit(0)
