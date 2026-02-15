import streamlit as st
import random
import wikiquote

# 1. Configuração da página (Aparência do Pop Nuvem)
st.set_page_config(page_title="Oráculo Estoico", page_icon="☁️")

# 2. Adicionando o plano de fundo e estilos (para ler bem no fundo escuro)
st.markdown("""
    <style>
    .stApp {
        background: url("https://images.unsplash.com/photo-1534796636912-3b95b3ab5986?auto=format&fit=crop&w=1920&q=80");
        background-size: cover;
        background-position: center;
    }
    /* Estilo para a frase aparecer bem nítida */
    .quote-box {
        padding: 20px;
        background-color: white;
        border-radius: 15px;
        border-left: 5px solid #0078ff;
        color: #333;
        margin: 10px 0;
    }
    /* Cores dos textos fora da caixa */
    h1, p, span { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("☁️ Oráculo Estoico Diário")
st.write("Respire fundo e peça uma perspectiva para o seu dia.")

# Inicializa o estado do clique
if 'foi_clicado' not in st.session_state:
    st.session_state.foi_clicado = False

# Lógica do Botão
if not st.session_state.foi_clicado:
    if st.button("Receber Sabedoria"):
        try:
            # Busca frases da internet (Wikiquote)
            autores = ["Seneca", "Marcus Aurelius", "Epictetus"]
            autor = random.choice(autores)
            frases_net = wikiquote.quotes(autor, lang='pt')
            
            if frases_net:
                escolhida_texto = random.choice(frases_net)
                escolhida_autor = autor
            else:
                # Caso a internet falhe, usa as suas frases originais como plano B
                backup = [
                    {"autor": "Marco Aurélio", "texto": "A nossa vida é o que os nossos pensamentos a constroem."},
                    {"autor": "Sêneca", "texto": "Muitas vezes sofremos mais na imaginação do que na realidade."}
                ]
                b = random.choice(backup)
                escolhida_texto, escolhida_autor = b['texto'], b['autor']

            # Salva na sessão para travar o clique
            st.session_state.foi_clicado = True
            st.session_state.texto = escolhida_texto
            st.session_state.autor = escolhida_autor
            st.rerun()
            
        except:
            st.error("Erro ao conectar. Tente novamente em instantes.")
else:
    # Exibe a frase (mesmo estilo que você gostou, mas com a caixa para ler no fundo)
    st.markdown(f"""
    <div class="quote-box">
        <p style='font-size: 20px; font-style: italic; color: #333 !important;'>"{st.session_state.texto}"</p>
        <p style='text-align: right; font-weight: bold; color: #0078ff !important;'>— {st.session_state.autor}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.success("Reflita sobre isso hoje. Como você pode aplicar esse pensamento agora?")
    st.warning("Você já recebeu sua sabedoria de hoje. Volte mais tarde! ✨")

st.divider()
st.info("Ferramenta exclusiva do blog Pop Nuvem.")
