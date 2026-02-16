# Réponses aux question théoriques

## Exercice 1:
- top: montre l'état de processeur
- pstree montre l'arboresence des processus sans le système avec comme racine pid si spécifié sinon init par défaut  
    - le flag -p affiche les pud des processus entre parenthèses
- ps : montre la liste des processus en cours d'éxecution 
- 
- Le pid change a chaque fois qu'on execute le programme python , parcque à chaque fois le os va lui donner un nouveau pid
- Par contre le pid de père ne change pas , c'est le pid du shell sur lequel on a lancé le programme




## Exercice 2:
- la commande ls  n'a pas été executé parceque le path ne contient pas le repertoire qui contient l'executable de ls après la modification qu'on a aporté
- la commande export continue a marcher malgré la modification du path parceque c'est une commande propre au shell
- le nombre de variables d'onvironnements obtenues  par os.enviroon et  env est le meme


## Exercice 3:

- L'ordre d'apparition des messages est aléatoires , si on lence le programme plusieurs fois on va voir un ordre potentiellement différent à chaque fois 
