import streamlit as st
st.set_page_config(page_title="COMO Python", page_icon=":snake:", layout="centered", initial_sidebar_state="collapsed")
st.header("Lekce č. 3")

st.subheader("Pravda a Nepravda")
st.markdown("""
Pokud si pamatujete z předešlé lekce, tak máme něco co se nazývá **Pravda** a **Nepravda** neboli **True** a **False**. \\
Pravda a Nepravda jsou základy počítačů, na kterých je postavený celý svět programování, které je postavené na podmínkování. \\
Nyni se podíváme více, co to vlastně znamená. 

Pravda označuje, že něco je pravdivé a Nepravda, že něco je nepravdivé. \\
K porovnávání se používají následující znaménka:
- `==` znamená rovná se
- `!=` znamená nerovná se
- `>` znamená větší než
- `<` znamená menší než
- `>=` znamená větší nebo rovno
- `<=` znamená menší nebo rovno

K porovnávní jsou třeba vždy 2 strany, 1 operátor a výsledek je vždy Pravda nebo Nepravda.
| 1 strana | operátor | 2 strana | Výsledek |
|----------|----------|----------|----------|
| 2        | ==       | 2        | Pravda   |
| 2        | !=       | 2        | Nepravda  |
| 5        | >        | 2        | Pravda   |
| 2        | <        | 5        | Pravda   |
| 5        | >=       | 5        | Pravda   |
| Tom      | !=       | ""       | Pravda   |
| Tom      | !=       | None     | Pravda   |
| 2        | !=       | None     | Pravda   |

Ještě oprášíme základní teorii logiky, což jsou `AND (A)` a `OR (NEBO)`. \\
`AND` neboli `A` znamená, že obě strany musí být pravdivé, aby byl výsledek pravdivý. \\
`OR` neboli `OR` znamená, že alespoň jedna strana musí být pravdivá, aby byl výsledek pravdivý.

Pojďme si to zkusit na příkladech
- Je Pravda, že 2 je větší než 1 a 2 je menší než 3?
- Je Pravda, že 2 je větší než 1 a 2 je větší než 3?
- Je Pravda, že 2 je menší než 1 nebo 2 je větší než 3?
- Je Pravda, že 2 je větší než 1 nebo 2 je menší než 3?
```
pravda = 2 > 1 and 2 < 3
st.write(pravda)
pravda = 2 > 1 and 2 > 3
st.write(pravda)
pravda = 2 < 1 or 2 > 3
st.write(pravda)
pravda = 2 > 1 or 2 < 3
st.write(pravda)
```
""")
pravda = (2 > 1) and (2 < 3)
st.write(pravda)
pravda = (2 > 1) and (2 > 3)
st.write(pravda)
pravda = (2 < 1) or (2 > 3)
st.write(pravda)
pravda = 2 > 1 or 2 < 3
st.write(pravda)


st.subheader("Podmínka if-else")
st.markdown("""
Podmínka je základním stavebním kamenem programování a navazuje na Pravdu/Nepravdu. \\
Podmínka je něco, co se vykonává, pokud je splněna určitá podmínka. \\
Podmínka se zapisuje pomocí klíčového slova `if` a `else`. \\
Pokud je podmínka splněna, vykoná se kód v `if` a pokud není, vykoná se kód v `else`. \\
Podmínka se zapisuje takto:
```
if podmínka:
    kód
else:
    kód
```
Například: \\
**POKUD (IF)** napsané číslo je větší než 5, řeknu, že vložené číslo je větší než 5 \\
**JINAK (ELSE)** řeknu, že číslo je menší než 5 vy vypadalo takto:
```
if cislo > 5:
    st.write("Číslo je větší než 5")
else:
    st.write("Číslo je menší nebo rovno 5")
```

Zkusíme si to rovnou se vstupem od uživatele na čísla a celý kód vypadá takto:
```
cislo = st.number_input("Zadejte číslo", key = "cislo_1")
if cislo > 5:
    st.write("Číslo je větší než 5")
else:
    st.write("Číslo je menší nebo rovno 5")
```
""")

cislo = st.number_input("Zadejte číslo", key = "cislo_1")
if cislo > 5:
    st.write("Číslo je větší než 5")
else:
    st.write("Číslo je menší nebo rovno 5")

st.markdown("""
---
Zkuste totéž provést s tím, že uživatel vám zadá věk a vy mu řeknete, zda je plnoletý nebo ne.
""")

