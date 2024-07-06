import streamlit as st
import time
import json

st.set_page_config(page_title="COMO Python", page_icon="icon.png", layout="centered")

st.header("Lekce č. 9")

st.subheader("st.form")
st.markdown("""
Streamlit form je další skvělou komponentou, která nám zlepší výkon naší apliace. \\
Streamlit je nastavený tak, aby při každé iteraci znovu napočítal a vykreslil celou stránku. \\
To může být pro některé případy nechtěné, protože to může zpomalovat a tím vytvořit špatný uživatelský zážitek.

Formuláře jsou fundamentální součástí webu. Na formulářích je založena většina interakce mezi uživatelem a webovou stránkou. \\
Vy jako uživatel defakto vždycky posíláte data ve formě formuláře aby je pak aplikace zpracovala.

Ve streamlitu můžeme formuláře vytvářet pomocí `st.form` a indikují se takto:
```
with st.form(key = "formular_na_registraci"):
    jmeno = st.text_input("Jméno")
    prijmeni = st.text_input("Příjmení")
    email = st.text_input("Email")
    
    if st.form_submit_button("Registrovat"):
        st.write(f"Jméno: {jmeno}")
        st.write(f"Příjmení: {prijmeni}")
        st.write(f"Email: {email}")
```
Všimněte si následujících věci:
- inicializujeme formulář pomocí `with`
- každý formulář musí mít st.form_submit_button, který po zmáčknutí zpracuje formulář

Výsledek horního kódu je takovýto formulář: 
""")
with st.form(key = "formular_na_registraci"):
    jmeno = st.text_input("Jméno")
    prijmeni = st.text_input("Příjmení")
    email = st.text_input("Email")
    
    if st.form_submit_button("Registrovat"):
        st.write(f"Jméno: {jmeno}")
        st.write(f"Příjmení: {prijmeni}")
        st.write(f"Email: {email}")

st.markdown("""
Pro práci se st.form je mnoho užitečných funcionalit, které se nyní ukážeme. \\
Nejdřív se podíváme na parametry pro st.form:

| Název | Popis |
| ----- | ------ |
| **key** | klíč, který je třeba vždy vyplnit|
| clear_on_submit | pokud je True, tak se formulář vyčistí po odeslání |
| border | pokud je True, tak se zobrazí ohraničení formuláře |


Pak poté pro st.form_submit_button:
| Název | Popis |
| ----- | ------ |
| **label** | název tlačítka |
| **help* | nápověda k tlačítku |
| type | typ tlačítka, nastavíme pomocí `type = "primary"` nebo `type = "secondary"` |
| disabled | pokud je True, tak se tlačítko zablokuje |
| use_container_width | pokud je True, tak se tlačítko přizpůsobí šířce kontejneru |
| on_click | funkce, která se spustí po kliknutí na tlačítko |
| args | argumenty pro funkci on_click |
| kwargs | keyword argumenty pro funkci on_click |


Pokud bych tedy trochu upravil náš předchozí kód, tak by to mohlo vypadat takto:
```
with st.form(key = "formular_na_registraci"):
    jmeno = st.text_input("Jméno")
    prijmeni = st.text_input("Příjmení")
    email = st.text_input("Email")
    
    if st.form_submit_button("Registrovat", help = "Tlačítko pro odeslání formuláře", type = "primary", use_container_width = True):
        st.write(f"Jméno: {jmeno}")
        st.write(f"Příjmení: {prijmeni}")
        st.write(f"Email: {email}")
```
""")
with st.form(key = "formular_na_registraci_upraveny"):
    jmeno = st.text_input("Jméno")
    prijmeni = st.text_input("Příjmení")
    email = st.text_input("Email")
    
    if st.form_submit_button("Registrovat", help = "Tlačítko pro odeslání formuláře", type = "primary", use_container_width = True):
        st.write(f"Jméno: {jmeno}")
        st.write(f"Příjmení: {prijmeni}")
        st.write(f"Email: {email}")

st.markdown("---")
st.subheader("Další možnosti pro zlepšení formuláře")
st.markdown("""
### st.success, st.error, st.warning
Při práci nejen s formuláři, ale i s celou aplikací můžeme využít tři funkce, které nám pomohou zlepšit uživatelský zážitek. \\
Tyto funkce jsou `st.success`, `st.error` a `st.warning`, které ukazují uživateli zprávu, která je buď úspěšná, chybová nebo varovná. \\
Příklady:
```
st.success("Text byl úspěšně uložen")
st.error("Chyba při ukládání textu")
st.warning("Pozor, text se neshoduje")
```
""")

st.success("Text byl úspěšně uložen")
st.error("Chyba při ukládání textu")
st.warning("Pozor, text se neshoduje")

