Teste de Nivelamento - Desenvolvimento FullStack (Vue.js + Flask)

Este repositório contém uma aplicação web desenvolvida como parte de um processo de nivelamento técnico, implementando:
✅ Backend em Python/Flask para processamento de dados
✅ Frontend em Vue.js para interface de busca
✅ API RESTful com integração Postman
📋 Requisitos do Teste

Desenvolver uma solução completa para consulta de operadoras de saúde cadastradas na ANS (Agência Nacional de Saúde Suplementar), atendendo aos seguintes critérios:
Tarefas Implementadas

1. Processamento de Dados
  - tilização do arquivo CSV fornecido (Relatorio_cadop.csv) como fonte de dados
  - Tratamento de dados faltantes e normalização

2. Backend (Flask)
  - Rota /buscar para consulta textual nas colunas Nome_Fantasia e Razao_Social
  
    
## 🗂 Estrutura do Projeto
```
/SimpleSearch/
| backend/
├── app.py # Servidor Flask
├── Relatorio_cadop.csv # Dados das operadoras
├── frontend/
│ ├── src/
│ │ ├── components/
│ │ │ └── Search.vue # Componente de busca
│ │ └── ...
│ └── ...
├── README.md
```
3. Frontend (Vue.js)
- Interface responsiva com campo de busca e listagem de resultados
- Feedback visual para:
    Carregamento
    Erros
    Resultados vazios

## 🚀 Como Executar o Projeto
Pré-requisitos
Python 3.8+
Node.js 14+
Vue CLI 

### Passo a Passo
### 1. Backend
```bash
# Instale as dependências
pip install flask pandas flask-cors

# Execute o servidor (porta 5000)
python app.py
 ```
 ### 2. Frontend
 ```bash
# Instale as dependências
 npm install

# Execute o servidor de desenvolvimento (porta 8080)
npm run serve
```
### 3. Acesse a aplicação
  Abra no navegador:
  🔗 http://localhost:xxxx
## 📱 Screenshots
![Capturar](https://github.com/user-attachments/assets/a82405a1-56fc-4b5c-9ca5-f84c2d94d9ba)

[Teste API.postman_collection.json](https://github.com/user-attachments/files/19479367/Teste.API.postman_collection.json)


## Observação

Este projeto faz parte de um teste de nivelamento técnico e não deve ser utilizado para outros fins sem autorização. Todos os dados utilizados são públicos e fornecidos pela ANS.
