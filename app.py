import random
opciones = ["piedra", "papel", "tijeras"]
puntuacion = 0
rondas = 0
jugar_de_nuevo = "s"
print("---"*15)
print("|\tBienvenido a Piedra, Papel o Tijeras.\t|\n")
while jugar_de_nuevo != "n":
    print("---"*15)
    eleccion_jugador = input("Elige una opción: \npiedra, papel o tijeras:\n ").lower()
    if eleccion_jugador not in opciones:
        print("Opción no válida. Inténtalo de nuevo.\n"); print("---"*15)
        continue
    eleccion_oponente = random.choice(opciones)
    print("Tu oponente ha elegido: ", eleccion_oponente ,"\n")
    if eleccion_jugador == eleccion_oponente:
        print("Es un empate. \n")
        rondas += 1; print("---"*15)
    elif    (eleccion_jugador == "piedra" and eleccion_oponente == "tijeras") or \
            (eleccion_jugador == "papel" and eleccion_oponente == "piedra") or \
            (eleccion_jugador == "tijeras" and eleccion_oponente == "papel"):
        print("Has ganado esta ronda.\n")
        rondas += 1
        puntuacion += 1; print("---"*15)
    else:
        rondas += 1
        print("Has perdido esta ronda.\n")
    print("Tu puntuación es: ", puntuacion)
    print("Rondas jugadas: ", rondas); print("---"*15)
    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): \n").lower()
    while jugar_de_nuevo != "s" and jugar_de_nuevo != "n":
        print("Opción no válida. Inténtalo de nuevo.\n"); print("---"*15)
        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): \n").lower()
print("---"*15); print("|\t\t¡Gracias por jugar!\t\t|"); print("---"*15)