st.markdown("""
Pokud bych tedy ještě vylepšil předchozí formulář, tak by to mohlo vypadat takto:
```
with st.form(key = "formular_na_registraci_upraveny_se_success"):
    jmeno = st.text_input("Jméno")
    prijmeni = st.text_input("Příjmení")
    email = st.text_input("Email")
    
    if st.form_submit_button("Registrovat", help = "Tlačítko pro odeslání formuláře", type = "primary", use_container_width = True):
        st.success("Formulář byl úspěšně odeslán")
        st.write(f"Jméno: {jmeno}")
        st.write(f"Příjmení: {prijmeni}")
        st.write(f"Email: {email}")
```
Kdy po odeslání se zobrazí zpráva, že formulář byl úspěšně odeslán.
""")
with st.form(key = "formular_na_registraci_upraveny_se_success", clear_on_submit = True):
    jmeno = st.text_input("Jméno")
    prijmeni = st.text_input("Příjmení")
    email = st.text_input("Email")
    
    if st.form_submit_button("Registrovat", help = "Tlačítko pro odeslání formuláře", type = "primary", use_container_width = True):
        st.success("Formulář byl úspěšně odeslán")
        st.write(f"Jméno: {jmeno}")
        st.write(f"Příjmení: {prijmeni}")
        st.write(f"Email: {email}")

st.markdown("""
### st.rerun()
Už jste si jistě všimli, že když odesíláte formulář, tak se celá aplikace znovu nespustí a zůstane vám tam poslední výsledek. \\
Pokud byste chtěli, aby se po odeslání vymazal ale nejen ty pole nahoře ale i ta hláška, musíme použít funkci `st.rerun()`, která znovu spustí celou aplikaci. \\
Pozor ale, to se aktivuje instantně takže se stane, že ani neuvidíme tu hlášku po odeslání. \\
Abychom to mohli použít, tak musíme importovat knihovnu `time` a použít funkci `time.sleep(1)`, která počká 1 nebo x sekund, co budeme specifikovat, než se spustí celá aplikace. \\
Příklad:
```
import time
with st.form(key = "formular_na_registraci_upraveny_se_success", clear_on_submit = True):
    jmeno = st.text_input("Jméno")
    prijmeni = st.text_input("Příjmení")
    email = st.text_input("Email")
    
    if st.form_submit_button("Registrovat", help = "Tlačítko pro odeslání formuláře", type = "primary", use_container_width = True):
        st.success("Formulář byl úspěšně odeslán")
        st.write(f"Jméno: {jmeno}")
        st.write(f"Příjmení: {prijmeni}")
        st.write(f"Email: {email}")
        time.sleep(3)
        st.rerun()
```
""")

with st.form(key = "formular_na_registraci_upraveny_se_success_a_rerun", clear_on_submit = True):
    jmeno = st.text_input("Jméno")
    prijmeni = st.text_input("Příjmení")
    email = st.text_input("Email")
    
    if st.form_submit_button("Registrovat", help = "Tlačítko pro odeslání formuláře", type = "primary", use_container_width = True):
        st.success("Formulář byl úspěšně odeslán")
        st.write(f"Jméno: {jmeno}")
        st.write(f"Příjmení: {prijmeni}")
        st.write(f"Email: {email}")
        time.sleep(3)
        st.rerun()

st.markdown("""
## Shrnutí a úkol
Naučili jsme se pracovat s formuláři a ukázali i několik užitečných funkcí, které nám pomohou zlepšit uživatelský zážitek. \\
Pojďme toto všechno nyní využít v praxi a vytvořit aplikaci, která bude mít formulář a bude ukládat data do JSONu. \\

### Úkol 1
1. Vytvořte formulář s následujícími vstupy:
    - Pořadové číslo
    - Jméno
2. Vytvořte tlačítko, které bude typ primary a na celou šířku kontejneru.
3. Po odeslání formuláře se zobrazí zpráva, že formulář byl úspěšně odeslán zobrazí se pořadové číslo a jméno.
4. Po odeslání použijte time.sleep(5) a st.rerun() pro vymazání formuláře.
""")
if st.toggle("Ukázat řešení", key = "ukol_1"):
    with st.form(key = "ukol_1"):
        cislo = st.number_input("Pořadové číslo", step = 1)
        jmeno = st.text_input("Jméno")
        
        if st.form_submit_button("Odeslat", type = "primary", use_container_width = True):
            st.success(f"Formulář byl úspěšně odeslán: Pořadové číslo: {cislo}, Jméno: {jmeno}")
            st.write(f"Pořadové číslo: {cislo}")
            st.write(f"Jméno: {jmeno}")
            time.sleep(5)
            st.rerun()
    if st.toggle("Ukázat kód"):
        st.code("""
    with st.form(key = "ukol_1"):
        cislo = st.number_input("Pořadové číslo", step = 1)
        jmeno = st.text_input("Jméno")
        
        if st.form_submit_button("Odeslat", type = "primary", use_container_width = True):
            st.success(f"Formulář byl úspěšně odeslán: Pořadové číslo: {cislo}, Jméno: {jmeno}")
            st.write(f"Pořadové číslo: {cislo}")
            st.write(f"Jméno: {jmeno}")
            time.sleep(5)
            st.rerun()
        """, language = "python")
    
st.divider()

