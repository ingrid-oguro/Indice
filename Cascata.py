import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go
import pip
pip.main(["install", "openpyxl"])

base_w = pd.read_excel('indice01.xlsx')
#st.write(base_w.HABILITACAO.unique())

curso3 = sorted(base_w.HABILITACAO.unique())
#curso_selecionado3 = st.selectbox('Graduação :',curso3)
#df3 = base_w.query('COMPLEMENTO == @curso_selecionado3 ')

#Base Total
base02 = base_w.drop(columns=['HABILITACAO'])
a02 = base02.drop_duplicates()
cont02 = a02.groupby('CODPERLET')['RA'].sum().reset_index()
cont02['Diferença'] = cont02['RA'].diff()

curso3 = sorted(base_w.HABILITACAO.unique())
cursos3 = ['Todos','Administração','Ciências Econômicas','Engenharia de Computação','Engenharia de Produção','Direito']
#cursos3.extend(curso3)
curso_selecionado3 = st.selectbox('Graduação:',cursos3)
df3 = cont02
if 'Todos' not in curso_selecionado3: 
    df3 = base_w.query('HABILITACAO == @curso_selecionado3 ')



df3['Diferença'] = df3['RA'].diff()

start = df3['CODPERLET'].min()
end = df3['CODPERLET'].max()

conditionlist = [(df3['CODPERLET'] == start),
                 (df3['CODPERLET'] == end),
            (df3['CODPERLET'] != start) & (df3['CODPERLET'] != end)]
choicelist   = ['absolute', 'total', 'relative']
df3['measure'] = np.select(conditionlist, choicelist,
                          default='absolute')
#df3=base_w
fig3  = go.Figure()
fig3.add_trace(go.Waterfall(
               x = df3['CODPERLET'], y = df3['Diferença'],
               measure = df3['measure'],
               base = 0,
               text = df3['Diferença'],
               textposition = 'outside',
               decreasing = {"marker":{"color":"crimson",                 
                  "line":{"color":"lightsalmon","width":2}}},
               increasing = {"marker":{"color":"forestgreen",
                  "line":{"color":"lightgreen", "width":2}}},
               totals     = {"marker":{"color":"mediumblue"}}
               ))
fig3.update_xaxes(type='category')
st.plotly_chart(fig3, use_container_width=True)


#with st.expander("Ver base"):
#    st.dataframe(base_w.style.format({"CODPERLET": "{:.0f}"}))



