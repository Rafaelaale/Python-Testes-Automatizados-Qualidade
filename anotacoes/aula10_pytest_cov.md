# Aula 10 - Cobertura de testes com pytest-cov

## Objetivo

Medir a cobertura da funcao serialize_user()
do microservico auth-service.

## Comandos utilizados

python -m pytest -v
python -m pytest --cov=models.user_model
python -m pytest --cov-report=term-missing

## Relatorios

- Terminal: percentual e linhas nao cobertas
- HTML: navegacao visual pelo codigo
- JSON: resultados estruturados

## Interpretacao

Stmts: instrucoes executaveis.
Miss: instrucoes nao cobertas.
Cover: percentual de cobertura.
Missing: linhas nao executadas.

## Observacao

Cobertura de 100% nao garante ausencia de bugs.
A medicao desta aula contempla somente
models.user_model, nao todos os microservicos.

## Arquivos

- auth-service/models/user_model.py
- auth-service/test/test_user_model.py
- resultados/aula10_cobertura/
