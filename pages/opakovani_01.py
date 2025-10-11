import streamlit as st

st.set_page_config(page_title="COMO Python", page_icon="icon.png", layout="centered")

st.header("Opakování lekce č. 1, 2 a 3")

st.subheader("Text, čísla, proměnné a podmínky")

st.markdown("""
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

if st.toggle("Zobrazit nápovědu"):
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

    if st.toggle("Zobrazit řešení"):
        vaha = st.number_input("Zadejte svou váhu (kg):", min_value=10.0, max_value=200.0, value=70.0, step=0.1)
        vyska = st.number_input("Zadejte svou výšku (cm):", min_value=100, max_value=250, value=170, step=1)

        bmi = vaha / ((vyska * vyska) / 10000)
        bmi_zaokrouhlene = round(bmi, 2)

        if st.button("Spočítat BMI"):
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

        if st.toggle("Zobrazit kód"):
            st.code("""
            vaha = st.number_input("Zadejte svou váhu (kg):", min_value=10.0, max_value=200.0, value=70.0, step=0.1)
            vyska = st.number_input("Zadejte svou výšku (cm):", min_value=100, max_value=250, value=170, step=1)

            bmi = vaha / ((vyska * vyska) / 10000)
            bmi_zaokrouhlene = round(bmi, 2)

            if st.button("Spočítat BMI"):
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
