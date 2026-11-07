# AI_LOG.md : journal d’usage de l’IA

## Outils utilisés (à remplir une fois)

| Outil | Modèle (si connu) | Mode (autocomplétion, chat, agent) |
| --- | --- | --- |
| Codex | GPT-6 | agent |

Fichier d’instructions pour agent versionné (`CLAUDE.md`, `AGENTS.md`…) : non

## Entrées

### 2026-11-07 : Walking skeleton en Python (US-01)
- **Demande (résumé fidèle)** : implémenter le minimum du bloc C en Python, avec saisie du nombre de joueurs et de leurs pseudos, chargement d’un backlog JSON et affichage de la première fonctionnalité.
- **Résultat** : version console générée puis étendue avec une interface graphique. Acceptation finale à confirmer après relecture du binôme.
- **Ce que nous avons vérifié** : Codex a exécuté le parcours avec deux joueurs et les cas de saisies invalides, JSON invalide, backlog vide, structure invalide, fichier absent et saisie interrompue. Contrôles réussis. Relecture du binôme à compléter.
- **Ce que nous avons changé ou rejeté, et pourquoi** : ajout ultérieur d’une interface graphique à la demande de l’utilisateur. Autres changements ou rejets du binôme à compléter.

### 2026-11-07 : Interface graphique Tkinter (US-01)
- **Demande (résumé fidèle)** : ajouter une interface graphique permettant de saisir les joueurs, de choisir un fichier JSON et d’afficher le backlog.
- **Résultat** : interface générée, puis affichage du backlog modifié à la demande de l’utilisateur. Acceptation finale à confirmer par le binôme.
- **Ce que nous avons vérifié** : compilation Python réussie par Codex. Le lancement de Tkinter dans son environnement de vérification a échoué avec le code 134. Une capture fournie par l’utilisateur montre ensuite l’interface ouverte avec un message de fichier introuvable. Parcours complet à confirmer par le binôme.
- **Ce que nous avons changé ou rejeté, et pourquoi** : remplacement de l’affichage de la seule première fonctionnalité par la liste complète, avec une barre de défilement, à la demande de l’utilisateur.

### 2026-11-07 : Messages d’erreur du chargement (US-01)
- **Demande (résumé fidèle)** : améliorer le traitement d’une erreur de fichier introuvable montrée dans une capture d’écran.
- **Résultat** : messages courts et explicites générés pour les erreurs de chargement. Acceptation finale à confirmer par le binôme.
- **Ce que nous avons vérifié** : Codex a contrôlé le chargement normal, le fichier absent, le chemin vers un dossier, le JSON invalide, l’encodage invalide et le backlog vide. Contrôles réussis. Vérification graphique du binôme à compléter.
- **Ce que nous avons changé ou rejeté, et pourquoi** : remplacement du message système détaillé par des indications permettant de corriger le problème. Le chemin de la capture contenait « baklog.json » au lieu de « backlog.json ».

## Bilan (à compléter en séance 4, 3 lignes)

- Nombre d’entrées et de propositions rejetées ou corrigées : à compléter.
- Tâches où l’IA a fait gagner du temps : Le developpment des fonctionnalités.
- Tâches où l’IA a fait perdre du temps : à compléter.
