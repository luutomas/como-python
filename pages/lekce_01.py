import streamlit as st
st.set_page_config(page_title="COMO Python", page_icon=":snake:", layout="centered", initial_sidebar_state="collapsed")
st.header("Lekce č. 1")

st.subheader("Proměnné a krátká cesta k nim")
st.markdown("""
V programování patří tzv. proměnné k základním kamenuům. \\
Z matematiky si vzpomeňme, že proměnná je něco, co se může měnit. \\
Jak už nejednou bylo řečeno: Matematika mi šla do té doby, než se začali používat písmena. 

Pro nás ale proměnná nebude tak strašná. Představte si to jako adresu, nebo odkaz, na který budete odkazovat. \\
Např. Místo toho, abyste pamatovali, že máte 5 jablek, si pamatujete, že máte 5 jablek na adrese `moje_jablka` a to tímto způsobem:

```
moje_jablka = 5
```

Pokud tedy teď budete chtít vědět, kolik máte jablek, stačí se podívat na adresu `moje_jablka` a to pomocí tohoto příkazu:

```
st.write(moje_jablka)
```

a výsledek bude 5. Celý kód tedy vypadá takto:
```
moje_jablka = 5
st.write(moje_jablka)
```

Proměnné v Pythonu se zapisují pomocí rovnítka `=` a názvy proměnné se píší bez mezer a s malými písmeny a BEZ DIAKRITIKY. \\
Pokud je třeba mezera tak pak se používá `_` podtržítko. \\

Proměnné mohou být různých typů a mohou se s nimi různě pracovat. Níže vidíte příklad práci s číselnými proměnnými. \\
Např. můžete mít proměnnou, `honzovo_jablka`, která bude vědět, kolik má Honza jablek a můžete zjistit kolik jablek mám já s Honzou dohromady.
```
moje_jablka = 5
honzovo_jablka = 1
celkem_jablek = moje_jablka + honzovo_jablka
st.write(celkem_jablek)
```
a výsledek:
""")

moje_jablka = 5
honzovo_jablka = 1
celkem_jablek = moje_jablka + honzovo_jablka
st.write(celkem_jablek)

st.markdown(""" --- """)
st.subheader("Řetěžce neboli Stringy")
st.markdown("""
V této lekci se podíváme na proměnné, které jsou textové. \\
Základní kostka v programování jsou tzv. stringy neboli řetěžce. \\
Název řetězec pochází z toho, že je to řetězec znaků. 

Stringy se zapisují tak, že jsou uzavřeny v uvozovkách, ať už jednoduchých nebo dvojitých. \\
Pro účely kurzy a jednoduchost na českých klávesnicích se používají `""` uvozovky. \\
Pojďme tedy pro účely kurzy s tím pokračovat ale pokud někomu vyhovuje ` '' ` tak ať je použije. \\
POZOR: Ostatní jazyky tuto výsadu nemají!!!

Pojďme si tedy vytvořit string a vypsat ho. \\
Například: 
```
jmeno = "Tomáš"
st.write(jmeno)
```
a výsledek:
""")

jmeno = "Tomáš"
st.write(jmeno)

st.markdown("""
---
Asi nejčastější operací s stringy je konkatenace neboli spojení dvou stringů dohromady. \\
Toho docílíme pomocí `+` znaménka. \\
Například:
```
jmeno = "Tomáš"
prijmeni = "Luu"
jmeno_a_prijmeni = jmeno + prijmeni
st.write(jmeno_a_prijmeni)
```
Výsledek:
""")

jmeno = "Tomáš"
prijmeni = "Luu"
jmeno_a_prijmeni = jmeno + prijmeni
st.write(jmeno_a_prijmeni)

st.markdown("""
---
Pokud bych chtěl lépe tak ještě bych tam dal mezeru mezi jménem a příjmením. \\
```
jmeno = "Tomáš"
prijmeni = "Luu"
jmeno_a_prijmeni = jmeno + " " + prijmeni
st.write(jmeno_a_prijmeni)
```
Výsledek:
""")

jmeno = "Tomáš"
prijmeni = "Luu"
jmeno_a_prijmeni = jmeno + " " + prijmeni
st.write(jmeno_a_prijmeni)

