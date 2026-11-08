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

## Bilan (à compléter en séance 4, 3 lignes)

- Nombre d’entrées et de propositions rejetées ou corrigées : à compléter.
- Tâches où l’IA a fait gagner du temps : Le developpment des fonctionnalités.
- Tâches où l’IA a fait perdre du temps : à compléter.
