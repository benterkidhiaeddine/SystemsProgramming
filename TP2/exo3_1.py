import os, sys, time, signal


STD_IN = 0
STD_OUT = 1

counter = 0


def signal_handler(sig_num, frame):
    global counter
    signal.alarm(2)
    counter += 1
    print(counter)
    if counter == 5:
        sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(2)
    bs = os.read(STD_IN, 1)
    if len(bs) != 0:
        os.write(STD_OUT, bs)
        bs = os.read(STD_IN, 1)
    sys.exit(0)
