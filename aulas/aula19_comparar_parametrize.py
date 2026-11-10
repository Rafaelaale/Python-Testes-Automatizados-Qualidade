"""Aula 19: compara testes tradicionais e parametrizados."""

import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUTH = ROOT / "burger-app" / "burguer-app" / "auth-service"
OUTPUT = ROOT / "resultados" / "aula19_parametrize"
OUTPUT.mkdir(parents=True, exist_ok=True)


def analisar(arquivo):
    """Calcula metricas de um arquivo de testes."""
    codigo = arquivo.read_text(encoding="utf-8-sig")
    arvore = ast.parse(codigo)

    funcoes = [
        node
        for node in arvore.body
        if isinstance(node, ast.FunctionDef)
        and node.name.startswith("test_")
    ]

    cenarios = 0

    for funcao in funcoes:
        quantidade = 1

        for decorator in funcao.decorator_list:
            if not isinstance(decorator, ast.Call):
                continue

            nome = decorator.func

            if not isinstance(nome, ast.Attribute):
                continue

            if nome.attr != "parametrize":
                continue

            if len(decorator.args) < 2:
                continue

            parametros = decorator.args[1]

            if isinstance(parametros, (ast.List, ast.Tuple)):
                quantidade *= len(parametros.elts)

        cenarios += quantidade

    asserts = sum(
        isinstance(node, ast.Assert)
        for node in ast.walk(arvore)
    )

    return {
        "linhas": len(codigo.splitlines()),
        "funcoes": len(funcoes),
        "cenarios": cenarios,
        "asserts": asserts,
    }


def main():
    """Compara os arquivos e produz um relatorio."""
    tradicional = AUTH / "test" / "test_user_model.py"
    parametrizado = (
        AUTH / "test" / "test_user_model_parametrize.py"
    )

    antes = analisar(tradicional)
    depois = analisar(parametrizado)

    reducao_funcoes = (
        (antes["funcoes"] - depois["funcoes"])
        / antes["funcoes"]
        * 100
        if antes["funcoes"]
        else 0
    )

    reducao_linhas = antes["linhas"] - depois["linhas"]

    linhas = [
        "# Aula 19 - Comparacao de testes",
        "",
        "| Metrica | Tradicional | Parametrizado |",
        "|---|---:|---:|",
    ]

    indicadores = [
        ("Funcoes", "funcoes"),
        ("Cenarios", "cenarios"),
        ("Linhas", "linhas"),
        ("Instrucoes assert", "asserts"),
    ]

    for titulo, chave in indicadores:
        linhas.append(
            f"| {titulo} | {antes[chave]} | {depois[chave]} |"
        )

    linhas.extend(
        [
            "",
            f"Reducao de funcoes: {reducao_funcoes:.1f}%",
            f"Diferenca de linhas: {reducao_linhas}",
            "",
            "## Interpretacao",
            "",
            "A parametrizacao concentra varios cenarios",
            "em menos funcoes de teste.",
            "",
            "Uma reducao na quantidade de funcoes",
            "nao implica necessariamente menos linhas.",
            "",
            "Os dois arquivos permanecem preservados.",
            "",
            "As contagens de cenarios sao estaticas;",
            "o Pytest confirma a coleta e execucao.",
            "",
        ]
    )

    relatorio = OUTPUT / "comparacao.md"

    relatorio.write_text(
        "\n".join(linhas),
        encoding="utf-8",
    )

    print("\n===== COMPARACAO REAL =====")
    print(f"Funcoes tradicionais: {antes['funcoes']}")
    print(f"Funcoes parametrizadas: {depois['funcoes']}")
    print(f"Cenarios tradicionais: {antes['cenarios']}")
    print(f"Cenarios parametrizados: {depois['cenarios']}")
    print(f"Linhas tradicionais: {antes['linhas']}")
    print(f"Linhas parametrizadas: {depois['linhas']}")
    print(f"Reducao de funcoes: {reducao_funcoes:.1f}%")
    print(f"Diferenca de linhas: {reducao_linhas}")
    print(f"Relatorio: {relatorio}")


if __name__ == "__main__":
    main()
