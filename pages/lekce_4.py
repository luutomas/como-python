import streamlit as st
st.set_page_config(page_title="COMO Python", page_icon=":snake:", layout="centered", initial_sidebar_state="collapsed")
st.header("Lekce č. 4")

st.subheader("Slovníky")
st.markdown("""
Slovnik je datová struktura, která ukládá data ve formě klíč-hodnota, podobně jako reálný slovník, kde máme hledaný výraz a jeho význam. \\
V Pythonu se slovník zapisuje pomocí složených závorek `{}` a klíč a hodnota se oddělují dvojtečkou `:`. \\
Např. slovník s názvy jídel a jejich cenami může vypadat takto:
```
jidla = { 
    "hamburger": 99,
    "pizza": 149,
    "sendvic": 59
    }
```
Pokud bych chtěl získat cenu pizzy, tak bych napsal:
```
cena_pizza = jidla["pizza"]
st.write(f"Cena pizzy je {cena_pizza}") # Všimněte si f-string v odpovědi
```
Výsledek pak vypíše:
""")

jidla = {
    "hamburger": 99,
    "pizza": 149,
    "sendvič": 59
    }
cena_pizza = jidla["pizza"]
st.write(f"Cena pizzy je {cena_pizza}")

st.markdown("""
---
Pokud bych chtěl přidat nové jídlo do seznamu, tak bych napsal:
```
jidla = {
    "hamburger": 99,
    "pizza": 149,
    "sendvič": 59
    }
jidla["pho"] = 150
st.write(jidla)
```
Výsledek pak vypíše:
""")

jidla["pho"] = 150
st.write(jidla)

st.markdown(""" 
---
Mezi další důležité funkce, které můžete s slovníky provádět patří:
| Funkce | Popis |
|--------|-------|
| `keys()` | Vrátí seznam klíčů |
| `values()` | Vrátí seznam hodnot |
| `items()` | Vrátí seznam klíč-hodnota |
| `get()` | Vrátí hodnotu klíče |
| `del` | Smaže klíč a hodnotu |
| `clear()` | Smaže celý slovník |
| `pop()` | Vrátí hodnotu klíče a smaže klíč |
---
Např. pokud bych chtěl zjistit všechny jídla, které mám v seznamu, tak bych napsal:
```
seznam_jidel = jídla.keys()
st.write(seznam_jidel)
```
A dostanu seznam jidel (hlouběji se na seznamy podíváme později):
""")
jidla = {
    "hamburger": 99,
    "pizza": 149,
    "sendvič": 59
    }
seznam_jidel = jidla.keys()
st.write(seznam_jidel)

st.markdown("""
---
Pokud bych chtěl seznam cen jídel, tak bych napsal:
```
jidla = {
    "hamburger": 99,
    "pizza": 149,
    "sendvič": 59
    }
seznam_cen = jidla.values()
st.write(seznam_cen)
```
A výsledek
""")
jidla = {
    "hamburger": 99,
    "pizza": 149,
    "sendvič": 59
    }
seznam_cen = jidla.values()
st.write(seznam_cen)

st.markdown("""
---
Pokud bych chtěl získat seznam jídel a cen, tak bych napsal:
```
jidla = {
    "hamburger": 99,
    "pizza": 149,
    "sendvič": 59
    }
seznam_jidel_a_cen = jidla.items()
st.write(seznam_jidel_a_cen)
```
A dostanu dvojice klíč-hodnota (hlouběji se na seznamy a n-tice podíváme později):
""")
jidla = {
    "hamburger": 99,
    "pizza": 149,
    "sendvič": 59
    }
seznam_jidel_a_cen = jidla.items()
st.write(seznam_jidel_a_cen)

st.markdown("""
---
Pokud bych chtěl znát hodnotu ceny ale chci tam také specifikovat, co se stane, když klíč není v seznamu, tak bych napsal:
```
jidla = {
    "hamburger": 99,
    "pizza": 149,
    "sendvič": 59
    }
pizza = jidla.get("pizza")
st.write(f"Cena pizzy je {pizza}")

kebab = jidla.get("kebab", 100)
st.write(f"Cena pizzy je {kebab}")
```
""")
jidla = {
    "hamburger": 99,
    "pizza": 149,
    "sendvič": 59
    }
pizza = jidla.get("pizza")
st.write(f"Cena pizzy je {pizza}")


