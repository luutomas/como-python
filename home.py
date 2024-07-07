import streamlit as st
pages = {
    "01: Naučte se programovat a vytvořte si svojí aplikaci za 6 dní":
        [
            st.Page("pages/lekce_00_uvod.py", title="Úvodní stránka"),
            st.Page("pages/lekce_01_text.py", title="Lekce č. 1 - Text"),
            st.Page("pages/lekce_02_cisla.py", title="Lekce č. 2 - Čísla"),
            st.Page("pages/lekce_03_if.py", title="Lekce č. 3 - Podmínky"),
            st.Page("pages/lekce_04_slovniky.py", title="Lekce č. 4 - Slovníky"),
            st.Page("pages/lekce_05_json.py", title="Lekce č. 5 - JSON"),
            st.Page("pages/lekce_06_seznamy.py", title="Lekce č. 6 - Seznamy"),
            st.Page("pages/lekce_07_cykly.py", title="Lekce č. 7 - Cykly"),
            st.Page("pages/lekce_08_session_state.py", title="Lekce č. 8 - Session State"),
            st.Page("pages/lekce_08_ukazka.py", title="Lekce č. 8 - Ukázka Session State aplikace"),
            st.Page("pages/lekce_09_form.py", title="Lekce č. 9 - Formuláře"),
            st.Page("pages/lekce_10_datetime.py", title="Lekce č. 10 - Datum a čas"),
        ],
    "02: Naučte se pokročile programovat a analyzovat data":
        [
            st.Page("pages/lekce_11_funkce.py", title="Lekce č. 11 - Funkce"),
            st.Page("pages/lekce_12_tridy.py", title="Lekce č. 12 - Třídy"),
            st.Page("pages/lekce_21_pandas.py", title="Lekce č. 13 - Pandas"),
        ],
    "99: Ostatní užitečné informace":
        [
            st.Page("pages/lekce_91_git.py", title="Lekce č. 91 - Git"),
        ]
}
pg = st.navigation(pages)
pg.run()
