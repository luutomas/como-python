import streamlit as st

st.set_page_config(page_title="COMO Python", page_icon=":snake:", layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
## Git a Github
Abychom mohli naší aplikaci sdílet s ostatními, je potřeba ji nahrát na internet. K tomu využijeme službu Github.
Github je postavené na Gitu, což je verzovací systém. Git nám umožňuje sledovat změny v kódu, vytvářet nové větve, spojovat je a mnoho dalšího.
My se tady budeme zabývat pouze základními příkazy, které nám pomohou nahrát náš kód na Github.

### Instalace Gitu
1. Stáhněte si instalační soubor z [Git](https://git-scm.com/downloads)
2. Spusťte instalační soubor a postupujte podle pokynů

### Vytvoření účtu na Github
1. Otevřete si stránku github.com

Každé prvotní nastavení může být trochu jiné, ale základní princip je stejný.
1. Nastavíte si jméno a email
2. Zahajíte repozitář - `git init`
3. Přidáte soubory do sledování - `git add název_souboru`
4. Zapišete změny - `git commit -m "popis změn"`
5. Přidejte si odkaz na repozitář - `git remote add origin odkaz_na_repozitář` (stačí jednou)
6. Nahrajte změny na Github - `git push`

### Vytvoření repozitáře
1. Klikněte na tlačítko "New"
2. Zadejte název repozitáře
3. Klikněte na tlačítko "Create repository"

### Nahrání kódu na Github
1. Otevřete si terminál ve visual studio code ve složce kde máte kód
2. Nastavte si jméno a email
```
git config --global user.name "vaše jméno na githubu"
git config --global user.email "emailova adresa na githubu"
```
3. Zahajte repozitář
```
git init
```
4. Přidejte soubory do sledování
```
git add název_souboru
```
5. Zapište změny
```
git commit -m "popis změn"
```
6. Přidejte si odkaz na repozitář
```
git remote add origin odkaz_na_repozitář
```
7. Nahrajte kód na Github
```
git push -u origin main
```

### Nejčastější příkazy
- `git status` - zobrazí stav repozitáře
- `git add název_souboru` - přidá soubor do sledování
- `git commit -m "popis změn"` - zapiše změny
- `git push` - nahraje změny na Github
- `git pull` - stáhne změny z repozitáře
""")