kebab = jidla.get("kebab", 100)
st.write(f"Cena kebabu je {kebab}")

st.markdown("""
----
Pokud bych chtěl smazat záznam tak můžu použít dva způsoby:
```
jidla = {
    "hamburger": 99,
    "pizza": 149,
    "sendvič": 59
    }
del jidla["pizza"]
st.write(jidla)
```
""")
jidla = {
    "hamburger": 99,
    "pizza": 149,
    "sendvič": 59
    }
del jidla["pizza"]
st.write(jidla)

st.markdown("""
nebo pomocí:
```
jidla = {
    "hamburger": 99,
    "pizza": 149,
    "sendvič": 59
    }
jídla.pop("sendvič")
st.write(jídla)
```
""")
jidla = {
    "hamburger": 99,
    "pizza": 149,
    "sendvič": 59
    }
jidla.pop("sendvič")
st.write(jidla)

st.markdown("""
----
Pojďme si to procvičit na příkladu. \\
Představte si, že máme dneska slovník s jídly a jejich cenami:
```
poledni_menu = {
    "hamburger": 99,
    "pizza": 149,
    "sendvič": 59,
    "kebab": 89,
    "pho": 79,
    "řízek": 119,
    "knedlo-vepřo-zelo": 139
    }
```
""")
poledni_menu = {
    "hamburger": 99,
    "pizza": 149,
    "sendvič": 59,
    "kebab": 89,
    "pho": 79,
    "řízek": 119,
    "knedlo-vepřo-zelo": 139
    }
st.markdown("""
### Úkol 1
Pomocí `[]` získejte cenu sendviče a vypište ji.
""")
if st.toggle("Zobrazit řešení", key = "reseni_1"):
    ### Úkol 1
    sendvic = poledni_menu["sendvič"]
    st.write(f"Cena sendviče je {sendvic}")

    if st.toggle("Zobrazit kód", key = "kod_1"):
        st.code("""
            ### Úkol 1
            sendvic = poledni_menu["sendvič"]
            st.write(f"Cena sendviče je {sendvic}")
            """)

st.markdown("""
---
### Úkol 2
Pomocí `get()` získejte cenu steaku a pokud to nenajde tak vypište 500
""")
if st.toggle("Zobrazit řešení", key = "reseni_2"):
    ### Úkol 2
    steak = poledni_menu.get("steak", 500)
    st.write(f"Cena steaku je {steak}")

    if st.toggle("Zobrazit kód", key = "kod_2"):
        st.code("""
            ### Úkol 2
            steak = poledni_menu.get("steak", 500)
            st.write(f"Cena steaku je {steak}")
            """)

st.markdown("""
---
### Úkol 3
Pomocí [] přidejte do menu položku kuřecí nudle za 99 a vypište nové menu.
""")
if st.toggle("Zobrazit řešení", key = "reseni_3"):
    ### Úkol 3
    poledni_menu["kuřecí nudle"] = 99
    st.write(poledni_menu)

    if st.toggle("Zobrazit kód", key = "kod_3"):
        st.code("""
            ### Úkol 3
            poledni_menu["kuřecí nudle"] = 99
            st.write(poledni_menu)
            """)

st.markdown("""
---
### Úkol 4
Vypište mi všechny položky v menu tedy názvy jídel.
""")
if st.toggle("Zobrazit řešení", key = "reseni_4"):
    ### Úkol 4
    polozky = poledni_menu.keys()
    st.write(polozky)

    if st.toggle("Zobrazit kód", key = "kod_4"):
        st.code("""
            ### Úkol 4
            polozky = poledni_menu.keys()
            st.write(polozky)
            """)
st.markdown("""

### Úkol 5
Vypište všechny ceny v menu.
""")
if st.toggle("Zobrazit řešení", key = "reseni_5"):
    ### Úkol 5
    ceny = poledni_menu.values()
    st.write(ceny)

    if st.toggle("Zobrazit kód", key = "kod_5"):
        st.code("""
            ### Úkol 5
            ceny = poledni_menu.values()
            st.write(ceny)
            """)
