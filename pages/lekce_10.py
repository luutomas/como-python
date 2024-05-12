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
    dt.datetime.strptime("2024-04-30 13:00:00", "%Y-%m-%d %H:%M:%S"),
    dt.datetime.strptime("2024-04-19 9:30:00", "%Y-%m-%d %H:%M:%S"),
    dt.datetime.strptime("2024-03-28 15:00:00", "%Y-%m-%d %H:%M:%S"),
    dt.datetime.strptime("2025-06-17 03:30:00", "%Y-%m-%d %H:%M:%S"),
    dt.datetime.strptime("2023-12-31 19:30:00", "%Y-%m-%d %H:%M:%S"),
    dt.datetime.strptime("2024-05-10 12:30:00", "%Y-%m-%d %H:%M:%S")
]
```
Datumy už máte rovnou definové jako datetime objekty, takže se převodem nemusíte zabývat a rovnou začít porovnávat.
### Úkol 1
Vypište všechy datumy, které nejsou starší více než 1 měsíc (30 dnů).
""")

if st.toggle("Zobrazit kód", key="ukol_1_kod"):
    st.code("""
    for datum in slovnik_datumu:
        if dt.datetime.now() - datum < dt.timedelta(days=30):
            st.write(datum)
    """)

st.markdown("""
### Úkol 2
Vypišty všechy datumy, které jsou v rozmezí od 1.1.2024 do 31.3.2024.
""")

if st.toggle("Zobrazit kód", key="ukol_2_kod"):
    st.code("""
    for datum in slovnik_datumu:
        if dt.datetime(2024, 1, 1) <= datum <= dt.datetime(2024, 3, 31):
            st.write(datum)
    """)

st.markdown("""
### Úkol 3
Vypište všechny datumy, které mají na pozici minut 30.
""")

if st.toggle("Zobrazit kód", key="ukol_3_kod"):
    st.code("""
    for datum in slovnik_datumu:
        if datum.minute == 30:
            st.write(datum)
    """)

st.markdown("""
### Úkol 4
Vypište všechny datumy, které mají nejsou starší více než 2 týdny.
""")

if st.toggle("Zobrazit kód", key="ukol_4_kod"):
    st.code("""
    for datum in slovnik_datumu:
        if dt.datetime.now() - datum < dt.timedelta(weeks=2):
            st.write(datum)
    """)

st.markdown("""
### Úkol 5
Vypište všechny datumy, které jsou starší než dnešní datum.
""")

if st.toggle("Zobrazit kód", key="ukol_5_kod"):
    st.code("""
    for datum in slovnik_datumu:
        if datum < dt.datetime.now():
            st.write(datum)
    """)

st.markdown("""
### Úkol 6
Spočítejte, jaký je rozdíl mezi nejstarším a nejmladším datem a vypište výsledek:
- ve dnech a sekundách
- v minutách
- v měsících *(zaokrouhlete na 1 desetinné místo)*
""")

if st.toggle("Zobrazit kód", key="ukol_6_kod"):
    st.code("""
    nejstarsi_datum = min(slovnik_datumu)
    nejmladsi_datum = max(slovnik_datumu)
    rozdil = nejmladsi_datum - nejstarsi_datum

    st.write(f"Rozdíl ve dnech a sekundách: {rozdil.days} dní a {rozdil.seconds} sekund.")
    st.write(f"Rozdíl v minutách: {rozdil.total_seconds() / 60} minut.")
    st.write(f"Rozdíl v měsících: {round(rozdil.days / 30, 1)} měsíců.")
    """)

st.markdown("""
### Úkol 7
Vyspiště pro každý datum ve slovníku, kolik let by bylo člověku, který se narodil 1.4.2000.
""")

if st.toggle("Zobrazit kód", key="ukol_7_kod"):
    st.code("""
    datum_narozeni = dt.datetime(2000, 4, 1)
    for datum in slovnik_datumu:
        st.write(f"Když se narodíte 1.4.2000, tak v tomto datu vám bude {round((datum - datum_narozeni).days / 365, 2)} let.")
    """)

st.markdown("""
### Úkol 8
Vytvořte pomocí `st.form` formulář, kam uživatel zadá své datum narození a po stisknutí tlačítka se vypíše, kolik let mu je dnes a za kolik dní bude mít narozeniny.
""")

st.markdown("""
### Úkol 9
Převeďte následující datumy do formátu DD.MM.YYYY a vypište je:
```python
datum_1 = "2024-04-30 13:00:00"
datum_2 = "1/4/2024"
datum_3 = "1.5.2024 12:00"
datum_4 = "12/5/24 9:30"
```
""")