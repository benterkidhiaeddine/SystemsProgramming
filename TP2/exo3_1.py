import os, sys, time

counter = 1
while counter <= 5:
    b = os.read(0, 1)

    os.write(1, b)
    counter += 1
    time.sleep(2)


sys.exit(0)
