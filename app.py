import streamlit as st

st.set_page_config(page_title="Clavícula Espiritual", layout="centered")

# Login
st.title("Clavícula Espiritual")
username = st.text_input("Usuário")
password = st.text_input("Senha", type="password")
if username == "xango" and password == "ramir17":
    st.success("Login bem-sucedido!")
    theme = st.selectbox("Escolha o tema de fundo", ["Branco", "Preto", "Velas", "Céu", "Umbral"])
    st.write(f"Tema selecionado: {theme}")
    prompt = st.text_input("Pergunte à Clavícula Espiritual:")
    if st.button("Enviar"):
        st.write("Resposta da IA: [Aqui virá sua resposta espiritual personalizada]")
else:
    st.warning("Credenciais incorretas.")