if st.toggle("Zobrazit řešení", key = "toggle_1"):
    vek = st.number_input("Zadejte věk", key = "vek_1")
    if vek >= 18:
        st.write("Jste plnoletý")
    else:
        st.write("Nejste plnoletý")

    if st.toggle("Zobrazit kód", key = "toggle_2"):
        st.code("""
        vek = st.number_input("Zadejte věk")
        if vek >= 18:
            st.write("Jste plnoletý")
        else:
            st.write("Nejste plnoletý")
        """)

st.markdown("""
---
Podmínky mohou mít ale více větví, než jen `if` a `else` a to pomocí klíčového slova `elif`. \\
Například pokud chceme zjistit, zda je číslo menší než 5, rovno 5 nebo větší než 5, můžeme napsat následující:
```
cislo = st.number_input("Zadejte číslo", key = "cislo_2")
if cislo < 5:
    st.write("Číslo je menší než 5")
elif cislo == 5:
    st.write("Číslo je rovno 5")
else:
    st.write("Číslo je větší než 5")
```
Výsledek:
""")
cislo = st.number_input("Zadejte číslo", key = "cislo_2")
if cislo < 5:
    st.write("Číslo je menší než 5")
elif cislo == 5:
    st.write("Číslo je rovno 5")
else:
    st.write("Číslo je větší než 5")

st.markdown("""
---
Zkuste totéž provést s tím, že uživatel vám zadá věk a vy mu řeknete, zda je plnoletý, je mu akorát 18 nebo není plnoletý.
""")
if st.toggle("Zobrazit řešení", key = "toggle_3"):
    vek = st.number_input("Zadejte věk", key = "vek_2")
    if vek > 18:
        st.write("Jste plnoletý")
    elif vek == 18:
        st.write("Je vám akorát 18")
    else:
        st.write("Nejste plnoletý")

    if st.toggle("Zobrazit kód", key = "toggle_4"):
        st.code("""
        vek = st.number_input("Zadejte věk", key = "vek_2")
        if vek > 18:
            st.write("Jste plnoletý")
        elif vek == 18:
            st.write("Je vám akorát 18")
        else:
            st.write("Nejste plnoletý")
        """)

st.markdown("""
---

Podmínkování je základním stavebním kamenem programování a je důležité si ho osvojit. \\
Podmínky se dají kombinovat a skládat dohromady a vytvářet tak složité programy. \\
Pro prvotní nástřel těchto algoritmů se doporučuje vzít tužku, papír a nakreslit si strom akcí, co chcete udělat s podmínkami.

Nejtěžší je uchopit problém a rozdělit ho na menší části, které se dají řešit jednoduše pomocí podmínek. \\

Zkusíme si pár příkladů na procvičení:
"""
)

st.markdown("""
### Úkol 1
Chcete aby uživatel zadal dvě čísla a porovnal je.
Výsledek bude vypsat, zda jsou čísla stejná, první je větší než druhé nebo druhé je větší než první.
""")
if st.toggle("Zobrazit podobu řešení", key="reseni_1"):
    prvni_cislo = st.number_input("Zadejte první číslo", key="prvni_cislo")
    druhe_cislo = st.number_input("Zadejte druhé číslo", key="druhe_cislo")
    if prvni_cislo == druhe_cislo:
        st.write("Čísla jsou stejná")
    elif prvni_cislo > druhe_cislo:
        st.write("První číslo je větší než druhé")
    else:
        st.write("Druhé číslo je větší než první")

    if st.toggle("Zobrazit kód", key="kod_3"):
        st.code("""
        prvni_cislo = st.number_input("Zadejte první číslo", key="prvni_cislo")
        druhe_cislo = st.number_input("Zadejte druhé číslo", key="druhe_cislo")
        if prvni_cislo == druhe_cislo:
            st.write("Čísla jsou stejná")
        elif prvni_cislo > druhe_cislo:
            st.write("První číslo je větší než druhé")
        else:
            st.write("Druhé číslo je větší než první")
        """)

