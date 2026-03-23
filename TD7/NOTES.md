# Sockets

- Défintion : communication bidirectionel entre deux processus
- AF_INET: INET c'est pour internet , ca permet la communication entre deux processus qui sont dans deux machines différentes

- Deux modes de communications:
  - Flow / Stream : TCP / Transmission Control Protocol :

  - DATAGRAN : UDP

Tableau de comparaison entre TCP et UDP:
| Caractéristique | TCP | UDP |
|-----------------|-----|-----|
| Type de communication | Communication nigociée | non nigociée |
| données | flot de données: les données sont découppées et envoyées séparément | bloc de données |
| Fiabilité | Fiable | Non fiable |

- Il y a un temps de latence entre la fermeture du socket et la libération du port ( TIME_WAIT ) , c'est pour ca que parfois on ne peut pas réutiliser le même port tout de suite après la fermeture du socket

- Liste des ports importants
  | Port | Service |
  |------|---------|
  | 20 | FTP (File Transfer Protocol) |
  | 21 | FTP (File Transfer Protocol) |
  | 22 | SSH (Secure Shell) |
  | 23 | Telnet |
  | 25 | SMTP (Simple Mail Transfer Protocol) |
  | 53 | DNS (Domain Name System) |
  | 80 | HTTP (Hypertext Transfer Protocol) |
  | 443 | HTTPS (Hypertext Transfer Protocol Secure) |
  | 465 | SMTPS (Secure Simple Mail Transfer Protocol) |

- Exo1 :
  Pour Faire en sorte que le serveur ne se ferme pas au fermeture du client , on utilise une boucle infinie pour accepter les connexions entrantes et traiter les demandes des clients. Voici un exemple de code pour un serveur TCP qui reste ouvert même après la fermeture d'un client .

Le défaut avec cette approche c'est que le serveur ne peut pas accepter plusieurs clients au meme temps , il doit finir avec un client pour passer au suivant
