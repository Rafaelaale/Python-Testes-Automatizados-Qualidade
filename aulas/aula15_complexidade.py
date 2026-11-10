"""Aula 15 - Explorando a complexidade ciclomática."""


def classificar_nota_complexa(nota):
    """Classifica notas usando varias decisoes."""
    if nota >= 90:
        return "A"
    elif nota >= 80:
        return "B"
    elif nota >= 70:
        return "C"
    elif nota >= 60:
        return "D"
    elif nota >= 50:
        return "E"
    elif nota >= 40:
        return "F"
    elif nota >= 30:
        return "G"
    elif nota >= 20:
        return "H"
    elif nota >= 10:
        return "I"
    else:
        return "J"


def classificar_nota_refatorada(nota):
    """Classifica notas usando uma tabela de limites."""
    limites = (
        (90, "A"),
        (80, "B"),
        (70, "C"),
        (60, "D"),
        (50, "E"),
        (40, "F"),
        (30, "G"),
        (20, "H"),
        (10, "I"),
    )

    for minimo, classificacao in limites:
        if nota >= minimo:
            return classificacao

    return "J"
