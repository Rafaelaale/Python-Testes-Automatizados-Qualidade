# Aula 12 - Centralizacao dos testes com pytest.ini

## Objetivo

Automatizar os argumentos do Pytest por meio
de um arquivo de configuracao no auth-service.

## Arquivo criado

burger-app/burguer-app/auth-service/pytest.ini

## Configuracoes

testpaths = test
Localiza os testes dentro da pasta test.

pythonpath = .
Disponibiliza os modulos do microservico.

-v
Exibe detalhes de cada teste.

--disable-warnings
Reduz avisos exibidos durante a execucao.

--cov=models
Mede a cobertura dos modelos.

--cov=controllers
Mede a cobertura dos controladores.

--cov=services
Mede a cobertura dos servicos.

--cov=config
Mede a cobertura das configuracoes.

--cov-report=term-missing
Apresenta linhas executaveis nao cobertas.

--cov-fail-under=80
Exige cobertura minima de 80%.

## Diferenca entre teste e cobertura

Um teste pode passar e o percentual de
cobertura do microservico permanecer baixo.

Isso nao significa que o teste esteja errado.

Significa que outras partes do codigo
ainda precisam de testes automatizados.

## Execucao

No diretorio auth-service:

python -m pytest

O pytest.ini aplica as opcoes automaticamente.

## Observacao

Nao alterar o codigo original apenas para
atingir artificialmente a meta de cobertura.

Os testes do microservico devem ser ampliados
nas proximas aulas.
