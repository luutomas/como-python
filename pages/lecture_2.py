import streamlit as st
st.set_page_config(page_title="COMO Python", page_icon=":snake:", layout="centered", initial_sidebar_state="collapsed")
st.header("Lekce č. 2")

st.subheader("Proměnné a cesta k nim")
st.markdown("""
V programování patří tzv. proměnné k základním znalostem. \\
Z matematiky si vzpomeňme, že proměnná je něco, co se mění a není to "číslo". \\
Jak už nejednou bylo řečeno: Matematika mi šla do té doby, než se začali používat písmena. 

Pro nás ale proměnná nebude tak nic strašného. Představte si to jako adresu, nebo odkaz, na který budete odkazovat. \\
Např. Místo toho, aby jste si pamatovali, že máte 5 jablka, si pamatujete, že máte 5 jablka na adrese `moje_jablka` a to tímto způsobem:

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

""")

moje_jablka = 5
st.write(moje_jablka)

st.markdown(""" --- """)

st.markdown("""
Proměnné v Pythonu se zapisují pomocí rovnítka `=` a názvy proměnné se píší bez mezer a s malými písmeny. \\
Pokud je třeba mezera tak pak se používá `_` podtržítko. \\

Proměnné mohou být různých typů a mohou se s nimi různě pracovat. Nyni si ukážeme, co můžeme dělat s číselnými proměnnými. \\
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
st.markdown("""
S čísli ale můžete provádět veškeré operace, které znáte z matematiky.
```
moje_jablka = 5
honzovo_jablka = 1

celkem_jablek = moje_jablka + honzovo_jablka # sčítání
st.write(f"celkem: {celkem_jablek}")

rozdil_jablek = moje_jablka - honzovo_jablka # odčítání
st.write(f"rozdil: {rozdil_jablek}")

soucin_jablek = moje_jablka * honzovo_jablka # násobení
st.write(f"soucin {soucin_jablek}")

podil_jablek = moje_jablka / honzovo_jablka  # dělení
st.write(f"podil: {podil_jablek}")

module_jablek = moje_jablka % honzovo_jablka # modulo -> dělení, kdy výsledek je zbytek
st.write(f"modulo: {module_jablek}")

moje_jablka_na_druhou = moje_jablka**2 # umocnění
st.write(f"na druhou: {moje_jablka_na_druhou}")

moje_jablka_vic_nez_honzova_jablka = moje_jablka > honzovo_jablka # porovnání
st.write(f"Mám víc?: {moje_jablka_vic_nez_honzova_jablka}")

moje_jablka_stejna_jako_honzova_jablka = moje_jablka == honzovo_jablka # porovnání všimněte si ==
st.write(f"Máme stejně? {moje_jablka_stejna_jako_honzova_jablka}")
```
a výsledky:
""")

moje_jablka = 5
honzovo_jablka = 1

celkem_jablek = moje_jablka + honzovo_jablka # sčítání
st.write(f"celkem: {celkem_jablek}")

rozdil_jablek = moje_jablka - honzovo_jablka # odčítání
st.write(f"rozdil: {rozdil_jablek}")

soucin_jablek = moje_jablka * honzovo_jablka # násobení
st.write(f"soucin {soucin_jablek}")

podil_jablek = moje_jablka / honzovo_jablka  # dělení
st.write(f"podil: {podil_jablek}")

module_jablek = moje_jablka % honzovo_jablka # modulo -> dělení, kdy výsledek je zbytek
st.write(f"modulo: {module_jablek}")

moje_jablka_na_druhou = moje_jablka**2 # umocnění
st.write(f"na druhou: {moje_jablka_na_druhou}")

moje_jablka_vic_nez_honzova_jablka = moje_jablka > honzovo_jablka # porovnání
st.write(f"Mám víc?: {moje_jablka_vic_nez_honzova_jablka}")

moje_jablka_stejna_jako_honzova_jablka = moje_jablka == honzovo_jablka # porovnání všimněte si ==
st.write(f"Máme stejně? {moje_jablka_stejna_jako_honzova_jablka}")

st.markdown("""
Všimněte si také těch zajímavých # značek -> ty slouží jako **komentáře**, tedy kód, který se nevykonává, ale slouží k vysvětlení kódu. \\
Je doporučené abyste si to poznamenávali právě do vašich kódů, abyste se v nich lépe vyznali v budoucnosti.\\
A také si všimněte jak jsme rovnou aplikovali f stringy, které nám umožňují vypisovat proměnné přímo do textu.

Také si všimněte odpovědí u porovnávní. Výsledkem porovnání je vždy **True** nebo **False** tedy **Pravda** nebo **Nepravda**.
""")
st.markdown(""" --- """)
st.markdown("""
Nyní se ukážeme, jak získat od vašich uživatelů čísla např. právě tech jablek, abyste mohli s nimi pracovat. \\
Používá se k tomu tzv. komponenta. V našem případě to bude st.number_input. \\
**number** znamená číslo a **input** znamená vstup, tedy vstup čísla. st indikuje pouze to, že je to z knihovny streamlit, kterou jsme si zkrátili na začátku kódu jako **st**.

Nyní sestavím kód, který mi umožní získat počet jablek, které mám a Honza a vypíše mi je do konzole.
```
moje_jablka = st.number_input("Zadejte počet jablek", key = "moje_jablka")
honzovo_jablka = st.number_input("Zadejte počet Honzových jablek", key = "honzovo_jablka")
celkem_jablek = moje_jablka + honzovo_jablka
st.write(celkem_jablek)
```
A díky tomu dostanu výsledek:
""")

moje_jablka = st.number_input("Zadejte počet jablek", key = "moje_jablka")
honzovo_jablka = st.number_input("Zadejte počet Honzových jablek", key = "honzovo_jablka")
celkem_jablek = moje_jablka + honzovo_jablka
st.write(celkem_jablek)

st.markdown(""" --- """)
st.markdown("""
Každá komponenta má mnoho parametrů, které můžete nastavit. Toto se aktualizije vždy na stránkách streamlitu, kde si můžete přečíst, co všechno můžete nastavit.

https://docs.streamlit.io/develop/api-reference/widgets/st.number_input

```
st.number_input(label, min_value=None, max_value=None, value="min", step=None, 
format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, 
placeholder=None, disabled=False, label_visibility="visible")
```
Spolu projdeme parametry, které jsou podle nás nejdůležitější a budeme vám je ukazovat na příkladech.

Pro všechny parametry plati, že pokud ten parametr za sebou nemá = něco, tak je povinná a tu musíme specifikovat.
Pokud má `=None`, tak je nepovinná a pokud ji nezadáme, tak se použije defaultní/výchozí hodnota (což je právě ta `None` což znamená nic).


| Název | Popis |
| ----- | ------ |
| **label** | popisek, který se zobrazí u komponenty |
| **min_value** | minimální hodnota, kterou může uživatel zadat |
|  **max_value** | maximální hodnota, kterou může uživatel zadat |
| **value** | počáteční hodnota, která se zobrazí |
| **step** | krok, o který se hodnota mění |
| **format** | formát, ve kterém se hodnota zobrazí |
| **key** | unikátní identifikátor, který se používá k aktualizaci komponenty - doporučujem vždy nastavovat, abyste si vybudovali dobré zvyky a naučili pojmenovávat věci |
| **help** | nápověda, která se zobrazí u komponenty |
| on_change | funkce, která se spustí, když se hodnota změní - pokročilé, nebudeme řešit|
| args | argumenty, které se předají funkci on_change - pokročilé, nebudeme řešit|
| kwargs | klíčové argumenty, které se předají funkci on_change - pokročilé, nebudeme řešit|

Nyní tedy s těmito znalostmi bych chtěl zlepšit náš předchozí kód, aby byl více uživatelsky přívětivý.
Nastavím, aby krok byl 1, aby uživatel nemohl zadat záporné hodnoty a aby se mu zobrazila nápověda, co má dělat.
```
moje_jablka = st.number_input("Zadejte počet jablek", min_value=0, step=1, 
    help="Zadejte počet jablek, které máte", key = "moje_jablka_2")
honzovo_jablka = st.number_input("Zadejte počet Honzových jablek", min_value=0, 
    step=1, help="Zadejte počet jablek, které má Honza", key = "honzovo_jablka_2")
celkem_jablek = moje_jablka + honzovo_jablka
st.write(celkem_jablek)
```
""")
moje_jablka = st.number_input("Zadejte počet jablek", min_value=0, step=1, 
    help="Zadejte počet jablek, které máte", key = "moje_jablka_2")
honzovo_jablka = st.number_input("Zadejte počet Honzových jablek", min_value=0, step=1, 
    help="Zadejte počet jablek, které má Honza", key = "honzovo_jablka_2")
celkem_jablek = moje_jablka + honzovo_jablka
st.write(celkem_jablek)

st.markdown(""" --- """)
st.markdown("""
Všimněte si, jak jsem musel zadat dva nové **key** parametry:

Ve staré části to byly:

`"moje_jablka" a "honzovo_jablka"`

ale v nové části to byly_

 `"moje_jablka_2" a "honzovo_jablka_2"`.

Je to právě z důvodu, že každá komponenta má svůj unikátní identifikátor a pokud bude duplicitní tak to nebude fungovat.

Zkuste tedy nyní vypracovat tuto vzorovou úlohu sami, abyste si to procvičili:

Je povolené kopírovat kód ale musíte mu rozumět a vědět, co dělá.

-----
### Úloha č.1
Chcete aby uživatel zadal rok narození a vy mu vypíšete kolik mu je let.
""")

if st.toggle("Zobrazit podobu řešení", key="reseni_1"):
    rok_narozeni = st.number_input("Zadejte rok narození", min_value=1900, max_value=2021, step=1, help="Zadejte rok narození", key="rok_narozeni")
    vek = 2024 - rok_narozeni
    st.write(vek)
    if st.toggle("Zobrazit kód", key="kod_1"):
        st.code("""
        rok_narozeni = st.number_input("Zadejte rok narození", min_value=1900, max_value=2021, step=1, help="Zadejte rok narození", key="rok_narozeni")
        vek = 2024 - rok_narozeni
        st.write(vek)
        """)

    

st.markdown("""
----
### Úloha č.2
Chcete aby uživatel zadal dvě čísla a vypsal vám to větší z nich a o kolik je větší. \\
Použijte funkci max(cislo_1, cislo_2), které vrátí větší ze dvou čísel. \\
Pro rozdíl použijte funkci abs(cislo_1 - cislo_2), která vrátí absolutní hodnotu rozdílu dvou čísel.
""")
if st.toggle("Zobrazit podobu řešení", key = "reseni_2"):
    prvni_cislo = st.number_input("Zadejte první číslo", key="prvni_cislo")
    druhe_cislo = st.number_input("Zadejte druhé číslo", key="druhe_cislo")
    vetsi_cislo = max(prvni_cislo, druhe_cislo)
    rozdil = abs(prvni_cislo - druhe_cislo)
    st.write(vetsi_cislo)
    st.write(rozdil)
    
    if st.toggle("Zobrazit kód", key="kod_2"):
        st.code("""
            prvni_cislo = st.number_input("Zadejte první číslo", key="prvni_cislo")
            druhe_cislo = st.number_input("Zadejte druhé číslo", key="druhe_cislo")
            vetsi_cislo = max(prvni_cislo, druhe_cislo)
            rozdil = abs(prvni_cislo - druhe_cislo)
            st.write(vetsi_cislo)
            st.write(rozdil)
            """)