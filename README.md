# LegisIA - Assistente Jurídico Inteligente

## Descrição

O **LegisIA** é um assistente jurídico inteligente que utiliza **técnicas de Processamento de Linguagem Natural (PLN)** para fornecer respostas sobre a **Constituição Federal de 1988** (CF88) e outros documentos legais. O sistema é baseado em **Language Models** (LLMs) e **técnicas de recuperação de informações** (RAG), com integração ao **Streamlit** para uma interface de usuário interativa.

Este projeto visa facilitar a consulta a textos legais por meio de uma interface simples, permitindo que os usuários façam perguntas sobre a Constituição e recebam respostas contextualizadas.

## Funcionalidades

- **Consulta interativa**: Usuários podem perguntar sobre qualquer artigo ou inciso da Constituição Federal de 1988.
- **Recuperação de documentos legais**: Utiliza um vetorstore (FAISS) para buscar documentos relevantes e fornecer respostas precisas.
- **Interface com Streamlit**: Interface de fácil utilização para interação com o assistente jurídico.

## Tecnologias Usadas

- **Streamlit**: Para criar a interface interativa.
- **Langchain**: Para processamento de linguagem natural e manipulação de embeddings.
- **FAISS**: Para indexação e busca de documentos legais.
- **OpenAI API**: Para gerar embeddings e fornecer respostas baseadas nos dados processados.
- **Google Gemini API**: Para embeddings baseados em IA (se necessário).
- **Python**: Linguagem de programação principal para implementação.

## Instalação

### Requisitos

Antes de rodar o projeto, instale as dependências usando o `pip`. Crie um ambiente virtual (opcional, mas recomendado) e execute o seguinte:

```bash
pip install -r requirements.txt
Arquivos Necessários
.env: Este arquivo deve conter sua chave da API do OpenAI. Exemplo:

ini
Copiar
OPENAI_API_KEY=your-openai-api-key
GOOGLE_API_KEY=your-google-api-key
Dados de entrada: Para rodar o sistema, é necessário ter documentos da Constituição Federal de 1988 ou outro conteúdo legal em PDF. O diretório padrão onde os PDFs são carregados é data/leis.

Rodando o Projeto
Ingestão dos dados: Antes de rodar a interface, execute o script de ingestão para carregar e processar os PDFs:



python src/ingest.py
Rodando a aplicação: Após a ingestão dos dados, execute a aplicação Streamlit:



streamlit run src/interface.py
A interface será acessível em http://localhost:8501.

Estrutura do Projeto


LegisIA/
│
├── src/
│   ├── ingest.py               # Script para processar e gerar o vetorstore
│   ├── qa_chain.py             # Função para criar a cadeia de QA (RAG)
│   └── interface.py            # Interface Streamlit
│
├── data/
│   └── leis/                  # PDFs da Constituição e outros documentos legais
│
├── vectorstore/                # Diretório com o vetorstore FAISS gerado
│
├── .env                        # Arquivo de variáveis de ambiente
├── requirements.txt            # Arquivo com as dependências do projeto
└── README.md                   # Este arquivo
