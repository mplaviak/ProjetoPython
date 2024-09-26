import streamlit as st

def main ():
    st.title("Projeto Pipeline")
    nome = st.text_input ("Nome: ")
    data = st.date_input("Data da compra:")
    hora = st.time_input("Horas da compra:")
    preco = st.number_input("Valor da compra")
    qtde = st.number_input("Quantidade de produtos: ")
    produtos = st.selectbox("Produtos", ["Produto 1", "Produto 2", "Produto 3"])

    if st.button("Salvar"):
        st.write("**Dados da Venda*")
        st.write(f"Nome: {nome}")
        st.write(f"Data: {data}")
        st.write(f"Horario: {hora}")
        st.write(f"Valor: {preco}")
        st.write(f"qtde: {qtdee}")
        st.write(f"produtos {produtos}")
        st.write(f"Valor total: {preco * qtde}")


if __name__=="__main__":
    main()
