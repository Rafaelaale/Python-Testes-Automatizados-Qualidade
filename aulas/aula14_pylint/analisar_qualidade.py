"""Aula 14: analise e melhoria de qualidade com Pylint."""

import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AUTH = ROOT / "burger-app" / "burguer-app" / "auth-service"
AULA = ROOT / "aulas" / "aula14_pylint"
SAIDA = ROOT / "resultados" / "aula14_pylint"
COPIAS = AULA / "copias"

SAIDA.mkdir(parents=True, exist_ok=True)
COPIAS.mkdir(parents=True, exist_ok=True)


def executar(comando, diretorio=AUTH):
    """Executa ferramenta e devolve codigo e saida."""
    ambiente = os.environ.copy()
    ambiente["PYTHONPATH"] = str(AUTH)

    processo = subprocess.run(
        comando,
        cwd=diretorio,
        env=ambiente,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )

    return processo.returncode, (
        processo.stdout + processo.stderr
    )


def analisar(nome, caminho):
    """Executa Pylint e grava relatorio individual."""
    codigo, texto = executar(
        [
            sys.executable,
            "-m",
            "pylint",
            str(caminho),
            "--output-format=text",
            "--score=y",
        ]
    )

    arquivo = SAIDA / f"{nome}.txt"
    arquivo.write_text(texto, encoding="utf-8")

    notas = re.findall(
        r"rated at (-?\d+(?:\.\d+)?)/10",
        texto,
    )

    nota = notas[-1] if notas else "nao disponivel"

    print(f"\n===== {nome.upper()} =====")
    print(texto.strip() or "Nenhuma mensagem.")
    print(f"Nota Pylint: {nota}/10")
    print(f"Codigo de saida: {codigo}")
    print(f"Relatorio: {arquivo}")

    return nota


def criar_copia(relativo):
    """Copia arquivo de producao sem alterar o original."""
    origem = AUTH / relativo
    destino = COPIAS / relativo

    destino.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    conteudo = origem.read_text(encoding="utf-8-sig")
    destino.write_text(conteudo, encoding="utf-8")

    return destino


def corrigir_modelo(arquivo):
    """Adiciona a quebra de linha final ausente."""
    conteudo = arquivo.read_text(encoding="utf-8")
    arquivo.write_text(
        conteudo.rstrip("\r\n") + "\n",
        encoding="utf-8",
    )


def corrigir_database(arquivo):
    """Documenta modulo e funcao na copia didatica."""
    conteudo = arquivo.read_text(encoding="utf-8")

    conteudo = conteudo.replace("\r\n", "\n")

    # Remove apenas comentarios e linhas vazias
    # anteriores ao primeiro comando Python.
    linhas = conteudo.splitlines(keepends=True)

    while linhas and (
        not linhas[0].strip()
        or linhas[0].lstrip().startswith("#")
    ):
        linhas.pop(0)

    conteudo = "".join(linhas)

    cabecalho = (
        '"""Conexao com o banco de dados MongoDB."""\n\n'
    )

    conteudo = cabecalho + conteudo

    conteudo = conteudo.replace(
        "def get_db():\n",
        (
            "def get_db():\n"
            '    """Retorna a instancia do banco de dados."""\n'
        ),
    )

    arquivo.write_text(
        conteudo.rstrip() + "\n",
        encoding="utf-8",
    )


def organizar_imports(arquivo):
    """Organiza imports da copia usando Ruff."""
    codigo, saida = executar(
        [
            sys.executable,
            "-m",
            "ruff",
            "check",
            str(arquivo),
            "--select",
            "I",
            "--fix",
        ]
    )

    if codigo != 0:
        raise RuntimeError(
            f"Falha ao organizar imports: {saida}"
        )


def main():
    """Analisa originais e compara copias melhoradas."""
    fontes = {
        "modelo": AUTH / "models" / "user_model.py",
        "config": AUTH / "config" / "database.py",
        "controller": (
            AUTH / "controllers" / "auth_controller.py"
        ),
    }

    print("\n1. ANALISE DOS ARQUIVOS ORIGINAIS")

    notas_antes = {}

    for nome, arquivo in fontes.items():
        notas_antes[nome] = analisar(
            f"original_{nome}",
            arquivo,
        )

    print("\n2. CRIANDO COPIAS DE ESTUDO")

    modelo = criar_copia("models/user_model.py")
    database = criar_copia("config/database.py")

    corrigir_modelo(modelo)
    corrigir_database(database)
    organizar_imports(database)

    print(f"Modelo corrigido: {modelo}")
    print(f"Database corrigido: {database}")

    print("\n3. VALIDANDO SINTAXE DAS COPIAS")

    for arquivo in (modelo, database):
        codigo, saida = executar(
            [
                sys.executable,
                "-m",
                "py_compile",
                str(arquivo),
            ]
        )

        if codigo != 0:
            raise RuntimeError(saida)

        print(f"[OK] {arquivo.name}")

    print("\n4. ANALISANDO COPIAS CORRIGIDAS")

    notas_depois = {
        "modelo": analisar(
            "corrigido_modelo",
            modelo,
        ),
        "config": analisar(
            "corrigido_config",
            database,
        ),
    }

    print("\n5. COMPARACAO")

    resumo = ["AULA 14 - COMPARACAO PYLINT", ""]

    for nome in ("modelo", "config"):
        linha = (
            f"{nome}: "
            f"{notas_antes[nome]}/10 -> "
            f"{notas_depois[nome]}/10"
        )

        resumo.append(linha)
        print(linha)

    resumo.extend(
        [
            "",
            f"controller original: {notas_antes['controller']}/10",
            "",
            "Arquivos originais preservados.",
            "Apenas copias didaticas foram corrigidas.",
        ]
    )

    (SAIDA / "comparacao.txt").write_text(
        "\n".join(resumo) + "\n",
        encoding="utf-8",
    )

    print("\nAULA 14 - ANALISE CONCLUIDA")


if __name__ == "__main__":
    main()
