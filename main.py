import sys
sys.dont_write_bytecode = True
from validators import pedir_longitud, pedir_opcion
from config import construir_caracteres
from generator import generate_password


def main():
    print("GENERADOR DE CONTRASEÑAS 🔐\n")

    longitud = pedir_longitud()

    usar_mayus = pedir_opcion("¿Incluir letras MAYÚSCULAS? (s/n): ")
    usar_minus = pedir_opcion("¿Incluir letras minúsculas? (s/n): ")
    usar_numeros = pedir_opcion("¿Incluir números? (s/n): ")
    usar_simbolos = pedir_opcion("¿Incluir símbolos? (s/n): ")

    caracteres = construir_caracteres(
        usar_mayus,
        usar_minus,
        usar_numeros,
        usar_simbolos
    )

    if not caracteres:
        print("\n❌ Debes seleccionar al menos un tipo de carácter.")
        return

    contrasena = generate_password(longitud, caracteres)

    print("\n✅ Contraseña generada:")
    print(contrasena)


if __name__ == "__main__":
    main()
