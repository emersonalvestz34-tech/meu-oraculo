import streamlit as st
import random

# Configuração da página
st.set_page_config(page_title="Oráculo Pop Nuvem", page_icon="🏛️")

# CSS Avançado para Plano de Fundo e Estética Filosófica
st.markdown("""
    <style>
    /* Plano de fundo em degradê suave (remete ao céu/nuvens e mármore) */
    .stApp {
        background: linear-gradient(180deg, #f5f7fa 0%, #c3cfe2 100%);
    }

    /* Estilização da caixa de texto (Mármore Moderno) */
    .quote-box {
        padding: 30px;
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 5px;
        border-left: 8px solid #2c3e50;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.05);
        margin-top: 20px;
        transition: all 0.5s ease;
    }

    /* Botão Sóbrio e Elegante */
    .stButton>button {
        width: 100%;
        border-radius: 0px;
        border: 1px solid #2c3e50;
        background-color: transparent;
        color: #2c3e50;
        letter-spacing: 2px;
        font-weight: bold;
        padding: 10px;
        transition: 0.4s;
    }
    .stButton>button:hover {
        background-color: #2c3e50;
        color: white;
        border: 1px solid #2c3e50;
    }

    /* Títulos */
    h1 { color: #2c3e50; font-family: 'Georgia', serif; }
    p { color: #34495e; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏛️ Oráculo Estoico")
st.write("Silencie a mente por um instante. O que os antigos têm a lhe dizer?")

frases = [
    {"autor": "Marco Aurélio", "texto": "A felicidade da sua vida depende da qualidade dos seus pensamentos."},
    {"autor": "Sêneca", "texto": "Não é que temos pouco tempo, é que perdemos muito dele."},
    {"autor": "Epicteto", "texto": "Primeiro diga a si mesmo o que você seria; depois faça o que você tem que fazer."},
    {"autor": "Marco Aurélio", "texto": "Tudo o que ouvimos é uma opinião, não um fato. Tudo o que vemos é uma perspectiva, não a verdade."},
    {"autor": "Sêneca", "texto": "A sorte é o que acontece quando a preparação encontra a oportunidade."},
    {"autor": "Zeno de Cítio", "texto": "O bem-estar é alcançado por pequenos passos, mas não é algo pequeno."},
]

if st.button("BUSCAR PERSPECTIVA"):
    escolhida = random.choice(frases)
    # Exibição elegante sem balões ou efeitos infantis
    st.markdown(f"""
    <div class="quote-box">
        <p style='font-size: 22px; font-family: "Georgia", serif; line-height: 1.6; color: #2c3e50;'>
            "{escolhida['texto']}"
        </p>
        <hr style='border: 0; border-top: 1px solid #eee;'>
        <p style='text-align: right; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; color: #7f8c8d;'>
            — {escolhida['autor']}
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br><p style='text-align: center; font-size: 10px; opacity: 0.5;'>POP NUVEM • FILOSOFIA PRÁTICA</p>", unsafe_allow_html=True)
