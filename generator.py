import random


def generate_password(longitud, caracteres):
    if not caracteres:
        raise ValueError("No hay caracteres disponibles para generar la contraseña")

    contrasena = "".join(
        random.choice(caracteres)
        for _ in range(longitud)
    )

    return contrasena
