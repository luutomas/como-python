import streamlit as st
import json 
st.set_page_config(page_title="COMO Python", page_icon="icon.png", layout="centered")

st.header("Domácí úkol")
st.markdown("""
V tété sekci najdete zadání domácích úkolů, které by pro vás mohli být zajímavé. \\
Na kurzu nebude možné probrat veškerou látku takže i zde bude zajímavosti, které jsme nestihli probrat. \\
## Domácí úkol 1
Vytvořte aplikaci podle následujícího zadání. 
1. Vytvořte file uzivatele.json, kde budete mít uložené informace o uživatelích.
```
{
    "tomas": "heslo",
    "honza": "heslo",
}
```
2. Vytvořte pomocí text_inputu dvě pole st.text_input, kde první pole bude uživatelské jméno a druhé bude pole typu `password` (tedy bude skryté).
3. Pomocí st.button ověřte, zda uživatel zadal správné heslo. 
4. Pokud heslo bude správné, vypište "Přihlášení úspěšné", jinak "Přihlášení neúspěšné".

## Domácí úkol 2
Podívejte se na komponenty v této části: 
https://docs.streamlit.io/develop/api-reference/layout
a zkuste použít některé z nich v této aplikaci.

1. Vytvořte aplikaci, kde budete mít 2 sloupce
2. V jednom sloupci budou vstupy pro uživatele a v druhém budou výstupy.
3. Budete mít 2 textové vstupy, 1 číselný vstup a 1 checkbox a 1 tlačitko.
- jmeno
- prijmeni
- věk
- muž

4.Pomocí těchto vstupu pak vypište ve druhém sloupci informace o uživateli.

## Domácí úkol 3
Zkuste si vytvořit aplikaci, která bude mít následující funkce: 
1. Vytvořte aplikaci, kde bude textové pole a tlačítko.
2. Pomocí této první části budete moci zadat text, který se uloží do texty.json. Klíč bude vždycky číslo, které bude o 1 vyšší než předchozí klíč a začíná se od 0.
3. Vytvořte druhou část, kde bude textové pole a tlačítko.
4. Pomocí této části budete moci načísty texty.json a vypsat texty, které se aspoň shodují v nějaké části s textem, který jste zadali. \\
Napříkla: v texty.json máte uložené texty:
```
{
    "0" : "Ahoj jak se máš?",
    "1" : "Dobrý den",
    "2" : "Jak se máš?"
}
```
Pokud zadáte do textového pole "Jak", tak vám aplikace vypíše text pod klíčem 0 a pod klíčem 2. \\
Dávejte ale pozor na velikost písmen, tedy "Jak" a "jak" se neshodují. \\
Také dávejte pozor, že do JSON se všechno převede do písmen. Takže bude třeba, aby jste s tím počítali, když budete přidávat klíče do JSONu a pracovat s nimi. \\
Dávejte taky pozor, že pokud texty.json bude prázdný tak tam žádný klíč není a nebudete moci nic načíst.
5. Nakonec vytvořte tlačítko, které vymaže texty.json.

Tato úloha patří v k velmi náročným a pravdpěodobně budete muset hledat i mimo naší lekce. \\
Budete muset používat i for cyklus a podmínky pro hledání textu. \\
Na hodině se k této úloze vyjádřím, pokud zbyde čas poté, co probereme cykly. \\
Pokud to bude na vás příliš těžké tak stačí udělat jenom body: \\
1., 2. a 5. což jsou tedy zápis a výmaz textu.

---
""")

if st.toggle("Ukázat řešení"):
    with open("data/json/texty.json", "r") as f:
            data = json.load(f)
    text = st.text_input("Textové pole pro zadání textu")
    btn_add_text = st.button("Uložit text")
    if btn_add_text:
        try:
            posledni_klic = int(max(data.keys())) + 1
        except:
            posledni_klic = 0
        data[posledni_klic] = text
        with open("data/json/texty.json", "w") as f:
            json.dump(data, f)
        st.success("Text byl uložen")
    st.write("---")
    search_text = st.text_input("Textové pole pro vyhledání textu")
    btn_search = st.button("Vyhledat text")
    if btn_search:
        nalezen = False
        for k, v in data.items():
            if search_text.lower() in v.lower():
                nalezen = True
                st.write(f"Klíč: {k}, Text: {v}")
        if nalezen:
            st.success("Text nalezen")
        else:
            st.error("Text nebyl nalezen")

    st.write("---")
    btn_delete = st.button("Vymazat texty")
    if btn_delete:
        with open("data/json/texty.json", "w") as f:
            json.dump({}, f)
        st.success("Texty byly vymazány")
    
    if st.toggle("Ukázat kód"):
        st.code("""
    with open("data/json/texty.json", "r") as f:
            data = json.load(f)
    text = st.text_input("Textové pole pro zadání textu")
    btn_add_text = st.button("Uložit text")
    if btn_add_text:
        try:
            posledni_klic = int(max(data.keys())) + 1
        except:
            posledni_klic = 0
        data[posledni_klic] = text
        with open("data/json/texty.json", "w") as f:
            json.dump(data, f)
        st.success("Text byl uložen")
    st.write("---")
    search_text = st.text_input("Textové pole pro vyhledání textu")
    btn_search = st.button("Vyhledat text")
    if btn_search:
        nalezen = False
        for k, v in data.items():
            if search_text.lower() in v.lower():
                nalezen = True
                st.write(f"Klíč: {k}, Text: {v}")
        if nalezen:
            st.success("Text nalezen")
        else:
            st.error("Text nebyl nalezen")

    st.write("---")
    btn_delete = st.button("Vymazat texty")
    if btn_delete:
        with open("data/json/texty.json", "w") as f:
            json.dump({}, f)
        st.success("Texty byly vymazány")
        """)

