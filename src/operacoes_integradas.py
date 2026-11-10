from src.calculadora import somar


def multiplicar(a: float, b: float) -> float:
    return a * b


def multiplicar_e_somar(
    a: float,
    b: float,
    adicional: float,
) -> float:
    resultado = multiplicar(a, b)
    return somar(resultado, adicional)
