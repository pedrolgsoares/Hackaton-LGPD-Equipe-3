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

## 🏗️ PRINTS DAS TELAS

<img width="1915" height="903" alt="Image" src="https://github.com/user-attachments/assets/3e95a55d-54a7-4154-b15f-fa1009684b93" />

<img width="1922" height="907" alt="Image" src="https://github.com/user-attachments/assets/11700936-86dd-451d-bd41-2bc32c4c99f3" />

---

## 🏗️ Arquitetura e Fluxo de Execução

```
Usuário → Interface Streamlit → LangChain RAG → OpenAI GPT → Resposta + Fontes
```

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
git clone https://github.com/pedrolgsoares/Hackaton-LGPD-Equipe-3.git
cd Hackaton-LGPD-Equipe-3
```

### 2️⃣ Criar e ativar ambiente virtual
```bash
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
.venv\Scripts\activate         # Windows
```

### 3️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar variáveis de ambiente
Crie um arquivo `.env` na raiz com o conteúdo:

```env
OPENAI_API_KEY=your_openai_api_key
APP_USER=admin
APP_PASS=1234
```

### 5️⃣ Adicionar seus documentos PDF
Crie a pasta `docs/` na raiz do projeto e coloque seus PDFs nela:
```
docs/
├── contrato_trabalho.pdf
├── lei_trabalhista.pdf
└── jurisprudencia_recente.pdf
```

### 6️⃣ Executar o aplicativo
```bash
streamlit run app.py
```

Acesse no navegador:  
👉 http://localhost:8501  

---

## 🧪 Exemplo de Uso

1. Faça login com seu usuário e senha.  
2. O sistema carregará automaticamente todos os PDFs da pasta `docs/`.  
3. Digite uma pergunta como:
   ```
   Quais são os direitos previstos na CLT sobre jornada de trabalho?
   ```
4. O chatbot responderá com base nos trechos mais relevantes dos documentos.  
5. As fontes consultadas aparecerão em um *expander* abaixo da resposta.  

---

## 🧰 Estrutura de Pastas

```
📂 chatpdf-juridico/
├── app.py                  # Código principal Streamlit
├── .env                    # Variáveis de ambiente
├── requirements.txt        # Dependências do projeto
├── docs/                   # Pasta com PDFs
└── README.md               # Este arquivo
```

---

## 🧠 Conceito RAG (Retrieval-Augmented Generation)

O **RAG** é uma técnica que combina **busca em base de conhecimento** com **geração de texto**.  
Em vez de confiar apenas na memória do modelo, o RAG:
1. Busca os trechos mais relevantes nos documentos (FAISS + embeddings);
2. Fornece esses trechos ao LLM (GPT);
3. Gera uma resposta precisa e contextualizada.  

Essa abordagem é ideal para **assistentes jurídicos**, **chats corporativos** ou **análise de documentos empresariais**.

---

## 🔒 Segurança

- Autenticação simples via `.env`.  
- Dados dos PDFs processados localmente (sem envio para banco externo).  
- OpenAI API utilizada apenas para inferência textual, sem armazenamento de dados.  

---

