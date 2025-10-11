import streamlit as st

st.set_page_config(page_title="COMO Python", page_icon="icon.png", layout="centered")

st.header("Opakování lekce č. 1, 2 a 3")

st.subheader("Text, čísla, proměnné a podmínky")

st.markdown("""
---
### Cena jízdenky
Vytvořte si nový soubor `cena_jizdenky.py` a podle instrukcí jednoduchý kalkulátor ceny jízdenky
na městskou hromadnou dopravu, dle věku, který uživatel zadá do číselného pole a vytvořte zašktávací
pole (`st.checkbox()`), zda je držitelem studentského průkazu, nebo průkazu ZTP / ZTP-P.
            
**Instrukce:**
- Číselné pole pro věk bude omezeno na hodnoty mezi 0 a 120 lety,
bude mít výchozí hodnotu 25 let a krok 1 rok.
- Zaškrtávací pole pro studentský průkaz bude mít popisek "Držitel studentského průkazu".
- Zaškrtávací pole pro průkaz ZTP / ZTP-P bude mít popisek "Držitel průkazu ZTP / ZTP-P".
- Pomocí podmínek `if`, `elif` a `else` vypište cenu jízdenky podle věku a držení průkazu
ve tvaru "Vaše jízdenka stojí: X Kč", kde X je vypočítaná cena.
- Cena jízdeneky bude vypočítána podle tabulky níže
            
| Podmínka | Cena |
| ----- | ------ |
| do 6 let | 0 Kč |
| 6-15 let | 15 Kč |
| 15-65 let | 40 Kč |
| nad 65 let | 20 Kč |
| Studentský průkaz | 0 Kč |
| ZTP / ZTP-P | 0 Kč |
""")

if st.toggle("Zobrazit nápovědu", key="napoveda_cena_jizdenky"):
    st.markdown("""
    1. Vytvořte si proměnnou `vek`, do které uložíte hodnotu z číselného pole
    pomocí `st.number_input()` a nastavte jí příslušné parametry jako `min_value`, `max_value`, `value` a `step`.
    2. Vytvořte si proměnné `je_student` a `je_ztp`, do kterých uložíte hodnoty ze zaškrtávacích polí
    pomocí `st.checkbox()` a nastavte jim příslušné popisky.
    3. Vytvořte si proměnnou `cena`, kterou inicializujete na hodnotu 0.
    4. Vytvořte podmínku `if`, která zkontroluje, zda je uživatel držitelem studentského průkazu nebo průkazu ZTP / ZTP-P.
    Pokud ano, nastaví cenu na 0 a zobrazí ji pomocí `st.write()`.
    5. Vytvořte podmínku `else`, která bude obsahovat další podmínky `if`, `elif` a `else`,
    které podle hodnoty věku uživatele nastaví cenu podle tabulky výše.
    6. Nakonec zobrazte cenu jízdenky pomocí `st.write()`.
    """)

    if st.toggle("Zobrazit řešení", key="reseni_cena_jizdenky"):
        with st.container(key="container_cena_jizdenky", border=True):
            vek = st.number_input("Zadejte svůj věk:", min_value=0, max_value=120, value=25, step=1, key="vek")
            je_student = st.checkbox("Držitel studentského průkazu", key="je_student")
            je_ztp = st.checkbox("Držitel průkazu ZTP / ZTP-P", key="je_ztp")

            if je_student or je_ztp or vek < 6:
                st.write("Vaše jízdenka stojí: 0 Kč")
            elif vek >= 6 and vek < 15:
                st.write("Vaše jízdenka stojí: 15 Kč")
            elif vek >= 15 and vek < 65:
                st.write("Vaše jízdenka stojí: 40 Kč")
            else:
                st.write("Vaše jízdenka stojí: 20 Kč")

        if st.toggle("Zobrazit kód", key="kod_cena_jizdenky"):
            st.code("""
            vek = st.number_input("Zadejte svůj věk:", min_value=0, max_value=120, value=25, step=1, key="vek")
            je_student = st.checkbox("Držitel studentského průkazu", key="je_student")
            je_ztp = st.checkbox("Držitel průkazu ZTP / ZTP-P", key="je_ztp")

            if je_student or je_ztp or vek < 6:
                st.write("Vaše jízdenka stojí: 0 Kč")
            elif vek >= 6 and vek < 15:
                st.write("Vaše jízdenka stojí: 15 Kč")
            elif vek >= 15 and vek < 65:
                st.write("Vaše jízdenka stojí: 40 Kč")
            else:
                st.write("Vaše jízdenka stojí: 20 Kč")
            """, language="python")

