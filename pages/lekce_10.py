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

Definujeme si proměnnou `utc_cas_nyni` a na ní si ukážeme jak můžeme dané hodnoty získat
""")

with st.echo():
    utc_cas_nyni = dt.datetime.utcnow()
    st.write(utc_cas_nyni)

st.markdown(f"""
| Kód | Výsledek | Popis výsledku |
| --- | -------- | -------------- |
| `utc_cas_nyni.time()` | {utc_cas_nyni.time()} | Vrátí nám čas |
| `utc_cas_nyni.date()` | {utc_cas_nyni.date()} | Vrátí nám datum |
| `utc_cas_nyni.year` | {utc_cas_nyni.year} | Vrátí nám rok |
| `utc_cas_nyni.month` | {utc_cas_nyni.month} | Vrátí nám měsíc |
| `utc_cas_nyni.day` | {utc_cas_nyni.day} | Vrátí nám den |
| `utc_cas_nyni.hour` | {utc_cas_nyni.hour} | Vrátí nám hodiny |
| `utc_cas_nyni.minute` | {utc_cas_nyni.minute} | Vrátí nám minuty |
| `utc_cas_nyni.second` | {utc_cas_nyni.second} | Vrátí nám sekundy |
| `utc_cas_nyni.microsecond` | {utc_cas_nyni.microsecond} | Vrátí nám mikrosekundy |
---
Také si všimněte rodzílu mezi objektem `datetime` a datumem ve formátu `"2024-01-01 13:00:00"`. 
""")

columns = st.columns(2)

with columns[0]:
    st.success("Toto je objekt datetime - tedy datum a čas.")
    with st.echo():
        datum = dt.datetime(year=2024, month=1, day=1, hour=13, minute=0, second=0)
        st.write(datum)

with columns[1]:
    st.error("Toto je pouze string.")
    with st.echo():
        datum = "2024-01-01 13:00:00"
        st.write(datum)
    
st.markdown("""
---
# Jak definovat datum a čas

Pokud chceme definovat datum a čas, můžeme to udělat několika způsoby:
- přímo jako objekt `dt.datetime()`, jak je uvedeno výše a jako parametry musíme zadat rok, měsíc a den a dále můžeme, ale nemusíme zadat hodiny, minuty, sekundy a i mikrosekundy.
- pomocí metod `dt.datetime.now()` nebo `dt.datetime.utcnow()`, které nám vrátí aktuální datum a čas.
- pomocí metody `dt.datetime.strptime()`, která nám umožní převést string (text) na objekt `datetime` a jako parametry musíme zadat string a formát pomocí speciálních značek, ve kterém je datum zapsán.

