# AI_LOG.md : journal d’usage de l’IA

## Outils utilisés (à remplir une fois)

| Outil | Modèle (si connu) | Mode (autocomplétion, chat, agent) |
| --- | --- | --- |
| Codex | GPT-6 | agent |

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

## Bilan (à compléter en séance 4, 3 lignes)

- Nombre d’entrées et de propositions rejetées ou corrigées : à compléter.
- Tâches où l’IA a fait gagner du temps : Le developpment des fonctionnalités.
- Tâches où l’IA a fait perdre du temps : à compléter.
