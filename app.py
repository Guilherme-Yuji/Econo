import streamlit as st


st.set_page_config(page_title='Estimativa do Fluxo díario de Pessoas',
    layout='wide')

st.write("""
# Processo Seletivo Economapas: Calculadora de Fluxo de pessoas
""")

st.write('Projeto desenvolvido por Guilherme Yuji Fernandes.')

st.subheader('Informe os valores para a realização dos cálculos:')

st.write('')

st.write('1. População Residente')

P1 = float(st.text_input('Total:', value = 0))

P2 = float(st.text_input('Economicamente ativa:', value = 0))

P3 = float(st.text_input('Empregada:', value = 0))

P4 = float(st.text_input('Estudantes:', value = 0))

P5 = float(st.text_input('Crianças:', value = 0))

P6 = float(st.text_input('Adultos:', value = 0))

P7 = float(st.text_input('Idosos', value = 0))

st.write('2. Número de estabelecimentos')

N1 = float(st.text_input('Total: ', value = 0))

N2 = float(st.text_input('Escolas:', value = 0))

N3 = float(st.text_input('Faculdades:', value = 0))

st.text(' ')

if st.button('Calcular'):

	fluxo = (P1 + (P2 + P3 + (P4 + P5)*((N2+N3)/N1) + P6 - P7)*0.7 + N1*0.8)* 0.7

	st.header(f'Fluxo de pessoas: {round(fluxo,2)}')