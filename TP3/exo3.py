import os, sys, signal


def HUP_handler(signum, frame):
    ppid = os.getppid()
    print("My parent is", ppid)
    print("I am immortal , killing the terminal won't stop me")


if __name__ == "__main__":
    signal.signal(signal.SIGHUP, signal.SIG_IGN)
    while True:
        pass
