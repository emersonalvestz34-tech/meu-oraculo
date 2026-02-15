import streamlit as st
import random

# Configuração da página - Isso remove o menu padrão e deixa mais profissional
st.set_page_config(page_title="Oráculo Pop Nuvem", page_icon="☁️", layout="centered")

# CSS Personalizado para o fundo ficar limpo e as fontes bonitas
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        border: 2px solid #0078ff;
        background-color: white;
        color: #0078ff;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #0078ff;
        color: white;
    }
    .quote-box {
        padding: 20px;
        background-color: white;
        border-radius: 15px;
        border-left: 5px solid #0078ff;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("☁️ Oráculo Estoico")
st.subheader("Pop Nuvem: Sabedoria para o dia a dia")

frases = [
    {"autor": "Marco Aurélio", "texto": "A nossa vida é o que os nossos pensamentos a constroem."},
    {"autor": "Sêneca", "texto": "Muitas vezes sofremos mais na imaginação do que na realidade."},
    {"autor": "Epicteto", "texto": "Não espere que os eventos aconteçam como você deseja. Deseje que eles aconteçam como acontecem."},
    {"autor": "Sêneca", "texto": "Apressa-te a viver bem e pensa que cada dia é, por si só, uma vida inteira."}
]

if st.button("✨ CONSULTAR ORÁCULO"):
    escolhida = random.choice(frases)
    st.markdown(f"""
    <div class="quote-box">
        <p style='font-size: 20px; font-style: italic;'>"{escolhida['texto']}"</p>
        <p style='text-align: right; font-weight: bold;'>— {escolhida['autor']}</p>
    </div>
    """, unsafe_allow_html=True)
    st.balloons() # Efeito de festa quando clica!

st.caption("© Pop Nuvem - Sabedoria Digital")
