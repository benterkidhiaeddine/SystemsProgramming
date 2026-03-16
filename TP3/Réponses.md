# Réponses théoriques

- la différence principal entre time.sleep() et signal.pause() est que la méthode sleep va continuer son décompte malgré la
  réception de signaux alors que signal.pause() va maitre le processus en pause jusqu'à la reception du premier signal,
  dans ce cas le processus va reprendre après le traitement de signal.
