import random
def ordre(): #Funció mostra els jugadors a l'atzar
    global cell0
    players = ["V","T","G","B"]
    orden = []
    for _ in range(4):    
        eleccio = random.choice(players)
        orden.append(eleccio)
        players.remove(eleccio)
    cell0 = orden[0] + orden[1] + orden[2]+ orden[3]
    global jugador_ve, jugador_tg, jugador_go, jugador_bl
    #Ordre tirada jugadors
    global Jugador_0, Jugador_1, Jugador_2, Jugador_3
    Jugador_0 = None
    Jugador_1 = None
    Jugador_2 = None
    Jugador_3 = None
#Defineixo per variables els jugadors
    if orden[0] == "V":#Si vermell es troba al primer lloc de la llista orden
        jugador_ve = Jugador_0 #Defineixo el jugador amb una variable
        Jugador_0 = "Vermell"
        if orden[1] == "T":##Segona posició
            jugador_tg = Jugador_1
            Jugador_1 = "Taronja"
            if orden[2] == "B":###tercera posició
                jugador_bl = Jugador_2
                Jugador_2 = "Blau"
            elif orden[2] == "G":###
                jugador_go = Jugador_2
                Jugador_2 = "Groc"
        elif orden[1] == "G":##
            jugador_go = Jugador_1
            Jugador_1 = "Groc"
            if orden[2] == "B":###
                jugador_bl = Jugador_2
                Jugador_2 = "Blau"
            elif orden[2] == "T":###
                jugador_tg = Jugador_2
                Jugador_2 = "Taronja"
        elif orden[1] == "B":##
            jugador_bl = Jugador_1
            Jugador_1 = "Blau"
            if orden[2] == "T":###
                jugador_tg = Jugador_2
                Jugador_2 = "Taronja"
            elif orden[2] == "G":###
                jugador_go = Jugador_2
                Jugador_2 = "Groc"
    elif orden[0] == "T":#Si taronja es troba al primer lloc de la llista orden
        jugador_tg = Jugador_0
        Jugador_0 = "Taronja"
        if orden[1] == "V":##
            jugador_ve = Jugador_1
            Jugador_1 = "Vermell"
            if orden[2] == "B":###
                jugador_bl = Jugador_2
                Jugador_2 = "Blau"
            elif orden[2] == "G":###
                jugador_go = Jugador_2
                Jugador_2 = "Groc"
        elif orden[1] == "G":##
            jugador_go = Jugador_1
            Jugador_1 = "Groc"
            if orden[2] == "B":###
                jugador_bl = Jugador_2
                Jugador_2 = "Blau"
            elif orden[2] == "V":###
                jugador_ve = Jugador_2
                Jugador_2 = "Vermell"
        elif orden[1] == "B":##
            jugador_bl = Jugador_1
            Jugador_1 = "Blau"
            if orden[2] == "V":###
                jugador_ve = Jugador_2
                Jugador_2 = "Vermell" 
            elif orden[2] == "G":###
                jugador_go = Jugador_2
                Jugador_2 = "Groc"
    elif  orden[0] == "G":#Si groc es troba al primer lloc de la llista orden
        jugador_go = Jugador_0
        Jugador_0 = "Groc"
        if orden[1] == "T":##
            jugador_tg = Jugador_1
            Jugador_1 = "Taronja"
            if orden[2] == "B":###
                jugador_bl = Jugador_2
                Jugador_2 = "Blau"
            elif orden[2] == "V":###
                jugador_ve = Jugador_2
                Jugador_2 = "Vermell"
        elif orden[1] == "V":##
            jugador_ve = Jugador_1
            Jugador_1 = "Vermell"
            if orden[2] == "B":###
                jugador_bl = Jugador_2
                Jugador_2 = "Blau"
            elif orden[2] == "T":###
                jugador_tg = Jugador_2
                Jugador_2 = "Taronja"
        elif orden[1] == "B":##
            jugador_bl = Jugador_1
            Jugador_1 = "Blau"
            if orden[2] == "V":###
                jugador_ve = Jugador_2
                Jugador_2 = "Vermell"
            elif orden[2] == "T":###
                jugador_tg = Jugador_2
                Jugador_2 = "Taronja"
    elif orden[0] == "B":#Si blau es troba al primer lloc de la llista orden
        jugador_bl = Jugador_0
        Jugador_0 = "Blau"
        if orden[1] == "T":##
            jugador_tg = Jugador_1
            Jugador_1 = "Taronja"
            if orden[2] == "V":###
                jugador_ve = Jugador_2
                Jugador_2 = "Vermell"
            elif orden[2] == "G":###
                jugador_go = Jugador_2
                Jugador_2 = "Groc"
        elif orden[1] == "G":##
            jugador_go = Jugador_1
            Jugador_1 = "Groc"
            if orden[2] == "T":###
                jugador_tg = Jugador_2
                Jugador_2 = "Taronja"
            elif orden[2] == "V":###
                jugador_ve = Jugador_2
                Jugador_2 = "Vermell"
        elif orden[1] == "V":##
            jugador_ve = Jugador_1
            Jugador_1 = "Vermell"
            if orden[2] == "T":###
                jugador_tg = Jugador_2
                Jugador_2 = "Taronja"
            elif orden[2] == "G":###
                jugador_go = Jugador_2
                Jugador_2 = "Groc"
    if orden[3] == "V":####
        jugador_ve = Jugador_3
        Jugador_3 = "Vermell"
    elif orden[3] == "G":####
        jugador_go = Jugador_3
        Jugador_3 = "Groc"
    elif orden[3] == "T":####
        jugador_tg = Jugador_3
        Jugador_3 = "Taronja"
    else:####
        jugador_bl = Jugador_3
        Jugador_3 = "Blau"
    
    return orden,players

players = ordre()
def torn():
    i = 0
    for _ in players:
        print(f"Torn {players[i]}")
        print()
        i +=1
torn()