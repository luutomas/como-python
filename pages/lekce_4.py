import streamlit as st
st.set_page_config(page_title="COMO Python", page_icon=":snake:", layout="centered", initial_sidebar_state="collapsed")
st.header("Lekce č. 4")

st.subheader("Slovníky")
st.markdown("""
Slovnik je datová struktura, která ukládá data ve formě klíč-hodnota, podobně jako reálný slovník, kde máme hledaný výraz a jeho význam. \\
V Pythonu se slovník zapisuje pomocí složených závorek `{}` a klíč a hodnota se oddělují dvojtečkou `:`. \\
Např. slovník s názvy jídel a jejich cenami může vypadat takto:
```
jidla = { 
    "hamburger": 99,
    "pizza": 149,
    "sendvic": 59
    }
```
Pokud bych chtěl získat cenu pizzy, tak bych napsal:
```
cena_pizza = jidla["pizza"]
st.write(f"Cena pizzy je {cena_pizza}") # Všimněte si f-string v odpovědi
```
Výsledek pak vypíše:
""")

jidla = {
    "hamburger": 99,
    "pizza": 149,
    "sendvič": 59
    }
cena_pizza = jidla["pizza"]
st.write(f"Cena pizzy je {cena_pizza}")

st.markdown("""
---
Pokud bych chtěl přidat nové jídlo do seznamu, tak bych napsal:
```
jidla = {
    "hamburger": 99,
    "pizza": 149,
    "sendvič": 59
    }
jidla["pho"] = 150
st.write(jidla)
```
Výsledek pak vypíše:
""")

jidla["pho"] = 150
st.write(jidla)

st.markdown(""" 
---
Mezi další důležité funkce, které můžete s slovníky provádět patří:
| Funkce | Popis |
|--------|-------|
| `keys()` | Vrátí seznam klíčů |
| `values()` | Vrátí seznam hodnot |
| `items()` | Vrátí seznam klíč-hodnota |
| `get()` | Vrátí hodnotu klíče |
| `del` | Smaže klíč a hodnotu |
| `clear()` | Smaže celý slovník |
| `pop()` | Vrátí hodnotu klíče a smaže klíč |
---
Např. pokud bych chtěl zjistit všechny jídla, které mám v seznamu, tak bych napsal:
```
seznam_jidel = jídla.keys()
st.write(seznam_jidel)
```
A dostanu seznam jidel (hlouběji se na seznamy podíváme později):
""")
jidla = {
    "hamburger": 99,
    "pizza": 149,
    "sendvič": 59
    }
seznam_jidel = jidla.keys()
st.write(seznam_jidel)

st.markdown("""
---
Pokud bych chtěl seznam cen jídel, tak bych napsal:
```
jidla = {
    "hamburger": 99,
    "pizza": 149,
    "sendvič": 59
    }
seznam_cen = jidla.values()
st.write(seznam_cen)
```
A výsledek
""")
jidla = {
    "hamburger": 99,
    "pizza": 149,
    "sendvič": 59
    }
seznam_cen = jidla.values()
st.write(seznam_cen)

st.markdown("""
---
Pokud bych chtěl získat seznam jídel a cen, tak bych napsal:
```
jidla = {
    "hamburger": 99,
    "pizza": 149,
    "sendvič": 59
    }
seznam_jidel_a_cen = jidla.items()
st.write(seznam_jidel_a_cen)
```
A dostanu dvojice klíč-hodnota (hlouběji se na seznamy a n-tice podíváme později):
""")
jidla = {
    "hamburger": 99,
    "pizza": 149,
    "sendvič": 59
    }
seznam_jidel_a_cen = jidla.items()
st.write(seznam_jidel_a_cen)

st.markdown("""
---
Pokud bych chtěl znát hodnotu ceny ale chci tam také specifikovat, co se stane, když klíč není v seznamu, tak bych napsal:
```
jidla = {
    "hamburger": 99,
    "pizza": 149,
    "sendvič": 59
    }
pizza = jidla.get("pizza")
st.write(f"Cena pizzy je {pizza}")

kebab = jidla.get("kebab", 100)
st.write(f"Cena pizzy je {kebab}")
```
""")
jidla = {
    "hamburger": 99,
    "pizza": 149,
    "sendvič": 59
    }
pizza = jidla.get("pizza")
st.write(f"Cena pizzy je {pizza}")


kebab = jidla.get("kebab", 100)
st.write(f"Cena kebabu je {kebab}")

st.markdown("""
----
Pokud bych chtěl smazat záznam tak můžu použít dva způsoby:
```
jidla = {
    "hamburger": 99,
    "pizza": 149,
    "sendvič": 59
    }
del jidla["pizza"]
st.write(jidla)
```
""")
jidla = {
    "hamburger": 99,
    "pizza": 149,
    "sendvič": 59
    }
del jidla["pizza"]
st.write(jidla)

st.markdown("""
nebo pomocí:
```
jidla = {
    "hamburger": 99,
    "pizza": 149,
    "sendvič": 59
    }
jídla.pop("sendvič")
st.write(jídla)
```
""")
jidla = {
    "hamburger": 99,
    "pizza": 149,
    "sendvič": 59
    }
jidla.pop("sendvič")
st.write(jidla)

st.markdown("""
----
Pojďme si to procvičit na příkladu. \\
Představte si, že máme dneska slovník s jídly a jejich cenami:
```
poledni_menu = {
    "hamburger": 99,
    "pizza": 149,
    "sendvič": 59,
    "kebab": 89,
    "pho": 79
    "řízek": 119,
    "knedlo-vepřo-zelo": 139
    }
```
""")

st.markdown("""
#### Úkol 1
Pomocí `[]` získejte cenu sendviče a vypište ji.

#### Úkol 2
Pomocí `get()` získejte cenu steaku a pokud to nenajde tak vypište 500

#### Úkol 3
Pomocí [] přidejte do menu položku kuřecí nudle za 99

#### Úkol 4
Vypište mi všechny položky v menu tedy názvy jídel.

#### Úkol 5
Vypište mi všechny ceny v menu.

#### Úkol 6
Vypište mi všechny položky a ceny v menu.

#### Úkol 7
Smažte položku hamburger z menu.

""")

st.subheader("JSON")
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
### Úkol 8
Uložte tento slovník do souboru `menu.json` a poté ho načtěte a vypište.

### Úkol 9
Přidejte do menu položku kuřecí nudle za 99 a uložte to zpět do souboru `menu.json`

### Úkol 10
Podívejte do `menu.json`, že tam kuřecí nudle jsou.
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
My jsme zatím používali jednoduché slovníky ale v reálu se používají složitější slovníky, které obsahují další slovníky a seznamy. \\
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
Vždy se snažte zjistit, co vám API vrací a jak s tím můžete pracovat.
""")