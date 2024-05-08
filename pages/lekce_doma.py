import streamlit as st

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
""")