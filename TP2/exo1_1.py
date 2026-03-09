import os, sys, time

if len(sys.argv) != 2:
    print(f"Usage {sys.argv[0]} [time in seconds]")
    sys.exit(1)


t = int(sys.argv[1])
print(f"Sleeping for {t} seconds ...")
time.sleep(t)

print("Exiting Programme")
sys.exit(0)
