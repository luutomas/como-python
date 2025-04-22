import streamlit as st
import json
import time 
st.set_page_config(page_title="COMO Python", page_icon="icon.png", layout="centered")

st.header("Lekce č. 8")

st.subheader("Streamlit session state")
st.markdown("""
Streamlit session state je dalším důležitým prvkem pro psaní aplikací ve Streamlitu. \\
Streamlit po každé interakci s komponentou aplikace znovu načte celý kód a ztratí tak veškeré změny proměnných, které uživatel svou interakcí provedl.
""")

with st.container(border=True):
    st.markdown("""
    Jednoduchým příkladem je tento seznam, který po stisknutí tlačíka přidá jméno z `st.text_input` do seznamu.
    ```json
    ["Tomáš", "Honza", "David"]
    ```
    """)

    jmena = ["Tomáš", "Honza", "David"]
    st.write("Jména před přidáním:")
    st.write(jmena)
    nove_jmeno = st.text_input("Zadej nové jméno:")
    if st.button("Přidej jméno"):
        jmena.append(nove_jmeno)
    st.write("Jména po přidání:")
    st.write(jmena)

st.markdown("""
Streamlit session state je vlastně jen slovník, který si Streamlit uchovává v paměti a který je dostupný po celou dobu běhu aplikace. \\
Po restartu (vypnutí a zapnutí aplikace), nebo aktualizaci stránky se všechny hodnoty v session state vymažou. \\
Session state je nám dostupný stejně jako ostatní komponenty, tedy pomocí `st.session_state` a při vypsání si můžeme všimout, že je to obyčejný slovník.
""")

with st.container(border=True):
    st.code("st.write(st.session_state)")
    st.write(st.session_state)

st.markdown("""
Se session state tedy můžeme pracovat stejně jako se slovníkem a můžeme na něj volat metody jako `.get()`, `.keys()`, `.values()`, `.items()`, ... ale v praxi se spíše nevyužívají. \\
Oproti slovníkům má ale jeden rozdíl a to, že k hodnotám v session state můžeme přistupovat i pomocí tečkové notace: `st.session_state.moje_hodnota`. \\
Další klíčovou vlastností Streamlit session state je možnost sdílení proměnné mezi jednotlivýmí stránkami aplikace (pages).
""")

with st.container(border=True):
    if "jmena" not in st.session_state:
        st.session_state["jmena"] = []

    nove_jmeno = st.text_input("Zadej nové jméno:", key="zadej_nove_jmeno_2")
    if st.button("Přidej jméno", use_container_width=True):
        st.session_state["jmena"].append(nove_jmeno)

    odstranit_jmeno = st.selectbox("Vyber jméno k odstranění:", st.session_state["jmena"], index=None, placeholder="Vyber jméno")
    if st.button("Odstraň jméno", use_container_width=True) and odstranit_jmeno:
        st.session_state["jmena"].remove(odstranit_jmeno)

    st.markdown("Session state `jmena`:")
    st.write(st.session_state["jmena"])

    st.markdown("---")
    st.code("""
    if "jmena" not in st.session_state:
        st.session_state["jmena"] = []

    nove_jmeno = st.text_input("Zadej nové jméno:", key="zadej_nove_jmeno_2")
    if st.button("Přidej jméno", use_container_width=True):
        st.session_state["jmena"].append(nove_jmeno)

    odstranit_jmeno = st.selectbox("Vyber jméno k odstranění:", st.session_state["jmena"], index=None, placeholder="Vyber jméno")
    if st.button("Odstraň jméno", use_container_width=True) and odstranit_jmeno:
        st.session_state["jmena"].remove(odstranit_jmeno)

    st.markdown("Session state `jmena`:")
    st.write(st.session_state["jmena"])
    """)

st.subheader("Inicializace session state")

st.markdown("""
Session state se obvykle definuje na začátku aplikace a definuje se v rámci podmínky, která zkontroluje, zda už session state existuje,
aby při opětovném spouštení kódu, způsobeným interakcí uživatele, nedošlo k jeho přepsání.
""")

with st.container(border=True):
    st.error("Chybná definice session state:")
    st.session_state["chybny_pocet"] = 0
    if st.button("Zvyš chybný počet"):
        st.session_state["chybny_pocet"] += 1
    st.write(f"Chybný počet: {st.session_state['chybny_pocet']}")
    st.code("""
    st.session_state["chybny_pocet"] = 0
    if st.button("Zvyš chybný počet"):
        st.session_state["chybny_pocet"] += 1
    st.write(f"Chybný počet: {st.session_state['chybny_pocet']}")
    """)

with st.container(border=True):
    st.success("Správná definice session state:")
    if "spravny_pocet" not in st.session_state:
        st.session_state["spravny_pocet"] = 0
    if st.button("Zvyš správný počet"):
        st.session_state["spravny_pocet"] += 1
    st.write(f"Správný počet: {st.session_state['spravny_pocet']}")
    st.code("""
    if "spravny_pocet" not in st.session_state:
        st.session_state["spravny_pocet"] = 0
    if st.button("Zvyš správný počet"):
        st.session_state["spravny_pocet"] += 1
    st.write(f"Správný počet: {st.session_state['spravny_pocet']}")
    """)

