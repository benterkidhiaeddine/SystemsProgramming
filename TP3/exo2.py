"""
time.sleep et signal.pause peuvent avoir un rôle équivalent. En fonction de l'implémenation de votre système,
une diférence existe entre eux, eu-égard aux signaux. Implémenter un programme qui :
- installe un traitant pour SIGINT. Ce traitant affiche un simple message
- le programme principal affiche son PID puis exécute un time.sleep(30).
Tester en envoyant un SIGI
Faire une seconde version du programme dans laquelle time.sleep() est remplacé par
signal.pause(). Conclusion ?

"""
import sys, os , time ,signal


def INT_handler(signum, frame):
    print("caputred Interruption")


if __name__ == "__main__":
    signal.signal(signal.SIGINT, INT_handler)
    print("Père:", os.getpid())
    # time.sleep(30)
    signal.pause()






