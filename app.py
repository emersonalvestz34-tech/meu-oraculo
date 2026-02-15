import streamlit as st
import random
import time

# Configuração da página
st.set_page_config(page_title="Oráculo Pop Nuvem", page_icon="☁️")

# Importando fontes bonitas do Google Fonts
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,400&family=Montserrat:wght@400;700&display=swap');

    /* Imagem de fundo */
    .stApp {
        background: url("https://images.unsplash.com/photo-1534796636912-3b95b3ab5986?auto=format&fit=crop&w=1920&q=80");
        background-size: cover;
        background-position: center;
    }

    /* Caixa de Reflexão - Ajustada para LEITURA MÁXIMA */
    .quote-box {
        padding: 40px;
        background: rgba(255, 255, 255, 0.98); /* Quase sólido para ler bem */
        border-radius: 10px;
        border-top: 5px solid #3a7bd5;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5);
        margin-top: 25px;
        color: #1a1a1a;
        text-align: center;
    }

    /* Estilo do Botão Moderno */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        border: none;
        background: #3a7bd5;
        color: white;
        font-family: 'Montserrat', sans-serif;
        font-weight: 700;
        padding: 15px;
        letter-spacing: 1px;
        transition: 0.4s;
    }
    .stButton>button:hover {
        background: #00d2ff;
        box-shadow: 0 0 20px rgba(0, 210, 255, 0.6);
    }

    /* Títulos e Textos */
    .titulo {
        font-family: 'Playfair Display', serif;
        color: white;
        font-size: 42px;
        text-align: center;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.8);
    }
    
    .subtitulo {
        font-family: 'Montserrat', sans-serif;
        color: #e0e0e0;
        text-align: center;
        margin-bottom: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="titulo">Oráculo Pop Nuvem</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitulo">SABEDORIA ESTÓICA PARA O DIA A DIA</p>', unsafe_allow_html=True)

frases = [
    {"autor": "Marco Aurélio", "texto": "A felicidade da sua vida depende da qualidade dos seus pensamentos."},
    {"autor": "Sêneca", "texto": "Não é que temos pouco tempo, é que perdemos muito dele."},
    {"autor": "Epicteto", "texto": "Não espere que os eventos aconteçam como você deseja. Deseje que eles aconteçam como acontecem."},
    {"autor": "Sêneca", "texto": "A sorte é o que acontece quando a preparação encontra a oportunidade."},
    {"autor": "Marco Aurélio", "texto": "A melhor vingança é não ser como o seu inimigo."}
]

if st.button("BUSCAR REFLEXÃO"):
    with st.spinner('✨ Consultando os antigos...'):
        time.sleep(1.2)
    
    escolhida = random.choice(frases)
    
    # Exibição com fonte bonita e leitura clara
    st.markdown(f"""
    <div class="quote-box">
        <p style='font-family: "Playfair Display", serif; font-size: 26px; font-style: italic; color: #2c3e50 !important; line-height: 1.4;'>
            "{escolhida['texto']}"
        </p>
        <p style='font-family: "Montserrat", sans-serif; font-size: 14px; font-weight: 700; color: #3a7bd5 !important; margin-top: 20px; text-transform: uppercase; letter-spacing: 2px;'>
            — {escolhida['autor']}
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><p style='text-align: center; color: white; font-size: 10px; opacity: 0.7;'>POP NUVEM • FERRAMENTA INTERATIVA</p>", unsafe_allow_html=True)
