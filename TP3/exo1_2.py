import signal, sys, os


def ALRM_handler(signum, frame):
    print("Terminating programme ...")
    sys.exit(0)


def INT_handler(signum, frame):
    signal.alarm(5)


if __name__ == "__main__":
    signal.signal(signal.SIGALRM, ALRM_handler)
    signal.signal(signal.SIGINT, INT_handler)
    signal.alarm(10)
    # Simuler un Travail du programme
    while True:
        pass
