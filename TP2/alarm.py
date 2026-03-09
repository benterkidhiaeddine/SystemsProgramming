import os, time, sys


pid = os.fork()

if pid == 0:  # fils
    ppid = os.getppid()
    while True:
        try:
            # Vérifier si le parent existe ou pas
            os.kill(ppid, 0)
            time.sleep(1)
        except OSError:
            os.write(0, "Mon père a terminé".encode("utf-8"))
            sys.exit(0)


counter = 1
while counter <= 5:
    b = os.read(0, 1)

    os.write(1, b)
    counter += 1
    time.sleep(2)


sys.exit(0)
