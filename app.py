import streamlit as st
import random
import time

# Configuração da página
st.set_page_config(page_title="Oráculo Pop Nuvem", page_icon="☁️")

# CSS para colocar a imagem de fundo e estilizar os elementos
st.markdown("""
    <style>
    /* Imagem de fundo cobrindo toda a tela */
    .stApp {
        background: url("https://images.unsplash.com/photo-1534796636912-3b95b3ab5986?auto=format&fit=crop&w=1920&q=80");
        background-size: cover;
        background-position: center;
    }

    /* Caixa da citação com transparência (Glassmorphism) */
    .quote-box {
        padding: 25px;
        background: rgba(255, 255, 255, 0.85);
        border-radius: 20px;
        border: 2px solid #00d2ff;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        backdrop-filter: blur(4px);
        margin-top: 20px;
        color: #1e272e;
    }

    /* Estilo do botão */
    .stButton>button {
        width: 100%;
        border-radius: 50px;
        border: none;
        background: linear-gradient(90deg, #00d2ff 0%, #3a7bd5 100%);
        color: white;
        font-weight: bold;
        padding: 15px;
        font-size: 18px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 5px 15px rgba(0,210,255,0.4);
    }

    /* Títulos em branco para destacar no fundo escuro */
    h1, h2, h3, p {
        color: white !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("☁️ Oráculo Pop Nuvem")
st.write("Conecte-se com a sabedoria estóica e veja além das nuvens.")

frases = [
    {"autor": "Marco Aurélio", "texto": "A nossa vida é o que os nossos pensamentos a constroem."},
    {"autor": "Sêneca", "texto": "Muitas vezes sofremos mais na imaginação do que na realidade."},
    {"autor": "Epicteto", "texto": "Não espere que os eventos aconteçam como você deseja. Deseje que eles aconteçam como acontecem."},
    {"autor": "Sêneca", "texto": "Apressa-te a viver bem e pensa que cada dia é, por si só, uma vida inteira."},
    {"autor": "Marco Aurélio", "texto": "A melhor vingança é não ser como o seu inimigo."}
]

if st.button("✨ CONSULTAR SABEDORIA"):
    # Efeito "Pensando" (Substitui os balões)
    with st.spinner('🌌 Consultando as estrelas e os antigos...'):
        time.sleep(1.5) # Simula um tempo de reflexão
    
    escolhida = random.choice(frases)
    
    # Exibição da frase
    st.markdown(f"""
    <div class="quote-box">
        <p style='font-size: 22px; font-style: italic; color: #2c3e50 !important; text-shadow: none;'>
            "{escolhida['texto']}"
        </p>
        <p style='text-align: right; font-weight: bold; color: #3a7bd5 !important; text-shadow: none;'>
            — {escolhida['autor']}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Pequena mensagem de calma
    st.info("Respire fundo e leve este pensamento com você hoje.")

st.markdown("<br><p style='text-align: center; font-size: 12px;'>POP NUVEM • CONEXÃO ESTÓICA</p>", unsafe_allow_html=True)
