import streamlit as st
st.set_page_config(page_title="COMO Python", page_icon=":snake:", layout="centered", initial_sidebar_state="collapsed")
st.header("Lekce č. 8")

st.subheader("Streamlit session state")
st.markdown("""
Streamlit session state je dalším důležitým prvkem pro psaní aplikací ve Streamlitu. \\
Streamlit po každé interakci s komponentou aplikace znovu načte celý kód a ztratí tak veškeré změny proměnných, které uživatel svou interakcí provedl. \\
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

st.code("st.write(st.session_state)")
st.write(st.session_state)

st.markdown("""
Se session state tedy můžeme pracovat stejně jako se slovníkem a můžeme na něj volat metody jako `.get()`, `.keys()`, `.values()`, `.items()` atd. \\
Oproti slovníkům má ale jednu výhodu a to, že k hodnotám v session state můžeme přistupovat i pomocí tečkové notace - `st.session_state.moje_hodnota`.
""")

st.markdown("""
Další klíčovou vlastností Streamlit session state je možnost sdílení proměnné mezi jednotlivýmí stránkami aplikace (pages).
""")

if "jmena" not in st.session_state:
    st.session_state.jmena = []

nove_jmeno = st.text_input("Zadej nové jméno:", key="zadej_nove_jmeno_2")
if st.button("Přidej jméno", use_container_width=True):
    st.session_state.jmena.append(nove_jmeno)

odstranit_jmeno = st.selectbox("Vyber jméno k odstranění:", st.session_state.jmena, index=None, placeholder="Vyber jméno")
if st.button("Odstraň jméno", use_container_width=True) and odstranit_jmeno:
    st.session_state.jmena.remove(odstranit_jmeno)

st.markdown("Session State `jmena`:")
st.write(st.session_state.jmena)

st.markdown("---")
st.code("""
if "jmena" not in st.session_state:
    st.session_state.jmena = []

nove_jmeno = st.text_input("Zadej nové jméno:")
if st.button("Přidej jméno", use_container_width=True):
    st.session_state.jmena.append(nove_jmeno)

odstranit_jmeno = st.selectbox("Vyber jméno k odstranění:", st.session_state.jmena, index=None, placeholder="Vyber jméno")
if st.button("Odstraň jméno", use_container_width=True) and odstranit_jmeno:
    st.session_state.jmena.remove(odstranit_jmeno)

st.markdown("Session State `jmena`:")
st.write(st.session_state.jmena)
""")

st.markdown("---")
st.subheader("Inicializace session state")

st.markdown("""
Session state se obvykle definuje na začátku aplikace a definuje se v rámci podmínky, která zkontroluje, zda už session state existuje,
aby při opětovném spouštení kódu, způsobeným interakcí uživatele, nedošlo k jeho přepsání.
""")

st.error("Chybná definice session state:")
st.session_state.chybny_pocet = 0
if st.button("Zvyš chybný počet"):
    st.session_state.chybny_pocet += 1
st.write(f"Chybný počet: {st.session_state.chybny_pocet}")
st.code("""
st.session_state.chybny_pocet = 0
if st.button("Zvyš chybný počet"):
    st.session_state.chybny_pocet += 1
st.write(f"Chybný počet: {st.session_state.chybny_pocet}")
""")

st.markdown("---")

st.success("Správná definice session state:")
if "spravny_pocet" not in st.session_state:
    st.session_state.spravny_pocet = 0
if st.button("Zvyš správný počet"):
    st.session_state.spravny_pocet += 1
st.write(f"Správný počet: {st.session_state.spravny_pocet}")
st.code("""
if "spravny_pocet" not in st.session_state:
    st.session_state.spravny_pocet = 0
if st.button("Zvyš správný počet"):
    st.session_state.spravny_pocet += 1
st.write(f"Správný počet: {st.session_state.spravny_pocet}")
""")

st.markdown("---")
st.subheader("Jak přistupovat k hodnotám session state a jak je měnit")

st.markdown("""
Máme definovaný session state `nazev_kurzu` a máme 3 možnosti, jak z něj získat hodnotu a 2 možnosti, jak hodnotu změnit.
1. `st.session_state["nazev_kurzu"]`
2. `st.session_state.nazev_kurzu`
3. `st.session_state.get("nazev_kurzu")`
            
A výsledkem všech tří moožností bude `COMO Python`.
""")

st.code("""
if "nazev_kurzu" not in st.session_state:
    st.session_state.nazev_kurzu = "COMO Python"
""")

if "nazev_kurzu" not in st.session_state:
    st.session_state.nazev_kurzu = "COMO Python"

st.markdown("""
Možnost 1 a 2 jsou ekvivalentní a obě vrátí hodnotu z session state. \\
Možnost 3 je bezpečnější, protože pokud klíč v session state neexistuje, tak vrátí `None` místo chyby, ale v praxi se moc nepoužívá. \\

Pro změnu hodnoty v session state můžeme použít 1. a 2. možnost, stačí pouze pomocí `=` přiřadit novou hodnotu. \\
Pokud session state klíč již existuje, tak se hodnota přepíše, pokud neexistuje, tak se vytvoří nový klíč s hodnotou.
""")



