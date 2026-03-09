import errno, os, sys, time

nbChildren = 20

# Stocker les pids de tous les fils crés
liste_de_pids = []
for i in range(nbChildren):
    pid = os.fork()
    if pid != 0:
        print(f"Un fils avec le pid {pid} a été crée")
    liste_de_pids.append(pid)
    if pid == 0:  # child
        time.sleep(20)
        sys.exit(100 + i)


for pid in liste_de_pids:
    pid, status = os.waitpid(pid, 0)
    if os.WIFEXITED(status):
        print(
            f"child {pid} terminated normally with exit status={os.WEXITSTATUS(status)}"
        )
    elif os.WIFSIGNALED(status):
        print(f"child {pid} terminated due to singal {os.WTERMSIG(status)}")
    else:
        print(f"child {pid} terminated abnormally")
print("No more children left. Bye")
sys.exit(0)
