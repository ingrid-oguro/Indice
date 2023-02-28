import pandas as pd
import numpy as np
import streamlit as st
import altair as alt

import pip
pip.main(["install", "openpyxl"])
PAGE_CONFIG = {"page_title": "Indicadores", "page_icon": ":globe_with_meridians:", "layout": "wide"}
st.set_page_config(**PAGE_CONFIG)

base = pd.read_excel('base/codperlet_graduação.xlsx')
base_turma = pd.read_excel('base/codperlet_turma.xlsx')
codperlet = pd.read_excel('base/codperlet.xlsx')
#

cursos_grad = ['Administração', 'Ciências Econômicas','Direito','Engenharia de Produção','Engenharia de Computação']

base = base.query('HABILITACAO == @cursos_grad')
base_turma = base_turma.query('HABILITACAO == @cursos_grad')
st.title('Índice de Evasão por Semestre')
st.title('Turma')
curso = sorted(base_turma.HABILITACAO.unique())
curso_selecionado = st.selectbox('Graduação',curso)
df = base_turma.query('HABILITACAO == @curso_selecionado ')

turma = sorted(df.CODTURMA.unique())
turma_selecionada = st.selectbox('Turma',turma)
df1 = df.query('CODTURMA == @turma_selecionada ')

df1['%'] = df1['%'].fillna(0)
df1['%'] = df1['%'] *100
a = alt.Chart(df1).mark_line().encode(
    x='CODPERLET:O',
    y='%'
)
st.altair_chart(a, use_container_width=True)

with st.expander("Ver base"):
    st.dataframe(df1.style.format({"CODPERLET": "{:.0f}"}))

#CURSO

#base_grad = grad.groupby(["CODPERLET","COMPLEMENTO"])[["Evasão","Inconsistencia","Permanencia","Total","%"]].mean().reset_index()
st.title('Graduação')
base['%'] = base['%'].fillna(0)

curso2 = sorted(base.HABILITACAO.unique())
cursos2 = ['Todos']
cursos2.extend(curso2)
curso_selecionado2 = st.selectbox('Graduação:',cursos2)

#df2 = base.query('COMPLEMENTO == @curso_selecionado02 ')

df2 = codperlet
if 'Todos' not in curso_selecionado2: 
    df2 = base.query('HABILITACAO == @curso_selecionado2 ')

df2['%'] = df2['%']*100

b = alt.Chart(df2).mark_line().encode(
    x='CODPERLET:O',
    y='%'
)
st.altair_chart(b, use_container_width=True)

with st.expander("Ver base"):
    st.dataframe(df2.style.format({"CODPERLET": "{:.0f}"}))














