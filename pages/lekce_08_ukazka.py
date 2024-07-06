import streamlit as st
st.set_page_config(page_title="COMO Python", page_icon="icon.png", layout="centered")

st.header("Lekce č. 8 - Ukázka Streamlit Session State")

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