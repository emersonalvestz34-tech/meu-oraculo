import streamlit as st
import random
import wikiquote # Para as frases automáticas

# 1. Configuração da página e Estilo (Adicionei o fundo que você queria)
st.set_page_config(page_title="Oráculo Estoico", page_icon="☁️")

st.markdown("""
    <style>
    .stApp {
        background: url("https://images.unsplash.com/photo-1534796636912-3b95b3ab5986?auto=format&fit=crop&w=1920&q=80");
        background-size: cover;
        background-position: center;
    }
    h1, p, span { color: white !important; }
    .stInfo, .stSuccess { color: black !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("☁️ Oráculo Estoico Diário")
st.write("Respire fundo e peça uma perspectiva para o seu dia.")

# --- LÓGICA DE TRAVA E CONTEÚDO AUTOMÁTICO ---
if 'clicou' not in st.session_state:
    st.session_state.clicou = False

if not st.session_state.clicou:
    if st.button("Receber Sabedoria"):
        try:
            # Busca automático da internet
            autores = ["Seneca", "Marcus Aurelius", "Epictetus"]
            autor_sorteado = random.choice(autores)
            lista = wikiquote.quotes(autor_sorteado, lang='pt')
            
            if lista:
                frase_final = random.choice(lista)
                autor_final = autor_sorteado
            else:
                # Backup se a internet falhar
                frase_final = "A nossa vida é o que os nossos pensamentos a constroem."
                autor_final = "Marco Aurélio"

            # Salva para travar o botão
            st.session_state.clicou = True
            st.session_state.texto = frase_final
            st.session_state.autor = autor_final
            st.rerun()
        except:
            st.error("Erro ao conectar com a sabedoria antiga. Tente novamente.")
else:
    # --- O MODELO QUE VOCÊ GOSTA (EXIBIÇÃO) ---
    st.markdown(f"> \"{st.session_state.texto}\"")
    st.caption(f"— **{st.session_state.autor}**")
    
    st.success("Reflita sobre isso hoje. Como você pode aplicar esse pensamento agora?")
    st.warning("Você já consultou o oráculo hoje. Volte amanhã! ✨")

st.divider()
st.info("Ferramenta exclusiva do blog Pop Nuvem.")
