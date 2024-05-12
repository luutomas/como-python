import datetime as dt
import streamlit as st
st.set_page_config(page_title="COMO Python", page_icon=":snake:", layout="centered", initial_sidebar_state="collapsed")
st.header("Lekce č. 10")

st.subheader("Datum a čas")
st.markdown("""
Abychom mohli pracovat s datem a časem, musíme importovat knihovnu `datetime`. \\
V praxi je více populárnější importovat tuto knihovnu jako `dt`. \\
""")
st.code("""
import datetime as dt
""")
st.markdown("""
Při práci s datumem a časem si také musíme uvědomit, že máme čas lokální a čas UTC. \\
UTC je koordinovaný světový čas, který je vždy stejný, bez ohledu na to, kde se nacházíte. \\
""")



st.markdown("""
---
# Úkoly
Zkopírujte si následující slovník do svého kódu:
```python
slovnik_datumu = {
    "1": 2024-04-30 13:00:00,
    "2": 2024-04-19 9:30:00,
    "3": 2024-03-28 15:00:00,
    "4": 2025-06-17 03:30:00,
    "5": 2023-12-31 19:30:00,
    "6": 2024-05-10 12:30:00,
}
```
### Úkol 1
Vypište klíče všech datumů, které nejsou starší více než 1 měsíc.
### Úkol 2
Vypiště klíče všech datumů, které jsou v rozmezí od 1.1.2024 do 31.3.2024.
### Úkol 3
Vypiště klíče všech datumů, které mají na pozici minut 30.
### Úkol 4
Vypiště klíče všech datumů, které mají nejsou starší více než 2 týdny.

""")