import streamlit as st
from config import APP_NAME, DEFAULT_METIER, METIER_CATEGORIES, COPILOT_URL
from lib.data_store import list_categories, list_prompts, search_prompts_by_keywords
from lib.components import sidebar_nav, category_card, prompt_card

st.set_page_config(page_title=APP_NAME, layout="wide")
st.session_state['COPILOT_URL'] = COPILOT_URL

st.title(APP_NAME)
st.caption("Home / Dashboard statique")


# Sidebar persistent navigation
active_metier = DEFAULT_METIER
categories = list_categories(active_metier)
sidebar_nav(active_metier, categories)

st.markdown("### Rechercher par mots-clés")
keywords = st.text_input("Mots-clés (ex: email, QBR, pricing)", key="home_search")

# 3 rectangles arrondis (catégories)
st.markdown("### Catégories (Sales)")
colA, colB, colC = st.columns(3)
keys = categories[:3] if len(categories)>=3 else categories + [""]*(3-len(categories))
with colA:
    if keys[0]: category_card(keys[0], key=keys[0])
with colB:
    if keys[1]: category_card(keys[1], key=keys[1])
with colC:
    if keys[2]: category_card(keys[2], key=keys[2])

# Handle clicks from HTML cards
msg = st.experimental_get_query_params().get("card_click", [None])[0]
if msg:
    st.session_state['selected_category'] = msg

st.markdown("---")

# Results area
selected_category = st.session_state.get('selected_category')
if keywords:
    st.subheader(f"Résultats pour '{keywords}'")
    hits = search_prompts_by_keywords(active_metier, keywords)
    if hits:
        for p in hits:
            prompt_card(p)
    else:
        st.info("Aucun résultat. Essaie d'autres mots-clés.")
elif selected_category:
    st.subheader(f"Prompts – Catégorie: {selected_category}")
    for p in list_prompts(active_metier, selected_category):
        prompt_card(p)
else:
    st.info("Choisis une catégorie ou lance une recherche par mots-clés.")
