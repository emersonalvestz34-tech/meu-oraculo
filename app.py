import streamlit as st
import random
import wikiquote

# 1. Configuração da página
st.set_page_config(page_title="Oráculo Estoico", page_icon="☁️")

# 2. CSS para Cor e Fundo (Garantindo que apareça no Pop Nuvem)
st.markdown("""
    <style>
    .stApp {
        background: url("https://images.unsplash.com/photo-1534796636912-3b95b3ab5986?auto=format&fit=crop&w=1920&q=80");
        background-size: cover;
        background-position: center;
    }
    h1, p, span, blockquote, .stMarkdown, [data-testid="stCaptionContainer"] {
        color: white !important;
    }
    blockquote {
        border-left: 3px solid #0078ff !important;
        background: rgba(255, 255, 255, 0.1);
        padding: 10px 20px;
    }
    .stButton button p { color: black !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("☁️ Oráculo Estoico Diário")
st.write("Respire fundo e peça uma perspectiva para o seu dia.")

# Suas frases originais (Plano B caso a internet falhe)
frases_originais = [
    {"autor": "Marco Aurélio", "texto": "A nossa vida é o que os nossos pensamentos a constroem."},
    {"autor": "Sêneca", "texto": "Muitas vezes sofremos mais na imaginação do que na realidade."},
    {"autor": "Epicteto", "texto": "Não espere que os eventos aconteçam como você deseja. Deseje que eles aconteçam como acontecem."},
    {"autor": "Marco Aurélio", "texto": "A melhor vingança é não ser como o seu inimigo."},
    {"autor": "Sêneca", "texto": "Apressa-te a viver bem e pensa que cada dia é, por si só, uma vida inteira."}
]

if 'clique' not in st.session_state:
    st.session_state.clique = False

if not st.session_state.clique:
    if st.button("Receber Sabedoria"):
        # Tenta buscar na internet
        try:
            autores = ["Sêneca", "Marco Aurélio", "Epicteto"]
            autor_escolhido = random.choice(autores)
            # Busca com limite de tempo (timeout)
            lista = wikiquote.quotes(autor_escolhido, lang='pt')
            
            if lista and len(lista) > 0:
                st.session_state.txt = random.choice(lista)
                st.session_state.aut = autor_escolhido
            else:
                raise Exception("Lista vazia")
        except:
            # Se der QUALQUER erro na internet, usa o seu banco de dados original
            reserva = random.choice(frases_originais)
            st.session_state.txt = reserva['texto']
            st.session_state.aut = reserva['autor']
        
        st.session_state.clique = True
        st.rerun()
else:
    # Exibição no modelo que você gosta
    st.markdown(f"> \"{st.session_state.txt}\"")
    st.caption(f"— **{st.session_state.aut}**")
    if st.session_state.aut in ["Seneca", "Marcus Aurelius", "Epictetus"]:
    st.write("🌐 Origem: Internet")
else:
    st.write("🏠 Origem: Banco de Dados Local")
    st.success("Reflita sobre isso hoje.")
    st.warning("Você já recebeu sua dose de sabedoria. Volte amanhã! ✨")

st.divider()
st.info("Ferramenta exclusiva do blog Pop Nuvem.")