st.markdown("""
---
### Úkol 6
Vypište mi všechny položky a ceny v menu.
""")
if st.toggle("Zobrazit řešení", key = "reseni_6"):
    ### Úkol 6
    polozky_a_ceny = poledni_menu.items()
    st.write(polozky_a_ceny)

    if st.toggle("Zobrazit kód", key = "kod_6"):
        st.code("""
            ### Úkol 6
            polozky_a_ceny = poledni_menu.items()
            st.write(polozky_a_ceny)
            """)

st.markdown("""
---
### Úkol 7
Smažte položku hamburger z menu a vypište nové menu.
""")
if st.toggle("Zobrazit řešení", key = "reseni_7"):
    ### Úkol 7
    del poledni_menu["hamburger"]
    st.write(poledni_menu)

    if st.toggle("Zobrazit kód", key = "kod_7"):
        st.code("""
            ### Úkol 7
            del poledni_menu["hamburger"]
            st.write(poledni_menu)
            """)

st.markdown("""
---
### Vnořené slovníky
Slovníky mohou být vnořené, což znamená, že můžeme mít slovník uvnitř slovníku. \\
Např. pokud budu mít restaurace a pro každou restauraci budu mít informace ohledně jejich menu tak to bude vypadat takto:
```
restaurace = {
    "KFC" : {
        "kuřecí křidélka": 99,
        "kuřecí strips": 129
        },
    "McDonalds" : {
        "hamburger": 79,
        "cheeseburger": 89
        }
    }
```
Pak tedy pokud se chci dostat na cenu kuřecího stripsu tak musím: 
```
cena_kfc_kureci_strips = restaurace["KFC"]["kuřecí strips"]
st.write(f"Cena kuřecího stripsu v KFC je {cena_kfc_kureci_strips}")
```
Tedy pak dostanu tento výsledek.
""")

restaurace = {
    "KFC" : {
        "kuřecí křidélka": 99,
        "kuřecí strips": 129
        },
    "McDonalds" : {
        "hamburger": 79,
        "cheeseburger": 89
        }
    }
cena_kfc_kureci_strips = restaurace["KFC"]["kuřecí strips"]
st.write(f"Cena kuřecího stripsu v KFC je {cena_kfc_kureci_strips}")

st.markdown("""
---
Pojďme si to procvičit na příkladu.
### Úkol 8
Vytvořte slovník s názvem `restaurace` a do něj vložte následující data:
Budete mít 3 restaurace a jejich následájící menu:
- Bilbo
    - Řizek za 100
    - Vepřový guláš za 120
- Lagarto
    - Avokádový toast za 130
    - Tacos za 150
- Panda
    - Sushi za 200
    - Ramen za 180
""")
restaurace = {
    "Bilbo" : {
        "řízek": 100,
        "vepřový guláš": 120
        },
    "Lagarto" : {
        "avokádový toast": 130,
        "tacos": 150
        },
    "Panda" : {
        "sushi": 200,
        "ramen": 180
        }
    }
if st.toggle("Zobrazit řešení", key = "reseni_8"):
    ### Úkol 8
    st.write(restaurace)

    if st.toggle("Zobrazit kód", key = "kod_8"):
        st.code("""
            ### Úkol 8
            restaurace = {
                "Bilbo" : {
                    "řízek": 100,
                    "vepřový guláš": 120
                    },
                "Lagarto" : {
                    "avokádový toast": 130,
                    "tacos": 150
                    },
                "Panda" : {
                    "sushi": 200,
                    "ramen": 180
                    }
                }
            st.write(restaurace)
            """)

st.markdown("""
---
### Úkol 9
Máte menu z minulého úkolu. Zjistěte cenu avokádového toastu v restauraci Lagarto.
""")
if st.toggle("Zobrazit řešení", key = "reseni_9"):
    ### Úkol 9
    cena_avokadovy_toast = restaurace["Lagarto"]["avokádový toast"]
    st.write(f"Cena avokádového toastu v Lagarto je {cena_avokadovy_toast}")

    if st.toggle("Zobrazit kód", key = "kod_9"):
        st.code("""
            ### Úkol 9
            cena_avokadovy_toast = restaurace["Lagarto"]["avokádový toast"]
            st.write(f"Cena avokádového toastu v Lagarto je {cena_avokadovy_toast}")
            """)

