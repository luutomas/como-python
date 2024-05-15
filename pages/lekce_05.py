import streamlit as st

st.header("JSON")
st.markdown("""
Struktura slovníků je velmi podobná JSON, který je zkratkou pro JavaScript Object Notation. \\
JSON je de fakto slovník, který je zapsaný v textové podobě a je to jeden z nejlepších způsobů, **jak ukládat data a posílat data**. \\
My můžeme tedy také slovníky ukládat a pak je používat. \\
Pojďme si to zkusit spolu.
Pro manipulaci s JSON používáme knihovnu `json` a pro načtení a zápis do souboru používáme funkce `load` a `dump`.
To vypadá takto:
```
import json
json.load(cesta_k_souboru)
json.dump(cesta_k_souboru, data)
```
Pojďme to spolu zkusit.
Nejdříve uložím náš jídelní lístek do souboru `jidla.json`:
```
jidla = {
    "hamburger": 99,
    "pizza": 149,
    "sendvič": 59
    }
with open("jidla.json", "w") as f:
    json.dump(jidla, f)
```
""")
import json
jidla = {
    "hamburger": 99,
    "pizza": 149,
    "sendvič": 59
    }
with open("jidla.json", "w") as f:
    json.dump(jidla, f)

st.markdown("""
---
Nově budeme mít soubor `jidla.json` a můžeme si ho načíst pomocí:
```
with open("jidla.json", "r") as f:
    nactena_jidla = json.load(f)
st.write(nactena_jidla)
```
Viz výsledek:
""")

with open("jidla.json", "r") as f:
    nactena_jidla = json.load(f)
st.write(nactena_jidla)

st.markdown("""
---
Nyní přidáme do našeho menu nové jídlo a uložíme to zpět do souboru:
```
nactena_jidla["kebab"] = 89
with open("jidla.json", "w") as f:
    json.dump(nactena_jidla, f)
``` 
""")
nactena_jidla["kebab"] = 89
with open("jidla.json", "w") as f:
    json.dump(nactena_jidla, f)

st.markdown("""
Nyní když se podívate na ten souboru, tak tam bude nové jídlo.

Ukázali jsme si tedy základní práci se slovníky a jak je ukládat a načítat z JSON souborů.

Pojďme si to zkusit na příkladu. Máte následující slovník:
```
menu = {
    "hamburger": 99,
    "pizza": 149,
    "sendvič": 59,
    "kebab": 89,
    "pho": 79,
    "řízek": 119,
    "knedlo-vepřo-zelo": 139
    }
```
### Úkol 1
Uložte tento slovník do souboru `menu.json` a poté ho načtěte a vypište. \\
Ověřte, že existuje soubor `menu.json` a že obsahuje správná data.
""")
if st.toggle("Zobrazit řešení", False, key = "reseni_1"):
    menu = {
        "hamburger": 99,
        "pizza": 149,
        "sendvič": 59,
        "kebab": 89,
        "pho": 79,
        "řízek": 119,
        "knedlo-vepřo-zelo": 139
        }
    with open("menu.json", "w") as f:
        json.dump(menu, f)
    with open("menu.json", "r") as f:
        nactene_menu = json.load(f)
    st.write(nactene_menu)
    if st.toggle("Zobrazit kód", False, key = "kod_1"):
        st.code("""
        menu = {
            "hamburger": 99,
            "pizza": 149,
            "sendvič": 59,
            "kebab": 89,
            "pho": 79,
            "řízek": 119,
            "knedlo-vepřo-zelo": 139
            }
        with open("menu.json", "w") as f:
            json.dump(menu, f)
        """)

