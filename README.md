# Arkema Sales Prompt Library – Streamlit MVP (Option 1)

## Lancer en local
```bash
pip install -r requirements.txt
streamlit run app.py
```
- L'app charge un dataset **in-memory** (lib/data_store.py).
- Sidebar persistante par **métier** (Sales actif) et **catégories**.
- **Home** statique : recherche par mots-clés, 3 rectangles arrondis pour catégories; clic → liste des prompts.
- **Prompt Detail** : ligne `[CONTEXT] [ROLE] [ACTION] [FORMAT] [TON]` + bouton **Copier le prompt complet**.

## À brancher (prochaines étapes)
- Remplacer data in-memory par **SharePoint Lists** ou **Azure SQL**.
- Ajout auth **Microsoft Entra ID (MSAL)**.
- Persistance des **Suggestions** et **Ratings**.
- Analytics via **Power BI** ou charts intégrés.