st.markdown("""
### Úkol 2
1. Vytvořte formulář s následujícími vstupy:
    - Pořadové číslo
    - Jméno
2. Vytvořte tlačítko, které bude typ primary a na celou šířku kontejneru.
3. Po odeslání formuláře se zobrazí zpráva, že formulář byl úspěšně odeslán zobrazí se pořadové číslo a jméno.
4. Použijte ucastnici.json k uloženi dat. (Nezapomeňte vytvořit soubor ucastnici.json s prázdným slovníkem {}.)
5. Po odeslání použijte time.sleep(5) a st.rerun() pro vymazání formuláře.
""")

if st.toggle("Ukázat řešení", key = "ukol_2_reseni"):
    with st.form(key = "ukol_2"):
        cislo = st.number_input("Pořadové číslo", step = 1)
        jmeno = st.text_input("Jméno")
        
        if st.form_submit_button("Odeslat", type = "primary", use_container_width = True):
            with open("ucastnici.json", "r") as f:
                data = json.load(f)
            data[cislo] = jmeno
            with open("ucastnici.json", "w") as f:
                json.dump(data, f)
            st.success(f"Formulář byl úspěšně odeslán: Pořadové číslo: {cislo}, Jméno: {jmeno}")
            st.write(f"Pořadové číslo: {cislo}")
            st.write(f"Jméno: {jmeno}")
            time.sleep(5)
            st.rerun()
    if st.toggle("Ukázat kód", key = "ukol_2_kod"):
        st.code("""
    with st.form(key = "ukol_2"):
        cislo = st.number_input("Pořadové číslo", step = 1)
        jmeno = st.text_input("Jméno")
        
        if st.form_submit_button("Odeslat", type = "primary", use_container_width = True):
            with open("ucastnici.json", "r") as f:
                data = json.load(f)
            data[cislo] = jmeno
            with open("ucastnici.json", "w") as f:
                json.dump(data, f)
            st.success(f"Formulář byl úspěšně odeslán: Pořadové číslo: {cislo}, Jméno: {jmeno}")
            st.write(f"Pořadové číslo: {cislo}")
            st.write(f"Jméno: {jmeno}")
            time.sleep(5)
            st.rerun()
        """, language = "python")

st.markdown("""
---
### Úkol 3
1. Vytvořte formulář s následujícími vstupy:
    - Pořadové číslo
    - Jméno
2. Vytvořte tlačítko, které bude typ primary a na celou šířku kontejneru.
3. Po zmáčknutí tlačítka proveďte tyto operace:
    1. Načtěte data z ucastnici.json
    2. Projděte si účastníky a zjistěte, zda účastník se stejným pořadovým číslem a stejným jménem již existuje
    3. Pokud existuje, vypište pomocí st.error, že účastnk již existuje
    4. Pokud existuje ale s jiným jménem, vypište pomocí st.warning, že účastník s jiným jménem již existuje a že se přepsala na nové jméno, které bylo zadáno
    5. Pokud neexistuje vypište pomocí st.success a zapište nového účastníka do ucastnici.json
5. Po odeslání použijte time.sleep(5) a st.rerun() pro vymazání formuláře.
""")
if st.toggle("Ukázat řešení", key = "ukol_3_reseni"):
    with st.form(key = "ukol_3"):
        cislo = st.number_input("Pořadové číslo", step = 1)
        jmeno = st.text_input("Jméno")
        
        if st.form_submit_button("Odeslat", type = "primary", use_container_width = True):
            with open("ucastnici.json", "r") as f:
                data = json.load(f)
            if str(cislo) in data:
                if data[str(cislo)] == jmeno:
                    st.error("Účastník již existuje")
                else:
                    st.warning(f"Účastník s jiným jménem již existuje a byl přepsán na nové jméno: {jmeno}")
                    data[str(cislo)] = jmeno
            else:
                data[str(cislo)] = jmeno
                st.success(f"Účastník byl úspěšně přidán: Pořadové číslo: {cislo}, Jméno: {jmeno}")
            with open("ucastnici.json", "w") as f:
                json.dump(data, f)
            time.sleep(5)
            st.rerun()
    if st.toggle("Ukázat kód", key = "ukol_3_kod"):
        st.code("""
    with st.form(key = "ukol_3"):
        cislo = st.number_input("Pořadové číslo", step = 1)
        jmeno = st.text_input("Jméno")
        
        if st.form_submit_button("Odeslat", type = "primary", use_container_width = True):
            with open("ucastnici.json", "r") as f:
                data = json.load(f)
            if str(cislo) in data:
                if data[str(cislo)] == jmeno:
                    st.error("Účastník již existuje")
                else:
                    st.warning(f"Účastník s jiným jménem již existuje a byl přepsán na nové jméno: {jmeno}")
                    data[str(cislo)] = jmeno
            else:
                data[str(cislo)] = jmeno
                st.success(f"Účastník byl úspěšně přidán: Pořadové číslo: {cislo}, Jméno: {jmeno}")
            with open("ucastnici.json", "w") as f:
                json.dump(data, f)
            time.sleep(5)
            st.rerun()
        """, language = "python")

