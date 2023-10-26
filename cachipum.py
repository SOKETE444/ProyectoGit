import random

def juguemos_cachipum(persona, cpu):
    opciones= ["piedra", "papel", "tijera"]

    while persona not in opciones:
        print("opciones invalida, por favor, elige una valida")
        persona= input ("elige tu opcion")

    if (persona== "piedra" and cpu == "tijera") or (persona== "papel" and cpu== "piedra") or (persona== "tijera" and cpu== "papel"):
        return "victoria"
    elif persona==cpu:
        return "empate"
    else:
        return "derroitado"
if __name__ == "__main__":
    print("bienvendio al juego cachipun contra la cpu")
    print("movimientos: piedra, papel y tijera")
    movimientos =["piedra", "papel", "tijera"]
    persona = input("ingrese su movimiento")
    while persona not in (movimientos):
        print("movimiento invalido, por favor, elige nuevamente")
        persona = input("elige tu jugada")
    cpu = random.choice(movimientos)

    print("la cpu eligio", cpu)
    result = juguemos_cachipum(persona, cpu)
    print("resultados", result)
