import os
import sys


def create_fifo(name: str):
    try:
        os.mkfifo(name)
    except OSError as e:
        print(f"Error while creating fifo {name}: {e.errno}", file=sys.stderr)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} nom_fifo", file=sys.stderr)
        sys.exit(1)

    print("On essaie de creer (erreur non fatale)")
    create_fifo(sys.argv[1])

    print("On essaie d'ouvrir:")
    fd = os.open(sys.argv[1], os.O_WRONLY)

    print("On essaie d'ecrire dans fifo:")
    os.write(fd, b"blabla\n")

    print("On essaie d'ecrire encore dans fifo:")
    os.write(fd, b"blabla2\n")

    print("On ferme la fifo")
    os.close(fd)

    sys.exit(0)
