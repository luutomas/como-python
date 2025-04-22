import datetime as dt
import streamlit as st
import pandas as pd

st.set_page_config(page_title="COMO Python", page_icon="icon.png", layout="centered")

st.header("Lekce č. 13")
st.subheader("Pandas")
st.markdown("""
Python se velmi často používá pro analýzu dat. Jednou z nejpoužívanějších knihoven pro analýzu dat je Pandas.
Pandas je knihovna, která nám umožňuje pracovat s daty ve formě DataFrame. 
DataFrame je tabulka, která obsahuje data ve formě sloupců a řádků.

Stáhněte si soubor objednavky.csv a načtěte si ho do DataFrame.
""")
st.download_button("Stáhnout objednavky.csv", "objednavky.csv")

st.markdown("---")

st.markdown("""
### Načtení dat do DataFrame z CSV
CSV neboli Comma Separated Values je formát pro ukládání dat, která je velmi populární. 
Je to forma, která je také velmi jednoduchá a čitelná a přátelská vůči EXCELu.
Pro načtení dat do DataFrame použijeme funkci pd.read_csv() a pro zobrazení dat použijeme funkci st.dataframe().
pd.read_csv() má několik parametrů, které můžeme použít pro načtení dat:

| parametr | popis | detail |
| -------- | ------ | ---|
| path | cesta k souboru | nejdůležitější parametr |
| sep | oddělovač sloupců | někdy pro české CSV soubory je to středník |
| encoding | kódování souboru | nejčastěji "utf-8", pokud máte problémy s diakritikou, zkuste nastavit na "cp1250" |

Nyní si načteme data do DataFrame a zobrazíme je pomocí st.dataframe().
```
df_objednavky =  pd.read_csv("objednavky.csv", sep = ",", encoding = "utf-8")
st.dataframe(df_objednavky)
```
""")
df_objednavky =  pd.read_csv("data/csv/objednavky.csv", sep = ",")
st.dataframe(df_objednavky)

st.markdown("""
### První pohled na data
Při načtení dat do DataFrame je dobré se podívat na prvních pár řádků a také na posledních pár řádků.
Pro zobrazení prvních pár řádků použijeme metodu head() a pro zobrazení posledních pár řádků použijeme metodu tail().
```
st.write(df_objednavky.head())
st.write(df_objednavky.tail())
```
Pokud chceme vědět kolik sloupců a řádků to má tak použijeme metodu shape.
```
st.write(df_objednavky.shape)
```
""")
st.write(df_objednavky.head())
st.write(df_objednavky.tail())
st.write(df_objednavky.shape)

st.markdown("""
Pokud bychom chtěli zjistit názvy sloupců, tak použijeme atribut columns.
```
st.write(df_objednavky.columns)
```
Vrátí nám to list názvů sloupců.
""")
st.write(df_objednavky.columns)

st.markdown("""
A pokud bychom přejmenovali sloupce, tak dodáme nový list názvů sloupců, který bude mít stejnou délku.
```
df_objednavky.columns = ["id_objednavky", "id_klienta", "datum_objednavky", "cena_objednavky", "typ_zaplaceni", "status", "cena_dopravy"]
st.write(df_objednavky)
```
""")
df_objednavky.columns = ["id_objednavky", "id_klienta", "datum_objednavky", "cena_objednavky", "typ_zaplaceni", "status", "cena_dopravy"]
st.write(df_objednavky)

st.markdown("""
### Výběr sloupce z DataFrame
Je mnoho způsobů jak vybrat sloupec z DataFrame. Základním způsobem je čistě pomocí hranatých závorek a názvu sloupce.
1. Použití hranatých závorek a názvu sloupce
```
st.write(df_objednavky["id_objednavky"])
```
2. Použití hranatých závorek a seznamu názvů sloupců v případě, že bychom chtěli více jak jeden sloupec
```
st.write(df_objednavky[["id_objednavky", "datum_objednavky"]])
```

""")
st.write(df_objednavky["id_objednavky"])
st.write(df_objednavky[["id_objednavky", "datum_objednavky"]])

st.markdown("""
### Filtrace
Pro filtrování dat použijeme metodu df_objednavky[df_objednavky["název_sloupce"] == hodnota] 
nebo metodu df_objednavky[(df_objednavky["název_sloupce"] > hodnota1) & (df_objednavky["název_sloupce"] < hodnota2)].
Záleží co přesně chceme filtrovat.

Například pokud bych chtěl filtrovat hotovostní platby, tak bych použil následující kód:
```
st.write(df_objednavky[df_objednavky["typ_zaplaceni"] == "hotově"])
```
""")
st.write(df_objednavky[df_objednavky["typ_zaplaceni"] == "hotově"])