st.markdown("""
---
### Úkol 10
Máte menu z minulého úkolu. Přidejte do restaurace Bilbo nové jídlo řízek s bramborem za 150.
""")
if st.toggle("Zobrazit řešení", key = "reseni_10"):
    ### Úkol 10
    restaurace["Bilbo"]["řízek s bramborem"] = 150
    st.write(restaurace)

    if st.toggle("Zobrazit kód", key = "kod_10"):
        st.code("""
            ### Úkol 10
            restaurace["Bilbo"]["řízek s bramborem"] = 150
            st.write(restaurace)
            """)

st.markdown("""
---
### Úkol 11
Máte menu z minulého úkolu. Smažte z restaurace Panda položku sushi.
""")
del restaurace["Panda"]["sushi"]
if st.toggle("Zobrazit řešení", key = "reseni_11"):
    ### Úkol 11
    st.write(restaurace)

    if st.toggle("Zobrazit kód", key = "kod_11"):
        st.code("""
            ### Úkol 11
            del restaurace["Panda"]["sushi"]
            st.write(restaurace)
            """)
st.markdown("""
---
### Úkol 12
Máte menu z minulého úkolu. Vypište všechny restaurace.
""")
if st.toggle("Zobrazit řešení", key = "reseni_12"):
    ### Úkol 12
    restaurace_nazvy = restaurace.keys()
    st.write(restaurace_nazvy)
    if st.toggle("Zobrazit kód", key = "kod_12"):
        st.code("""
            ### Úkol 12
            restaurace_nazvy = restaurace.keys()
            st.write(restaurace_nazvy)
            """)

st.markdown("""
---
### Úkol 13
Máte menu z minulého úkolu. Vypište všechny jídla v restauraci Lagarto.
""")
if st.toggle("Zobrazit řešení", key = "reseni_13"):
    ### Úkol 13
    jidla_lagarto = restaurace["Lagarto"].keys()
    st.write(jidla_lagarto)

    if st.toggle("Zobrazit kód", key = "kod_13"):
        st.code("""
            ### Úkol 13
            jidla_lagarto = restaurace["Lagarto"].keys()
            st.write(jidla_lagarto)
            """)

st.markdown("""
---
### Úkol 14
Máte menu z minulého úkolu. Vypište všechny ceny v restauraci Bilbo.
""")
if st.toggle("Zobrazit řešení", key = "reseni_14"):
    ### Úkol 14
    st.write(restaurace)
    ceny_bilbo = restaurace["Bilbo"].values()
    st.write(ceny_bilbo)

    if st.toggle("Zobrazit kód", key = "kod_14"):
        st.code("""
            ### Úkol 14
            ceny_bilbo = restaurace["Bilbo"].values()
            st.write(ceny_bilbo)
            """)

st.markdown("""
---
### Úkol 15
Máte menu z minulého úkolu. Vypište všechny jídla a ceny v restauraci Panda.
""")
if st.toggle("Zobrazit řešení", key = "reseni_15"):
    ### Úkol 15
    jidla_a_ceny_panda = restaurace["Panda"].items()
    st.write(jidla_a_ceny_panda)

    if st.toggle("Zobrazit kód", key = "kod_15"):
        st.code("""
            ### Úkol 15
            jidla_a_ceny_panda = restaurace["Panda"].items()
            st.write(jidla_a_ceny_panda)
            """)

st.markdown("""
---
Pojďme nyní zkombinovat se streamlit komponenty. 

### Úkol 16
Máte menu z minulého úkolu. Chcete od uživatele jak položku tak i cenu. Tuto položku přidáte tlačítkem st.button do menu restaurace Panda
a poté si nechte vypsat nové menu.
""")
if st.toggle("Zobrazit řešení", key = "reseni_16"):
    ### Úkol 16
    polozka = st.text_input("Zadejte název položky", key = "polozka_16")
    cena = st.number_input("Zadejte cenu položky", key = "cena_16")
    if st.button("Přidat položku"):
        restaurace["Panda"][polozka] = cena
        st.write(restaurace)

    if st.toggle("Zobrazit kód", key = "kod_16"):
        st.code("""
            ### Úkol 16
            polozka = st.text_input("Zadejte název položky")
            cena = st.number_input("Zadejte cenu položky")
            if st.button("Přidat položku"):
                restaurace["Panda"][polozka] = cena
                st.write(restaurace)
            """)

