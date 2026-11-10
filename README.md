# Python — Testes Automatizados e Qualidade de Código

Projeto de estudos desenvolvido durante a trilha da Alura.

## Conteúdos abordados

- Fundamentos de testes automatizados com Python
- Pytest e fixtures
- Parametrização de testes
- Testes unitários com unittest
- Mock e simulação de dependências
- Testes de integração entre microserviços
- Requisições HTTP e validação de respostas
- Flask e MongoDB
- Análise de complexidade ciclomática com Radon
- Cobertura de testes com pytest-cov
- Integração contínua com GitHub Actions

## Ambiente

- Python 3.12
- VS Code
- PowerShell
- Pytest
- Flask
- MongoDB
- Docker
- GitHub Actions

## Validações realizadas localmente

- Auth Service: 21 testes aprovados.
- Integração User/Order: 5 testes aprovados, com serviços e MongoDB ativos.
- Cobertura do Auth Service: 3,23%, abaixo da meta configurada de 80%.

## Integração contínua

O workflow está em `.github/workflows/auth-service.yml`.

A execução no GitHub Actions depende da disponibilidade das
dependências necessárias. Os testes de integração exigem serviços
HTTP e MongoDB configurados.

## Objetivo

Demonstrar aplicação prática de testes automatizados, qualidade
de código e integração contínua em Python.
