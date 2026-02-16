import signal , time, random
counter = 0

def first_try():
    counter = 0
    def handler(sig, ignore):
        print("bip")
        global counter 
        counter += 1
        if counter == 6:
            print("bye")
            exit(0)
        else:
            signal.alarm(1)

    signal.signal(signal.SIGALRM, handler)
    signal.alarm(1)

    while True:
        a = random.randint(2 ** 40, 2**45)
        b = random.randint(2 ** 40, 2**45)
        p = a * b
        try:
            print(a, b , p)
        except:
            continue

def second_try():
    def handler(sig, ignore):
        print("bip")
        global counter 
        counter += 1
        if counter == 6:
            print("bye")
            exit(0)

    signal.signal(signal.SIGALRM, handler)

    while True:
        signal.alarm(1)
        signal.pause()

    
    
if __name__ == "__main__":
    first_try()
    #second_try()