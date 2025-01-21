# Validação de CPF com Azure Functions

Este projeto implementa um microsserviço serverless para validação de CPFs utilizando Azure Functions e Python. O serviço é altamente escalável, eficiente e pode ser integrado a outras aplicações.

## Funcionalidades

- Validação de CPFs conforme as regras da Receita Federal.
- Resposta em formato JSON.
- Fácil integração com outras aplicações.
- Testes unitários para garantir a qualidade do código.

## Como Usar

### Executando Localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/validacao-cpf.git
   cd validacao-cpf
   cd function
   pip install -r requirements.txt
   func start
   curl "http://localhost:7071/api/validar-cpf?cpf=529.982.247-25"
   Exemplo de Resposta
   Para um CPF válido: {"cpf": "529.982.247-25", "valido": true}
   Para um CPF inválido:{"cpf": "123.456.789-09","valido": false}

## Tecnologias Utilizadas

Python: Linguagem de programação principal.
Azure Functions: Plataforma serverless para execução do microsserviço.
GitHub Actions: Automação de CI/CD.
unittest: Framework para testes unitários.
