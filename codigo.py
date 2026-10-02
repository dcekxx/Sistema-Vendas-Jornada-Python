# Fazer um dashboard
# Título - sistema de vendas
# Seção cadastrar vendas
    # Campo Data
    # Campo Vendedor - Ana, Bruno, Carla
    # Campo Produto - Notebook, Fone, Celular
    # Campo Quantidade
    # Campo Valor
    # Botão Cadastrar Venda
        # Quando eu clicar no botão -> adicionar a venda na tabela
# Seção Venda Cadastrada
    # Tabela com as Vendas
# Seção Dashboard
    # Card/Metrica -> Faturamento Total
    # Gráfico de Barra/Coluna -> Venda por vendedor
    # Gráfico de Pizza -> Venda por Produto

# pip install streamlit plotly pandas (tem que ter instalado todos esses pacotes)
# streamlit run codigo.pypython 

import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar a base de dados (ou o arquivo que estão os dados)
tabela_vendas = pd.read_csv("vendas.csv")

st.write("# Sistema de Vendas")


# Seção de cadastro de vendas
# Para colocar tudo na barra lateral, é só utilizar o "sidebar."
st.sidebar.write("## Cadastrar Vendas")

#st.write("## Cadastrar Vendas")

data = st.sidebar.date_input("Data")

vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"])

produto = st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone"])

quantidade = st.sidebar.number_input("Quantidade", step=1) # step = 1 é para o valor na tabela aumentar de 1 em 1 como números inteiros

valor = st.sidebar.number_input("Valor")

botao_cadastrar = st.sidebar.button("Cadastrar Venda") #botao_cadastrar

# Lógica de cadastro
if botao_cadastrar:
    nova_venda = [str(data), vendedor, produto, quantidade, valor] #str antes de data é para transformar a data como texto str é string
    ultima_linha = len(tabela_vendas) #len é para pegar o tamanho da tabela, ou seja, quantas linhas ela tem
    tabela_vendas.loc[ultima_linha] = nova_venda
    tabela_vendas.to_csv("vendas.csv", index=False)
    print(nova_venda)
    st.success("Venda cadastrada!")



# Seção de visualizar vendas
st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas) # dataframe é o nome que o pandas e o streamlit carregam e ordenam os dados



# Seção de Dashboard
st.write("## Dashboard")
# Card/Metrica -> Faturamento Total (Somar o valor das vendas)
faturamento = tabela_vendas["valor"].sum()
# o "f" na frente serve para colocar algo na frente do texto no caso foi R$, e depois tem que colocar entre chaves{}
st.metric("Faturamento Total", f"R$ {faturamento}")  

# Gráfico de Barra/Coluna -> Venda por vendedor
# Fazendo um gráfico de barras com a tabela de vendas, no eixo "X" Vendedor, eixo "Y" Valor e Colorir conforme produtos
grafico1 = px.bar(tabela_vendas, x= "vendedor", y= "valor", color="produto")
st.plotly_chart(grafico1)

# Gráfico de Pizza -> Venda por Produto
# O hole é para deixar um furo central no gráfico de pizza ou gráfico de torta, para ficar mais estilizado
grafico2 = px.pie(tabela_vendas, names= "produto", values= "valor", hole=0.5)
st.plotly_chart(grafico2)




