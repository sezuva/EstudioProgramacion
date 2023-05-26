print("""
Juego de papel, piedra o tijera

"""+"*"*60)
import random

opcion_pc=random.randint(1,3)
opciones={
    1:"piedra",
    2:"papel",
    3:"tijera",
    "tijera":"tijera",
    "piedra":"piedra",
    "papel":"papel",
}
op_usuario=input("""Escoja entre piedra, papel o tijera
Puede escribir la palabra o escoger 1,2 o 3 respectivamente. 
""")

print("La computadora ha escogido "+opciones[opcion_pc])

#if opciones[opcion_pc]==""
