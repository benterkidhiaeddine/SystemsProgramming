import os, sys


def afficher_mon_pid_et_ppid():
    print(f"pid: {os.getpid()} pid mon père:{os.getppid()}")

for i in range(3):
    resultat_fork = os.fork()
    if resultat_fork == 0:  # Rang des fils
        for j in range(2):  # Create 2 child processes for each child
            res_fork = os.fork()
            if res_fork == 0:  # Rang des petits fils
                print(f"Je suis le petit fils pid: {os.getpid()} pid mon père:{os.getppid()}")
                sys.exit(0)
        print(f"Je suis le fils pid: {os.getpid()} pid mon père:{os.getppid()}")
        sys.exit(0)

print(f"Je suis le père pid: {os.getpid()} pid de mon père:{os.getppid()}")


