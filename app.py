import streamlit as st
import random
import wikiquote

# 1. Configuração da página
st.set_page_config(page_title="Oráculo Estoico", page_icon="☁️")

# 2. CSS para Plano de Fundo e Leitura Perfeita
st.markdown("""
    <style>
    /* Imagem de fundo de estrelas */
    .stApp {
        background: url("https://images.unsplash.com/photo-1534796636912-3b95b3ab5986?auto=format&fit=crop&w=1920&q=80");
        background-size: cover;
        background-position: center;
    }

    /* Títulos e textos fora da caixa em branco com sombra para destacar */
    h1, p {
        color: white !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
    }

    /* O QUADRO DA FRASE - Fundo branco sólido para leitura máxima */
    blockquote {
        background-color: rgba(255, 255, 255, 0.98) !important;
        padding: 25px !important;
        border-radius: 12px !important;
        border-left: 8px solid #0078ff !important;
        box-shadow: 0px 10px 25px rgba(0,0,0,0.4) !important;
        margin: 20px 0 !important;
    }

    /* Texto da frase em preto dentro da caixa branca */
    blockquote p {
        color: #1e272e !important;
        font-size: 22px !important;
        font-weight: 500 !important;
        text-shadow: none !important;
        line-height: 1.4 !important;
    }

    /* Estilo para o Autor e Rodapé */
    .stCaption {
        color: #f0f2f6 !important;
        font-size: 16px !important;
        font-weight: bold !important;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.5);
    }
    
    /* Cor do texto dentro dos botões (para não ficar branco no cinza) */
    .stButton button p { color: black !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("☁️ Oráculo Estoico Diário")
st.write("Respire fundo e peça uma perspectiva para o seu dia.")

# 3. Frases de Reserva (Plano B caso a internet falhe)
frases_originais = [
    {"autor": "Marco Aurélio", "texto": "A nossa vida é o que os nossos pensamentos a constroem."},
    {"autor": "Sêneca", "texto": "Muitas vezes sofremos mais na imaginação do que na realidade."},
    {"autor": "Epicteto", "texto": "Não espere que os eventos aconteçam como você deseja. Deseje que eles aconteçam como acontecem."},
    {"autor": "Marco Aurélio", "texto": "A melhor vingança é não ser como o seu inimigo."},
    {"autor": "Sêneca", "texto": "Apressa-te a viver bem e pensa que cada dia é, por si só, uma vida inteira."}
]

# 4. Lógica de Clique Único (Sessão)
if 'clique_feito' not in st.session_state:
    st.session_state.clique_feito = False

if not st.session_state.clique_feito:
    if st.button("Receber Sabedoria"):
        try:
            # Tenta buscar frases reais da internet
            autores = ["Seneca", "Marcus Aurelius", "Epictetus"]
            autor_sorteado = random.choice(autores)
            lista_internet = wikiquote.quotes(autor_sorteado, lang='pt')
            
            if lista_internet and len(lista_internet) > 0:
                st.session_state.txt_exibir = random.choice(lista_internet)
                st.session_state.aut_exibir = autor_sorteado
            else:
                raise Exception("Internet vazia")
        except:
            # Se a internet der erro, usa suas frases originais
            reserva = random.choice(frases_originais)
            st.session_state.txt_exibir = reserva['texto']
            st.session_state.aut_exibir = reserva['autor']
        
        st.session_state.clique_feito = True
        st.rerun()
else:
    # 5. Exibição no seu modelo favorito (Markdown com ">")
    st.markdown(f"> \"{st.session_state.txt_exibir}\"")
    st.caption(f"— **{st.session_state.aut_exibir}**")
    
    st.success("Reflita sobre isso hoje.")
    st.warning("Você já consultou o oráculo agora. Volte em breve! ✨")

st.divider()
st.info("Ferramenta exclusiva do blog Pop Nuvem.")