st.markdown("""
---
### Úkol 2
Chcete aby uživatel zadal dvě čísla a porovnal je.
Výsledek bude třeba vypsat tak, že uvidíme jaké čísla byla zadaná a jaké z nich je větší
""")
if st.toggle("Zobrazit podobu řešení", key="reseni_2"):
    prvni_cislo = st.number_input("Zadejte první číslo", key="prvni_cislo_2")
    druhe_cislo = st.number_input("Zadejte druhé číslo", key="druhe_cislo_2")
    if prvni_cislo == druhe_cislo:
        st.write("Čísla jsou stejná")
    elif prvni_cislo > druhe_cislo:
        st.write(f"{prvni_cislo} je větší než {druhe_cislo}")
    else:
        st.write(f"{druhe_cislo} číslo je větší než {druhe_cislo}")

    if st.toggle("Zobrazit kód", key="kod_4"):
        st.code("""
        prvni_cislo = st.number_input("Zadejte první číslo", key="prvni_cislo_2")
        druhe_cislo = st.number_input("Zadejte druhé číslo", key="druhe_cislo_2")
        if prvni_cislo == druhe_cislo:
            st.write("Čísla jsou stejná")
        elif prvni_cislo > druhe_cislo:
            st.write(f"{prvni_cislo} je větší než {druhe_cislo}")
        else:
            st.write(f"{druhe_cislo} číslo je větší než {druhe_cislo}")
        """)

st.markdown("""
---
### Úkol 3
Chcete aby uživatel zadal vám počet bodů od 0 do 100 a vy mu vypíšete, jaké má hodnocení.
- 0 - 60 bodů: Nedostatečný
- 61 - 70 bodů: Dostatečný
- 71 - 80 bodů: Dobrý
- 81 - 90 bodů: Chvalitebný
- 91 - 100 bodů: Výborný
""")

st.markdown("""
---
### Úkol 4
Chcete aby uživatel zadal vám počet bodů od 0 do 100 a také počet ocenění, které získal a vy mu vypíšete, zda je přijat nebo ne.
Podmínky přijetí jsou následující:
- 0 - 60 bodů A aspoň 20 ocenění
- 61 - 70 bodů A aspoň 5 ocenění
- 71 - 80 bodů A aspoň 2 ocenění
- 81 - 90 bodů A aspoň 1 ocenění
- 91 - 100 bodů A aspoň 0 ocenění
""")

st.markdown("""
### Úkol 5
Chcete aby uživatel zadal jakkýkoliv rok větší než 0 a vy mu vypíšete, zda je rok přestupný nebo ne.
Rok je přestupný pokud:
- je dělitelný 4
- pokud je dělitelný 100 tak musí být dělitelný 400
""")

st.markdown("""
---
Tím, že jsme se naučili podmínky, tak můžeme se naučit další komponenty, které na tom byly závislé:
| Komponenta | Popis |
|------------|-------|
| st.button() | Tlačítko, které může být stisknuto |
| st.checkbox() | Zaškrtávací políčko |
| st.toggle() | Přepínač |
| st.download_button() | Tlačítko pro stažení souboru |


Tyto komponenty se používají k interakci s uživatelem a mohou být použity v kombinaci s podmínkami.
Např. pokud uživatel stiskne tlačítko, tak se sečtu dvě čísla a vypíšu výsledek:
```
prvni_cislo = st.number_input("Zadejte první číslo", key="prvni_cislo_3")
druhe_cislo = st.number_input("Zadejte druhé číslo", key="druhe_cislo_3")
if st.button("Sečti"):
    vysledek = prvni_cislo + druhe_cislo
    st.write(f"Výsledek je {vysledek}")
```
""")

prvni_cislo = st.number_input("Zadejte první číslo", key="prvni_cislo_3")
druhe_cislo = st.number_input("Zadejte druhé číslo", key="druhe_cislo_3")
if st.button("Sečti", key = "secti"):
    vysledek = prvni_cislo + druhe_cislo
    st.write(f"Výsledek je {vysledek}")

st.markdown("""
---
Podobně funguje i `st.checkbox()` a `st.toggle()`, které se používají k výběru nějaké možnosti.
Např. pokud uživatel zaškrtne políčko muž, tak se mu zobrazí výsledek že je muž:
```
if st.checkbox("Muž"):
    st.write("Jste muž")
else:
    st.write("Jste žena")
```
""")
if st.checkbox("Muž"):
    st.write("Jste muž")
else:
    st.write("Jste žena")

st.markdown("""
---
Zde `st.toggle()`:
""")
if st.toggle("Muž"):
    st.write("Jste muž")
else:
    st.write("Jste žena")

st.markdown("""
---
Pojďme si to zkusit na příkladu:
### Úkol 6
Chcete aby uživatel zadal věk a po stisknutí tlačítka "Jsem plnoletý?" se mu vypíše, zda je plnoletý nebo ne.

### Úkol 7
Chcete aby uživatel zadal jméno a příjmeni a měl tam st.toggle na pohlaví a po stisknutí tlačítka vypíšete, jaké jméno a příjmení a pohlaví zadal ve formě \\
`f"Jméno: {jmeno}, Příjmení: {prijmeni}, Pohlaví: {pohlavi}"`
""")
