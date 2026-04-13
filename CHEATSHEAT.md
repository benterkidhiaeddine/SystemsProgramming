# Exam Speed Sheet (Repo-Based)

Q1) Explique fork/wait et comment eviter les zombies.
Reponse: `fork()` retourne 0 au fils, le PID au pere, -1 en cas d'erreur. Le pere doit appeler `wait()` ou `waitpid(pid, 0)` pour reap les fils. Pour plusieurs fils, boucler sur tous les PIDs. Pour eviter les zombies en mode asynchrone: handler `SIGCHLD` + boucle `waitpid(-1, WNOHANG)`.
Micro exemple:
```python
pid = os.fork()
if pid == 0:
	sys.exit(0)
else:
	os.waitpid(pid, 0)
```

Q2) Pourquoi utiliser exec apres fork? Que se passe-t-il apres exec?
Reponse: `exec*` remplace l'image du processus; le code apres exec ne s'execute pas si exec reussit. Le schema standard est fork dans le pere, exec dans le fils, puis le pere attend et lit le status.
Micro exemple:
```python
if os.fork() == 0:
	os.execvp("ls", ["ls", "-l"])
os.wait()
```

Q3) Explique les race conditions des signaux et la reentrance.
Reponse: Les signaux standards ne sont pas tous mis en file; plusieurs signaux rapides peuvent se perdre. Un handler doit etre minimal, sans `print` (non reentrant). Preferer `os.write` et un code court.
Micro exemple:
```python
def handler(sig, frame):
	os.write(1, b"signal recu\n")
signal.signal(signal.SIGUSR1, handler)
```

Q4) Comment gere-t-on SIGCHLD sans rater des fils termines?
Reponse: Installer un handler SIGCHLD et boucler `while pid > 0: pid, status = waitpid(-1, WNOHANG)` pour reap tous les fils termines.
Micro exemple:
```python
def handler(sig, frame):
	while True:
		pid, _ = os.waitpid(-1, os.WNOHANG)
		if pid <= 0:
			break
signal.signal(signal.SIGCHLD, handler)
```

Q5) Pourquoi un FIFO peut bloquer a l'ouverture?
Reponse: Ouvrir un FIFO en lecture bloque tant qu'aucun writer n'est ouvert, et inversement. Il faut coordonner l'ordre d'ouverture ou ouvrir les deux extremites dans des processus differents pour eviter l'interblocage.
Micro exemple:
```python
os.mkfifo("p.fifo")
# Dans un autre processus: os.open("p.fifo", os.O_WRONLY)
fd_r = os.open("p.fifo", os.O_RDONLY)
```

Q6) Que se passe-t-il quand un pipe/FIFO est plein? Et si le lecteur ferme?
Reponse: En mode bloquant, l'ecriture attend; en non bloquant, `BlockingIOError` est leve. Si le lecteur ferme, `BrokenPipeError` peut apparaitre.
Micro exemple:
```python
os.set_blocking(fd_w, False)
try:
	os.write(fd_w, b"x" * 1024)
except BlockingIOError:
	pass
```

Q7) Donne le design ideal d'une boucle `select` pour un serveur TCP.
Reponse: Creer un socket serveur, l'ajouter a `socketlist`, appeler `select(socketlist, [], [])`. Si le socket serveur est lisible: `accept()` puis ajouter le client. Sinon `recv()`; si `len(data)==0` fermer et retirer; sinon traiter et `sendall`.
Micro exemple:
```python
readable, _, _ = select.select(socketlist, [], [])
for s in readable:
	if s is serversocket:
		client, _ = s.accept()
		socketlist.append(client)
	else:
		data = s.recv(4096)
```

Q8) Pourquoi bytes vs str est critique en IPC?
Reponse: `os.read/os.write` et `recv/send` manipulent des bytes. Il faut `encode()` avant envoi et `decode()` apres reception. Ne jamais passer une liste/str a `sendall`.
Micro exemple:
```python
sock.sendall("hello".encode("utf-8"))
data = sock.recv(4096).decode("utf-8")
```

Q9) Comment faire une redirection avec dup2?
Reponse: `fd = os.open(...)`, puis `os.dup2(fd, 0/1/2)` pour rediriger stdin/stdout/stderr, ensuite fermer `fd` et exec la commande.
Micro exemple:
```python
fd = os.open("out.txt", os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
os.dup2(fd, 1)
os.close(fd)
os.execvp("ls", ["ls"]) 
```

Q10) Pourquoi `os.system` est dangereux en remote shell?
Reponse: Il execute des commandes brutes (risque d'injection). Il faut valider l'entree, limiter les commandes, et preferer `execvp` avec une liste d'arguments.
Micro exemple:
```python
cmd = ["ls", "-l"]
os.execvp(cmd[0], cmd)
```

Q11) Donne un mini template fork/wait.
Reponse:
- `pid = fork()`
- si `pid == 0`: faire le travail, `exit(1/0)`
- sinon: `waitpid(pid, 0)` et verifier le status.
Micro exemple:
```python
pid = os.fork()
if pid == 0:
	sys.exit(0)
os.waitpid(pid, 0)
```

Q12) Donne un mini template handler SIGCHLD.
Reponse:
- installer handler
- dans handler: boucle `waitpid(-1, WNOHANG)`
- utiliser `os.write` si besoin d'afficher.
Micro exemple:
```python
def handler(sig, frame):
	while os.waitpid(-1, os.WNOHANG)[0] > 0:
		pass
signal.signal(signal.SIGCHLD, handler)
```

Q13) Donne un mini template FIFO handshake.
Reponse:
- `mkfifo(...)`
- un process ouvre en lecture, l'autre en ecriture
- eviter l'ordre inverse qui bloque; fermer les descripteurs inutiles.
Micro exemple:
```python
os.mkfifo("a.fifo")
fd_w = os.open("a.fifo", os.O_WRONLY)
os.write(fd_w, b"ping")
```
