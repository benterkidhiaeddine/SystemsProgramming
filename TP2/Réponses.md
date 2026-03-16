# Réponses aux question théoriques du TP

dans l'exercice 4 on nous demande de reprendre l'exercie de handler de SIGUSR1 lorsque unn fils
envoie un nombre n de signaux vers son père , le père à son tour incremente un variable à chaque
fois qu'il recoit ce signal, Le problème c'est lorsque on envoie plusieurs signaux au meme temps
10 , 100 ou meme 10_000 certains signaux vont arrivé au meme temps et vont écraser l'un l'autre
au final , le nombre d'incrémentaions final ne va pas nécessairement correspondre aux nombre de signaux
envoyés.

Pour chaque nombre de signal standard on a pas une queue pour tous les signaux qui arrivent