st.markdown("""
---
### BMI kalkulačka
Vytvořte si nový soubor `bmi_kalkulacka.py` a podle instrukcí jednoduchou BMI kalkulačku,
kam uživatel zadá do číselných polí zadá svou váhu a výšku a po kliku na tlačítko
se mu zobrazí jeho BMI a kategorie, do které spadá.

**Instrukce:**
- Číselné pole pro váhu bude omezeno na hodnoty mezi 10 a 200 kg,
bude mít výchozí hodnotu 70 kg a krok 0.1 kg.
- Číselné pole pro výšku bude omezeno na hodnoty mezi 100 a 250 cm,
bude mít výchozí hodnotu 170 cm a krok 1 cm.
- Tlačítko bude mít popisek "Spočítat BMI" a po jeho stisku se provede výpočet
- BMI se vypočítá podle vzorce: `váha (kg) / ((výška (cm) * výška (cm)) / 10000)`
- Uživateli se zobrazí jeho BMI zaokrouhlené na 2 desetinná místa a kategorie podle tabulky níže.
            
| BMI | Kategorie |
| ----- | ------ |
| < 18.5 | Podváha |
| 18.5 - 24.9 | Normální váha |
| 25 - 29.9 | Nadváha |
| 30 - 34.9 | Obezita 1. stupně |
| 35 - 39.9 | Obezita 2. stupně |
| >= 40 | Obezita 3. stupně |
""")

if st.toggle("Zobrazit nápovědu", key="napoveda_bmi_kalkulacka"):
    st.markdown("""
    1. Vytvořte si 2 proměnné `vaha` a `vyska`, do kterých uložíte hodnoty z číselných polí
    pomocí `st.number_input()` a nastavte jim příslušné parametry jako `min_value`, `max_value`, `value` a `step`.
    2. Vytvořte si proměnnou `bmi`, do které uložíte výpočet BMI podle vzorce
    """)
    st.code("vaha / ((vyska * vyska) / 10000)", language="python")
    st.markdown("""
    3. Pomocí funkce `round()` zaokrouhlete hodnotu `bmi` na 2 desetinná místa.
    4. Vytvořte si tlačítko pomocí `st.button()`, které bude mít popisek "Spočítat BMI" a dosaďte ho do podmínky `if`.
    5. Uvnitř podmínky `if` vytvořte další podmínky `if`, `elif` a `else`, které podle hodnoty `bmi`
    zobrazí příslušnou kategorii pomocí `st.write()`.
    """)

    if st.toggle("Zobrazit řešení", key="reseni_bmi_kalkulacka"):
        with st.container(key="container_bmi_kalkulacka", border=True):
            vaha = st.number_input("Zadejte svou váhu (kg):", min_value=10.0, max_value=200.0, value=70.0, step=0.1, key="vaha")
            vyska = st.number_input("Zadejte svou výšku (cm):", min_value=100, max_value=250, value=170, step=1, key="vyska")

            bmi = vaha / ((vyska * vyska) / 10000)
            bmi_zaokrouhlene = round(bmi, 2)

            if st.button("Spočítat BMI", key="spocitat_bmi"):
                st.write(f"Vaše BMI je: {bmi_zaokrouhlene}")

                if bmi_zaokrouhlene < 18.5:
                    st.write("Kategorie: Podváha")
                elif 18.5 <= bmi_zaokrouhlene < 24.9:
                    st.write("Kategorie: Normální váha")
                elif 25 <= bmi_zaokrouhlene < 29.9:
                    st.write("Kategorie: Nadváha")
                elif 30 <= bmi_zaokrouhlene < 34.9:
                    st.write("Kategorie: Obezita 1. stupně")
                elif 35 <= bmi < 39.9:
                    st.write("Kategorie: Obezita 2. stupně")
                else:
                    st.write("Kategorie: Obezita 3. stupně")

        if st.toggle("Zobrazit kód", key="kod_bmi_kalkulacka"):
            st.code("""
            vaha = st.number_input("Zadejte svou váhu (kg):", min_value=10.0, max_value=200.0, value=70.0, step=0.1, key="vaha")
            vyska = st.number_input("Zadejte svou výšku (cm):", min_value=100, max_value=250, value=170, step=1, key="vyska")

            bmi = vaha / ((vyska * vyska) / 10000)
            bmi_zaokrouhlene = round(bmi, 2)

            if st.button("Spočítat BMI", key="spocitat_bmi"):
                st.write(f"Vaše BMI je: {bmi_zaokrouhlene}")
                
                if bmi_zaokrouhlene < 18.5:
                    st.write("Kategorie: Podváha")
                elif 18.5 <= bmi_zaokrouhlene < 24.9:
                    st.write("Kategorie: Normální váha")
                elif 25 <= bmi_zaokrouhlene < 29.9:
                    st.write("Kategorie: Nadváha")
                elif 30 <= bmi_zaokrouhlene < 34.9:
                    st.write("Kategorie: Obezita 1. stupně")
                elif 35 <= bmi < 39.9:
                    st.write("Kategorie: Obezita 2. stupně")
                else:
                    st.write("Kategorie: Obezita 3. stupně")
            """, language="python")