def nacti_texty():
    """Načte texty ze souboru JSON."""
    try:
        with open("data/json/texty.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return [] # Vrátí prázdný seznam, pokud soubor neexistuje

def uloz_texty(texty):
    """Uloží texty do souboru JSON."""
    with open("data/json/texty.json", "w") as f:
        json.dump(texty, f, indent=4)

# --- Hlavní část aplikace ---
if st.toggle("Ukázat řešení"):
    texty = nacti_texty()
    text = st.text_input("Textové pole pro zadání textu")
    btn_add_text = st.button("Uložit text")
    if btn_add_text:
        texty.append(text)
        uloz_texty(texty) # Uložení aktualizovaného seznamu
        st.success("Text byl úspěšně přidán!")
        st.rerun() # Znovu načte stránku, aby se zobrazil nový text

    st.write("---")
    search_text = st.text_input("Textové pole pro vyhledání textu")
    btn_search = st.button("Vyhledat text")
    if btn_search:
        nalezen = False
        for k, v in texty:
            if search_text.lower() in v.lower():
                nalezen = True
                st.write(f"Text: {v}")
        if nalezen:
            st.success("Text nalezen")
        else:
            st.error("Text nebyl nalezen")

    st.write("---")
    index_textu = st.number_input("Index textu pro úpravu", min_value=0, max_value=len(texty)-1, value=0)
    btn_upravit = st.button("Upravit text")
    if btn_upravit:
        upraveny_text = st.text_input("Upravený text")
        texty[index_textu] = upraveny_text
        uloz_texty(texty) # Uložení aktualizovaného seznamu
        st.success(f"Text na indexu {index_textu} byl upraven!")
        st.rerun()

    st.write("---")
    index_textu_ke_smazani = st.number_input("Index textu pro smazání", min_value=0, max_value=len(texty)-1, value=0)
    btn_smazat = st.button("Smazat text")
    if btn_smazat:
        del texty[index_textu_ke_smazani]
        uloz_texty(texty) # Uložení aktualizovaného seznamu
        st.success(f"Text na indexu {index_textu_ke_smazani} byl smazán!")
        st.rerun()

    if st.toggle("Ukázat kód"):
        st.code("""
def nacti_texty():
    '''Načte texty ze souboru JSON.'''
    try:
        with open("data/json/texty.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return [] # Vrátí prázdný seznam, pokud soubor neexistuje

def uloz_texty(texty):
    '''Uloží texty do souboru JSON.'''
    with open("data/json/texty.json", "w") as f:
        json.dump(texty, f, indent=4)

# --- Hlavní část aplikace ---
if st.toggle("Ukázat řešení"):
    texty = nacti_texty()
    text = st.text_input("Textové pole pro zadání textu")
    btn_add_text = st.button("Uložit text")
    if btn_add_text:
        texty.append(text)
        uloz_texty(texty) # Uložení aktualizovaného seznamu
        st.success("Text byl úspěšně přidán!")
        st.rerun() # Znovu načte stránku, aby se zobrazil nový text

    st.write("---")
    search_text = st.text_input("Textové pole pro vyhledání textu")
    btn_search = st.button("Vyhledat text")
    if btn_search:
        nalezen = False
        for k, v in texty:
            if search_text.lower() in v.lower():
                nalezen = True
                st.write(f"Text: {v}")
        if nalezen:
            st.success("Text nalezen")
        else:
            st.error("Text nebyl nalezen")

    st.write("---")
    index_textu = st.number_input("Index textu pro úpravu", min_value=0, max_value=len(texty)-1, value=0)
    btn_upravit = st.button("Upravit text")
    if btn_upravit:
        upraveny_text = st.text_input("Upravený text")
        texty[index_textu] = upraveny_text
        uloz_texty(texty) # Uložení aktualizovaného seznamu
        st.success(f"Text na indexu {index_textu} byl upraven!")
        st.rerun()

    st.write("---")
    index_textu_ke_smazani = st.number_input("Index textu pro smazání", min_value=0, max_value=len(texty)-1, value=0)
    btn_smazat = st.button("Smazat text")
    if btn_smazat:
        del texty[index_textu_ke_smazani]
        uloz_texty(texty) # Uložení aktualizovaného seznamu
        st.success(f"Text na indexu {index_textu_ke_smazani} byl smazán!")
        st.rerun()
        """
        )