st.subheader("Jak přistupovat k hodnotám session state, jak je měnit a případně i mazat")

st.markdown("""
Máme definovaný session state `nazev_kurzu` a máme 3 možnosti, jak z něj získat hodnotu a 2 možnosti, jak hodnotu změnit.
1. `st.session_state["nazev_kurzu"]`
2. `st.session_state.nazev_kurzu`
3. `st.session_state.get("nazev_kurzu")`
            
A výsledkem všech tří moožností bude `COMO Python`.
""")

st.code("""
if "nazev_kurzu" not in st.session_state:
    st.session_state["nazev_kurzu"] = "COMO Python"
""")

if "nazev_kurzu" not in st.session_state:
    st.session_state["nazev_kurzu"] = "COMO Python"

st.markdown("""
Možnost 1 a 2 jsou ekvivalentní a obě vrátí hodnotu z session state. \\
Možnost 3 je bezpečnější, protože pokud klíč v session state neexistuje, tak vrátí `None` místo chyby, ale v praxi se moc nepoužívá.

Pro změnu hodnoty v session state můžeme použít 1. a 2. možnost, stačí pouze pomocí `=` přiřadit novou hodnotu.
Pokud session state klíč již existuje, tak se hodnota přepíše, pokud neexistuje, tak se vytvoří nový klíč s hodnotou.
            
Smazání session state je velice jednoduché, stačí pouze použít výraz `del` a hned za ním se odkázat na session state, který chceme smazat.
""")

with st.container(border=True):
    del st.session_state["nazev_kurzu"]
    st.write(st.session_state.get("nazev_kurzu", "Session state nebyl nalezen.")) # Pro demonstraci použijeme .get() aby se nevyvolala chyba
    st.code("""
    del st.session_state["nazev_kurzu"]
    st.write(st.session_state.get("nazev_kurzu", "Session state nebyl nalezen.")) # Pro demonstraci použijeme .get() aby se nevyvolala chyba
    """)

st.markdown("""
Další vlastností session state je přistupování k hodnotám ostatních komponent,
které využívají parametr `key`.
""")

with st.container(border=True):
    st.text_input("Zadejte Vaše jméno:", key="vase_jmeno")
    st.write(f"Vaše jméno: {st.session_state['vase_jmeno']}")
    st.code("""
    st.text_input("Zadejte Vaše jméno:", key="vase_jmeno")
    st.write(f"Vaše jméno: {st.session_state['vase_jmeno']}")
    """)

st.markdown("""
---
### Úkol
Vytvořte si ve vaší aplikaci novou stránku ve složce `pages` s názvem `prihlaseni.py`.
Vytvořte si json soubr `uzivatele.json` a do něj si zkopírujte následující data:
```json
{
    "uzivatele": [
        {
            "prihlasovaci_jmeno": "admin",
            "heslo": "como123",
            "jmeno": "Admin",
            "email": "admin@coworking-most.cz"
        }
    ]
}
```
Vytvořte si na stránce `prihlaseni.py` formulář, kde uživatel zadá své přihlašovací jméno, heslo a po stisknutí tlačítka se zkontroluje,
zda se uživatel nachází v json souboru a zda zadal správné heslo. 
*Nezapomeňte si nejdříve načíst json do Vaší aplikace a ve funkci `open()` \\
zadejte parametr `encoding="utf-8"`,
aby aplikace správně české znaky.*\\
Pokud ano, uložte jméno (`jmeno`) a email uživatele do session states `jmeno` a `email` a skryjte přihlašovací formulář a místo něj
zobrazte pozdrav uživatele s jeho jménem, emailem a zobrazte tlačítko pro odhlášení, které bude viditelné pouze pokud je uživatel přihlášený.
""")
if st.toggle("Nápověda"):
    st.markdown("""
    1. Pro kontrolu přihlašovacích údajů budete muset využít for loop a podívat se, jestli se zadaná kombinace jména a hesla nachází v json souboru.
    2. Pro zobrazení/skytí formuláře a tlačítka pro odhlášení budete muset použít pomocný session state (např. `prihlasen`), pro ukladání informace, zda je uživatel přihlášený a použít if podmínku, pro zobrazní formuláře, nebo pozdravu s tlačítkem pro odhlášení.
""")
    
