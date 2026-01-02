from config import MIN_LONGITUD

"validates the length of the password requested by the user"
def pedir_longitud():
    while True:
        try:
            longitud = int(input("Longitud de la contraseña: "))
            if longitud < MIN_LONGITUD:
                print(f"La longitud mínima es {MIN_LONGITUD}")
            else:
                return longitud
        except ValueError:
            print("Debes ingresar un número válido")


"asks the user if he wants to include certain character types"
def pedir_opcion(mensaje):
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta in ("s", "n"):
            return respuesta == "s"
        print("Ingresa solo 's' o 'n'")
