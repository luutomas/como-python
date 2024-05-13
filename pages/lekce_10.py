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
UTC je koordinovaný světový čas, který je vždy stejný, bez ohledu na to, kde se nacházíte, proto je také v praxi lepší pracovat s ním. \\
            
Pro získání aktuálního data a času můžeme použít metody:
- pro lokální čas: `dt.datetime.now()`
- pro UTC: `dt.datetime.utcnow()`
            
ZÍskáme tak objekt `datetime`, který obsahuje datum a čas a z něj můžeme získat různé informace, jako jsou rok, měsíc, den, hodiny, minuty, sekundy a mikrosekundy. \\
Můžeme získat ale i jen datum nebo jen čas.
""")

utc_now = dt.datetime.utcnow()
st.write(f"Datum i čas: {utc_now}")

st.write("Datum:", utc_now.date()) 

st.write("Čas:", utc_now.time())


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
""")

st.markdown("""        
### Úkol 1
Vypište všechny datumy, které nejsou starší více než 1 měsíc (30 dnů).
""")

if st.toggle("Zobrazit řešení", key="ukol_1_reseni"):
    st.markdown("""
    Řešení:
    - 2024-04-30 13:00:00
    - 2024-04-19 09:30:00
    - 2025-06-17 03:30:00
    - 2024-05-10 12:30:00
    """)

    if st.toggle("Zobrazit kód", key="ukol_1_kod"):
        st.code("""
        for datum in slovnik_datumu:
            if dt.datetime.utcnow() - datum < dt.timedelta(days=30):
                st.write(datum)
        """)

st.markdown("""
### Úkol 2
Vypište všechny datumy, které jsou v rozmezí od 1.1.2024 do 31.3.2024.
""")

