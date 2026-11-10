# Aula 07 - Iniciando testes unitarios com Pytest

## Funcao estudada
auth-service/models/user_model.py
serialize_user(user)

## Casos de teste
1. Usuario completo: preserva os quatro campos.
2. Usuario incompleto: aplica os valores padrao.
3. Entrada invalida: gera AttributeError.

## Conceitos
- Convencao de nomes test_*.py
- Funcoes de teste com prefixo test_
- Uso de assert
- pytest.raises para verificar excecoes
- Isolamento dos testes unitarios

## Observacoes
Os testes nao precisam de MongoDB.
Nenhum dado real e alterado.
O codigo original do professor foi preservado.

## Execucao
python -m pytest -v test/test_user_model.py

Executar dentro de auth-service com o ambiente
virtual da trilha.
