# AI_LOG.md : journal d’usage de l’IA

## Outils utilisés (à remplir une fois)

| Outil | Modèle (si connu) | Mode (autocomplétion, chat, agent) |
| --- | --- | --- |
| Codex | GPT-6 | agent |
/Claude Chat/ Sonnet 5.5/ Agent

Fichier d’instructions pour agent versionné (`CLAUDE.md`, `AGENTS.md`…) : non

## Entrées

2026-11-07 : Créer une session (US-01)
- **Demande (résumé fidèle)** : implémenter le minimum du bloc C en Python, avec saisie du nombre de joueurs et de leurs pseudos.
- **Résultat** : version console générée puis étendue avec une interface graphique. Acceptation finale à confirmer après relecture du binôme.
- **Ce que nous avons vérifié** : Codex a exécuté le parcours avec deux joueurs et les cas de saisies invalides, structure invalide et saisie interrompue. Contrôles réussis. Relecture du binôme à compléter.
- **Ce que nous avons changé ou rejeté, et pourquoi** : ajout de contrôles sur le nombre de joueurs et les pseudos pour empêcher la création d’une session avec un nombre invalide ou un pseudo vide.

### 2026-11-07 : Interface graphique Tkinter (US-01)
- **Demande (résumé fidèle)** : ajouter une interface graphique permettant de saisir les joueurs.
- **Résultat** : interface générée, Acceptation finale à confirmer par le binôme.
- **Ce que nous avons vérifié** : compilation Python réussie par Codex. Le lancement de Tkinter dans son environnement de vérification a échoué avec le code 134. Une capture fournie par l’utilisateur montre ensuite l’interface ouverte avec un message de fichier introuvable. Parcours complet à confirmer par le binôme.
- **Ce que nous avons changé ou rejeté, et pourquoi** : ajout d’une interface graphique pour faciliter la saisie des joueurs.

### 2026-11-07 : Charger le backlog et afficher les fonctionnalités à estimer (US-10)
- **Demande (résumé fidèle)** : dans la même demande initiale de walking skeleton, charger un backlog JSON et afficher la première fonctionnalité à estimer.
- **Résultat** : code de chargement et d’affichage généré avec la création de session, puis séparé par le binôme dans une branche dédiée à l’US-10. L’affichage a ensuite été étendu à toutes les fonctionnalités.
- **Ce que nous avons vérifié** : Codex a exécuté le chargement normal ainsi que les cas de JSON invalide, de backlog vide, de structure invalide et de fichier absent. Contrôles réussis. Relecture du binôme à compléter.
- **Ce que nous avons changé ou rejeté, et pourquoi** : remplacement de l’affichage de la seule première fonctionnalité par l’affichage de tous les identifiants et titres du backlog, dans l’ordre du fichier JSON, avec une barre de défilement pour consulter la liste complète.

### 2026-11-07 : Messages d’erreur du chargement (US-10)
- **Demande (résumé fidèle)** : améliorer le traitement d’une erreur de fichier introuvable montrée dans une capture d’écran.
- **Résultat** : messages courts et explicites générés pour les erreurs de chargement. Acceptation finale à confirmer par le binôme.
- **Ce que nous avons vérifié** : Codex a contrôlé le chargement normal, le fichier absent, le chemin vers un dossier, le JSON invalide, l’encodage invalide et le backlog vide. Contrôles réussis. Vérification graphique du binôme à compléter.
- **Ce que nous avons changé ou rejeté, et pourquoi** : remplacement du message système détaillé par des indications permettant de corriger le problème. Le chemin de la capture contenait « baklog.json » au lieu de « backlog.json ».

### 2026-11-15 : Relecture de la logique des règles et de la validation des joueurs (US-01, US-04, US-07)
- **Demande (résumé fidèle)** : relire `game.py` (règles de validation, `validate_player_count`, `validate_players`).
- **Résultat** : Quatres remarques : Une erreur de logique qui concernait l'affichage et sortie prématurés de l'étape de verification de l'unanimité;  la détection des doublons utilise `lower()`, donc « Straße » et « STRASSE » passent, `casefold()` les détecterait ; `StrictRule` renvoie `-1` ou `-2` quand tous les joueurs jouent café ou « ? », alors que notre décision dit qu'une carte café force un revote, et aucun test ne le couvre ; un seul vote est validé par `StrictRule` (non bloquant, le minimum de 2 joueurs est garanti en amont).
- **Ce que nous avons vérifié** : cas limites exécutés par Claude : 1 joueur, 0 et nombre négatif, pseudos vides, doublons avec espaces, majuscules et accents, votes `[5,5,8]`, `[5,5,5]`, `[0,0,0]`, `[5,8,5]`, `[]`. Tous les résultats attendus sont corrects. 
- **Ce que nous avons changé ou rejeté, et pourquoi** : Après adoption des remarques pertinentes liés à la validation des joueurs ainsi que des règles

### 2026-11-21 : Amélioration visuelle du menu principal (US-04)
- **Demande (résumé fidèle)** : améliorer uniquement l'apparence de `gui.py` (couleurs, polices, boutons, couleur du message d'état) sans modifier la logique.
- **Résultat** : nouveau `gui.py` modernisé, une palette de couleurs en constantes, des cartes pour chaque bloc, un bouton principal, et un message d'état coloré (rouge pour une erreur, vert pour une session prête) via une méthode `update_status_color`.
- **Ce que nous avons vérifié** : Claude a comparé le code des méthodes `show_feature`, `choose_backlog`, `start_session` et `main` avec la version précédente (identiques), vérifié que le fichier se compile et se construit avec un Tkinter simulé, et testé la méthode de couleur sur 5 messages. Claude n'a pas pu afficher la fenêtre. Ma binôme et moi avons vérifiés que nous étions satisfaits du rendu, que rien n'était cassé côté test ou logique en lançant gui.py ainsi que le main.py seulement. 
- **Ce que nous avons changé ou rejeté, et pourquoi** : N/A


## Bilan (à compléter en séance 4, 3 lignes)

- Nombre d’entrées et de propositions rejetées ou corrigées : à compléter.
- Tâches où l’IA a fait gagner du temps : Le developpment des fonctionnalités.
- Tâches où l’IA a fait perdre du temps : à compléter.