st.markdown("""
---
Ještě lepší je použít f-stringy, které jsou v Pythonu a jsou mnohem přehlednější na práci. \\
F-stringy jsou stringy, které se zapisují pomocí `f` před uvozovkami, můžete tam mít různý text a text, který se má měnit tak je vyznačen `{}`. \\
Pokud bychom chtěli spojit jméno a příjmení pomocí f-stringu, tak to bude vypadat takto:
```
jmeno = "Tomáš"
prijmeni = "Luu"
jmeno_a_prijmeni = f"{jmeno} {prijmeni}"
st.write(jmeno_a_prijmeni)
```
Výsledek:
""")
jmeno = "Tomáš"
prijmeni = "Luu"
jmeno_a_prijmeni = f"{jmeno} {prijmeni}"
st.write(jmeno_a_prijmeni)

st.markdown("""
----
Je to mnohem čistější a přehlednější. \\
A sílá je právě v tom, že dokážete spojovat i čísla k tomu např.
```
vek = 28
jmeno = "Tomáš"
jmeno_vek = f"{jmeno} je starý {vek} let."
st.write(jmeno_vek)
```
Výsledek:
""")
vek = 28
jmeno = "Tomáš"
jmeno_vek = f"{jmeno} je starý {vek} let."
st.write(jmeno_vek)


st.subheader("Textové vstupy a komponenty")
st.markdown("""
Nyní si ukážeme jak vytvořit vstup pro uživatele. \\
Používá se k tomu tzv. komponenta. Komponenta je něco, co se přepoužívá někde jinde. 

Pro textové vstupy se používá komponenta **st.text_input**. \\
**text** znamená text a **input** znamená vstup, tedy vstup textu. \\
**st** indikuje pouze to, že je to z knihovny streamlit, kterou jsme si zkrátili na začátku kódu jako **st**.
```
jmeno = st.text_input("Zadejte jméno")
st.write(jmeno)
```
""")
jmeno = st.text_input("Zadejte jméno", key = "jmeno_1")
st.write(jmeno)

st.markdown("""
---
Každá komponenta má mnoho parametrů, které můžete nastavit. Toto se aktualizije vždy na stránkách streamlitu, kde si můžete přečíst, co všechno můžete nastavit.

https://docs.streamlit.io/develop/api-reference/widgets/st.text_input

```
st.text_input(label, value="", max_chars=None, key=None, type="default", 
help=None, autocomplete=None, on_change=None, 
args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible")
```
Spolu projdeme parametry, které jsou podle nás nejdůležitější a budeme vám je ukazovat na příkladech.

Pro všechny parametry plati, že pokud ten parametr za sebou nemá = něco, tak je povinná a tu musíme specifikovat.
Pokud má `=None`, tak je nepovinná a pokud ji nezadáme, tak se použije defaultní/výchozí hodnota (což je právě ta `None` což znamená nic).

| Název | Popis |
| ----- | ------ |
| **label** | popisek, který se zobrazí u komponenty |
| **value** | defaultní hodnota, která se zobrazí v komponentě |
| **max_chars** | maximální počet znaků, které může uživatel zadat |
| **key** | klíč, který se používá k identifikaci komponenty - vždy vyplňovat (není povinný ale vytvoří to dobrý zvyk)|
| **type** | typ komponenty, defaultně je to "default", jinak pak je "password", který schovává vstup |
| **help** | nápověda, která se zobrazí u komponenty |
| **placeholder** | text, který se zobrazí v komponentě, pokud je prázdná |
| **disabled** | zda je komponenta aktivní nebo ne |
| **label_visibility** | zda je popisek vidět nebo ne |
| autocomplete | možnost autocomplete - nebudeme rozebírat|
| on_change | funkce, která se spustí, když se změní hodnota v komponentě - pokročilé, nebudeme rozebírat|
| args | argumenty pro funkci on_change - pokročilé, nebudeme rozebírat|
| kwargs | keyword argumenty pro funkci on_change - pokročilé, nebudeme rozebírat|

Pokud bych tedy chtěl vytvořit textový vstup, kde bude defaultní hodnota "Jméno", tak to bude vypadat takto:
```
jmeno = st.text_input("Zadejte jméno", value="Jméno", key="jmeno_2")
prijmeni = st.text_input("Zadejte příjmení", value="Příjmení", key="prijmeni_2")
mesto = st.text_input("Zadejte město", value="Most", key="mesto_2", placeholder="Napište město", type = "password")
jmeno_a_prijmeni_mesto = f"{jmeno} {prijmeni} {mesto}"
st.write(jmeno_a_prijmeni_mesto)
```
""")

