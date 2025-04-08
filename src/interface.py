import streamlit as st
from qa_chain import build_qa_chain

st.set_page_config(page_title="LegisIA - Assistente Jurídico", page_icon="⚖️")

st.title("⚖️ LegisIA - Assistente Jurídico Inteligente")

st.markdown("""
Digite uma pergunta sobre a Constituição Federal de 1988.
""")

query = st.text_input("Sua pergunta:", placeholder="Ex: Quais são os direitos fundamentais garantidos pela CF?")

if query:
    try:
        with st.spinner("Consultando os documentos legais..."):
            qa_chain = build_qa_chain()

            result = qa_chain.invoke({"query": query})

            st.markdown("### 📜 Resposta:")
            st.write(result['result'])

            with st.expander("🔍 Fontes utilizadas"):
                for doc in result['source_documents']:
                    source = doc.metadata.get('source', 'Desconhecida')
                    st.markdown(f"- **Fonte:** `{source}`")
    except Exception as e:
        st.error(f"Ocorreu um erro ao processar a consulta: {str(e)}")
