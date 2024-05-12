import datetime as dt
import streamlit as st
st.set_page_config(page_title="COMO Python", page_icon=":snake:", layout="centered", initial_sidebar_state="collapsed")
st.header("Lekce č. 10")

st.subheader("Datum a čas")
st.markdown("""
Abychom mohli pracovat s datem a časem, musíme importovat knihovnu `datetime`. \\
V praxi je více populárnější importovat tuto knihovnu jako `dt`.
""")
st.code("""
import datetime as dt
""")
st.markdown("""
Při práci s datumem a časem si také musíme uvědomit, že máme čas lokální a čas UTC. \\
UTC je koordinovaný světový čas, který je vždy stejný, bez ohledu na to, kde se nacházíte.
""")



st.markdown("""
---
# Úkoly
Zkopírujte si následující seznam do svého kódu:
```python
slovnik_datumu = [
    dt.datetime.strptime(2024-04-30 13:00:00, "%Y-%m-%d %H:%M:%S"),
    dt.datetime.strptime(2024-04-19 9:30:00, "%Y-%m-%d %H:%M:%S"),
    dt.datetime.strptime(2024-03-28 15:00:00, "%Y-%m-%d %H:%M:%S"),
    dt.datetime.strptime(2025-06-17 03:30:00, "%Y-%m-%d %H:%M:%S"),
    dt.datetime.strptime(2023-12-31 19:30:00, "%Y-%m-%d %H:%M:%S"),
    dt.datetime.strptime(2024-05-10 12:30:00, "%Y-%m-%d %H:%M:%S")
]
```
### Úkol 1
Vypište všechy datumy, které nejsou starší více než 1 měsíc (30 dnů).
""")

st.markdown("""
### Úkol 2
Vypišty všechy datumy, které jsou v rozmezí od 1.1.2024 do 31.3.2024.
### Úkol 3
Vypište všechny datumy, které mají na pozici minut 30.
### Úkol 4
Vypište všechny datumy, které mají nejsou starší více než 2 týdny.
### Úkol 5
Vypište všechny datumy, které jsou starší než dnešní datum.
### Úkol 6
Spočítejte, jaký je rozdíl mezi nejstarším a nejmladším datem a vypište výsledek:
- ve dnech a sekundách
- v minutách
- v měsících *(zaokrouhlete na 1 desetinné místo)*
### Úkol 7
Vyspiště pro každý datum ve slovníku, kolik let by bylo člověku, který se narodil 1.4.2024.
### Úkol 8
Vytvořte pomocí `st.form` formulář, kam uživatel zadá své datum narození a po stisknutí tlačítka se vypíše, kolik let mu je dnes a za kolik dní bude mít narozeniny.
### Úkol 9
Převeďte následující datumy do formátu DD.MM.YYYY a vypište je:
```python
datum_1 = "2024-04-30 13:00:00"
datum_2 = "1/4/2024"
datum_3 = "1.5.2024 12:00"
datum_4 = "12/5/24 9:30"
```
""")