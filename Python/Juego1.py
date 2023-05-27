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

op_usuario=(input("""Escoja entre piedra, papel o tijera
Puede escribir la palabra o escoger 1,2 o 3 respectivamente. 
"""))

try:
    if op_usuario=="1" or op_usuario=="2" or op_usuario=="3":
        op_usuario=int(op_usuario)

    else:
        op_usuario=op_usuario.lower()
    print("La computadora ha escogido "+opciones[opcion_pc])

    if opciones[opcion_pc]==opciones[op_usuario]:
        print("Empataste!")

    elif (opciones[opcion_pc] =="tijera" and opciones[op_usuario]=="piedra") or (opciones[opcion_pc] =="piedra" and opciones[op_usuario]=="papel") or (opciones[opcion_pc] =="papel" and opciones[op_usuario]=="tijera"):
        print("Ganaste!")

    else: 
        print("Perdiste!")
        
except:
    print("Has escogido una opción no valida")