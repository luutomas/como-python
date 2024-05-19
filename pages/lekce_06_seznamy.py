import streamlit as st
import json
st.set_page_config(page_title="COMO Python", page_icon=":snake:", layout="centered", initial_sidebar_state="collapsed")
st.header("Lekce č.5")

st.subheader("Seznamy, sety a n-tice")
st.markdown("""
Mezi další kličovou datovou strukturu patří seznamy. Sety a n-tice jsou podobné seznamům, ale mají několik rozdílů. \\
Seznam je datová struktura, která ukládá data v pořadí, podobně jako seznam v reálném životě. \\
V Pythonu se seznam zapisuje pomocí hranatých závorek `[]` nebo zaobalením něčeho, co by se dalo převést na seznam pomocí `list()`. \\
Např. seznam s názvy jídel může vypadat takto:
```
jidla = ["hamburger", "pizza", "sendvič"]
```
Pokud bych chtěl získat první jídlo v seznamu, tak bych napsal:
```
prvni_jidlo = jidla[0]
st.write(f"První jídlo je {prvni_jidlo}") # Všimněte si f-string v odpovědi
```
a tedy výsledek:
""")
jidla = ["hamburger", "pizza", "sendvič"]
prvni_jidlo = jidla[0]
st.write(f"První jídlo je {prvni_jidlo}") # Všimněte si f-string v odpovědi

st.markdown("""
---
Všimněte si, že indexování v Pythonu začíná od 0. \\
Sety jsou datová struktura, která ukládá data bez pořadí a bez duplicit. \\
V Pythonu se set zapisuje pomocí složených závorek `{}` ale inicializuje pomocí `set()` protože složené závorky jsou dle domluvy vyhrazené pro slovníky. \\
Např. set s názvy jídel může vypadat takto:
```
jidla = set(["hamburger", "pizza", "sendvič"])
```
Všimněte si, že set je inicializován pomocí `set()` a v ní je seznam jídel. \\
Tohle je velmi časté používání setů, protože se takto odstraní duplicitní hodnoty. \\
Např. máme seznam s jídlem:
```
seznam_jidel = ["hamburger", "pizza", "sendvič", "hamburger", "pizza"]
set_jidel = set(seznam_jidel)
```
""")

seznam_jidel = ["hamburger", "pizza", "sendvič", "hamburger", "pizza"]
set_jidel = set(seznam_jidel)
st.write(seznam_jidel)
st.write(set_jidel)

st.markdown("""
---
N-tice jsou datová struktura, která ukládá data v pořadí, ale nemůžeme je měnit. \\
V Pythonu se n-tice zapisuje pomocí kulatých závorek `()`. \\
Nelze měnit ani nelze vzít "první" pozici jako u seznamu. \\
Např. n-tice s názvy jídel může vypadat takto:
```
hamburger = ("hamburger", 115)
sendvič = ("sendvič", 59)
pizza = ("pizza", 149)
```
Všimněte si, že n-tice jsou právě výsledkem operace na slovníky .items() např.:
```
jidla = {
    "hamburger": 115,
    "sendvič": 59,
    "pizza": 149
}
st.write(jidla.items())
st.write(list(jidla.items())[0])
```
Výsledkem dostáváme LIST s n-ticemi, kdy každá n-tice má název a cenu. \\
Tedy pak můžeme manipulovat s listem např. 
""")

jidla = {
    "hamburger": 115,
    "sendvič": 59,
    "pizza": 149
}
st.write(jidla.items())
st.write(list(jidla.items())[0])

st.markdown("""
---
Pro naší práci bude nejdůležiější práce se seznamy a s nimi budeme pokračovat. \\
Pro sety a n-tice si pouze třeba uvědomit, že existují a že pomocí set() můžeme odstranit duplicitní hodnoty ze seznamu.

Mezi nejdůležitější funkce, které můžete se seznamem provádět patří:
| Funkce | Popis |
|--------|-------|
| `append()` | Přidá prvek na konec seznamu |
| `insert()` | Přidá prvek na zvolenou pozici |
| `remove()` | Odebere prvek ze seznamu |
| `pop()` | Odebere prvek na zvolené pozici |
| `clear()` | Smaže celý seznam |
| `sort()` | Seřadí seznam |
| `reverse()` | Otočí pořadí seznamu |
| `index()` | Vrátí pozici prvku |
| `count()` | Vrátí počet prvků |
| `copy()` | Zkopíruje seznam |
| `extend()` | Rozšíří seznam o další seznam |
| `len()` | Vrátí délku seznamu |
---

Pojďme si je ukázat v akci:
```
menu = ["hamburger", "pizza", "sendvič"]
menu = ["hamburger", "pizza", "sendvič"]

menu.append("pho")
st.write(f"Po appendu: {menu}")

menu.insert(1, "gyros")
st.write(f"Po insertu: {menu}")

menu.remove("pizza")
st.write(f"Po remove: {menu}")

menu.pop(0)
st.write(f"Po pop: {menu}")

menu.sort()
st.write(f"Po sort: {menu}")

menu.reverse()
st.write(f"Po reverse: {menu}")
```
""")

