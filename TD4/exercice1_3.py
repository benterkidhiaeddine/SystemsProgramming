import os, signal , sys, time

counter = 0
def handler(sig, ignore):
    global counter
    counter += 1
    time.sleep(0.1)


def parent():
    
    try:
        os.wait()
    except:
        pass
    print(f"counter {counter}")
    sys.exit(0)


def child():
    for i in range(5):
        os.kill(os.getppid(), signal.SIGUSR2)
        print("send SIGUSR2 to parent")
    sys.exit(0)

    
if __name__ == "__main__":
    signal.signal(signal.SIGUSR2, handler)
    pid = os.fork()
    if pid == 0:
        child()
    else:
        parent()