if st.toggle("Zobrazit řešení", key="ukol_2_reseni"):
    st.markdown("""
    Řešení:
    - 2024-03-28 15:00:00
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

if st.toggle("Zobrazit řešení", key="ukol_3_reseni"):
    st.markdown("""
    Řešení:
    - 2024-04-19 09:30:00
    - 2025-06-17 03:30:00
    - 2023-12-31 19:30:00
    - 2024-05-10 12:30:00
    """)

    if st.toggle("Zobrazit kód", key="ukol_3_kod"):
        st.code("""
        for datum in slovnik_datumu:
            if datum.minute == 30:
                st.write(datum)
        """)

st.markdown("""
### Úkol 4
Vypište všechny datumy, které jsou v rozmezí 2 týdnů od dnešního data do dnešního data.
""")

if st.toggle("Zobrazit řešení", key="ukol_4_reseni"):
    st.markdown("""
    Řešení:
    - 2024-04-30 13:00:00
    - 2024-05-10 12:30:00
    """)

    if st.toggle("Zobrazit kód", key="ukol_4_kod"):
        st.code("""
        for datum in slovnik_datumu:
            if dt.datetime.utcnow() - dt.timedelta(weeks=2) <= datum <= dt.datetime.utcnow():
                st.write(datum)
        """)

st.markdown("""
### Úkol 5
Vypište všechny datumy, které jsou starší než dnešní datum.
""")

if st.toggle("Zobrazit řešení", key="ukol_5_reseni"):
    st.markdown("""
    Řešení:
    - 2025-06-17 03:30:00
    """)

    if st.toggle("Zobrazit kód", key="ukol_5_kod"):
        st.code("""
        for datum in slovnik_datumu:
            if datum > dt.datetime.utcnow():
                st.write(datum)
        """)

st.markdown("""
### Úkol 6
Spočítejte, jaký je rozdíl mezi nejstarším a nejmladším datem a vypište výsledek:
- ve dnech a sekundách
- v minutách
- v měsících *(zaokrouhlete na 1 desetinné místo)*
""")

if st.toggle("Zobrazit řešení", key="ukol_6_reseni"):
    st.markdown("""
    Řešení:
    - Rozdíl ve dnech a sekundách: 533 dní a 28800 sekund.
    - Rozdíl v minutách: 768000.0 minut.
    - Rozdíl v měsících: 17.8 měsíců.
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

if st.toggle("Zobrazit řešení", key="ukol_7_reseni"):
    st.markdown("""
    Řešení:
    - Když se narodíte 1.4.2000, tak vám 2024-04-30 bude 24 let.
    - Když se narodíte 1.4.2000, tak vám 2024-04-19 bude 24 let.
    - Když se narodíte 1.4.2000, tak vám 2024-03-28 bude 24 let.
    - Když se narodíte 1.4.2000, tak vám 2025-06-17 bude 25 let.
    - Když se narodíte 1.4.2000, tak vám 2023-12-31 bude 23 let.
    - Když se narodíte 1.4.2000, tak vám 2024-05-10 bude 24 let.
    """)

    if st.toggle("Zobrazit kód", key="ukol_7_kod"):
        st.code("""
        datum_narozeni = dt.datetime(2000, 4, 1)
        for datum in slovnik_datumu:
            st.write(f"Když se narodíte 1.4.2000, tak vám {datum.date()} bude {int((datum - datum_narozeni).days / 365)} let.")
        """)

st.markdown("""
### Úkol 8
Vytvořte pomocí `st.form` formulář, kam uživatel zadá své datum narození a po stisknutí tlačítka se vypíše, kolik let mu je dnes a za kolik dní bude mít narozeniny. \\
*Pozor si dejte na to, že pokud budete využívat k dělení počet dní v roce, tak rok má 365.25 dní.*
""")

if st.toggle("Zobrazit řešení", key="ukol_8_reseni"):
    with st.form(key="datum_narozeni"):
        datum_narozeni = st.date_input("Datum narození:", value=None, min_value=dt.datetime(1900, 1, 1), max_value=dt.datetime.utcnow)   

        if st.form_submit_button("Odeslat"):
            dnesni_datum = dt.datetime.utcnow().date()
            vek = int((dnesni_datum - datum_narozeni).days / 365.25)
            narozeniny = dt.datetime(dnesni_datum.year, datum_narozeni.month, datum_narozeni.day).date()

            if narozeniny < dnesni_datum:
                narozeniny = narozeniny.replace(year=narozeniny.year + 1)

            pocet_dni_do_narozenin = int((narozeniny - dnesni_datum).days)

            st.write(f"Dnes je vám {vek} let.")
            st.write(f"Do narozenin zbývá {pocet_dni_do_narozenin} dní.")

    if st.toggle("Zobrazit kód", key="ukol_8_kod"):
        st.code("""
        with st.form(key="datum_narozeni"):
            datum_narozeni = st.date_input("Datum narození:", value=None, min_value=dt.datetime(1900, 1, 1), max_value=dt.datetime.utcnow())   

            if st.form_submit_button("Odeslat"):
                dnesni_datum = dt.datetime.utcnow().date()
                vek = int((dnesni_datum - datum_narozeni).days / 365.25)
                narozeniny = dt.datetime(dnesni_datum.year, datum_narozeni.month, datum_narozeni.day).date()

                if narozeniny < dnesni_datum:
                    narozeniny = narozeniny.replace(year=narozeniny.year + 1)

                pocet_dni_do_narozenin = int((narozeniny - dnesni_datum).days)

                st.write(f"Dnes je vám {vek} let.")
                st.write(f"Do narozenin zbývá {pocet_dni_do_narozenin} dní.")
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

if st.toggle("Zobrazit řešení", key="ukol_9_reseni"):
    st.markdown("""
    Řešení:
    - 30.04.2024
    - 01.04.2024
    - 01.05.2024
    - 12.05.2024
    """)

    if st.toggle("Zobrazit kód", key="ukol_9_kod"):
        st.code("""
        datum_1 = dt.datetime.strptime(datum_1, "%Y-%m-%d %H:%M:%S")
        st.write(datum_1.strftime("%d.%m.%Y"))
        datum_2 = dt.datetime.strptime(datum_2, "%d/%m/%Y")
        st.write(datum_2.strftime("%d.%m.%Y"))
        datum_3 = dt.datetime.strptime(datum_3, "%d.%m.%Y %H:%M")
        st.write(datum_3.strftime("%d.%m.%Y"))
        datum_4 = dt.datetime.strptime(datum_4, "%d/%m/%y %H:%M")
        st.write(datum_4.strftime("%d.%m.%Y"))
        """)