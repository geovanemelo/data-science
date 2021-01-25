import pandas as pd
import streamlit as st

#carregando arquivos
df = pd.read_csv("datasets/criminalidade_sp_2.csv")

#dashbord

st.title("Criminalidade em São Paulo")
st.markdown(
    """
     É de senso comum que em grande maioria das cidades brasileiras, a violencia é presente de diversas maneiras em todos dias e horarios nas vidas dos cidadões. Nesse estudo, com a ajuda da Ciência de Dados vamos entender melhor o que acontece e propor algumas sujestões para redução da **criminalidade**
    """
)

#informaçao

st.sidebar.info("foram carregadas {} linhas".format(df.shape[0]))

if st.sidebar.checkbox("VER DADOS DE ENTRADA"):
    st.header("Dados de entrada")
    st.write(df)


df.time = pd.to_datetime(df.time)
ano_selecionado = st.sidebar.slider("Selecione um ano", 2010, 2018, 2015)
df_selected = df[df.time.dt.year == ano_selecionado]

st.subheader("Mapa da criminalidade")
st.map(df_selected)#é necessario de a coluna latitude e longitude
