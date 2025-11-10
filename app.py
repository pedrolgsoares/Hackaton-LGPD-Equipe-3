import os
import fitz  # PyMuPDF
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import PyMuPDFLoader

# === 0. Corrigir conflito de bibliotecas OpenMP ===
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# === 1. Carregar variáveis de ambiente ===
load_dotenv()

st.set_page_config(page_title="ChatPDF com RAG", layout="wide")

# === 2. Função de autenticação ===
def autenticar(usuario, senha):
    usuario_correto = os.getenv("APP_USER", "admin")
    senha_correta = os.getenv("APP_PASS", "1234")
    return usuario == usuario_correto and senha == senha_correta

# === 3. Controle de sessão ===
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False
if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = None

# === 4. Tela de login ===
if not st.session_state.autenticado:
    st.title("🔐 Login de Acesso")

    usuario = st.text_input("Usuário:")
    senha = st.text_input("Senha:", type="password")

    if st.button("Entrar"):
        if autenticar(usuario, senha):
            st.session_state.autenticado = True
            st.success("✅ Login realizado com sucesso!")
            st.rerun()
        else:
            st.error("❌ Usuário ou senha incorretos.")
    st.stop()

# === 5. Tela principal ===
st.title("📄 Chat de auxílio jurídico")

# === 6. Carregar automaticamente PDFs após login ===
docs_path = "docs"
os.makedirs(docs_path, exist_ok=True)
pdf_files = [f for f in os.listdir(docs_path) if f.lower().endswith(".pdf")]

if not pdf_files:
    st.warning("⚠️ Nenhum PDF encontrado na pasta `docs/`. Coloque os arquivos lá e recarregue a página.")
    st.stop()

# === 7. Montar o vetorstore apenas uma vez ===
if st.session_state.rag_chain is None:
    st.info("⏳ Processando documentos... aguarde um momento.")

    all_docs = []
    for pdf in pdf_files:
        file_path = os.path.join(docs_path, pdf)
        loader = PyMuPDFLoader(file_path)
        all_docs.extend(loader.load())

    splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=100
    )
    texts = splitter.split_documents(all_docs)

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(texts, embeddings)

    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 4})
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    st.session_state.rag_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    st.success("✅ PDFs carregados e processados com sucesso!")

# === 8. Interface de perguntas ===
st.markdown("### ❓ Pergunte algo sobre os documentos:")

user_question = st.text_input("Digite sua pergunta:")

if user_question:
    with st.spinner("🔍 Consultando o conteúdo dos documentos..."):
        resposta = st.session_state.rag_chain.invoke({"query": user_question})

    st.markdown("### 🧠 Resposta:")
    st.write(resposta["result"])

    with st.expander("📚 Fontes consultadas"):
        for i, doc in enumerate(resposta["source_documents"]):
            st.markdown(f"**Trecho {i+1}:**")
            st.write(doc.page_content)