st.markdown("""
---
### Úkol 2
Přidejte do menu položku kuřecí nudle za 99 a uložte to zpět do souboru `menu.json`.
Ověřte, že se změna provedla správně i v souboru.
""")
if st.toggle("Zobrazit řešení", False, key = "reseni_9"):
    with open("menu.json", "r") as f:
        menu = json.load(f)
    menu["kuřecí nudle"] = 99
    with open("menu.json", "w") as f:
        json.dump(menu, f)
    with open("menu.json", "r") as f:
        nactene_menu = json.load(f)
    st.write(nactene_menu)
    if st.toggle("Zobrazit kód", False, key = "kod_9"):
        st.code("""
        with open("menu.json", "r") as f:
            menu = json.load(f)
        menu["kuřecí nudle"] = 99
        with open("menu.json", "w") as f:
            json.dump(menu, f)
        """)

st.markdown("""
---
### Úkol 3
Chcete od uživatele zadat nové jídlo a cenu. \\
Přidejte ho do menu poté, co zmáčknou tlačítko přidat do menu. \\
Ověřte, že se změna provedla správně i v souboru.
""")
if st.toggle("Zobrazit řešení", False, key = "reseni_3"):
    with open("menu.json", "r") as f:
        menu = json.load(f)
    nove_jidlo = st.text_input("Název jídla")
    cena = st.number_input("Cena")
    if st.button("Přidat do menu"):
        menu[nove_jidlo] = cena
        with open("menu.json", "w") as f:
            json.dump(menu, f)
        with open("menu.json", "r") as f:
            nactene_menu = json.load(f)
        st.write(nactene_menu)
    if st.toggle("Zobrazit kód", False, key = "kod_3"):
        st.code("""
        with open("menu.json", "r") as f:
            menu = json.load(f)
        nove_jidlo = st.text_input("Název jídla")
        cena = st.number_input("Cena")
        if st.button("Přidat do menu"):
            menu[nove_jidlo] = cena
            with open("menu.json", "w") as f:
                json.dump(menu, f)
            with open("menu.json", "r") as f:
                nactene_menu = json.load(f)
            st.write(nactene_menu)
        """)

st.markdown("""
---
Důvod proč je třeba toto ukládat je v případě, kdy vlastně budete chtít aby ten člověk uložil nějaké informace někam a pak se k nim mohl dostat znovu. 
To je jeden z nejčastějších způsobů, jak ukládat data a jak s nimi pracovat. 
Jelikož pokud např. bychom chtěli ukládat data do proměnné, tak bychom je ztratili po ukončení programu. \\
Toto si ukážeme úplně nejlépe na tomto příkladu:
### Úkol 4
1. Vytvořte si nový page a pojmenujte ho `lekce_znamky.py`. \\
2. Vytvořte ve své složce nový soubor `znamky.json`. \\
3. Načtěte tento soubor pomocí tohoto příkazu:
```
try:
    with open("znamky.json", "r") as f:
        znamky = json.load(f)
except:
    znamky = {}
```
4. Vypište si tento slovník pomocí `st.write(znamky)`. \\
5. Chcete od uživatele, aby zadal jméno a znamku. \\
6. Po stisknutí tlačítka: Přidejte toto jméno a znamku do slovníku a uložte to do souboru `znamky.json`. \\
7. Ověřte, že se změna provedla správně i v souboru.
8. Zkuste zadat jméno a známku pro 3 lidi a ověřte, že se to uložilo správně.
""")
if st.toggle("Zobrazit řešení", False, key = "reseni_4"):
    try:
        with open("znamky.json", "r") as f:
            znamky = json.load(f)
    except:
        znamky = {}
    jmeno = st.text_input("Jméno")
    znamka = st.number_input("Znamka")
    if st.button("Přidat znamku"):
        znamky[jmeno] = znamka
        with open("znamky.json", "w") as f:
            json.dump(znamky, f)
        with open("znamky.json", "r") as f:
            nactene_znamky = json.load(f)
        st.write(nactene_znamky)
    if st.toggle("Zobrazit kód", False, key = "kod_4"):
        st.code("""
        with open("znamky.json", "w") as f:
            json.dump({}, f)
        with open("znamky.json", "r") as f:
            znamky = json.load(f)
        jmeno = st.text_input("Jméno")
        znamka = st.number_input("Znamka")
        if st.button("Přidat znamku"):
            znamky[jmeno] = znamka
            with open("znamky.json", "w") as f:
                json.dump(znamky, f)
            with open("znamky.json", "r") as f:
                nactene_znamky = json.load(f)
            st.write(nactene_znamky)
        """)

