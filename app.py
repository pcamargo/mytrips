import streamlit as st

st.set_page_config(
    page_title="Planejador de Viagens",
    layout="wide"
)

st.title("🌍 Planejador de Viagens")
st.subheader("Comparação e planejamento detalhado de destinos")

st.markdown("""
Use o menu lateral para navegar entre:
- 📊 Comparativo geral
- 🇦🇷 Planejamento completo da Argentina
- 🇨🇱 Planejamento completo do Chile
""")

st.info("💡 Novos destinos podem ser adicionados criando novos arquivos em `pages/`.")
