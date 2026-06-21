# Desafio Técnico - Estágio Python (b2bflow)

Este repositório contém a solução para o desafio técnico de estágio. O script lê contatos de um banco de dados Supabase e envia mensagens personalizadas via Z-API.

## 🚀 Como rodar o projeto

### 1. Configuração da Tabela (Supabase)
Crie uma tabela chamada `contatos` no seu painel do Supabase com as colunas `nome` e `telefone`.

### 2. Variáveis de Ambiente
Crie um arquivo `.env` na raiz do projeto com a seguinte estrutura (substituindo pelas suas chaves):

```text
SUPABASE_URL=seu_url_do_supabase
SUPABASE_KEY=sua_chave_anon_do_supabase
ZAPI_INSTANCE_ID=seu_id_da_instancia_zapi
ZAPI_TOKEN=seu_token_zapi
```
3. Instalação das Dependências
Instale os pacotes necessários utilizando o pip:

```
pip install supabase python-dotenv requests
4. Execução
Para rodar o script, execute:

```
python main.py
```