st.subheader("API")
st.markdown("""
Abychom si krátce ukázali, jak funguje výměna dat na webu, tak si ukážeme, jaké data získáme pokud si zavoláme Pokemon API. \\
API je zkratka pro Application Programming Interface a je to způsob, jak můžeme získat data z jiných služeb. \\
V tomto případě si zavoláme službu, která nám vrátí data o pokemonech. \\
Použijeme knihovnu `requests`, která nám umožní zavolat API a získat data. \\
Pojďme si to zkusit.
```
import requests
response = requests.get("https://pokeapi.co/api/v2/pokemon/1")
data = response.json()
st.write(data)
```
""")

import requests
response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
data = response.json()
st.write(data)

st.markdown("""
Na první pohled Vás to může vyděsit ale nic to není. \\
My jsme zatím používali jednoduché slovníky ale v reálu se používají složitější slovníky, které obsahují další slovníky a seznamy (seznamy jsme ještě neprobírali ale budeme). \\
To je způsob, jak se ukládají data na webu a jak se s nimi pracuje. \\
Např. pokud bych si chtěl najít fotku pikachu tak bych napsal:
```
foto = data["sprites"]["front_default"]
st.image(foto)
```
""")
foto = data["sprites"]["front_default"]
st.image(foto)

st.markdown("""
Je tedy vždy velmi důležité se naučit pracovat s dokumentací a s výstupem, který dostanete. \\
Je totiž možné, že budete muset si nechat vyjet výstup z jednoho API a poslat ho do druhého. \\
Například tato API mi vrací vtipy o Chuck Norrisovi.
```
import requests
response = requests.get("https://api.chucknorris.io/jokes/random")
data = response.json()
st.write(data)
```
""")
response = requests.get("https://api.chucknorris.io/jokes/random")
data = response.json()
st.write(data)

st.markdown("""
Když jsem si prostudoval ale dokumentaci na stránkách https://api.chucknorris.io/
tak jsem zjistil, že mohu získat vtipy o Chuck Norrisovi podle kategorie. \\
Potřebuju ale zjisti, jaké kategorie jsou k dispozici. \\
To zjistím pomocí:
```
response = requests.get("https://api.chucknorris.io/jokes/categories")
data = response.json()
st.write(data)
```
""")
response = requests.get("https://api.chucknorris.io/jokes/categories")
data = response.json()
st.write(data)

st.markdown("""
A nyní si mohu vybrat kategorii a získat vtip z této kategorie. \\
Např. kategorie `dev`:
```
response = requests.get("https://api.chucknorris.io/jokes/random?category=music")
data = response.json()
st.write(data)
```
Můžu dokonce tu skupinu dát jako proměnnou pomocí f-stringu takto:
```
kategorie = "dev"
response = requests.get(f"https://api.chucknorris.io/jokes/random?category={kategorie}")
data = response.json()
st.write(data)
""")
response = requests.get("https://api.chucknorris.io/jokes/random?category=music")
data = response.json()
st.write(data)

st.markdown("""
### Úkol 5
Zkuste si zavolat API na stránce https://api.chucknorris.io/ a získat vtip o Chuck Norrisovi. \\
Chcete po uživateli napsat kategorii a získat vtip z této kategorie.\\
Použijte k tomu try-except v případě že uživatel zadá špatnou kategorii. \\
""")
if st.toggle("Zobrazit řešení", False, key = "reseni_5"):
    kategorie = st.text_input("Kategorie")
    try:
        response = requests.get(f"https://api.chucknorris.io/jokes/random?category={kategorie}")
        data = response.json()
        st.write(data)
    except:
        st.write("Špatná kategorie")
    if st.toggle("Zobrazit kód", False, key = "kod_5"):
        st.code("""
        kategorie = st.text_input("Kategorie")
        try:
            response = requests.get(f"https://api.chucknorris.io/jokes/random?category={kategorie}")
            data = response.json()
            st.write(data)
        except:
            st.write("Špatná kategorie")
        """)

