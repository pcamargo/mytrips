import streamlit as st
import pandas as pd

st.title("❄️ Comparador de Viagem — Argentina x Chile")
st.subheader("📅 27 de junho a 05 de julho | 👨‍👩‍👧‍👦 4 adultos e 1 criança")

st.markdown("---")

# ======================
# Dados principais
# ======================
data = {
    "Categoria": [
        "Passagens Aéreas",
        "Hospedagem",
        "Alimentação",
        "Carro Alugado",
        "Passeios",
        "Experiência para Criança",
        "Custo Total Geral"
    ],
    "🇦🇷 Buenos Aires": [2, 2, 2, 2, 2, 4, 2],
    "🇨🇱 Santiago": [3, 3, 3, 3, 3, 5, 4]
}

df = pd.DataFrame(data)

# ======================
# Layout em colunas
# ======================
col1, col2 = st.columns(2)

with col1:
    st.header("🇦🇷 Argentina — Buenos Aires")
    st.markdown("""
    **Perfil ideal:**  
    ✔️ Melhor custo-benefício  
    ✔️ Passeios urbanos e bate-voltas leves  
    ✔️ Excelente gastronomia  
    ✔️ Clima frio confortável  

    **Passeios de carro:**
    - Tigre e Delta do Paraná
    - Estância argentina (almoço + show)
    - La Plata
    - Palermo, Recoleta, Puerto Madero

    **Clima:** 8°C a 15°C  
    **Moeda:** Peso Argentino (vantagem com câmbio paralelo)
    """)

with col2:
    st.header("🇨🇱 Chile — Santiago")
    st.markdown("""
    **Perfil ideal:**  
    ✔️ Neve e paisagens alpinas  
    ✔️ Estrutura turística moderna  
    ✔️ Vinhos e frutos do mar  

    **Passeios de carro:**
    - Valle Nevado / Farellones
    - Cajón del Maipo
    - Viña del Mar e Valparaíso

    **Clima:** 5°C a 14°C  
    **Moeda:** Peso Chileno (economia estável)
    """)

st.markdown("---")

# ======================
# Tabela comparativa
# ======================
st.header("📊 Comparativo de Custos")
st.dataframe(df, use_container_width=True)

st.markdown("---")

# ======================
# Custos estimados
# ======================
st.header("💰 Estimativa de Custos Totais (5 pessoas)")

costs = pd.DataFrame({
    "Item": ["Passagens", "Hospedagem (8 noites)", "Carro + Combustível", "Alimentação", "Passeios"],
    "Argentina (R$)": ["6.000 – 11.000", "4.000 – 7.200", "1.800 – 3.000", "2.500 – 4.000", "1.500 – 2.500"],
    "Chile (R$)": ["7.000 – 13.000", "5.200 – 8.800", "2.500 – 4.000", "3.200 – 5.000", "2.000 – 3.500"]
})

st.dataframe(costs, use_container_width=True)

st.markdown("---")

# ======================
# Conclusão
# ======================
st.header("🏆 Recomendação Final")

st.success("""
**Melhor opção para esse grupo e datas:** 🇦🇷 **ARGENTINA**

✔️ Menor custo total  
✔️ Mais conforto para idosos  
✔️ Passeios menos cansativos  
✔️ Gastronomia excelente  
✔️ Logística mais simples com carro  

👉 Chile só é mais indicado se o **foco principal for neve**.
""")

st.markdown("---")

# ======================
# Data ideal
# ======================
st.header("📅 Melhor período de Julho")

st.info("""
✅ **27/06 a 05/07 é ideal**
- Neve já presente
- Menos movimento
- Preços melhores que a segunda quinzena
- Melhor experiência para famílias
""")
