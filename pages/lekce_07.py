import streamlit as st
st.set_page_config(page_title="COMO Python", page_icon=":snake:", layout="centered", initial_sidebar_state="collapsed")
st.header("Lekce č. 7")

st.subheader("Cykly")
st.markdown("""
Cykly jsou důležitým prvkem programování, které sdílí všechny jazyky programování. \\
Cyklus je kód, který se opakuje dokud je splněná určitá podmínka. \\
V Pythonu máme dva druhy cyklů: `for` a `while`. \\
Cyklus `for` se používá, když známe počet opakování. \\
Cyklus `while` se používá, když neznáme počet opakování.

Např. cyklus `for` může vypadat takto:
```
for kazde_jmeno in ["Adam", "Eva"]:
    st.write(f"Zdravím {kazde_jmeno}")
```
""")

for kazde_jmeno in ["Adam", "Eva"]:
    st.write(f"Zdravím {kazde_jmeno}")

st.markdown("""
Věděli jsme, že máme dvě jména, takže jsme použili cyklus `for`. \\
Co když ale víme, že cyklus chceme opakovat 10, 20, 1000 krát? Nebudeme přeci vypisovat sami seznam ručně ne? Že? \\
V tom případě použijeme cyklus `for` s funkcí `range()`. \\
Funkce `range()` má různé parametry:
`range(start, stop, step)`
| Parametr | Popis |
|----------|-------|
| start | Počáteční hodnota VČETNĚ|
| stop | Koncová hodnota BEZ|
| step | Krok, o který se bude zvyšovat |

Tedy pokud chceme vypsat čísla od 0 do 9, tak napíšeme: `range(0, 10, 1)`. \\
Pokud chceme vypsat všechna sudá čísla od 0 do 9, tak napíšeme: `range(0, 10, 2)`. \\
Pokud chceme vypsat všechna lichá čísla od 0 do 9, tak napíšeme: `range(1, 10, 2)`. \\
Například tedy budeme chtít opakovat nějaký cyklus 10x:
```
for kazde_cislo in range(5):
    st.write(f"Opakuji {kazde_cislo}.")
```
A výsledek bude:
""")
for kazde_cislo in range(5):
    st.write(f"Opakuji {kazde_cislo}.")


st.markdown("""
---
Pojďme si to zkusit na nějakém příkladu. 

### Úkol 1
Chcete pozdravit 3x `Ahoj!!`. 

### Úkol 2
Chcete aby uživatel zadal číslo a pomocí cyklu `for` vytiskněte všechna čísla od 0 do zadaného čísla.

### Úkol 3
Máte seznam jmen [`Tomáš`, `Jan`, `Petr`, `Jana`, `Eva`]. 
Pozdravte každého zvlášť. \\

### Úkol 4
Máte seznam jmen [`Tomáš`, `Jan`, `Petr`, `Jana`, `Eva`]. \\
Pozdravte slečny: `Dobrý den paní` a pane: `Dobrý den pane`. \\
Nápověda: `if`.
""")

st.markdown("""
---
Cyklus `while` se používá, když neznáme počet opakování. \\
Cyklus `while` se opakuje dokud je splněná podmínka. \\
Např. cyklus `while` může vypadat takto:
```
cislo = 0
while cislo < 5:
    st.write(f"Opakuji {cislo}.")
    cislo += 1
```
""")

cislo = 0
while cislo < 5:
    st.write(f"Opakuji {cislo}.")
    cislo += 1

st.markdown("""
Důležité jsou dvě věci: 
- `cislo = 0` je počáteční hodnota, která se musí nastavit
- `cislo += 1` neboli `cislo = cislo + 1` zvyšuje samo o sobě to číslo o 1, jinak by se cyklus nikdy nezastavil.

Pojďme si to zkusit na nějakém příkladu.
### Úkol 5
Chcete aby uživatel zadal číslo a pomocí cyklu `while` vytiskněte všechna čísla od 0 do zadaného čísla.

### Úkol 6
Chcete aby uživatel zadal číslo a pomocí cyklu `while` vytiskněte všechna sudá čísla od 0 do zadaného čísla.
""")

st.markdown("""
---
Oba dva cykly můžeme ukončit pomocí `break`. \\
`break` je klíčové slovo, které ukončí cyklus. \\
Např. cyklus `for` může vypadat takto:
```
for kazde_cislo in range(10):
    if kazde_cislo == 3:
        break
    st.write(f"Opakuji {kazde_cislo}.")
```
""")
for kazde_cislo in range(5):
    if kazde_cislo == 3:
        break
    st.write(f"Opakuji {kazde_cislo}.")

st.markdown("""
Všimněte si, že cyklus se zastavil na 3, protože tam bylo `if kazde_cislo == 3: break`. \\
Vytisklo se ale jenom do 2, protože se nejprve porovná a pak se vytiskne. \\
Tedy ono se zastaví na 3, ale vytiskne se jenom 0, 1, 2.

---

S `while` cyklem je to stejné:
```
cislo = 0
while cislo < 5:
    if cislo == 3:
        break
    st.write(f"Opakuji {cislo}.")
    cislo += 1
```
""")

cislo = 0
while cislo < 5:
    if cislo == 3:
        break
    st.write(f"Opakuji {cislo}.")
    cislo += 1

st.markdown("""
---
Pojďme si to zkusit na nějakém příkladu.
### Úkol 7
Chcete aby uživatel zadal číslo a pomocí cyklu `for` vytiskněte všechna čísla od 0 do zadaného čísla pokud nenarazíte na číslo 5. \\
To pak ukončíte cyklus pomocí `break`.

### Úkol 8
Máte seznam jmen [`Tomáš`, `Jan`, `Petr`, `Jana`, `Eva`]. \\
Pozdravte každého zvlášť, ale pokud narazíte na jméno `Petr`, tak ukončete cyklus pomocí `break`.
""")

st.markdown("""
---
Cyklus se často používají i se slovníkem, aby člověk dokázal vytáhnout lépe informace. \\
Např. slovník s názvy jídel a jejich cenami může vypadat takto:
```
jidla = { 
    "hamburger": 99,
    "pizza": 149,
    "sendvic": 59
    }
```
Pokud bych chtěl pro každé jídlo vypsat cenu, tak bych napsal:
```
for kazde_jidlo in jidla:
    st.write(f"Cena {kazde_jidlo} je {jidla[kazde_jidlo]} Kč.")
```
""")

jidla = { 
    "hamburger": 99,
    "pizza": 149,
    "sendvic": 59
    }
for kazde_jidlo in jidla:
    st.write(f"Cena {kazde_jidlo} je {jidla[kazde_jidlo]} Kč.")

st.markdown("""
Může ale nastat, že budu potřebovat každé jídlo zdražit o 20% tedy vynásobit cenu s 1.2. \\
V tom případě bych napsal:
```
for kazde_jidlo in jidla:
    jidla[kazde_jidlo] = jidla[kazde_jidlo] * 1.2
""")

jidla = { 
    "hamburger": 99,
    "pizza": 149,
    "sendvic": 59
    }
st.write(f"Před zdražením {jidla}")
for kazde_jidlo in jidla:
    jidla[kazde_jidlo] = round(jidla[kazde_jidlo] * 1.2,2)
st.write(f"Po zdražením {jidla}")

st.markdown("""
---
Pojďme si to zkusit na nějakém příkladu.
### Úkol 9
Máte slovník s názvy jídel a jejich cenami:
```
jidla = { 
    "hamburger": 99,
    "pizza": 149,
    "sendvic": 59
    }
```
Zdražte každé jídlo o 30% a vypište nové ceny.
""")
