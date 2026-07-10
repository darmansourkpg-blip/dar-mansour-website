# Gabarits d'articles — Dar Mansour Journal

Squelettes prêts à remplir, conformes à l'**Editorial Playbook** et au document
**Journal Structure**. Objectif : garder la même logique éditoriale sans que
tous les articles se ressemblent.

## Comment s'en servir
1. Copie le gabarit qui correspond au sujet dans `site/content/journal/` et
   renomme-le (le nom de fichier = l'URL, ex. `best-restaurants-koh-phangan.md`).
2. Remplis le front matter (entre les `---`) puis le corps.
3. **Supprime tous les commentaires `<!-- ... -->`** avant de publier — ce sont
   des repères, pas du contenu.
4. Lance `cd site && python3 build/build.py`. Le générateur affiche des
   **avertissements éditoriaux** (longueur de meta description, liens internes,
   mots à bannir, FAQ manquante…). Corrige-les avant de mettre en ligne.

> Le bloc « About the Dar Mansour Journal » est **ajouté automatiquement** en
> fin d'article — ne le recopie pas. Pour le personnaliser, ajoute un champ
> `about:` dans le front matter.

## Les gabarits
| Fichier | Type | Longueur visée |
|---|---|---|
| `01-pillar-best-restaurants.md` | Pilier / classement | 3 500–5 000 mots |
| `02-local-guide.md` | Guide de quartier (Hin Kong, Sri Thanu…) | 1 200–2 000 mots |
| `03-culture-article.md` | Culture / cuisine marocaine | 1 000–1 800 mots |
| `04-quick-read.md` | Réponse à une question précise | 600–900 mots |
| `05-brand-story.md` | Récit de marque (coulisses, fondateurs) | 800–1 800 mots |

## Rappels de style (voir CLAUDE.md → « Règles éditoriales du Journal »)
- Écris pour une personne réelle, ton chaleureux et informé, phrases courtes/moyennes.
- **Montre** (détails concrets) au lieu de **déclarer** (« délicieux », « incroyable »).
- Jamais inventer : prix, horaires, plats, récompenses, citations, faits historiques.
- Au moins 3 liens internes par article. Dar Mansour cité avec transparence,
  jamais gagnant de toutes les catégories.