menu = ["hamburger", "pizza", "sendvič"]
menu = ["hamburger", "pizza", "sendvič"]

menu.append("pho")
st.write(f"Po appendu: {menu}")

menu.insert(1, "gyros")
st.write(f"Po insertu: {menu}")

menu.remove("pizza")
st.write(f"Po remove: {menu}")

menu.pop(0)
st.write(f"Po pop: {menu}")

menu.sort()
st.write(f"Po sort: {menu}")

menu.reverse()
st.write(f"Po reverse: {menu}")

st.markdown("""
---
Zkuste nyní sami pár úloh:
Máte seznam jmen:
```
jmena = ["Adéla", "Albert", "Míša", "Jára", "David", "Martin", "Oksana"]
```

### Úkol 1
Přidejte do seznamu jméno Tomáš.

### Úkol 2
Seřaďte seznam jmen. 

### Úkol 3
Odeberte z listu jméno David.

### Úkol 4
Pžidejte do seznamu jméno Adéla znovu.

### Úkol 5
Vytvořte ze seznamu set a vypište ho. \\
Vytvořte ze setu seznam a vypište ho.

### Úkol 6
Vypište délku seznamu jmen z úkolu 5.

""")

st.markdown("""
---
### Komponenty
Jelikož jsme se naučili pracovat se seznamy, můžeme se podívat na další streamlit komponenty, které potřebovali seznamy. \\
Jedná se o `st.selectbox()` a `st.multiselect()`. \\
Obě komponenty potřebují seznam, ze kterého se bude vybírat. \\
Parametry pro `st.selectbox()`:
| Parametr | Popis |
|----------|-------|
| **label** | Popisek pro komponentu |
| **options** | Seznam možností |
| **index** | Index vybrané možnosti |
| **key** | Klíč pro komponentu |
| **help** | Nápověda pro komponentu |
| on_change | Funkce, která se spustí při změně |
| args | Argumenty pro funkci on_change |
| kwargs | Keyword argumenty pro funkci on_change |

Parametry pro `st.multiselect()`:
| Parametr | Popis |
|----------|-------|
| **label** | Popisek pro komponentu |
| **options** | Seznam možností |
| **default** | Defaultní hodnota |
| **key** | Klíč pro komponentu |
| **help** | Nápověda pro komponentu |


Např. máme seznam jmen:
```
jmena = ["Adéla", "Albert", "Míša", "Jára", "David", "Martin", "Oksana"]
```
a chceme, aby uživatel vybral jedno jméno:
```
jmeno = st.selectbox("Vyber jméno", jmena)
st.write(f"Vybral jsi {jmeno}")
```
a tedy výsledek:
""")
jmena = ["Adéla", "Albert", "Míša", "Jára", "David", "Martin", "Oksana"]
jmeno = st.selectbox("Vyber jméno", options = jmena, index = 3)
st.write(f"Vybral jsi {jmeno}")


st.markdown("""
---
Seznamy jsou velmi důležitou částí Pythonu, protože na nich stojí cykly, které jsou klíčovou součástí programování. \\
Co totiž umí stroj nejlépe a mnohem lépe než člověk? Opakovat věci. 

A to si nyní ukážeme v další lekci
""")

st.markdown("""
---
### Úkol 1
Zkuste si nadefinovat json, který bude obsahovat seznam jídel a jejich cenu. \\
Pro začátek nám postačí, aby měl json 3 jídla a 3 nápoje, včetně cen. \\
Např.:
```json
{
    "hambruger": 115,
    "pizza": 149,
    "sendvič": 59,
    "cola": 35,
    "pivo": 45,
    "voda": 25
}
```
Soubor si uložte jako `menu.json`, načtěte do aplikace a vytvořte pro uživatele select box pro výběr tak, aby si mohl vybrat jako více položek.

### Úkol 2
Upravte json tak, aby byly položky uložené v kategoriích `jídla` a `nápoje`.
""")

