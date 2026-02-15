import streamlit as st
import random

# Banco de dados de sabedoria
frases = [
    {"autor": "Marco Aurélio", "texto": "A nossa vida é o que os nossos pensamentos a constroem."},
    {"autor": "Sêneca", "texto": "Muitas vezes sofremos mais na imaginação do que na realidade."},
    {"autor": "Epicteto", "texto": "Não espere que os eventos aconteçam como você deseja. Deseje que eles aconteçam como acontecem."},
    {"autor": "Marco Aurélio", "texto": "A melhor vingança é não ser como o seu inimigo."},
    {"autor": "Sêneca", "texto": "Apressa-te a viver bem e pensa que cada dia é, por si só, uma vida inteira."}
]

# Configuração da página (Aparência do Pop Nuvem)
st.set_page_config(page_title="Oráculo Estoico", page_icon="☁️")

st.title("☁️ Oráculo Estoico Diário")
st.write("Respire fundo e peça uma perspectiva para o seu dia.")

if st.button("Receber Sabedoria"):
    escolhida = random.choice(frases)
    st.markdown(f"> \"{escolhida['texto']}\"")
    st.caption(f"— **{escolhida['autor']}**")
    
    # Mensagem motivadora extra
    st.success("Reflita sobre isso hoje. Como você pode aplicar esse pensamento agora?")

st.divider()
st.info("Ferramenta exclusiva do blog Pop Nuvem.")