if st.toggle("Zobrazit řešení:"):
    with open("data/json/uzivatele.json", "r", encoding="utf-8") as f:
        uzivatele = json.load(f)

    if "prihlasen" not in st.session_state:
        st.session_state["prihlasen"] = False
    if "jmeno" not in st.session_state:
        st.session_state["jmeno"] = None
    if "email" not in st.session_state:
        st.session_state["email"] = None

    if not st.session_state["prihlasen"]:
        with st.form("prihlaseni", clear_on_submit=True):
            prihlasovaci_jmeno = st.text_input("Přihlašovací jméno:")
            heslo = st.text_input("Heslo:", type="password")

            if st.form_submit_button("Přihlásit se", use_container_width=True):
                for uzivatel in uzivatele["uzivatele"]:
                    if prihlasovaci_jmeno == uzivatel["prihlasovaci_jmeno"] and heslo == uzivatel["heslo"]:
                        st.session_state["jmeno"] = uzivatel["jmeno"]
                        st.session_state["email"] = uzivatel["email"]
                        st.session_state["prihlasen"] = True
                        break
                if st.session_state["prihlasen"]:
                    st.success("Přihlášení proběhlo úspěšně.")
                    time.sleep(3)
                    st.rerun()
                else:
                    st.error("Špatné přihlašovací údaje.")
            
    if st.session_state["prihlasen"]:
        st.write(f"Ahoj {st.session_state['jmeno']}")
        st.write(f"Tvůj email je: {st.session_state['email']}")
        if st.button("Odhlásit se"):
            st.session_state["prihlasen"] = False
            st.session_state["jmeno"] = None
            st.session_state["email"] = None
            st.success("Odhlášení proběhlo úspěšně.")
            time.sleep(3)
            st.rerun()

    if st.toggle("Zobrazit kód"):
        st.code("""
            import streamlit as st
            import json
            import time    

            # Načtení json souboru
            with open("data/json/uzivatele.json", "r", encoding="utf-8") as f:
                uzivatele = json.load(f)

            # Inicializace session state
            if "prihlasen" not in st.session_state:
                st.session_state["prihlasen"] = False # Status přihlášení uživatele
            if "jmeno" not in st.session_state:
                st.session_state["jmeno"] = None # Jméno přihlášeného uživatele
            if "email" not in st.session_state:
                st.session_state["email"] = None # Email přihlášeného uživatele
            
            # Pokud je status přihlášení False (Nepravda), zobrazí se formulář pro přihlášení
            if not st.session_state["prihlasen"]:

                # Formulář pro přihlášení
                with st.form("prihlaseni", clear_on_submit=True):
                    prihlasovaci_jmeno = st.text_input("Přihlašovací jméno:")
                    heslo = st.text_input("Heslo:", type="password")

                    # Proces přihlášení
                    if st.form_submit_button("Přihlásit se", use_container_width=True):
                
                        # Podíváme se přes for loop na každého uživatele v json souboru a zkontrolujem, zda se zadané přihlašovací jméno a heslo nachází shoďují s některým uživatelem
                        for uzivatel in uzivatele["uzivatele"]:
                            # Pokud najdeme shodu, tak uložíme jméno a email uživatele do session state, změníme status přihlášení na True a přerušíme smyčku přes break, protože už nemá cenu hledat dál
                            if prihlasovaci_jmeno == uzivatel["prihlasovaci_jmeno"] and heslo == uzivatel["heslo"]:
                                st.session_state["jmeno"] = uzivatel["jmeno"]
                                st.session_state["email"] = uzivatel["email"]
                                st.session_state["prihlasen"] = True
                                break
                        # Pokud je status přihlášení True (Pravda), zobrazí se zpráva o úspěšném přihlášení a aplikace se restartuje
                        if st.session_state["prihlasen"]:
                            st.success("Přihlášení proběhlo úspěšně.")
                            time.sleep(3)
                            st.rerun()
                        # Pokud je status přihlášení False (Nepravda), zobrazí se chybová zpráva
                        else:
                            st.error("Špatné přihlašovací údaje.")

            # Pokud je status přihlášení True (Pravda), zobrazí se pozdrav uživatele s jeho jménem a emailem a tlačítko pro odhlášení    
            if st.session_state["prihlasen"]:
                st.write(f"Ahoj {st.session_state['jmeno']}")
                st.write(f"Tvůj email je: {st.session_state['email']}")
                # Tlačítko pro odhlášení, pokud je stisknuto, tak se status přihlášení změní na False, jméno a email se vymažou a zobrazí se zpráva o úspěšném odhlášení a aplikace se restartuje
                if st.button("Odhlásit se"):
                    st.session_state["prihlasen"] = False
                    st.session_state["jmeno"] = None
                    st.session_state["email"] = None
                    st.success("Odhlášení proběhlo úspěšně.")
                    time.sleep(3)
                    st.rerun()
        """)

def uloz_uzivatele(uzivatele):
    # Uložení uživatelů do souboru
    try:
        with open("data/json/uzivatele.json", "w", encoding="utf-8") as f:
            json.dump(uzivatele, f, indent=4, ensure_ascii=False)
        st.success("Uživatelé byli úspěšně uloženi!")
    except Exception as e:
        st.error(f"Chyba při ukládání uživatelů: {e}")

def nacti_uzivatele():
    # Načtení uživatelů ze souboru
    try:
        with open("data/json/uzivatele.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


        