st.markdown("""
---
### Úkol 17
Máte menu z minulého úkolu. 
Nechte si ho vypsat. \\
Chcete od uživatele jméno restaurace a název jídla a po stisknutí tlačítka st.button se vypíše cena tohoto jídla.
""")
if st.toggle("Zobrazit řešení", key = "reseni_17"):
    ### Úkol 17
    st.write(restaurace)
    restaurace_jmeno = st.text_input("Zadejte název restaurace", key = "restaurcae_17")
    jidlo = st.text_input("Zadejte název jídla", key = "jidlo_17")
    if st.button("Zjistit cenu"):
        cena = restaurace[restaurace_jmeno][jidlo]
        st.write(f"Cena jídla {jidlo} v restauraci {restaurace_jmeno} je {cena}")

    if st.toggle("Zobrazit kód", key = "kod_17"):
        st.code("""
            ### Úkol 17
            st.write(restaurace)
            restaurace_jmeno = st.text_input("Zadejte název restaurace")
            jidlo = st.text_input("Zadejte název jídla")
            if st.button("Zjistit cenu"):
                cena = restaurace[restaurace_jmeno][jidlo]
                st.write(f"Cena jídla {jidlo} v restauraci {restaurace_jmeno} je {cena}")
            """)

st.markdown("""
---
Trochu zatočíme a ukážeme si skvělou funkci try a except. \\
Pokud se vám někdy stane, že se vám program zastaví kvůli chybě, tak můžete použít try a except, 
které vám umožní zachytit chybu a pokračovat dál. \\
Např v předchozím příkladu když bych zadal nesprávné jméno restaurace nebo napsali špatný jméno jídla tak by mi to vyhodilo chybu. \\
Pokud chci tuto chybu zachytit tak můžu napsat:
```
st.write(restaurace)
restaurace_jmeno = st.text_input("Zadejte název restaurace")
jidlo = st.text_input("Zadejte název jídla")
if st.button("Zjistit cenu"):
    try:
        cena = restaurace[restaurace_jmeno][jidlo]
        st.write(f"Cena jídla {jidlo} v restauraci {restaurace_jmeno} je {cena}")
    except:
        st.write("Něco se pokazilo")
```
""")
st.write(restaurace)
restaurace_jmeno = st.text_input("Zadejte název restaurace", key = "restaurace_17_try")
jidlo = st.text_input("Zadejte název jídla", key = "jidlo_17_try")
if st.button("Zjistit cenu", key = "button_17_try"):
    try:
        cena = restaurace[restaurace_jmeno][jidlo]
        st.write(f"Cena jídla {jidlo} v restauraci {restaurace_jmeno} je {cena}")
    except:
        st.write("Něco se pokazilo")

st.markdown("""
---
Toto jenom používejte opatrně a s rozmyslem. \\
Může se stát, že chybu nezachytíte a program bude pokračovat dál a může se stát, že se vám to zasekne. \\
Používejte to tedy jenom tam, kde je to opravdu potřeba. \\
Pojďme si to zkusit na příkladu.
### Úkol 18
Máte menu z minulého úkolu.
Nechte si ho vypsat. \\
Chcete od uživatele jméno restaurace a chcete vypsat všechna jídla v této restauraci. \\
Pokud se něco pokazí tak vypište "Něco se pokazilo".
""")
if st.toggle("Zobrazit řešení", key = "reseni_18"):
    st.write(restaurace)
    restaurace_jmeno = st.text_input("Zadejte název restaurace", key = "restaurace_18_try")
    if st.button("Zjistit jídla", key= "button_18_try"):
        try:
            jidla = restaurace[restaurace_jmeno].keys()
            st.write(jidla)
        except:
            st.write("Něco se pokazilo")
    if st.toggle("Zobrazit kód", key = "kod_18"):
        st.code("""
            ### Úkol 18
            st.write(restaurace)
            restaurace_jmeno = st.text_input("Zadejte název restaurace")
            if st.button("Zjistit jídla"):
                try:
                    jidla = restaurace[restaurace_jmeno].keys()
                    st.write(jidla)
                except:
                    st.write("Něco se pokazilo")
            """)

