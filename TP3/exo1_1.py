import time, signal

og_sig_int_handler = signal.getsignal(signal.SIGINT)


def capter_INT(sign_num, frame):
    print("Captured Interruption")

    # Get the orginal handler of the signum , in this case the SIGINT handler
    global og_sig_int_handler
    signal.signal(signal.SIGINT, og_sig_int_handler)


if __name__ == "__main__":

    signal.signal(signal.SIGINT, capter_INT)
    while True:
        time.sleep(1)
        print("Alive!")
