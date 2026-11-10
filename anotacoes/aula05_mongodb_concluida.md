# Aula 05 - Configurando MongoDB

## Objetivo
Configurar um banco MongoDB para os quatro
microservicos da aplicacao Burger App.

## Ambiente utilizado
- MongoDB Community Server 8.0
- Docker Desktop
- Python 3.11
- PyMongo
- python-dotenv

## Banco
Nome: burguer_app_db
Endereco: mongodb://127.0.0.1:27018/
Container: alura-burger-mongodb
Volume: alura-burger-mongodb-data

## Microservicos configurados
- auth-service
- order-service
- product-service
- user-service

## Validacoes realizadas
- Conexao MongoDB: aprovada
- Gravacao de documento: aprovada
- Leitura de documento: aprovada
- Remocao do registro de teste: aprovada
- Pytest: 29 testes aprovados
- Ruff: aprovado

## Observacoes
O banco e executado localmente com Docker.
Nao foi necessario utilizar MongoDB Atlas.

Os arquivos .env foram configurados e protegidos
contra inclusao acidental no Git.

Os testes completos das funcionalidades Flask
serao desenvolvidos nas proximas aulas.

## Situacao
AULA CONCLUIDA.
