import streamlit as st
import random
import wikiquote

# 1. Configuração da página
st.set_page_config(page_title="Oráculo Estoico", page_icon="☁️")

# 2. CSS Corrigido para COR e FUNDO
st.markdown("""
    <style>
    /* Imagem de fundo */
    .stApp {
        background: url("https://images.unsplash.com/photo-1534796636912-3b95b3ab5986?auto=format&fit=crop&w=1920&q=80");
        background-size: cover;
        background-position: center;
    }

    /* FORÇAR COR BRANCA EM TUDO: Títulos, parágrafos, blockquotes e legendas */
    h1, h2, h3, p, li, div, span, blockquote, .stMarkdown, [data-testid="stCaptionContainer"] {
        color: white !important;
    }

    /* Ajuste da barra lateral do blockquote (o ">" do seu código) */
    blockquote {
        border-left: 3px solid #0078ff !important;
        background: rgba(255, 255, 255, 0.1); /* Um leve fundo para ajudar a ler */
        padding: 10px 20px;
    }
    
    /* Manter o texto dos botões e alertas legíveis */
    .stButton button p { color: black !important; }
    .stSuccess p, .stInfo p, .stWarning p { color: #155724 !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("☁️ Oráculo Estoico Diário")
st.write("Respire fundo e peça uma perspectiva para o seu dia.")

# --- LÓGICA DE TRAVA E CONTEÚDO AUTOMÁTICO ---
if 'clique_realizado' not in st.session_state:
    st.session_state.clique_realizado = False

if not st.session_state.clique_realizado:
    if st.button("Receber Sabedoria"):
        try:
            # Busca da internet
            autores = ["Seneca", "Marcus Aurelius", "Epictetus"]
            autor_escolhido = random.choice(autores)
            lista_quotes = wikiquote.quotes(autor_escolhido, lang='pt')
            
            if lista_quotes:
                st.session_state.txt_dia = random.choice(lista_quotes)
                st.session_state.aut_dia = autor_escolhido
            else:
                # Se falhar, usa as suas frases originais como plano B
                backup = [
                    {"autor": "Marco Aurélio", "texto": "A nossa vida é o que os nossos pensamentos a constroem."},
                    {"autor": "Sêneca", "texto": "Muitas vezes sofremos mais na imaginação do que na realidade."}
                ]
                escolhida = random.choice(backup)
                st.session_state.txt_dia = escolhida['texto']
                st.session_state.aut_dia = escolhida['autor']
            
            st.session_state.clique_realizado = True
            st.rerun()
        except:
            st.error("Erro na conexão. Tente novamente.")
else:
    # --- SEU MODELO ORIGINAL DE EXIBIÇÃO ---
    st.markdown(f"> \"{st.session_state.txt_dia}\"")
    st.caption(f"— **{st.session_state.aut_dia}**")
    
    st.success("Reflita sobre isso hoje. Como você pode aplicar esse pensamento agora?")
    st.warning("Você já consultou o oráculo hoje. Volte amanhã! ✨")

st.divider()
st.info("Ferramenta exclusiva do blog Pop Nuvem.")