jmeno = st.text_input("Zadejte jméno", value="Jméno", key="jmeno_2")
prijmeni = st.text_input("Zadejte příjmení", value="Příjmení", key="prijmeni_2")
mesto = st.text_input("Zadejte město", value="Most", key="mesto_2", placeholder="Napište město", type = "password")
jmeno_a_prijmeni_mesto = f"{jmeno} {prijmeni} {mesto}"
st.write(jmeno_a_prijmeni_mesto)

st.markdown("""
---
Vyzkoušejte si to sami a zkuste si vytvořit vlastní textový vstup a zkuste si pohrát s parametry. 
""")

st.markdown("""
### Úkol 1

Vytvořte textový vstup, kde bude defaultní/výchozí hodnota "Jméno" a maximální počet znaků bude 5.
""")
if st.toggle("Zobrazit řešení 1"):
    jmeno = st.text_input("Zadejte jméno", value="Jméno", key="jmeno_3", max_chars=5)

    if st.toggle("Zobrazit kód 1"):
        st.code("""
        jmeno = st.text_input("Zadejte jméno", value="Jméno", key="jmeno_3", max_chars=5)
        """, language="python")

st.markdown("""
---
### Úkol 2
Vytvořte textový vstup, kde bude defaultní/výchozí hodnota "Příjmení" a bude mít schovaný label. 
""")
if st.toggle("Zobrazit řešení 2"):
    prijmeni = st.text_input("Zadejte příjmení", value="Příjmení", key="prijmeni_3", label_visibility="hidden")
    
    if st.toggle("Zobrazit kód 2"):
        st.code("""
        prijmeni = st.text_input("Zadejte příjmení", value="Příjmení", key="prijmeni_3", label_visibility="hidden"),
        """, language="python")

st.markdown("""
---
### Úkol 3
Vytvořte textový vstup, kde bude defaultní/výchozí hodnota "Město" a bude typ password a bude mít nápovědu "Zadejte město". 
""")
if st.toggle("Zobrazit řešení 3"):
    mesto = st.text_input("Zadejte město", value="Město", key="mesto_3", placeholder="Napište město", help="Zadejte město", type = "password")
    
    if st.toggle("Zobrazit kód 3"):
        st.code("""
        mesto = st.text_input("Zadejte město", value="Město", key="mesto_3", placeholder="Napište město", help="Zadejte město", type = "password")
        """, language="python")

st.markdown("""
---
### Úkol 4
Spojte ty 3 textové vstupy dohromady proměnné spojeni_pomoci_plus a spojte je pomocí `+` znaménka.
""")
if st.toggle("Zobrazit řešení 4"):
    jmeno_a_prijmeni_mesto = jmeno + " " + prijmeni + " " + mesto
    st.write(jmeno_a_prijmeni_mesto)

    if st.toggle("Zobrazit kód 4"):
        st.code("""
        jmeno_a_prijmeni_mesto = jmeno + " " + prijmeni + " " + mesto
        st.write(jmeno_a_prijmeni_mesto)
        """, language="python")
st.markdown("""
---
### Úkol 5
Spojte ty 3 textové vstupy dohromady proměnné spojeni_pomoci_fstring a spojte je pomocí f-stringu.
""")
if st.toggle("Zobrazit řešení 5"):
    jmeno_a_prijmeni_mesto = f"{jmeno} {prijmeni} {mesto}"
    st.write(jmeno_a_prijmeni_mesto)

    if st.toggle("Zobrazit kód 5"):
        st.code("""
        jmeno_a_prijmeni_mesto = f"{jmeno} {prijmeni} {mesto}"
        st.write(jmeno_a_prijmeni_mesto)
        """, language="python")

st.markdown("""
---
Mezi často využívané funkce, které budete potřebovat když budete pracovat s řetězci patří:
- `len()` - délka řetězce
- `lower()` - převod na malá písmena
- `upper()` - převod na velká písmena
- `capitalize()` - první písmeno velké
- `replace()` - nahrazení řetězce
- `strip()` - odstranění bílých znaků
- `startswith()` - zda začíná řetězec na něco
- `endswith()` - zda končí řetězec na něco
- `find()` - najít pozici řetězce
- `join()` - spojení řetězců

Příklady jak to využít naleznete níže.
""")

