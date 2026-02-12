# Poker Hand Evaluator

Un système d'évaluation de mains de poker en Texas Hold'em.

## Description

Ce projet implémente un évaluateur de mains de poker permettant de :
- Normaliser et valider les cartes
- Parser les configurations de jeu
- Générer les combinaisons de 5 cartes à partir de 7 cartes
- Évaluer et comparer les mains de poker

## Fichiers principaux

- `pokerRef.py` : Module principal contenant toutes les fonctions d'évaluation
- `dosstest/` : Dossier contenant les tests

## Tests

Pour exécuter les tests :

```bash
pytest dosstest/
```

Tests disponibles :
- `eval_one_pair.py` : Tests pour les paires
- `eval_hight_card.py` : Tests pour les cartes hautes
- `eval_groups.py` : Tests pour les combinaisons multiples
- `generation.py` : Tests de génération de mains
- `validation_script.py` : Tests de validation des doublons

## Fonctions principales

- `evaluate_hand_5(main5)` : Évalue une main de 5 cartes
- `generate_5_from_7(cartes7)` : Génère toutes les combinaisons de 5 cartes à partir de 7
- `list_duplicates(board, holes)` : Détecte les doublons de cartes
- `normalize_card(token)` : Normalise le format d'une carte
- `parse_cards(texte)` : Parse une chaîne de cartes
- `build_game_state(board_text, holes_text_par_joueur)` : Construit l'état du jeu
