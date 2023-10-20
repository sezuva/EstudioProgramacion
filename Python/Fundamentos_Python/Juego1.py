import random
Juego=1


while Juego == 1:
    print("""
    Juego de papel, piedra o tijera
    """+"*"*60)
    play=int(input("""\n Presione 1 para jugar
               """))
    Jugadas_ganadas=0
    Jugadas_perdidas=0
    Partidas_ganadas=0
    Partidas_perdidas=0

    while play == 1:
        Jugadas_ganadas=0
        Jugadas_perdidas=0
        contador=int(0)
        
        for i in range (1,4):
            contador =+1
            opcion_pc=random.randint(1,3)
            opciones={
                1:"piedra",
                2:"papel",
                3:"tijera",
                "tijera":"tijera",
                "piedra":"piedra",
                "papel":"papel",
            }
            print("-"*60)
            op_usuario=(input(f"\n Jugada {i} de 3 \nEscoja entre piedra, papel o tijera o 1,2 o 3 respectivamente.\n"))

            try:
                if op_usuario=="1" or op_usuario=="2" or op_usuario=="3":
                     op_usuario=int(op_usuario)

                else:
                    op_usuario=op_usuario.lower()
                print("\nHas escogido "+opciones[op_usuario])
                print("La computadora ha escogido "+opciones[opcion_pc])
            except:
                print("Has escogido una opción no valida, vuelve a comenzar")
                break

            if opciones[opcion_pc]==opciones[op_usuario]:
                print("¡Empataste la jugada!")

            elif (opciones[opcion_pc] =="tijera" and opciones[op_usuario]=="piedra") or (opciones[opcion_pc] =="piedra" and opciones[op_usuario]=="papel") or (opciones[opcion_pc] =="papel" and opciones[op_usuario]=="tijera"):
                    Jugadas_ganadas=Jugadas_ganadas+1
                    print("¡Ganaste esta jugada!")

            elif (opciones[opcion_pc] =="piedra" and opciones[op_usuario]=="tijera") or (opciones[opcion_pc] =="papel" and opciones[op_usuario]=="piedra") or (opciones[opcion_pc] =="tijera" and opciones[op_usuario]=="papel"):
                    Jugadas_perdidas=Jugadas_perdidas+1
                    print("¡Perdiste esta jugada!")

            else: 
                print("Has escogido una opción no valida")
                break
            
            print("\nPuntos Jugador:"+str(Jugadas_ganadas))
            print("Puntos PC:"+str(Jugadas_perdidas))

            if (i==2 and Jugadas_ganadas == 2) or (i==3 and Jugadas_ganadas>Jugadas_perdidas):
                 print("\nGanaste esta partida")
                 Partidas_ganadas=Partidas_ganadas+1
                 print(f"\nPartidas ganadas: {Partidas_ganadas}")
                 print(f"Partidas perdidas: {Partidas_perdidas}")
                 play=int(input("\nEscoja 1 para Seguir con otra partida o 0 para abandonar"))
            elif (i==2 and Jugadas_perdidas==2) or (i==3 and Jugadas_perdidas>Jugadas_ganadas):
                 print("\nPerdiste esta partida")
                 Partidas_perdidas=Partidas_perdidas+1
                 print(f"\nPartidas ganadas: {Partidas_ganadas}")
                 print(f"Partidas perdidas: {Partidas_perdidas}")
                 play=int(input("\nEscoja 1 para Seguir con otra partida o 0 para abandonar"))
            elif (i==3) and Jugadas_ganadas==Jugadas_perdidas:
                 print("\nEmpataste la partida")
                 print(f"\nPartidas ganadas: {Partidas_ganadas}")
                 print(f"Partidas perdidas: {Partidas_perdidas}")
                 play=int(input("\nEscoja 1 para Seguir con otra partida o 0 para abandonar"))