st.markdown("""
Pokud bych chtěl filtrovat objednávky s id_objednavky větší jak 1, tak bych použil následující kód:
```
st.write(df_objednavky[df_objednavky["id_objednavky"] > 1])
```
""")

st.write(df_objednavky[df_objednavky["id_objednavky"] > 1])
st.markdown("""
Podmínky můžu kombinovat pomocí operátorů & (a) a | (nebo).
Například pokud bych chtěl filtrovat objednávky s id_objednavky větší jak 1 a menší jak 4, tak bych použil následující kód:
```
st.write(df_objednavky[(df_objednavky["id_objednavky"] > 1) & (df_objednavky["id_objednavky"] < 4)])
```
""")
st.write(df_objednavky[(df_objednavky["id_objednavky"] > 1) & (df_objednavky["id_objednavky"] < 4)])

st.markdown("""
A pokud bych chtěl filtrovat objednávky s id_objednavky rovno 1 nebo id_klienta rovno 12, tak bych použil následující kód:
```
st.write(df_objednavky[(df_objednavky["id_objednavky"] == 1) | (df_objednavky["id_klienta"] == 12)])
```
""")
st.write(df_objednavky[(df_objednavky["id_objednavky"] == 1) | (df_objednavky["id_klienta"] == 12)])

st.markdown("""
### Metody LOC
Pro filtraci je také dobré znát metodu loc[], která nám umožňuje filtrovat data podle indexu a sloupce.
Například pokud bych chtěl zobrazit první řádek, tak bych použil následující kód:
```
st.write(df_objednavky.loc[0])
```
My se touto metodou zde nebudeme příliš zabývat.
""")
st.write(df_objednavky.loc[0])

st.markdown("""
### Přidání sloupce
Pro přidání sloupce do DataFrame funguje následující zápis:
df_objednavky["název_sloupce"] = hodnota
Například pokud bych chtěl přidat sloupec "mena_objednavky" s hodnotou "CZK", tak bych použil následující kód:
```
df_objednavky["mena_objednavky"] = "CZK"
st.write(df_objednavky)
```
""")
df_objednavky["mena_objednavky"] = "CZK"
st.write(df_objednavky)

st.markdown("""
Pokud bych chtěl změnit hodnotu sloupce "mena_objednavky" pro klienta s id_klienta rovno 3 na "EUR", tak bych použil následující kód:
```
df_objednavky.loc[df_objednavky["id_klienta"] == 3, "mena_objednavky"] = "EUR"
st.write(df_objednavky)
```
""")
df_objednavky.loc[df_objednavky["id_klienta"] == 3, "mena_objednavky"] = "EUR"
st.write(df_objednavky)

st.markdown("""
### Převod datového typu
Převod datového typu je velmi důležitý, pokud chceme pracovat s daty.
Převod datového typu se provádí pomocí metody astype().
Například pokud bych chtěl převést sloupec "id_klienta" na typ string, tak bych použil následující kód:
```
df_objednavky["id_klienta"] = df_objednavky["id_klienta"].astype(str)
st.write(df_objednavky)
```
""")
df_objednavky["id_klienta"] = df_objednavky["id_klienta"].astype(str)
st.write(df_objednavky)
st.markdown("""
Datové typy je dobré mít správně nastavené, protože se s nimi bude lépe pracovat a i filtrovat.
Např: 
```
df_objednavky[df_objednavky["id_klienta"] == 1]
df_objednavky[df_objednavky["id_klienta"] == "1"]
```
my budou vracet jiné výsledky, podle toho jaký je to datový typ.
""")
st.markdown("""
```
df_objednavky[df_objednavky["id_klienta"] == 1]
```
Dostaneme:
""")
df_objednavky[df_objednavky["id_klienta"] == 1]
st.markdown(""" --- """)
st.markdown("""
```
df_objednavky[df_objednavky["id_klienta"] == "1"] 
```
Dostaneme:
""")
df_objednavky[df_objednavky["id_klienta"] == "1"]

st.markdown(""" --- """)
st.markdown("""
Další důležitou věcí je převod data na datový typ datetime.
Tento převod má již pandas zabudovaný a stačí použít metodu pd.to_datetime().
S tímto sloupcem pak lze dále pracovat a například zjistit stáří objednávky.
""")
with st.echo():
    df_objednavky["datum_objednavky_dt"] = pd.to_datetime(df_objednavky["datum_objednavky"])
    df_objednavky["stari_objendavky"] = dt.datetime.now() - df_objednavky["datum_objednavky_dt"]
    st.write(df_objednavky)