if st.toggle("Nápověda pro úkol 2"):
    st.markdown("""
        Výsledný json by měl vypadat takto:
        ```json
        {
            "jídla": {
                "hambruger": 115,
                ...
            },
            "nápoje": {
                "cola": 35,
                ...
            }
        }
        ```      
        """)
    
st.markdown("""
Načtěte nový json a vytvořte pro uživatele 2 nové select boxy, kde si bude moci vybrat pouze jedno jídlo a jeden nápoj. \\
Pozor na to, že se změnou struktury jsonu nám nebude fungovat předchozí select box. \\
Na závěr vypište vybrané jídlo a nápoj.

### Úkol 3
Na základě vybraného jídla a nápoje vypište celkovou cenu objednávky, ale dejte si pozor na to, že pokud nebude vybráno jídlo i nápoj, tak kalkulace nebude fungovat.
""")

if st.toggle("Nápověda pro úkol 3"):
    st.markdown("""
        Pro vyhledávání ve slovníku můžete tedy využít funkci `get()` a jako defaultní hodnotu nastavit 0.   
        """)

st.markdown("""            
### Úkol 4
Do jsonu přidejte další kategorii `typ platby` a do ní jako hodnotu seznam možných plateb (hotově, kartou, kupon). \\
*Všimněte si, že jako hodnotu ve slovníku můžete mít jen další vnořený slovník, ale i seznam.* \\
*Ale pozor na to, že klíč musí být **VŽDY STRING.*** \\
```json
{"klic": ["hodnota1", "hodnota2"]}
```
Aktualizujte aplikaci tak, aby uživatel mohl vybrat i typ platby a vypište vybraný typ platby.
            
### Úkol 5
Pokud uživatel vybere typ platby `kupon`, tak přepočítejte celkovou cenu objednávky tak, aby uživatel dostal 10% slevu. A na závěr vypište novou cenu objednávky.
""")

if st.toggle("Ukázat řešení"):
    with open("nove_menu.json", "r") as f:
        menu = json.load(f)

    jidla = list(menu["jídla"].keys())
    napoje = list(menu["nápoje"].keys())
    typ_platby = menu["typ platby"]

    vybrane_jidlo = st.selectbox("Vyber jídlo", jidla, index = None, key="vybrane_jidlo", placeholder="Vyber jídlo")
    vybrany_napoj = st.selectbox("Vyber nápoj", napoje, index = None, key="vybrany_napoj", placeholder="Vyber nápoj")
    vybrana_platba = st.selectbox("Vyber typ platby", typ_platby, index = None, key="vybrana_platba", placeholder="Vyber typ platby")

    st.write(f"Vybral jsi jídlo: {vybrane_jidlo}")
    st.write(f"Vybral jsi nápoj: {vybrany_napoj}")
    st.write(f"Vybral jsi platbu: {vybrana_platba}")

    cena = menu["jídla"].get(vybrane_jidlo, 0) + menu["nápoje"].get(vybrany_napoj, 0)
    st.write(f"Celková cena objednávky je {cena}")

    if vybrana_platba == "kupon":
        cena = cena * 0.9
        st.write(f"Po slevě je cena objednávky {cena}")

    if st.toggle("Ukázat kód"):
        st.code("""
            with open("nove_menu.json", "r") as f:
                menu = json.load(f)

            jidla = list(menu["jídla"].keys())
            napoje = list(menu["nápoje"].keys())
            typ_platby = menu["typ platby"]

            vybrane_jidlo = st.selectbox("Vyber jídlo", jidla, index = None, key="vybrane_jidlo", placeholder="Vyber jídlo")
            vybrany_napoj = st.selectbox("Vyber nápoj", napoje, index = None, key="vybrany_napoj", placeholder="Vyber nápoj")
            vybrana_platba = st.selectbox("Vyber typ platby", typ_platby, index = None, key="vybrana_platba", placeholder="Vyber typ platby")

            st.write(f"Vybral jsi jídlo: {vybrane_jidlo}")
            st.write(f"Vybral jsi nápoj: {vybrany_napoj}")
            st.write(f"Vybral jsi platbu: {vybrana_platba}")

            cena = menu["jídla"].get(vybrane_jidlo, 0) + menu["nápoje"].get(vybrany_napoj, 0)
            st.write(f"Celková cena objednávky je {cena}")

            if vybrana_platba == "kupon":
                cena = cena * 0.9
                st.write(f"Po slevě je cena objednávky {cena}")
        """)
        

    