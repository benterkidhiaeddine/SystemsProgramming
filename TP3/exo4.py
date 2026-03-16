import os, sys, signal, atexit, time

signaux = [signal.SIGABRT, signal.SIGINT, signal.SIGTERM, signal.SIGQUIT]


def cleanup(signum, frame):
    if signum in signaux:
        print("Exited from signal")
        print("Doing cleanup work...")
    else:
        print("Exited normally from programme")


if __name__ == "__main__":
    for sig in signaux:
        signal.signal(sig, cleanup)

    atexit.register(cleanup, 1, None)
    time.sleep(5)
    sys.exit(0)
