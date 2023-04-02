import streamlit as st

'''
Napište aplikaci, která vám dovolí vybrat si jednu ze 3 možností:
st.selectbox()/st.radio()
1. Čtverec
2. Obdelnik
3. Kvádr
A podle toho Vám umožní, zadat parametry:
if-else + number_input
1. Ctvrec - 1 strana
2. Obdelnik - 1 poloměr
3. Kvádr - 2 strany
A také podle toho mi vrátíte výsledek:
1. Obsah a obvod
2. Obsah a obvod
3. Objem a plochu a součet hran
'''

st.header('Moje aplikace')
tvar = st.selectbox('Vyberte si tvar', ['čtverec', 'obdélník', 'kvádr'])
if tvar == 'čtverec':
    strana_ctverce = st.number_input('Zadejte stranu čtverce', min_value = 0.5)
    st.text(f'Obsah je {strana_ctverce**2} a Obvod  je {strana_ctverce*4}')
elif tvar == 'obdélník':
    strana_a = st.number_input('Zadejte stranu a obdélníku', min_value = 1)
    strana_b = st.number_input('Zadejte stranu b obdélknu', min_value = 1)
    st.text(f'Obsah je {strana_a * strana_b} a Obvod  je {2*(strana_a+strana_b)}')
elif tvar == 'kvádr':
    strana_a = st.number_input('Zadejte stranu a obdélníku', min_value = 1)
    strana_b = st.number_input('Zadejte stranu b obdélknu', min_value = 1)
    strana_c = st.number_input('Zadejte stranu c obdélníku', min_value = 1)
    st.text(f'Plocha je {2*(strana_a*strana_b+strana_a*strana_c+strana_b*strana_c)} a Objem  je {strana_a*strana_b*strana_c}, a součet hran je {4*(strana_a + strana_b + strana_c)}')