st.markdown("""
---
### Úkol 6
Zkuste si podobný úkol na této API
1. Z této adresy získejte a podívejte se jaké páry jsou k dispozici: https://www.frankfurter.app/currencies
2. Vyberte si jeden měnu a nadefinujte tuto měnu pod proměnnou `mena_volby` (nejlépe to bude CZK)
3. Získejte poslední data o směnném kurzu této měny vůči ostatním pomocí: https://www.frankfurter.app/latest?from={mena_volby}
4. Zobrazte si data.
""")
if st.toggle("Zobrazit řešení", False, key = "reseni_6"):
    request = requests.get("https://www.frankfurter.app/currencies")
    data = request.json()
    st.write(data)
    mena_volby = "CZK"
    request = requests.get(f"https://www.frankfurter.app/latest?from={mena_volby}")
    data = request.json()
    st.write(data)
    if st.toggle("Zobrazit kód", False, key = "kod_6"):
        st.code("""
        request = requests.get("https://www.frankfurter.app/currencies")
        data = request.json()
        st.write(data)
        mena_volby = "CZK"
        request = requests.get(f"https://www.frankfurter.app/latest?from={mena_volby}")
        data = request.json()
        st.write(data)
        """)

st.markdown("""
---
### Úkol 7
Zkuste si ještě další úkol s API a zkusíte si zavolat API, které potřebuje klíč.
1. Vytvořte novou page s názvem `lekce_api.py`.
2. Zaregistrujte se na této strance: https://www.alphavantage.co/support/#api-key
3. Získáný API klíč si u vás uložte do proměnné `api_key`.
4. Z této dokumentace použijte tzv endpoint: Daily Adjusted který má podobu: 
```
f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol_firmy}&apikey={api_klic}"
```
5. Po uživateli chcete, aby zadal symbol firmy a získali jste data o této firmě.
6. Vytvořte tlačítko pro získání dat. 
6. Po stisknutí předchozího tlačítka se spustí, try-except, který bude chtít získat data o této firmě a zobrazte je.
7. Pokud máte správně data, zjistěte cenu této akcie ze dne 2024-05-03 pod klíčem "5. adjusted close".
""")
if st.toggle("Zobrazit řešení", False, key = "reseni_7"):
    api_key = "demo"
    symbol_firmy = st.text_input("Symbol firmy")
    if st.button("Získat data", key= "btn_reseni_7"):
        try:
            request = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol_firmy}&apikey={api_key}")
            data = request.json()
            st.write(data)
            cena = data["Time Series (Daily)"]["2024-05-03"]["5. adjusted close"]
            st.write(f"Cena akcie {symbol_firmy} ze dne 2024-05-03 je {cena}")
        except:
            st.write("Špatný symbol firmy")
    if st.toggle("Zobrazit kód", False, key = "kod_7"):
        st.code("""
            api_key = "demo"
            symbol_firmy = st.text_input("Symbol firmy")
            if st.button("Získat data", key= "btn_reseni_7"):
                try:
                    request = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol_firmy}&apikey={api_key}")
                    data = request.json()
                    st.write(data)
                    cena = data["Time Series (Daily)"]["2024-05-03"]["5. adjusted close"]
                    st.write(f"Cena akcie {symbol_firmy} ze dne 2024-05-03 je {cena}")
                except:
                    st.write("Špatný symbol firmy")
            """)


st.markdown("""
---
Práce s API je jenom jedna z mnoho způsobů jak získávat data. \\
Data z API nemusí chodit jenom jako JSON ale také jako XML nebo i dokonce CSV. \\
Pro naše účely nyní jsme si ukázali základní postupy jak získávat data z API a případně umíme pracovat pokud to jsou JSON. 
""")