libovolny_retezec = "Magistrát města Mostu "
st.code("""
libovolny_retezec = "Magistrát města Mostu "
delka_retezce = len(libovolny_retezec)
st.write(delka_retezce)
""")
st.write(len(libovolny_retezec))
st.write("---")
st.code("""
libovolny_retezec = "Magistrát města Mostu "
retezec_mala_pismena = libovolny_retezec.lower()
st.write(retezec_mala_pismena)
""")
st.write(libovolny_retezec.lower())
st.write("---")
st.code("""
libovolny_retezec = "Magistrát města Mostu "
retezec_velka_pismena = libovolny_retezec.upper()
st.write(retezec_velka_pismena)
""")
st.write(libovolny_retezec.upper())
st.write("---")
st.code("""
libovolny_retezec = "Magistrát města Mostu "
retezec_prvni_velke = libovolny_retezec.capitalize()
st.write(retezec_prvni_velke)
""")
st.write(libovolny_retezec.capitalize())
st.write("---")
st.code("""
libovolny_retezec = "Magistrát města Mostu "
retezec_nahrazeny = libovolny_retezec.replace("Magistrát města", "Dycky")
st.write(retezec_nahrazeny)
""")
st.write(libovolny_retezec.replace("Magistrát města", "Dycky"))
st.write("---")
st.code("""
libovolny_retezec = "Magistrát města Mostu "
retezec_zacinajici = libovolny_retezec.startswith("Mag")
st.write(retezec_zacinajici)
""")
st.write(libovolny_retezec.startswith("Mag"))
st.write("---")
st.code("""
libovolny_retezec = "Magistrát města Mostu "
retezec_koncici = libovolny_retezec.endswith("Mostu")
st.write(retezec_koncici) # pozor na mezery
""")
st.write(libovolny_retezec.endswith("Mostu")) 
st.write("---")
st.code("""
libovolny_retezec = "Magistrát města Mostu "
retezec_ocisteny = libovolny_retezec.strip()
st.write(retezec_ocisteny)
""")
st.write(libovolny_retezec.strip())
st.write("---")
st.code("""
libovolny_retezec = "Magistrát města Mostu "
retezec_ocisteny = libovolny_retezec.strip()
retezec_ocisteny_koncici = retezec_ocisteny.endswith("Mostu")
st.write(retezec_ocisteny_koncici)
""")
st.write(libovolny_retezec.strip().endswith("Mostu"))
st.write("---")
st.code("""
libovolny_retezec = "Magistrát města Mostu "
retezec_nalezeny = libovolny_retezec.find("Mostu")
st.write(retezec_nalezeny)
""")
st.write(libovolny_retezec.find("Mostu"))
st.write("---")
st.code("""
libovolny_retezec_1 = "Magistrát"
libovolny_retezec_2 = "města"
libovolny_retezec_3 = "Mostu"
retezec_spojeny_s_mezerou = " ".join([libovolny_retezec_1, libovolny_retezec_2, libovolny_retezec_3])
retezec_spojeny_pomlckou = "-".join([libovolny_retezec_1, libovolny_retezec_2, libovolny_retezec_3])
st.write(retezec_spojeny_s_mezerou)
st.write(retezec_spojeny_pomlckou)
""")

libovolny_retezec_1 = "Magistrát"
libovolny_retezec_2 = "města"
libovolny_retezec_3 = "Mostu"
retezec_spojeny_s_mezerou = " ".join([libovolny_retezec_1, libovolny_retezec_2, libovolny_retezec_3])
retezec_spojeny_pomlckou = "-".join([libovolny_retezec_1, libovolny_retezec_2, libovolny_retezec_3])
st.write(retezec_spojeny_s_mezerou)
st.write(retezec_spojeny_pomlckou)

st.markdown("""
---
Příklady na procvičení:

### Úkol 6
Nechte si od uživatele dodat jméno a příjmení.
Zajistěte, že první písmeno jména a příjmení budou velké a zbytek malé a napište toto celé jméno pomocí f-stringu.
""")

if st.toggle("Zobrazit řešení 6"):
    jmeno = st.text_input("Zadejte jméno", key="jmeno_6")
    prijmeni = st.text_input("Zadejte příjmení", key="prijmeni_6")
    jmeno = jmeno.capitalize()
    prijmeni = prijmeni.capitalize()
    cele_jmeno = f"{jmeno} {prijmeni}"
    st.write(cele_jmeno)
    
    if st.toggle("Zobrazit kód 6"):
        st.code("""
        jmeno = st.text_input("Zadejte jméno", key="jmeno_6")
        prijmeni = st.text_input("Zadejte příjmení", key="prijmeni_6")
        jmeno = jmeno.capitalize()
        prijmeni = prijmeni.capitalize()
        cele_jmeno = f"{jmeno} {prijmeni}"
        st.write(cele_jmeno)
        """, language="python")
    