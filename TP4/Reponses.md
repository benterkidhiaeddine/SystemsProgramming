# Réponses

1. La première ligne va lire un buffer d'une longeur maximum de 100 octets de l'entrée standard
2. la deuxième ligne écrit les meme octets lu dans la sortie standard
3. la 3ème ligne va écrire dans la sortie d'erreur le nombre d'octets qui a été lu

# Exercice 3

- Lorsque on ferme l'entrée standard de processus envoyeur , l'entrée standard du processus receveur est également fermé

- Lorsque on Tue l'entrée standard du processus receveur , le processus envoyeur ne se ferme pas mais il aura un code d'erreur 141 correspondant au
  numero de signal numéro 13 SIGPIPE, Broken pipe litérairement veut dire tube cassé

## Questions par rapport aux pipes

- Es que c'est important que le receveur ouvre le tube en premier?
- Réponse : non c'est pas important, on peut ovurir l'envoyeur en premier ,dès que le receveur s'ouvre il va recevoir tous les messages
  dans l'ordre ou ils était envoyés

- On peut avoir plusieurs envoyeurs au meme temps, il faut qu'on ferme tous les envoyeurs pour que le receveur se ferme aussi

- Lorsque il y a plusieurs receveurs il vont recevoir les derniers messages à tour de role