Například pokud bychom chtěli převést string `"1.1.2024 13:00:00"` na objekt `datetime`, tak bychom provedli následujícím způsobem:
""")

with st.echo():
    datum_string = "1.1.2024 13:00:00"
    format_datumu = "%d.%m.%Y %H:%M:%S"
    datum = dt.datetime.strptime(datum_string, format_datumu)
    st.write(datum)

st.markdown("""
A datum `"2024-01-01 13:00:00"` bychom převedli následujícím způsobem:
""")

with st.echo():
    datum_string = "2024-01-01 13:00:00"
    format_datumu = "%Y-%m-%d %H:%M:%S"
    datum = dt.datetime.strptime(datum_string, format_datumu)
    st.write(datum)

st.markdown("""
### Tabulka nejpoužívanějších formátovacích značek
| Značka | Popis |
| ------ | ----- |
| %Y | Rok ve čtyřech číslicích |
| %y | Rok ve dvou číslicích |
| %m | Měsíc v číslech |
| %d | Den v měsíci |
| %H | Hodina |
| %M | Minuta |
| %S | Sekunda |
---
Více formátovacích značek a o jejich používání můžete najít například na [Programiz.com](https://www.programiz.com/python-programming/datetime/strftime).
""")

st.markdown("""
---
# Matematické operace s datem a časem

S datem a časem můžeme provádět různé matematické operace, jako je sčítání, odčítání, porovnávání a další. \\
K opreacím sčítání a odčítání se používá další objekt a tím je `timedelta`. \\
Objekt `timedelta` nám umožňuje přičítat nebo odečítat určitý počet sekund, minut, hodnin, dní a týdnů k objektu `datetime` a definujeme ho následujícím způsobem:
""")

with st.echo():
    timedelta_priklad = dt.timedelta(days=1, hours=12, minutes=30)

st.markdown("""
A nyní můžeme pomocí proměnné `timedelta_priklad` přičíst i odečíst 1 den, 12 hodin a 30 minut k našemu lokálnímu času:
""")

with st.echo():
    lokalni_cas_nyni = dt.datetime.now()
    lokalni_cas_plus = lokalni_cas_nyni + timedelta_priklad
    lokalni_cas_minus = lokalni_cas_nyni - timedelta_priklad
    st.write(f"Akuální datum a čas: {lokalni_cas_nyni}.")
    st.write(f"Datum a čas po přičtení: {lokalni_cas_plus}.")
    st.write(f"Datum a čas po odečtení: {lokalni_cas_minus}.")

st.markdown("""
Dejte si pozor, že nemůžeme přímo sčítat dva objekty `datetime`. To by vlastně nedávalo ani smysl že? Co by mělo výsledkem součtu dnešního a zítřejšího dne? \\
Můžeme ale od sebe odečítat dva objekty `datetime` a jako výsledek dostaneme objekt `timedelta`, ze kterého můžeme získat pouze počet dní (`.days`) a počet sekund (`.seconds`).
Pokud bychom chtěli znát například počet hodin, tak bychom museli převést sekundy na hodiny, pomocí jednoduchého dělení tak, jako bychom tu udělali v běžném životě. \\
*Pozor ale na to, že výsledek odčítání bucou celé dny a co nepůjde převést na celé dny, bude v sekundách. Můžeme si ale zavolat metodu `.total_seconds()`, která nám vrátí celkový rozdíl v sekundách.*
""")

with st.echo():
    dnesni_datum = dt.datetime.now()
    zitrek = dnesni_datum + dt.timedelta(days=1)

    st.write(f"Dnešní datum: {dnesni_datum}.")
    st.write(f"Zítřejší datum: {zitrek}.")

    rozdil = zitrek - dnesni_datum
    st.write(f"Rozdíl je {rozdil.days} den a {rozdil.seconds} sekund.")

    rozdil_v_hodinach = rozdil.total_seconds() / 3600
    st.write(f"Rozdíl je {rozdil_v_hodinach} hodin.")

st.markdown("""
A datumy mezi sebou můžeme porovnávat pomocí porovnávacích operátorů, jako jsou `==`, `!=`, `>`, `<`, `>=` a `<=`. \\
Pozor si dejte na to, že pokud porovnáváme dva objekty `datetime`, tak se porovnává i čas, pokud si nezavoláte metodu `.date()`, která vrátí pouze datum. \\  
Například:
""")

with st.echo():
    dnesni_datum = dt.datetime.now()
    zitrek = dnesni_datum + dt.timedelta(days=1)

    st.write(f"Dnešní datum: {dnesni_datum}.")
    st.write(f"Zítřejší datum: {zitrek}.")

    if zitrek > dnesni_datum:
        st.write("Zítřejší datum je větší než dnešní datum.")

    if dnesni_datum < zitrek:
        st.write("Dnešní datum je menší než zítřejší datum.")

    if dnesni_datum.date() == zitrek.date():
        st.write("Dnešní datum a zítřejší datum jsou stejné.")
    elif dnesni_datum.date() != zitrek.date():
        st.write("Dnešní datum a zítřejší datum nejsou stejné.")

    zacatek_roku_datum = dt.datetime(2024, 1, 1)
    konec_roku_datum = dt.datetime(2024, 12, 31)

    if zacatek_roku_datum <= dnesni_datum <= konec_roku_datum:
        st.write("Dnešní datum je v roce 2024.")

st.markdown("""
---
# Úkoly
Zkopírujte si následující seznam do svého kódu:
```python
seznam_datumu = [
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
        for datum in seznam_datumu:
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
        for datum in seznam_datumu:
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
        for datum in seznam_datumu:
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
        for datum in seznam_datumu:
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
        for datum in seznam_datumu:
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
        nejstarsi_datum = min(seznam_datumu)
        nejmladsi_datum = max(seznam_datumu)
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
        for datum in seznam_datumu:
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