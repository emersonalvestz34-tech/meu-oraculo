import streamlit as st
import random
import wikiquote

# 1. Configuração da página
st.set_page_config(page_title="Oráculo Estoico", page_icon="☁️")

# 2. Plano de fundo e ajuste de cor para o SEU modelo ficar visível
st.markdown("""
    <style>
    .stApp {
        background: url("https://images.unsplash.com/photo-1534796636912-3b95b3ab5986?auto=format&fit=crop&w=1920&q=80");
        background-size: cover;
        background-position: center;
    }
    /* Deixa o texto do seu markdown e caption brancos para ler no fundo escuro */
    .stMarkdown p, blockquote, .stCaption { 
        color: white !important; 
        border-left-color: #0078ff !important; 
    }
    h1, p { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("☁️ Oráculo Estoico Diário")
st.write("Respire fundo e peça uma perspectiva para o seu dia.")

# --- LÓGICA DE UM CLIQUE E CONTEÚDO DA INTERNET ---
if 'foi' not in st.session_state:
    st.session_state.foi = False

if not st.session_state.foi:
    if st.button("Receber Sabedoria"):
        try:
            autores = ["Seneca", "Marcus Aurelius", "Epictetus"]
            autor_sorteado = random.choice(autores)
            lista = wikiquote.quotes(autor_sorteado, lang='pt')
            
            if lista:
                st.session_state.txt = random.choice(lista)
                st.session_state.aut = autor_sorteado
            else:
                st.session_state.txt = "A nossa vida é o que os nossos pensamentos a constroem."
                st.session_state.aut = "Marco Aurélio"
            
            st.session_state.foi = True
            st.rerun()
        except:
            st.error("Erro ao conectar. Tente novamente.")
else:
    # --- EXATAMENTE O SEU MODELO DE EXIBIÇÃO ---
    st.markdown(f"> \"{st.session_state.txt}\"")
    st.caption(f"— **{st.session_state.aut}**")
    
    st.success("Reflita sobre isso hoje. Como você pode aplicar esse pensamento agora?")
    st.warning("Você já recebeu sua sabedoria de hoje. Volte amanhã!")

st.divider()
st.info("Ferramenta exclusiva do blog Pop Nuvem.")
