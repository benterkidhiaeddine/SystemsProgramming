# Introduction

Ce repo contient le code pour le module Systèmes 2 au sein de l'Université Cote d'azur.
L'objectif est d'apprendre comment un Système d'exploitation est concu et organisé , ainsi de maitriser
La programmation système dans le langage python

# Bon partiques de programmation Systèmes

## Organisation du code

- Utiliser toujours une entrée **main** pour éxecuter les programmes

```
ìf __name__ == "__main__":
    # Main code goes here
```

## Gestion d'erreurs

- Encadrer chaque appel système critique avec try/except :
  os.fork, os.wait / os.waitpid, os.exec*, os.open, os.read, os.write, os.pipe, os.mkfifo, socket.*, select.select.
- Attraper OSError (et ses sous-types utiles : FileNotFoundError, PermissionError,
  BlockingIOError, BrokenPipeError) et afficher un message explicite sur stderr.
- Vérifier les arguments de la ligne de commande dès le début, afficher un message Usage,
  puis quitter avec un code non nul en cas d’erreur.
- Après un fork :
  le fils doit terminer avec sys.exit(...) après son travail ou après une erreur d’exec ;
  le père doit attendre ses fils (wait/waitpid) pour éviter les zombies.
- Vérifier systématiquement les statuts de terminaison avec WIFEXITED/WEXITSTATUS
  (et WIFSIGNALED si nécessaire).
- En I/O bas niveau, respecter bytes vs str :
  encoder avant os.write/send, décoder après os.read/recv.
- Interpréter correctement EOF/déconnexion :
  len(data) == 0 signifie fermeture du flux distant.
- Pour les FIFO, éviter l’interblocage :
  organiser l’ordre d’ouverture lecture/écriture et fermer les descripteurs inutiles.
- Dans les handlers de signaux, éviter print et les traitements lourds :
  privilégier os.write et un minimum de logique.
- Fermer les descripteurs ouverts et nettoyer les ressources (fifos/fichiers temporaires),
  idéalement via atexit pour garantir le nettoyage à la sortie.
- Éviter les except trop larges ; capturer des exceptions précises pour garder un diagnostic fiable.
