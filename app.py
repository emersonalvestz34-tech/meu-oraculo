import streamlit as st
import random

# 1. Configuração da página
st.set_page_config(page_title="Oráculo Pop Nuvem", page_icon="☁️")

# 2. Adicionando o plano de fundo e ajustando cores básicas
st.markdown("""
    <style>
    /* Imagem de fundo */
    .stApp {
        background: url("https://unsplash.com/pt-br/fotografias/estatua-de-ceramica-verde-de-um-homem-2RRq1BHPq4E");
        background-size: cover;
        background-position: center;
    }

    /* Estilo da caixa de texto para garantir leitura (Branco sólido) */
    .quote-box {
        padding: 20px;
        background-color: white;
        border-radius: 15px;
        border-left: 5px solid #0078ff;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.5);
        color: #333;
    }

    /* Deixando os textos fixos em branco para aparecerem no fundo escuro */
    h1, p, span {
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Título e introdução
st.title("☁️ Oráculo Estoico Diário")
st.write("Respire fundo e peça uma perspectiva para o seu dia.")

# 4. Banco de dados de sabedoria
frases = [
    {"autor": "Marco Aurélio", "texto": "A nossa vida é o que os nossos pensamentos a constroem."},
    {"autor": "Sêneca", "texto": "Muitas vezes sofremos mais na imaginação do que na realidade."},
    {"autor": "Epicteto", "texto": "Não espere que os eventos aconteçam como você deseja. Deseje que eles aconteçam como acontecem."},
    {"autor": "Marco Aurélio", "texto": "A melhor vingança é não ser como o seu inimigo."},
    {"autor": "Sêneca", "texto": "Apressa-te a viver bem e pensa que cada dia é, por si só, uma vida inteira."}
]

# 5. Botão e Lógica (Igual ao primeiro código, sem balões)
if st.button("Receber Sabedoria"):
    escolhida = random.choice(frases)
    
    # Exibição dentro da caixa branca para leitura perfeita
    st.markdown(f"""
    <div class="quote-box">
        <p style='font-size: 20px; font-style: italic; color: #333 !important;'>"{escolhida['texto']}"</p>
        <p style='text-align: right; font-weight: bold; color: #0078ff !important;'>— {escolhida['autor']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("Reflita sobre isso hoje.")

st.divider()
st.write("Ferramenta exclusiva do blog Pop Nuvem.")

