import datetime as dt
import streamlit as st
import pandas as pd

st.set_page_config(page_title="COMO Python", page_icon=":snake:", layout="centered", initial_sidebar_state="collapsed")
st.header("Lekce č. 11")

df_objednavky =  pd.read_csv("objednavky.csv", sep = ",")
st.dataframe(df_objednavky)

st.markdown("""
### Výběr sloupce z DataFrame   
""")
st.write(df_objednavky["id_objednavky"])
st.write(df_objednavky["datum_objednavky"])
st.write(df_objednavky[["id_objednavky", "datum_objednavky"]])

st.markdown("""
### Filtrace
""")
st.write(df_objednavky[df_objednavky["id_objednavky"] == 1])
st.write(df_objednavky[df_objednavky["id_objednavky"] > 1])
st.write(df_objednavky[(df_objednavky["id_objednavky"] > 1) & (df_objednavky["id_objednavky"] < 4)])
st.write(df_objednavky[(df_objednavky["id_objednavky"] == 1) | (df_objednavky["id_klienta"] == 12)])

st.write(df_objednavky.loc[0])
st.write(df_objednavky.loc[[0,1]])
st.write(df_objednavky.loc[df_objednavky["id_objednavky"] == 1])
st.write(df_objednavky.loc[df_objednavky["id_objednavky"] == 1, ["id_objednavky", "cena_objednavky"]])

st.markdown("""
### Přidání sloupce
""")
df_objednavky["mena_objednavky"] = "CZK"
st.write(df_objednavky)
df_objednavky.loc[df_objednavky["id_klienta"] == 3, "mena_objednavky"] = "EUR"
st.write(df_objednavky)

st.markdown("""
### Převod datového typu
""")
#df_objednavky["id_klienta"] = df_objednavky["id_klienta"].astype(str)
st.write(df_objednavky)

df_objednavky[df_objednavky["id_klienta"] == 1]
df_objednavky[df_objednavky["id_klienta"] == "1"]

df_objednavky["datum_objednavky_dt"] = pd.to_datetime(df_objednavky["datum_objednavky"])
st.write(df_objednavky)
df_objednavky["stari_objendavky"] = dt.datetime.now() - df_objednavky["datum_objednavky_dt"]
st.write(df_objednavky)

st.write(df_objednavky.sort_values("cena_objednavky"))
st.write(df_objednavky.sort_values("cena_objednavky", ascending = False))

st.write(df_objednavky.sort_values(["id_klienta", "cena_objednavky"], ascending = [True, False]))

st.markdown("""
### Grouping
""")
df_objednavky_gb_id_klienta = df_objednavky[["id_klienta", "cena_objednavky"]].groupby("id_klienta").sum()
df_objednavky_gb_id_klienta_reset_index = df_objednavky[["id_klienta", "cena_objednavky"]].groupby("id_klienta").sum().reset_index()
col_grouping = st.columns(2)
with col_grouping[0]:
    st.write(df_objednavky_gb_id_klienta)
with col_grouping[1]:
    st.write(df_objednavky_gb_id_klienta_reset_index)

df_objednavky_gb_id_klienta_zpusob_platby = df_objednavky[["id_klienta", "typ_zaplaceni", "cena_objednavky"]].groupby(["typ_zaplaceni", "id_klienta"]).sum()
col_grouping_2 = st.columns(2)
with col_grouping_2[0]:
    st.write(df_objednavky_gb_id_klienta_zpusob_platby)
with col_grouping_2[1]:
    st.write(df_objednavky_gb_id_klienta_zpusob_platby.reset_index())

df_objednavky_gb_id_klienta_zpusob_platby = df_objednavky[["id_klienta", "typ_zaplaceni", "cena_objednavky"]].groupby(["id_klienta", "typ_zaplaceni"]).sum()
col_grouping_3 = st.columns(2)
with col_grouping_3[0]:
    st.write(df_objednavky_gb_id_klienta_zpusob_platby)
with col_grouping_3[1]:
    st.write(df_objednavky_gb_id_klienta_zpusob_platby.reset_index())


st.markdown("""
### st.date_editor
""")
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

