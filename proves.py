orden = ["V","G","T","B"]
def torn(torn_actual): #Funció  que determina el jugador que toca jugar
    jugador_actual = orden[torn_actual]
    return f"Jugador {jugador_actual}"

torn_actual = 0
torn(torn_actual)