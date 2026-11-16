import random


def obtener_palabra_aleatoria():
    palabras = ["perro", "gato", "python", "codigo", "ahorcado", "programacion"]
    return random.choice(palabras)


def mostrar_tablero(palabra_secreta, letras_adivinadas):
    tablero = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero += letra + " "
        else:
            tablero += "_ "
    print(tablero)


def jugar_ahorcado():
    palabra_secreta = obtener_palabra_aleatoria()
    letras_adivinadas = []
    letras_incorrectas = []
    intentos_restantes = 6

    print("¡Bienvenido al Ahorcado!")

    while intentos_restantes > 0:
        print()
        mostrar_tablero(palabra_secreta, letras_adivinadas)
        if letras_incorrectas:
            print("Letras incorrectas:", ", ".join(letras_incorrectas))

        letra = input("Introduce una letra: ").lower().strip()

        # Validar que sea una sola letra
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, introduce una sola letra.")
            continue

        if letra in letras_adivinadas or letra in letras_incorrectas:
            print("Esa letra ya la has dicho.")
            continue

        if letra in palabra_secreta:
            letras_adivinadas.append(letra)
            print("¡Bien! La letra está en la palabra.")
            if set(letras_adivinadas) == set(palabra_secreta):
                print()
                mostrar_tablero(palabra_secreta, letras_adivinadas)
                print("¡Has ganado el juego!")
                return
        else:
            letras_incorrectas.append(letra)
            intentos_restantes -= 1
            print(f"Letra incorrecta. Te quedan {intentos_restantes} intentos.")

    print(f"Has perdido. La palabra secreta era: {palabra_secreta}")


if __name__ == "__main__":
    jugar_ahorcado()
