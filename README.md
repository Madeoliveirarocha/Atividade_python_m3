📌 README – API FastAPI + Cliente Python
🚀 Sobre o Projeto

Este projeto tem como objetivo aplicar conceitos básicos de comunicação entre cliente e servidor, utilizando:

FastAPI para criação da API

Uvicorn como servidor ASGI

Requests para consumo da API pelo cliente Python

A API possui dois endpoints principais:

GET /status → retorna um JSON indicando que o servidor está ativo

POST /eco → recebe um JSON e devolve o mesmo conteúdo

📁 Estrutura do Projeto
Trabalho_python_final/
│── server.py      # Código do servidor FastAPI
│── client.py      # Script cliente que consome a API
│── README.md      # Este arquivo

📦 Pré-requisitos

Antes de rodar o projeto, instale as dependências:

python -m pip install fastapi uvicorn requests

▶️ Executando o Servidor

No terminal, dentro da pasta do projeto:

python -m uvicorn server:app --reload


Se estiver usando o Python instalado em C:\Python312:

C:\Python312\python.exe -m uvicorn server:app --reload


O servidor ficará disponível em:

👉 http://127.0.0.1:8000

📌 Endpoints da API
✔ GET /status

Resposta:

{
  "status": "ok"
}

✔ POST /eco

Exemplo de envio:

{
  "message": "Olá servidor!",
  "value": 123
}


Resposta:

{
  "message": "Olá servidor!",
  "value": 123
}

🧪 Testando a API pelo Navegador

O FastAPI oferece documentação automática:

👉 http://127.0.0.1:8000/docs

Lá você pode testar todos os endpoints sem escrever código.

💻 Executando o Cliente Python

Com o servidor rodando, execute:

python client.py


O resultado esperado:

Status: {'status': 'ok'}
Eco: {'message': 'Teste do cliente', 'value': 99}

🧠 Tecnologias Utilizadas

Python 3.12

FastAPI

Uvicorn

Requests

✨ Autor

Matheus Rocha
Projeto desenvolvido para prática de comunicação Cliente ↔ Servidor usando FastAPI.