st.markdown("""
---
Nyní do toho všeho zkusíme dát ještě podmínky. \\

### Úkol 19
Máte menu z minulého úkolu. \\
Nechte si ho vypsat. \\
Chcete od uživatele jméno restaurace. \\
Pokud jméno restaurace je v seznamu tak vypište všechna jídla v této restauraci. \\
Pokud jméno restaurace není v seznamu tak vypište "Restaurace není v seznamu".
""")
if st.toggle("Zobrazit řešení", key = "reseni_19"):
    st.write(restaurace)
    restaurace_jmeno = st.text_input("Zadejte název restaurace", key = "restaurace_19_try")
    if st.button("Zjistit jídla", key= "button_19_try"):
        if restaurace_jmeno in restaurace:
            jidla = restaurace[restaurace_jmeno].keys()
            st.write(jidla)
        else:
            st.write("Restaurace není v seznamu")
    if st.toggle("Zobrazit kód", key = "kod_19"):
        st.code("""
            ### Úkol 19
            st.write(restaurace)
            restaurace_jmeno = st.text_input("Zadejte název restaurace")
            if st.button("Zjistit jídla"):
                if restaurace_jmeno in restaurace:
                    jidla = restaurace[restaurace_jmeno].keys()
                    st.write(jidla)
                else:
                    st.write("Restaurace není v seznamu")
            """)

st.markdown("""
---
Vidíte, že nemusíte již používat try a except. Toto je také jeden způsobů, jak to udělat. \\
Try a Except jsou spíš jedny z pokročilejších funkcí, které se hodí, když víte, že se může něco pokazit a pokud
jsou případy, kdy if-else na to nestačí. Pokud ale if-else stačí tak je lepší použít if-else. \\
""")

st.markdown("""
---
### Úkol 20
Máte menu z minulého úkolu. \\
Chcete od uživate název jídla a cenu do menu restaurace Bilbo. \\
Pokud je jídlo již v menu tak vypište "Jídlo je již v menu". \\
Pokud není a cena je větší než 0 a vypište nové menu.
Pokud není a cena je rovno 0 vypište "Cena musí být větší než 0.
""")
if st.toggle("Zobrazit řešení", key = "reseni_20"):
    polozka = st.text_input("Zadejte název položky", key = "polozka_20")
    cena = st.number_input("Zadejte cenu položky", key = "cena_20")
    if st.button("Přidat položku", key = "button_20"):
        if polozka in restaurace["Bilbo"]:
            st.write("Jídlo je již v menu")
        elif cena > 0:
            restaurace["Bilbo"][polozka] = cena
            st.write(restaurace)
        else:
            st.write("Cena musí být větší než 0")

    if st.toggle("Zobrazit kód", key = "kod_20"):
        st.code("""
            ### Úkol 20
            polozka = st.text_input("Zadejte název položky")
            cena = st.number_input("Zadejte cenu položky")
            if st.button("Přidat položku"):
                if polozka in restaurace["Bilbo"]:
                    st.write("Jídlo je již v menu")
                elif cena > 0:
                    restaurace["Bilbo"][polozka] = cena
                    st.write(restaurace)
                else:
                    st.write("Cena musí být větší než 0")
            """)

st.markdown("""
---
### Úkol 21
Máte menu z minulého úkolu. \\
Chcete od uživatele název jídla a cenu do menu restaurace McDonalds. \\
Pokud je jídlo již v menu tak vypište "Jídlo je již v menu". \\
Pokud není a cena je větší než 20 a vypište nové menu.
Pokud není a cena je menší než 20 vypište "Cena musí být větší než 20.
""")
if st.toggle("Zobrazit řešení", key = "reseni_21"):
    polozka = st.text_input("Zadejte název položky", key = "polozka_21")
    cena = st.number_input("Zadejte cenu položky", key = "cena_21")
    if st.button("Přidat položku", key = "button_21"):
        if polozka in restaurace["McDonalds"]:
            st.write("Jídlo je již v menu")
        elif cena > 0:
            restaurace["McDonalds"][polozka] = cena
            st.write(restaurace)
        else:
            st.write("Cena musí být větší než 0")

    if st.toggle("Zobrazit kód", key = "kod_21"):
        st.code("""
            ### Úkol 21
            polozka = st.text_input("Zadejte název položky")
            cena = st.number_input("Zadejte cenu položky")
            if st.button("Přidat položku"):
                if polozka in restaurace["McDonalds"]:
                    st.write("Jídlo je již v menu")
                elif cena > 0:
                    restaurace["McDonalds"][polozka] = cena
                    st.write(restaurace)
                else:
                    st.write("Cena musí být větší než 0")
            """)