st.markdown("""
### Řazení
Pro řazení dat použijeme metodu sort_values().
Tato metoda má několik parametrů, které můžeme použít pro řazení:
| parametr | popis | detail |
| -------- | ------ | ---|
| by | sloupec, podle kterého chceme řadit | nejdůležitější parametr |
| ascending | zda chceme řadit vzestupně nebo sestupně | True nebo False |

Pokud bychom chtěli použít více sloupců pro řazení, tak použijeme list názvů sloupců a list hodnot pro ascending.

""")
with st.echo():
    st.write(df_objednavky.sort_values("cena_objednavky"))
with st.echo():
    st.write(df_objednavky.sort_values("cena_objednavky", ascending = False))
with st.echo():
    st.write(df_objednavky.sort_values(["id_klienta", "cena_objednavky"], ascending = [True, False]))

st.markdown("""
### Grouping
Další důležitou funkcí je grouping, která nám umožňuje seskupit data podle sloupce a provést nad nimi nějakou agregační funkci.
Pro grouping použijeme metodu groupby().
S groupby() se často také používá metoda sum(), mean(), count(), min(), max() a další.
Poté se také používá metoda reset_index(), která nám vrátí DataFrame zpět do původní podoby bez složených indexů.
Například pokud bych chtěl zjistit celkovou cenu objednávek podle id_klienta a srovnání tabulek před a po reset_index().
""")
with st.echo():
    df_objednavky_gb_id_klienta = df_objednavky[["id_klienta", "cena_objednavky"]].groupby("id_klienta").sum()
    df_objednavky_gb_id_klienta_reset_index = df_objednavky[["id_klienta", "cena_objednavky"]].groupby("id_klienta").sum().reset_index()
    col_grouping = st.columns(2)
    with col_grouping[0]:
        st.write(df_objednavky_gb_id_klienta)
    with col_grouping[1]:
        st.write(df_objednavky_gb_id_klienta_reset_index)

st.markdown("""
Další příklad je zjištění celkové ceny objednávek podle id_klienta a typu způsobu platby.
""")
with st.echo():
    df_objednavky_gb_id_klienta_zpusob_platby = df_objednavky[["id_klienta", "typ_zaplaceni", "cena_objednavky"]].groupby(["typ_zaplaceni", "id_klienta"]).sum()
    col_grouping_2 = st.columns(2)
    with col_grouping_2[0]:
        st.write(df_objednavky_gb_id_klienta_zpusob_platby)
    with col_grouping_2[1]:
        st.write(df_objednavky_gb_id_klienta_zpusob_platby.reset_index())
st.markdown("""
Na pořadí sloupců v případě groupby() záleží, protože se podle nich seskupují data.
""")
with st.echo():
    df_objednavky_gb_id_klienta_zpusob_platby = df_objednavky[["id_klienta", "typ_zaplaceni", "cena_objednavky"]].groupby(["id_klienta", "typ_zaplaceni"]).sum()
    col_grouping_3 = st.columns(2)
    with col_grouping_3[0]:
        st.write(df_objednavky_gb_id_klienta_zpusob_platby)
    with col_grouping_3[1]:
        st.write(df_objednavky_gb_id_klienta_zpusob_platby.reset_index())


st.markdown("""
### st.date_editor
Pro práci s DataFrame je možné použít st.date_editor, který nám umožňuje editovat data přímo v aplikaci.
Pro použití st.date_editor je potřeba mít data v DataFrame a následně je zobrazit pomocí st.data_editor().
Je tam i možnost nastavit typ sloupce, zda je to text, číslo nebo selectbox.
Nebo zda je vůbec editovatelný.
""")
with st.echo():
    with st.form(key = "data_editor_1"):
        df_objednavky_vystup = st.data_editor(df_objednavky, key = "data_editor_objednvky",
        column_config = {"id_objednavky": {"disabled": True},
                        "id_klienta": {"disabled": True},
                        "datum_objednavky": {"disabled": True},
                        "cena_objednavky": {"disabled": False},
                        "typ_zaplaceni": st.column_config.SelectboxColumn(label = "typ_zaplaceni", options = ["hotově", "kartou", "šekem"], required = True),
        })
        if st.form_submit_button("Uložit"):
            st.write(df_objednavky_vystup)
            st.session_state["data_editor_objednvky"].to_csv("objednavky_vystup.csv", index = False)
            st.success("Data uložena")
