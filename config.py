import string

# This is the minimum length for generated passwords
MIN_LONGITUD = 4


def construir_caracteres(usar_mayus, usar_minus, usar_numeros, usar_simbolos):
    """
    Construye el conjunto de caracteres según las opciones elegidas.
    """
    caracteres = ""

    if usar_mayus:
        caracteres += string.ascii_uppercase
    if usar_minus:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    return caracteres
