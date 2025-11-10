# 📘 ChatPDF Jurídico com RAG  

Este projeto implementa um **chat inteligente de auxílio jurídico** que permite ao usuário **consultar automaticamente o conteúdo de arquivos PDF** (leis, contratos, jurisprudências, etc.) por meio de **perguntas em linguagem natural**.  
A aplicação utiliza **RAG (Retrieval-Augmented Generation)** com **LangChain**, **FAISS** e **OpenAI GPT**, tudo integrado em uma interface **Streamlit** com autenticação.  

---

## 🚀 Funcionalidades

- 🔐 **Login seguro** com autenticação via variáveis de ambiente.  
- 📂 **Carregamento automático de PDFs** da pasta `docs/`.  
- 🧠 **Geração de respostas contextuais** com base no conteúdo dos documentos.  
- 🗂️ **Busca semântica** de trechos relevantes usando embeddings e FAISS.  
- 💬 **Interface interativa Streamlit**, permitindo perguntar e visualizar fontes consultadas.  

---

## 🏗️ Arquitetura e Fluxo de Execução

Usuário → Interface Streamlit → LangChain RAG → OpenAI GPT → Resposta + Fontes


### Componentes principais:
1. **Autenticação**
   - Usuário e senha definidos via `.env` (ou padrão: admin/1234).  
   - Controle de sessão feito pelo `st.session_state`.

2. **Leitura de PDFs**
   - Leitura com `PyMuPDFLoader` (LangChain Community).  
   - Armazenamento temporário dos textos divididos por blocos (`CharacterTextSplitter`).  

3. **Criação do Vetorstore**
   - Embeddings gerados via `OpenAIEmbeddings`.  
   - Vetores armazenados localmente em **FAISS** para buscas rápidas.  

4. **RAG (Retrieval-Augmented Generation)**
   - Recupera os trechos mais relevantes (`k=4`) e envia ao modelo `gpt-3.5-turbo`.  
   - Retorna resposta + fontes.  

---

## 🧩 Tecnologias Utilizadas

| Categoria | Ferramenta |
|------------|-------------|
| Linguagem | Python 3.10+ |
| Framework Web | Streamlit |
| LLM | OpenAI GPT (via LangChain) |
| Vetorstore | FAISS |
| Document Loader | PyMuPDF (fitz) |
| Gerenciamento de Variáveis | python-dotenv |
| Embeddings | OpenAIEmbeddings |

---

## ⚙️ Instalação e Execução

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/seuusuario/chatpdf-juridico.git
cd chatpdf-juridico
2️⃣ Criar e ativar ambiente virtual
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
.venv\Scripts\activate         # Windows

3️⃣ Instalar dependências
pip install -r requirements.txt

4️⃣ Configurar variáveis de ambiente

Crie um arquivo .env na raiz com o conteúdo:

OPENAI_API_KEY=your_openai_api_key
APP_USER=admin
APP_PASS=1234

5️⃣ Adicionar seus documentos PDF

Crie a pasta docs/ na raiz do projeto e coloque seus PDFs nela:

docs/
├── contrato_trabalho.pdf
├── lei_trabalhista.pdf
└── jurisprudencia_recente.pdf

6️⃣ Executar o aplicativo
streamlit run app.py


Acesse no navegador:
👉 http://localhost:8501
