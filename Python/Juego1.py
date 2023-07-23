import random
Juego=1


while Juego == 1:
    print("""
    Juego de papel, piedra o tijera
    """+"*"*60)
    play=int(input("""Presione 1 para jugar
               """))
    Jugadas_ganadas=0
    Jugadas_perdidas=0
    Partidas_ganadas=0
    Partidas_perdidas=0

    while play == 1:
        Jugadas_ganadas=0
        Jugadas_perdidas=0
        
        for i in range (0,3):
            opcion_pc=random.randint(1,3)
            opciones={
                1:"piedra",
                2:"papel",
                3:"tijera",
                "tijera":"tijera",
                "piedra":"piedra",
                "papel":"papel",
            }
            op_usuario=(input("""
Escoja entre piedra, papel o tijera. Puede escribir la palabra o escoger 1,2 o 3 respectivamente. 
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
                    print("¡Ganaste esta jugada!")
                    Jugadas_ganadas=+1
                else: 
                    print("¡Perdiste esta jugada!")
                    Jugadas_perdidas=+1
            except:
                print("Has escogido una opción no valida")
                i=0

            print("Puntos Jugador:"+str(Jugadas_ganadas))
            print("Puntos PC:"+str(Jugadas_perdidas))
            Diferencia =Jugadas_ganadas-Jugadas_perdidas
            if i>=2 and Diferencia>=1:
                Partidas_ganadas=+1
                print(f"""
Partidas ganadas: {Partidas_ganadas}
Partidas perdidas: {Partidas_perdidas}""")
                break
            elif i>=2 and Diferencia <=-1:
                Partidas_perdidas=+1
                print(f"""
Partidas ganadas: {Partidas_ganadas}
Partidas perdidas: {Partidas_perdidas}""")
                break
            elif i>=2 and Diferencia==0:
                print("Partida empatada")
                print(f"""
Partidas ganadas: {Partidas_ganadas}
Partidas perdidas: {Partidas_perdidas}""")       
        play=int(input("Escoja 1 para Seguir con otra partida o 0 para abandonar"))