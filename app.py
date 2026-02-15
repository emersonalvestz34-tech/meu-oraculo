import streamlit as st
import wikiquote
import random
from datetime import date

# Configuração da página
st.set_page_config(page_title="Oráculo Pop Nuvem", page_icon="☁️")

# Estilo original com plano de fundo
st.markdown("""
    <style>
    .stApp {
        background: url("https://images.unsplash.com/photo-1534796636912-3b95b3ab5986?auto=format&fit=crop&w=1920&q=80");
        background-size: cover;
        background-position: center;
    }
    .quote-box {
        padding: 20px;
        background-color: white;
        border-radius: 15px;
        border-left: 5px solid #0078ff;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.5);
        color: #333;
    }
    h1, p, span { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("☁️ Oráculo Estoico Diário")
st.write("A sabedoria dos antigos, buscada agora na rede.")

# Lógica de clique único (por sessão de navegador)
if 'clicou' not in st.session_state:
    st.session_state.clicou = False

if not st.session_state.clicou:
    if st.button("Receber Minha Sabedoria do Dia"):
        try:
            # Busca frases de um autor estóico aleatório na internet
            autores = ["Seneca", "Marcus Aurelius", "Epictetus"]
            autor_escolhido = random.choice(autores)
            
            # Puxa frases reais da internet (via Wikiquote)
            lista_frases = wikiquote.quotes(autor_escolhido, lang='pt')
            
            if lista_frases:
                frase_final = random.choice(lista_frases)
                
                st.session_state.clicou = True
                st.session_state.frase_do_dia = frase_final
                st.session_state.autor_do_dia = autor_escolhido
                st.rerun() # Atualiza a tela para mostrar a frase e sumir com o botão
            else:
                st.error("Não consegui conectar com a biblioteca agora. Tente novamente.")
        except:
            st.error("Erro ao buscar frase na internet. Verifique sua conexão.")

else:
    # Se já clicou, mostra a frase salva na sessão e esconde o botão
    st.markdown(f"""
    <div class="quote-box">
        <p style='font-size: 20px; font-style: italic; color: #333 !important;'>"{st.session_state.frase_do_dia}"</p>
        <p style='text-align: right; font-weight: bold; color: #0078ff !important;'>— {st.session_state.autor_do_dia}</p>
    </div>
    """, unsafe_allow_html=True)
    st.warning("Você já recebeu sua sabedoria de hoje. Volte amanhã! ✨")

st.divider()
st.write("Ferramenta exclusiva do blog Pop Nuvem.")
