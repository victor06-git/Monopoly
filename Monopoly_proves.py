"""
Monopoly --> grupo: Manel y Víctor

1 -- Dibuixar tauler i fer funció daus individualment
2 -- Tauler amb noms
3 -- Definir banca quan doni diners als jugadors i es quedi amb 500.000 euros (Fer que s'afegeixin 1M d'euros).
4 -- Definir ordre tirada (amb random) fer que apareixin les inicials dels colors
       que comencen en ordre (exemple: VGTB)
5 -- Definir inici_partida(); Els jugadors comencen amb 2000 euros.
6 -- Definir els jugadors amb 4 funcions diferents; (Els color taronja, groc, blava i vermell)(class Jugador)
7 -- Definir casella(); a cada casella hi ha d'haver un espai que faci que hi hagi el jugador quan cau.
8 -- Definir cases i hotels en dos funcions diferents. (Es mostraran en l'espai o hi ha "|" cap a la dreta)
9 -- Informació jugadors; es mostra a la dreta del taulell, 
     on hi ha la banca amb 1M d'euros a sota surt; Jugador: --/ Carrers: --/ Diners: --/ Especial: --
     Es mostren per ordre de tirada els valors dels jugadors / I els carrers amb nom complet per ordre en taulell (ordre: agulles del rellotge)
10 -- Definir llista amb noms dels carrers: 
                                            **Els noms dels carrers són**:

                                            - Lauria, Rosselló, Marina, Consell de cent
                                            - Muntaner, Aribau, Sant Joan, Aragó
                                            - Urquinaona, Fontana, Les Rambles, Plaça Catalunya
                                            - Portal de l'Àngel, Via Augusta, Balmes, Passeig de Gràcia
11 -- Definir caselles especials:
                                    **Sortida**: quan passa per aquesta casella el jugador guanya 200€

                                    **Presó**: quan el jugador cau a la *presó* pot sortir de tres maneres:

                                    - Si té una carta *"Sortir de la presó"*
                                    - Si quan li toca jugar treu *"Dobles"*, és a dir dos daus amb el mateix número
                                    - Si passen tres torns a la pressó, sense jugar

                                    **Anr pró**: quan el jugador cau a *Anr pró* va a la casella de presó, com si hi hagués caigut.

                                    **Parking**: aquesta casella no afecta als jugadors que hi cauen.

                                    **Sort**: quan un jugador cau en aquesta casella li pot tocar a l'atzar:

                                    - Sortir de la presó: quan cau a la presó podrà seguir jugant (i perdrà aquesta opció)
                                    - Anar a la presó: el jugador va a la presó sense cobrar la sortida i sense jugar 3 torns
                                    - Anar a la sortida: el jugador va a la sortida i cobra els 200€
                                    - Anar tres espais endarrera
                                    - Fer reparacions a les propietats: el jugador paga 25€ per cada propietat i 100€ per cada hotel a la banca
                                    - Ets escollit alcalde, cada jugador el paga 50€

                                    **Caixa**: 

                                    - Sortir de la presó: quan cau a la presó podrà seguir jugant (i perdrà aquesta opció)
                                    - Anar a la presó: el jugador va a la presó sense cobrar la sortida i sense jugar 3 torns
                                    - Error de la banca al teu favor, guanyes 150€
                                    - Despeses mèdiques, pagues 50€
                                    - Despeses escolars, pagues 50€
                                    - Reparacions al carrer, pagues 40€
                                    - Concurs de bellesa, guanyes 10€
12 -- Definir caselles de carrer:
                                -   **Si són del banc**, els jugadors tenen la oportunitat de comprar-ne el terreny
                                -   **Si són d'un altre jugador**, el jugador que hi cau ha de pagar al propietari en concepte de lloguer
                                -   **Si són el mateix jugador**, té la oportunitat d'invertir-hi amb casses i hotels. 
13 -- Definir una funció que mostri la informació de la partida en el centre del tauler durant la partida
      O es mostri EXEMPLE: (Juga "B", ha sortit 4 i 3, "B" avança fins "Aribau", "B" compra el terreny)
14 -- A la part de sota del taulell es mostra el que és la interacció de l'usuari amb el taulell; EXEMPLE:(Juga "T", opcions: passar, comprar terreny, preus(Si el jugador no té el terreny on ha caigut)
      En el cas que el jugador tingui el terreny EXEMPLE:(Juga "T", opcions: passar, comprar casa, compra terreny, preus))
      Si el jugador no pot fer res, per exemple cau al pàrquing, no es mostra res a sota pero si que surt al centre del tauler.
15 -- Definir les opcions(): 
                                  **passar**, segueix amb la jugada del següent jugador
                                  **comprar terreny**, només si el terreny no té propietari
                                  **comprar casa**, només pel propietari del terreny si n'hi ha menys de 4
                                  **comprar hotel**, només pel propietari si hi ha 2 cases. Al comprar cada hotel resta 2 cases. No hi pot haber més de 2 hotels.
                                  **preus**, mostra els preus de comprar una casa o un hotel a l'espai central d'informació
                                  **preu banc**, disponible si el jugador no pot pagar, mostra a l'espai d'informació el què guanyarà si ven totes les propietats al banc (50% del què ha pagat per comprar les propietats)
                                  **preu jugador**, disponible si el jugador no pot pagar, mostra a l'espai d'informació el què guanyarà si ven totes les propietats a un altre jugador (90% del què ha pagat per comprar les propietats)
                                  **vendre al banc**, disponible si el jugador no pot pagar, ven totes les propietats al banc (terrenys, cases i hotels) al 50% del què ha pagat el jugador. La casella torna a quedar buida amb el terreny disponible.
                                  **vendre a B**, disponible si el jugador no pot pagar i "B" pot comprar totes les propietats (terrenys, cases i hotels) per un valor del 90% del què ha pagat el jugador
                                  **vendre a T**, **vendre a G**, **vendre a V**, igual que "vendre a B" però pels altres jugadors si ho poden comprar
16 -- Definir els preus de les cases, els hotels, el terreny, compra casa, compra hotel.
17 -- Definir trucs
"""

"""
IMPORTS
"""
from llistes import *
from daus import *
import random
"""
FUNCIÓO TAULER
"""

"""
BANCA
        -Si el valor de la banca es menor que 500.000 euros suma a la banca 1M
        -Retorna el valor de la banca
"""
valor_banca = None

def banca():#Funció diners banca
    global valor_banca
    valor_inicial = 1000000
    valor = 500000
    if valor_inicial <= valor:
        valor_banca = valor_inicial + 1000000 #Afegeix 1M d'euros a la banca si té 500mil o menys 
        return valor_banca
    else:
        valor_banca = valor_inicial
        return valor_banca # Retorna el valor en diners que te la banca en aquell moment
"""
ORDRE TIRADA
                -Aleatoriament selecciona al principi de cada partida
                -Condicional para saber que valores entre el 0 i el 3 tienen los jugadores
                -Orden lista
"""

def ordre(): #Funció mostra els jugadors a l'atzar
    global cell0,orden
    players = ["V","T","G","B"]
    orden = []
    for _ in range(4):    
        eleccio = random.choice(players)
        orden.append(eleccio)
        players.remove(eleccio)
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
orden,players = ordre()
"""
TORN JUGADOR
"""
def preu_terreny(casilla): #Definir el preu que ha de pagar per el terreny seleccionat
        if jugador_b.posicio == casilla: #Casilla igual al número de casella
            if casilla == [1,2,4,5]:
                return f"El preu del terreny és de:{diners_propietats[0]}"
            elif casilla == [7,8,10,11]:
                return f"El preu del terreny és de:{diners_propietats[1]}"
            elif casilla == [13,14,16,17]:
                return f"El preu del terreny és de:{diners_propietats[2]}"
            elif casilla == [19,20,22,23]:
                return f"El preu del terreny és de:{diners_propietats[3]}"
            else:
                pass
        if jugador_g.posicio == casilla:
            if casilla == [1,2,4,5]:
                return f"El preu del terreny és de:{diners_propietats[0]}"
            elif casilla == [7,8,10,11]:
                return f"El preu del terreny és de:{diners_propietats[1]}"
            elif casilla == [13,14,16,17]:
                return f"El preu del terreny és de:{diners_propietats[2]}"
            elif casilla == [19,20,22,23]:
                return f"El preu del terreny és de:{diners_propietats[3]}"
        if jugador_t.posicio == casilla:
            if casilla == [1,2,4,5]:
                return f"El preu del terreny és de:{diners_propietats[0]}"
            elif casilla == [7,8,10,11]:
                return f"El preu del terreny és de:{diners_propietats[1]}"
            elif casilla == [13,14,16,17]:
                return f"El preu del terreny és de:{diners_propietats[2]}"
            elif casilla == [19,20,22,23]:
                return f"El preu del terreny és de:{diners_propietats[3]}"
        if jugador_v.posicio == casilla:
            if casilla == [1,2,4,5]:
                return f"El preu del terreny és de:{diners_propietats[0]}"
            elif casilla == [7,8,10,11]:
                return f"El preu del terreny és de:{diners_propietats[1]}"
            elif casilla == [13,14,16,17]:
                return f"El preu del terreny és de:{diners_propietats[2]}"
            elif casilla == [19,20,22,23]:
                return f"El preu del terreny és de:{diners_propietats[3]}"

def torn(torn_actual): #Funció  que determina el jugador que toca jugar
    if torn_actual  == 0:
       jugador_actual = Jugador_0
    elif torn_actual == 1:
        jugador_actual = Jugador_1
    elif torn_actual == 2:
       jugador_actual = Jugador_2
    else:
        jugador_actual = Jugador_3
    return  jugador_actual

torn_actual = 0
jugador_actual = torn(torn_actual)

def torn_jugador_B(): #Si el torn és del jugador B
    return jugador_actual == "Blau"
def torn_jugador_V():  #Si el torn és del jugador V
    return jugador_actual == "Vermell"
def torn_jugador_G():   #Si el torn és del jugador G
    return jugador_actual == "Groc"
def torn_jugador_T(): #Si el torn és del jugador T
    return jugador_actual == "Taronja"

"""
OPCIONS USUARI A CADA TORN
"""

def opcions(jugador_actual): 
    opcions_jugadors = {
        "Vermell": jugador_v,
        "Blau" : jugador_b,
        "Groc" : jugador_g,
        "Taronja" : jugador_t
    }

    jugador = opcions_jugadors[jugador_actual]
    print(f"Torn Jugador: \"{jugador_actual}\"")
    opcion_jugador = input(f"Torn \"{jugador_actual}\", opcions --> (passar, compra terreny, preus):  ")
    if opcion_jugador == 1 or opcion_jugador == "comprar  terreny":
        if torn_jugador_B():
            jugador_b.compra_propietat(tauler[jugador_b.posicio])
        elif torn_jugador_G():
            jugador_g.compra_propietat(tauler[jugador_g.posicio])
        elif torn_jugador_T():
            jugador_t.compra_propietat(tauler[jugador_t.posicio])
        elif  torn_jugador_V():
            jugador_v.compra_propietat(tauler[jugador_v.posicio])

    elif opcion_jugador == "preus" or opcion_jugador == 2:
        return preu_terreny(jugador.posicio)
    elif opcion_jugador == "trucs".lower():
        trucs()
    



"""
JUGADORS
            -Class Jugador
            -Jugadors definits per color
"""
  


class Jugador:#Definir class Jugador
    
    def __init__(self,name,color):
        self.name = name
        self.color = color
        self.posicio = 0 #Comença a la casella "sortida"
        self.propietats = [] #Lista de les propietats que té l'usuari
        self.carta_especial = [] #Lista de les cartes especials (Sortir de la presó)
        self.diners = 2000 #Diners amb els que comença cada partida els jugadors
        self.a_preso = False #False per definir que el jugador no es troba a presó
        self.torns_a_preso = 0 #Número torns a preso
    
    def en_preso(self):
        return self.a_preso()
    
    def move(self,passos,cells):
        global cell0,cell1,cell2, cell3,cell4,cell5,cell6,cell7,cell8,cell9,cell10, cell11,cell12,cell13,cell14,cell15,cell16,cell17, cell18, cell19,cell20,cell21,cell22,cell23
        if self.a_preso == True:
            missatge = print("Jugador a presó, no pot tirar")
            return missatge
        else:
            self.posicio = (self.posicio + passos) % len(cells) #Passos == resultat_daus
            casella_actual = cells[self.posicio]
            if len(casella_actual) == 0:
                if casella_actual == cell0:    
                    if torn_jugador_T():
                        cell0 =  "T"
                    elif torn_jugador_G():
                        cell0 = "G"
                    elif torn_jugador_V():
                        cell0 = "V"
                    elif torn_jugador_B():
                        cell0 = "B"

                if casella_actual == cell1:
                    if torn_jugador_T():
                        cell1 =  "T"
                    elif torn_jugador_G():
                        cell1 = "G"
                    elif torn_jugador_V():
                        cell1 = "V"
                    elif torn_jugador_B():
                        cell1 = "B"

                if casella_actual == cell2:
                    if torn_jugador_T():
                        cell2 =  "T"
                    elif torn_jugador_G():
                        cell2 = "G"
                    elif torn_jugador_V():
                        cell2 = "V"
                    elif torn_jugador_B():
                        cell2 = "B"

                if casella_actual == cell3:
                    if torn_jugador_T():
                        cell3 =  "T"
                    elif torn_jugador_G():
                        cell3 = "G"
                    elif torn_jugador_V():
                        cell3 = "V"
                    elif torn_jugador_B():
                        cell3 = "B"

                if casella_actual == cell4:
                    if torn_jugador_T():
                        cell4 =  "T"
                    elif torn_jugador_G():
                        cell4 = "G"
                    elif torn_jugador_V():
                        cell4 = "V"
                    elif torn_jugador_B():
                        cell4 = "B"

                if casella_actual == cell5:
                    if torn_jugador_T():
                        cell5 =  "T"
                    elif torn_jugador_G():
                        cell5 = "G"
                    elif torn_jugador_V():
                        cell5 = "V"
                    elif torn_jugador_B():
                        cell5 = "B"

                if casella_actual == cell6:
                    if torn_jugador_T():
                        cell6 =  "T"
                    elif torn_jugador_G():
                        cell6 = "G"
                    elif torn_jugador_V():
                        cell6 = "V"
                    elif torn_jugador_B():
                        cell6 = "B"

                if casella_actual == cell7:
                    if torn_jugador_T():
                        cell7 =  "T"
                    elif torn_jugador_G():
                        cell7 = "G"
                    elif torn_jugador_V():
                        cell7 = "V"
                    elif torn_jugador_B():
                        cell7 = "B"

                if casella_actual == cell8:
                    if torn_jugador_T():
                        cell8 =  "T"
                    elif torn_jugador_G():
                        cell8 = "G"
                    elif torn_jugador_V():
                        cell8 = "V"
                    elif torn_jugador_B():
                        cell8 = "B"

                if casella_actual == cell9:
                    if torn_jugador_T():
                        cell9 =  "T"
                    elif torn_jugador_G():
                        cell9 = "G"
                    elif torn_jugador_V():
                        cell9 = "V"
                    elif torn_jugador_B():
                        cell9 = "B"

                if casella_actual == cell10:
                    if torn_jugador_T():
                        cell10 =  "T"
                    elif torn_jugador_G():
                        cell10 = "G"
                    elif torn_jugador_V():
                        cell10 = "V"
                    elif torn_jugador_B():
                        cell10 = "B"

                if casella_actual == cell11:
                    if torn_jugador_T():
                        cell11 =  "T"
                    elif torn_jugador_G():
                        cell11 = "G"
                    elif torn_jugador_V():
                        cell11 = "V"
                    elif torn_jugador_B():
                        cell11 = "B"

                if casella_actual == cell12:
                    if torn_jugador_T():
                        cell12 =  "T"
                    elif torn_jugador_G():
                        cell12 = "G"
                    elif torn_jugador_V():
                        cell12 = "V"
                    elif torn_jugador_B():
                        cell12 = "B"

                if casella_actual == cell13:
                    if torn_jugador_T():
                        cell13 =  "T"
                    elif torn_jugador_G():
                        cell13 = "G"
                    elif torn_jugador_V():
                        cell13 = "V"
                    elif torn_jugador_B():
                        cell13 = "B"

                if casella_actual == cell14:
                    if torn_jugador_T():
                        cell14 =  "T"
                    elif torn_jugador_G():
                        cell14 = "G"
                    elif torn_jugador_V():
                        cell14 = "V"
                    elif torn_jugador_B():
                        cell14 = "B"

                if casella_actual == cell15:
                    if torn_jugador_T():
                        cell15 =  "T"
                    elif torn_jugador_G():
                        cell15 = "G"
                    elif torn_jugador_V():
                        cell15 = "V"
                    elif torn_jugador_B():
                        cell15 = "B"

                if casella_actual == cell16:
                    if torn_jugador_T():
                        cell16 =  "T"
                    elif torn_jugador_G():
                        cell16 = "G"
                    elif torn_jugador_V():
                        cell16 = "V"
                    elif torn_jugador_B():
                        cell16 = "B"

                if casella_actual == cell17:
                    if torn_jugador_T():
                        cell17 =  "T"
                    elif torn_jugador_G():
                        cell17 = "G"
                    elif torn_jugador_V():
                        cell17 = "V"
                    elif torn_jugador_B():
                        cell17 = "B"

                if casella_actual == cell18:
                    if torn_jugador_T():
                        cell18 =  "T"
                    elif torn_jugador_G():
                        cell18 = "G"
                    elif torn_jugador_V():
                        cell18 = "V"
                    elif torn_jugador_B():
                        cell18 = "B"

                if casella_actual == cell19:
                    if torn_jugador_T():
                        cell19 =  "T"
                    elif torn_jugador_G():
                        cell19 = "G"
                    elif torn_jugador_V():
                        cell19 = "V"
                    elif torn_jugador_B():
                        cell19 = "B"

                if casella_actual == cell20:
                    if torn_jugador_T():
                        cell20 =  "T"
                    elif torn_jugador_G():
                        cell20 = "G"
                    elif torn_jugador_V():
                        cell20 = "V"
                    elif torn_jugador_B():
                        cell20 = "B"

                if casella_actual == cell21:
                    if torn_jugador_T():
                        cell21 =  "T"
                    elif torn_jugador_G():
                        cell21 = "G"
                    elif torn_jugador_V():
                        cell21 = "V"
                    elif torn_jugador_B():
                        cell21 = "B"

                if casella_actual == cell22:
                    if torn_jugador_T():
                        cell22 =  "T"
                    elif torn_jugador_G():
                        cell22 = "G"
                    elif torn_jugador_V():
                        cell22 = "V"
                    elif torn_jugador_B():
                        cell22 = "B"

                if casella_actual == cell23:
                    if torn_jugador_T():
                        cell23 =  "T"
                    elif torn_jugador_G():
                        cell23 = "G"
                    elif torn_jugador_V():
                        cell23 = "V"
                    elif torn_jugador_B():
                        cell23 = "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell0:    
                    if torn_jugador_T():
                        cell0 = cell0 + "T"
                    elif torn_jugador_G():
                        cell0 = cell0 + "G"
                    elif torn_jugador_V():
                        cell0 = cell0 + "V"
                    elif torn_jugador_B():
                        cell0 = cell0 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell1:    
                    if torn_jugador_T():
                        cell1 = cell1 + "T"
                    elif torn_jugador_G():
                        cell1 = cell1 + "G"
                    elif torn_jugador_V():
                        cell1 = cell1 + "V"
                    elif torn_jugador_B():
                        cell1 = cell1 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell2:    
                    if torn_jugador_T():
                        cell2 = cell2 + "T"
                    elif torn_jugador_G():
                        cell2 = cell2 + "G"
                    elif torn_jugador_V():
                        cell2 = cell2 + "V"
                    elif torn_jugador_B():
                        cell2 = cell2 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell3:    
                    if torn_jugador_T():
                        cell3 = cell3 + "T"
                    elif torn_jugador_G():
                        cell3 = cell3 + "G"
                    elif torn_jugador_V():
                        cell3 = cell3 + "V"
                    elif torn_jugador_B():
                        cell3 = cell3 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell4:    
                    if torn_jugador_T():
                        cell4 = cell4 + "T"
                    elif torn_jugador_G():
                        cell4 = cell4 + "G"
                    elif torn_jugador_V():
                        cell4 = cell4 + "V"
                    elif torn_jugador_B():
                        cell4 = cell4 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell5:    
                    if torn_jugador_T():
                        cell5 = cell5 + "T"
                    elif torn_jugador_G():
                        cell5 = cell5 + "G"
                    elif torn_jugador_V():
                        cell5 = cell5 + "V"
                    elif torn_jugador_B():
                        cell5 = cell5 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell6:    
                    if torn_jugador_T():
                        cell6 = cell6 + "T"
                    elif torn_jugador_G():
                        cell6 = cell6 + "G"
                    elif torn_jugador_V():
                        cell6 = cell6 + "V"
                    elif torn_jugador_B():
                        cell6 = cell6 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell7:    
                    if torn_jugador_T():
                        cell7 = cell7 + "T"
                    elif torn_jugador_G():
                        cell7 = cell7 + "G"
                    elif torn_jugador_V():
                        cell7 = cell7 + "V"
                    elif torn_jugador_B():
                        cell7 = cell7 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell8:    
                    if torn_jugador_T():
                        cell8 = cell8 + "T"
                    elif torn_jugador_G():
                        cell8 = cell8 + "G"
                    elif torn_jugador_V():
                        cell8 = cell8 + "V"
                    elif torn_jugador_B():
                        cell8 = cell8 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell9:    
                    if torn_jugador_T():
                        cell9 = cell9 + "T"
                    elif torn_jugador_G():
                        cell9 = cell9 + "G"
                    elif torn_jugador_V():
                        cell9 = cell9 + "V"
                    elif torn_jugador_B():
                        cell9 = cell9 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell10:    
                    if torn_jugador_T():
                        cell10 = cell10 + "T"
                    elif torn_jugador_G():
                        cell10 = cell10 + "G"
                    elif torn_jugador_V():
                        cell10 = cell10 + "V"
                    elif torn_jugador_B():
                        cell10 = cell10 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell11:    
                    if torn_jugador_T():
                        cell11 = cell11 + "T"
                    elif torn_jugador_G():
                        cell11 = cell11 + "G"
                    elif torn_jugador_V():
                        cell11 = cell11 + "V"
                    elif torn_jugador_B():
                        cell11 = cell11 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell12:    
                    if torn_jugador_T():
                        cell12 = cell12 + "T"
                    elif torn_jugador_G():
                        cell12 = cell12 + "G"
                    elif torn_jugador_V():
                        cell12 = cell12 + "V"
                    elif torn_jugador_B():
                        cell12 = cell12 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell13:    
                    if torn_jugador_T():
                        cell13 = cell13 + "T"
                    elif torn_jugador_G():
                        cell13 = cell13 + "G"
                    elif torn_jugador_V():
                        cell13 = cell13 + "V"
                    elif torn_jugador_B():
                        cell13 = cell13 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell14:    
                    if torn_jugador_T():
                        cell14 = cell14 + "T"
                    elif torn_jugador_G():
                        cell14 = cell14 + "G"
                    elif torn_jugador_V():
                        cell14 = cell14 + "V"
                    elif torn_jugador_B():
                        cell14 = cell14 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell15:    
                    if torn_jugador_T():
                        cell15 = cell15 + "T"
                    elif torn_jugador_G():
                        cell15 = cell15 + "G"
                    elif torn_jugador_V():
                        cell15 = cell15 + "V"
                    elif torn_jugador_B():
                        cell15 = cell15 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell16:    
                    if torn_jugador_T():
                        cell16 = cell16 + "T"
                    elif torn_jugador_G():
                        cell16 = cell16 + "G"
                    elif torn_jugador_V():
                        cell16 = cell16 + "V"
                    elif torn_jugador_B():
                        cell16 = cell16 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell17:    
                    if torn_jugador_T():
                        cell17 = cell17 + "T"
                    elif torn_jugador_G():
                        cell17 = cell17 + "G"
                    elif torn_jugador_V():
                        cell17 = cell17 + "V"
                    elif torn_jugador_B():
                        cell17 = cell17 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell18:    
                    if torn_jugador_T():
                        cell18 = cell18 + "T"
                    elif torn_jugador_G():
                        cell18 = cell18 + "G"
                    elif torn_jugador_V():
                        cell18 = cell18 + "V"
                    elif torn_jugador_B():
                        cell18 = cell18 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell19:    
                    if torn_jugador_T():
                        cell19 = cell19 + "T"
                    elif torn_jugador_G():
                        cell19 = cell19 + "G"
                    elif torn_jugador_V():
                        cell19 = cell19 + "V"
                    elif torn_jugador_B():
                        cell19 = cell19 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell20:    
                    if torn_jugador_T():
                        cell20 = cell20 + "T"
                    elif torn_jugador_G():
                        cell20 = cell20 + "G"
                    elif torn_jugador_V():
                        cell20 = cell20 + "V"
                    elif torn_jugador_B():
                        cell20 = cell20 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell21:    
                    if torn_jugador_T():
                        cell21 = cell21 + "T"
                    elif torn_jugador_G():
                        cell21 = cell21 + "G"
                    elif torn_jugador_V():
                        cell21 = cell21 + "V"
                    elif torn_jugador_B():
                        cell21 = cell21 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell22:    
                    if torn_jugador_T():
                        cell22 = cell22 + "T"
                    elif torn_jugador_G():
                        cell22 = cell22 + "G"
                    elif torn_jugador_V():
                        cell22 = cell22 + "V"
                    elif torn_jugador_B():
                        cell22 = cell22 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell23:    
                    if torn_jugador_T():
                        cell23 = cell23 + "T"
                    elif torn_jugador_G():
                        cell23 = cell23 + "G"
                    elif torn_jugador_V():
                        cell23 = cell23 + "V"
                    elif torn_jugador_B():
                        cell23 = cell23 + "B"

           
        
    def move_to(self, casella):  #Funció moure a casella
        global cell0,cell1,cell2, cell3,cell4,cell5,cell6,cell7,cell8,cell9,cell10, cell11,cell12,cell13,cell14,cell15,cell16,cell17, cell18, cell19,cell20,cell21,cell22,cell23
        if 0 <= casella < len(cells):
            self.posicio = casella
            casella_actual = cells[self.posicio]
            if len(casella_actual) == 0:
                if casella_actual == cell0:    
                    if torn_jugador_T():
                        cell0 =  "T"
                    elif torn_jugador_G():
                        cell0 = "G"
                    elif torn_jugador_V():
                        cell0 = "V"
                    elif torn_jugador_B():
                        cell0 = "B"

                if casella_actual == cell1:
                    if torn_jugador_T():
                        cell1 =  "T"
                    elif torn_jugador_G():
                        cell1 = "G"
                    elif torn_jugador_V():
                        cell1 = "V"
                    elif torn_jugador_B():
                        cell1 = "B"

                if casella_actual == cell2:
                    if torn_jugador_T():
                        cell2 =  "T"
                    elif torn_jugador_G():
                        cell2 = "G"
                    elif torn_jugador_V():
                        cell2 = "V"
                    elif torn_jugador_B():
                        cell2 = "B"

                if casella_actual == cell3:
                    if torn_jugador_T():
                        cell3 =  "T"
                    elif torn_jugador_G():
                        cell3 = "G"
                    elif torn_jugador_V():
                        cell3 = "V"
                    elif torn_jugador_B():
                        cell3 = "B"

                if casella_actual == cell4:
                    if torn_jugador_T():
                        cell4 =  "T"
                    elif torn_jugador_G():
                        cell4 = "G"
                    elif torn_jugador_V():
                        cell4 = "V"
                    elif torn_jugador_B():
                        cell4 = "B"

                if casella_actual == cell5:
                    if torn_jugador_T():
                        cell5 =  "T"
                    elif torn_jugador_G():
                        cell5 = "G"
                    elif torn_jugador_V():
                        cell5 = "V"
                    elif torn_jugador_B():
                        cell5 = "B"

                if casella_actual == cell6:
                    if torn_jugador_T():
                        cell6 =  "T"
                    elif torn_jugador_G():
                        cell6 = "G"
                    elif torn_jugador_V():
                        cell6 = "V"
                    elif torn_jugador_B():
                        cell6 = "B"

                if casella_actual == cell7:
                    if torn_jugador_T():
                        cell7 =  "T"
                    elif torn_jugador_G():
                        cell7 = "G"
                    elif torn_jugador_V():
                        cell7 = "V"
                    elif torn_jugador_B():
                        cell7 = "B"

                if casella_actual == cell8:
                    if torn_jugador_T():
                        cell8 =  "T"
                    elif torn_jugador_G():
                        cell8 = "G"
                    elif torn_jugador_V():
                        cell8 = "V"
                    elif torn_jugador_B():
                        cell8 = "B"

                if casella_actual == cell9:
                    if torn_jugador_T():
                        cell9 =  "T"
                    elif torn_jugador_G():
                        cell9 = "G"
                    elif torn_jugador_V():
                        cell9 = "V"
                    elif torn_jugador_B():
                        cell9 = "B"

                if casella_actual == cell10:
                    if torn_jugador_T():
                        cell10 =  "T"
                    elif torn_jugador_G():
                        cell10 = "G"
                    elif torn_jugador_V():
                        cell10 = "V"
                    elif torn_jugador_B():
                        cell10 = "B"

                if casella_actual == cell11:
                    if torn_jugador_T():
                        cell11 =  "T"
                    elif torn_jugador_G():
                        cell11 = "G"
                    elif torn_jugador_V():
                        cell11 = "V"
                    elif torn_jugador_B():
                        cell11 = "B"

                if casella_actual == cell12:
                    if torn_jugador_T():
                        cell12 =  "T"
                    elif torn_jugador_G():
                        cell12 = "G"
                    elif torn_jugador_V():
                        cell12 = "V"
                    elif torn_jugador_B():
                        cell12 = "B"

                if casella_actual == cell13:
                    if torn_jugador_T():
                        cell13 =  "T"
                    elif torn_jugador_G():
                        cell13 = "G"
                    elif torn_jugador_V():
                        cell13 = "V"
                    elif torn_jugador_B():
                        cell13 = "B"

                if casella_actual == cell14:
                    if torn_jugador_T():
                        cell14 =  "T"
                    elif torn_jugador_G():
                        cell14 = "G"
                    elif torn_jugador_V():
                        cell14 = "V"
                    elif torn_jugador_B():
                        cell14 = "B"

                if casella_actual == cell15:
                    if torn_jugador_T():
                        cell15 =  "T"
                    elif torn_jugador_G():
                        cell15 = "G"
                    elif torn_jugador_V():
                        cell15 = "V"
                    elif torn_jugador_B():
                        cell15 = "B"

                if casella_actual == cell16:
                    if torn_jugador_T():
                        cell16 =  "T"
                    elif torn_jugador_G():
                        cell16 = "G"
                    elif torn_jugador_V():
                        cell16 = "V"
                    elif torn_jugador_B():
                        cell16 = "B"

                if casella_actual == cell17:
                    if torn_jugador_T():
                        cell17 =  "T"
                    elif torn_jugador_G():
                        cell17 = "G"
                    elif torn_jugador_V():
                        cell17 = "V"
                    elif torn_jugador_B():
                        cell17 = "B"

                if casella_actual == cell18:
                    if torn_jugador_T():
                        cell18 =  "T"
                    elif torn_jugador_G():
                        cell18 = "G"
                    elif torn_jugador_V():
                        cell18 = "V"
                    elif torn_jugador_B():
                        cell18 = "B"

                if casella_actual == cell19:
                    if torn_jugador_T():
                        cell19 =  "T"
                    elif torn_jugador_G():
                        cell19 = "G"
                    elif torn_jugador_V():
                        cell19 = "V"
                    elif torn_jugador_B():
                        cell19 = "B"

                if casella_actual == cell20:
                    if torn_jugador_T():
                        cell20 =  "T"
                    elif torn_jugador_G():
                        cell20 = "G"
                    elif torn_jugador_V():
                        cell20 = "V"
                    elif torn_jugador_B():
                        cell20 = "B"

                if casella_actual == cell21:
                    if torn_jugador_T():
                        cell21 =  "T"
                    elif torn_jugador_G():
                        cell21 = "G"
                    elif torn_jugador_V():
                        cell21 = "V"
                    elif torn_jugador_B():
                        cell21 = "B"

                if casella_actual == cell22:
                    if torn_jugador_T():
                        cell22 =  "T"
                    elif torn_jugador_G():
                        cell22 = "G"
                    elif torn_jugador_V():
                        cell22 = "V"
                    elif torn_jugador_B():
                        cell22 = "B"

                if casella_actual == cell23:
                    if torn_jugador_T():
                        cell23 =  "T"
                    elif torn_jugador_G():
                        cell23 = "G"
                    elif torn_jugador_V():
                        cell23 = "V"
                    elif torn_jugador_B():
                        cell23 = "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell0:    
                    if torn_jugador_T():
                        cell0 = cell0 + "T"
                    elif torn_jugador_G():
                        cell0 = cell0 + "G"
                    elif torn_jugador_V():
                        cell0 = cell0 + "V"
                    elif torn_jugador_B():
                        cell0 = cell0 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell1:    
                    if torn_jugador_T():
                        cell1 = cell1 + "T"
                    elif torn_jugador_G():
                        cell1 = cell1 + "G"
                    elif torn_jugador_V():
                        cell1 = cell1 + "V"
                    elif torn_jugador_B():
                        cell1 = cell1 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell2:    
                    if torn_jugador_T():
                        cell2 = cell2 + "T"
                    elif torn_jugador_G():
                        cell2 = cell2 + "G"
                    elif torn_jugador_V():
                        cell2 = cell2 + "V"
                    elif torn_jugador_B():
                        cell2 = cell2 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell3:    
                    if torn_jugador_T():
                        cell3 = cell3 + "T"
                    elif torn_jugador_G():
                        cell3 = cell3 + "G"
                    elif torn_jugador_V():
                        cell3 = cell3 + "V"
                    elif torn_jugador_B():
                        cell3 = cell3 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell4:    
                    if torn_jugador_T():
                        cell4 = cell4 + "T"
                    elif torn_jugador_G():
                        cell4 = cell4 + "G"
                    elif torn_jugador_V():
                        cell4 = cell4 + "V"
                    elif torn_jugador_B():
                        cell4 = cell4 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell5:    
                    if torn_jugador_T():
                        cell5 = cell5 + "T"
                    elif torn_jugador_G():
                        cell5 = cell5 + "G"
                    elif torn_jugador_V():
                        cell5 = cell5 + "V"
                    elif torn_jugador_B():
                        cell5 = cell5 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell6:    
                    if torn_jugador_T():
                        cell6 = cell6 + "T"
                    elif torn_jugador_G():
                        cell6 = cell6 + "G"
                    elif torn_jugador_V():
                        cell6 = cell6 + "V"
                    elif torn_jugador_B():
                        cell6 = cell6 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell7:    
                    if torn_jugador_T():
                        cell7 = cell7 + "T"
                    elif torn_jugador_G():
                        cell7 = cell7 + "G"
                    elif torn_jugador_V():
                        cell7 = cell7 + "V"
                    elif torn_jugador_B():
                        cell7 = cell7 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell8:    
                    if torn_jugador_T():
                        cell8 = cell8 + "T"
                    elif torn_jugador_G():
                        cell8 = cell8 + "G"
                    elif torn_jugador_V():
                        cell8 = cell8 + "V"
                    elif torn_jugador_B():
                        cell8 = cell8 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell9:    
                    if torn_jugador_T():
                        cell9 = cell9 + "T"
                    elif torn_jugador_G():
                        cell9 = cell9 + "G"
                    elif torn_jugador_V():
                        cell9 = cell9 + "V"
                    elif torn_jugador_B():
                        cell9 = cell9 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell10:    
                    if torn_jugador_T():
                        cell10 = cell10 + "T"
                    elif torn_jugador_G():
                        cell10 = cell10 + "G"
                    elif torn_jugador_V():
                        cell10 = cell10 + "V"
                    elif torn_jugador_B():
                        cell10 = cell10 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell11:    
                    if torn_jugador_T():
                        cell11 = cell11 + "T"
                    elif torn_jugador_G():
                        cell11 = cell11 + "G"
                    elif torn_jugador_V():
                        cell11 = cell11 + "V"
                    elif torn_jugador_B():
                        cell11 = cell11 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell12:    
                    if torn_jugador_T():
                        cell12 = cell12 + "T"
                    elif torn_jugador_G():
                        cell12 = cell12 + "G"
                    elif torn_jugador_V():
                        cell12 = cell12 + "V"
                    elif torn_jugador_B():
                        cell12 = cell12 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell13:    
                    if torn_jugador_T():
                        cell13 = cell13 + "T"
                    elif torn_jugador_G():
                        cell13 = cell13 + "G"
                    elif torn_jugador_V():
                        cell13 = cell13 + "V"
                    elif torn_jugador_B():
                        cell13 = cell13 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell14:    
                    if torn_jugador_T():
                        cell14 = cell14 + "T"
                    elif torn_jugador_G():
                        cell14 = cell14 + "G"
                    elif torn_jugador_V():
                        cell14 = cell14 + "V"
                    elif torn_jugador_B():
                        cell14 = cell14 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell15:    
                    if torn_jugador_T():
                        cell15 = cell15 + "T"
                    elif torn_jugador_G():
                        cell15 = cell15 + "G"
                    elif torn_jugador_V():
                        cell15 = cell15 + "V"
                    elif torn_jugador_B():
                        cell15 = cell15 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell16:    
                    if torn_jugador_T():
                        cell16 = cell16 + "T"
                    elif torn_jugador_G():
                        cell16 = cell16 + "G"
                    elif torn_jugador_V():
                        cell16 = cell16 + "V"
                    elif torn_jugador_B():
                        cell16 = cell16 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell17:    
                    if torn_jugador_T():
                        cell17 = cell17 + "T"
                    elif torn_jugador_G():
                        cell17 = cell17 + "G"
                    elif torn_jugador_V():
                        cell17 = cell17 + "V"
                    elif torn_jugador_B():
                        cell17 = cell17 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell18:    
                    if torn_jugador_T():
                        cell18 = cell18 + "T"
                    elif torn_jugador_G():
                        cell18 = cell18 + "G"
                    elif torn_jugador_V():
                        cell18 = cell18 + "V"
                    elif torn_jugador_B():
                        cell18 = cell18 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell19:    
                    if torn_jugador_T():
                        cell19 = cell19 + "T"
                    elif torn_jugador_G():
                        cell19 = cell19 + "G"
                    elif torn_jugador_V():
                        cell19 = cell19 + "V"
                    elif torn_jugador_B():
                        cell19 = cell19 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell20:    
                    if torn_jugador_T():
                        cell20 = cell20 + "T"
                    elif torn_jugador_G():
                        cell20 = cell20 + "G"
                    elif torn_jugador_V():
                        cell20 = cell20 + "V"
                    elif torn_jugador_B():
                        cell20 = cell20 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell21:    
                    if torn_jugador_T():
                        cell21 = cell21 + "T"
                    elif torn_jugador_G():
                        cell21 = cell21 + "G"
                    elif torn_jugador_V():
                        cell21 = cell21 + "V"
                    elif torn_jugador_B():
                        cell21 = cell21 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell22:    
                    if torn_jugador_T():
                        cell22 = cell22 + "T"
                    elif torn_jugador_G():
                        cell22 = cell22 + "G"
                    elif torn_jugador_V():
                        cell22 = cell22 + "V"
                    elif torn_jugador_B():
                        cell22 = cell22 + "B"

            if len(casella_actual) >= 1:
                if casella_actual == cell23:    
                    if torn_jugador_T():
                        cell23 = cell23 + "T"
                    elif torn_jugador_G():
                        cell23 = cell23 + "G"
                    elif torn_jugador_V():
                        cell23 = cell23 + "V"
                    elif torn_jugador_B():
                        cell23 = cell23 + "B"
        else:
            pass
    def compra_propietat(self,name_propietat): #Definir les propietats que té el jugador
        self.propietats.append(name_propietat)

    def add_carta_especial(self, carta): #Definir les cartes especials que té el jugador
        self.carta_especial.append(carta)#Només hi ha una carta especial
    
    def show_especial_card(self):
        if len(self.carta_especial) != 0:
            return True
        else:
            pass
    def add_especial_card(self): #Si el jugador té una carta especial mostrala, sino mostra "(res)""
        pass
    def diners_propietat(self, diner_propietat): #Definir els diners que té després de comprar un terreny, casa o hotel
        self.diners = (self.diners - diner_propietat)  
   
    def diners_sortida(self, sortida):#Definir els diners que té després de passar per la casella de sortida
        self.diners = (self.diners + sortida)
   
    def propietat_info(self):#Definir informació que es mostra en la pantalla
        return f"Propietats: {self.propietats}"
    def diner_info(self):
        return f"Diners: {self.diners}"
        
    def especial_info(self):
        return f"Especial:  {self.carta_especial}"


jugador_v = Jugador("V", "Vermell")
jugador_b =Jugador("B", "Blau")
jugador_g = Jugador("G", "Groc")
jugador_t = Jugador("T","Taronja")


"""
CASELLES ESPECIALS
"""


def Sortida (): #Funció casella sortida
    global valor_banca
    diners_sortida = 200
    if jugador_g.posicio == 0: #Si el jugador groc es troba en la casella sortida
        jugador_g.diners_sortida(diners_sortida) #El jugador guanya 200 euros
        valor_banca -= diners_sortida
    elif jugador_b.posicio == 0:
        jugador_b.diners_sortida(diners_sortida)
        valor_banca -= diners_sortida
    elif jugador_t.posicio == 0:
        jugador_t.diners_sortida(diners_sortida)
        valor_banca -= diners_sortida
    elif jugador_v.posicio == 0:
        jugador_v.diners_sortida(diners_sortida)
        valor_banca -= diners_sortida
    

def Anr_pro  (): #Funció casella anar presó
    anar_preso = 18
    if jugador_b.posicio == anar_preso:
        jugador_b.move_to(6,cells)
        jugador_b.a_preso = True
    elif jugador_g.posicio == anar_preso:
        jugador_g.move_to(6, cells)
        jugador_g.a_preso  = True
    elif jugador_t.posicio == anar_preso:
        jugador_t.move_to(6,cells)
        jugador_t.a_preso = True
    elif jugador_v.posicio == anar_preso:
        jugador_v.move_to(6,cells)
        jugador_v.a_preso = True

def Caixa (): #Funció casella caixa
    if jugador_b.posicio == 9 or jugador_b.posicio == 21:# Jugador blau
        carta_jugador = random.choice(cartes_caixa) 
        if carta_jugador == "Sortir de la presó": # Jugador Blau guanya sortir de la preso
            jugador_b.add_carta_especial(carta_jugador)
            cartes_caixa.remove(carta_jugador)
        else:
            if carta_jugador == "Anar a la presó": # Jugador Blau va a la presó
                Anr_pro()
            elif carta_jugador == "Error de la banca": # Jugador Blau guanya diners per error de la banca
                jugador_b.diners += 150
                print(f"Quina sort! Guanyes 150 per un error a la banca, carta: {carta_jugador}")
            elif carta_jugador == "Despeses mèdiques": # Jugador Blau perd diners per despeses mèdiques 
                jugador_b.diners -= 50
                print(f"Has de pagar 50, carta: {carta_jugador}")
            elif carta_jugador == "Despeses escolars": # Jugador Blau perd diners per despeses escolars
                jugador_b.diners -= 50
                print(f"Has de pagar 50, carta: {carta_jugador}")
            elif carta_jugador == "Reparacions al carrer": # Jugador Blau perd diners per  reparacions al carrer
                jugador_b.diners -= 40
                print(f"Has de pagar 40, carta: {carta_jugador}")
            elif carta_jugador  == "Concurs de bellesa":  # Jugador Blau guanya diners per guanyar un concurs de bellesa
                jugador_b.diners += 10
                print(f"Guanyes 10, carta: {carta_jugador}") 
            cartes_caixa.remove(carta_jugador)
            cartes_caixa.index(carta_jugador)   

    elif jugador_g.posicio == 9 or jugador_g.posicio == 21:#Jugador groc
        carta_jugador = random.choice(cartes_caixa)
        if carta_jugador == "Sortir de la presó": # Jugador Groc guanya sortir de la presó
            jugador_g.add_carta_especial(carta_jugador)
            cartes_caixa.remove(carta_jugador)
        else:
            if carta_jugador == "Anar a la presó": # Jugador Groc va a la presó
                Anr_pro()
            elif carta_jugador == "Error de la banca": # Jugador Groc guanya diners per error de la banca
                jugador_g.diners += 150
                print(f"Quina sort! Guanyes 150 per un error a la banca, carta: {carta_jugador}")
            elif carta_jugador == "Despeses mèdiques": # Jugador Groc perd diners per despeses mèdiques 
                jugador_g.diners -= 50
                print(f"Has de pagar 50, carta: {carta_jugador}")
            elif carta_jugador == "Despeses escolars": # Jugador Groc perd diners per despeses escolars
                jugador_g.diners -= 50
                print(f"Has de pagar 50, carta: {carta_jugador}")
            elif carta_jugador == "Reparacions al carrer": # Jugador Groc perd diners per  reparacions al carrer
                jugador_g.diners -= 40
                print(f"Has de pagar 40, carta: {carta_jugador}")
            elif carta_jugador  == "Concurs de bellesa": # Jugador Groc guanya diners per guanyar un concurs de bellesa
                jugador_g.diners += 10
                print(f"Guanyes 10, carta: {carta_jugador}")
            cartes_caixa.remove(carta_jugador)
            cartes_caixa.index(carta_jugador)

    elif jugador_t.posicio == 9 or jugador_t.posicio == 21: #Jugador taronja
        carta_jugador = random.choice(cartes_caixa)
        if carta_jugador == "Sortir de la presó": # Jugador Taronja guanya surt de la presó
            jugador_t.add_carta_especial(carta_jugador)
            cartes_caixa.remove(carta_jugador)
        else:
            if carta_jugador == "Anar a la presó": # Jugador Taronja  va a la presó
                Anr_pro()
            elif carta_jugador == "Error de la banca": # Jugador Taronja guanya diners per despesa de la banca 
                jugador_t.diners += 150
                print(f"Quina sort! Guanyes 150 per un error a la banca, carta: {carta_jugador}")
            elif carta_jugador == "Despeses mèdiques": # Jugador Taronja perd diners per despeses mèdiques
                jugador_t.diners -= 50
                print(f"Has de pagar 50, carta: {carta_jugador}")
            elif carta_jugador == "Despeses escolars": # Jugador Taronja perd diners per despeses escolars
                jugador_t.diners -= 50
                print(f"Has de pagar 50, carta: {carta_jugador}")
            elif carta_jugador == "Reparacions al carrer": # Jugador Taronja perd diners per reparacions al carrer
                jugador_t.diners -= 40
                print(f"Has de pagar 40, carta: {carta_jugador}")
            elif carta_jugador  == "Concurs de bellesa":  # Jugador Taronja guanya diners per guanyar un concurs de belles
                jugador_t.diners += 10
                print(f"Guanyes 10, carta: {carta_jugador}")
            cartes_caixa.remove(carta_jugador)
            cartes_caixa.index(carta_jugador) 

    elif jugador_v.posicio == 9 or jugador_v.posicio == 21: #Jugador vermell
        carta_jugador = random.choice(cartes_caixa)
        if carta_jugador == "Sortir de la presó": # Jugador Vermell guanya sortir de la presó
            jugador_v.add_carta_especial(carta_jugador)
            cartes_caixa.remove(carta_jugador)
        else:
            if carta_jugador == "Anar a la presó": # Jugador Vermell va a la presó
                Anr_pro()
            elif carta_jugador == "Error de la banca": # Jugador Vermell guanya diners per error de la banca
                jugador_v.diners += 150
                print(f"Quina sort! Guanyes 150 per un error a la banca, carta: {carta_jugador}")
            elif carta_jugador == "Despeses mèdiques": # Jugador Vermell perd diners per despeses mèdiques 
                jugador_v.diners -= 50
                print(f"Has de pagar 50, carta: {carta_jugador}")
            elif carta_jugador == "Despeses escolars": # Jugador Vermell perd diners per despeses escolars 
                jugador_v.diners -= 50
                print(f"Has de pagar 50, carta: {carta_jugador}")
            elif carta_jugador == "Reparacions al carrer":  # Jugador Vermell perd diners per reparacions al carrer    
                jugador_v.diners -= 40
                print(f"Has de pagar 40, carta: {carta_jugador}")
            elif carta_jugador  == "Concurs de bellesa": # Jugador Vermell guanya diners per concurs de bellesa
                jugador_v.diners += 10
                print(f"Guanyes 10, carta: {carta_jugador}")
                cartes_caixa.remove(carta_jugador)
                cartes_caixa.index(carta_jugador) 
def Sort  (): #Funció casella sort
    if jugador_b.posicio == 3 or jugador_b.posicio == 15: #Jugador blau
        carta_jugador2 = random.choice(cartes_sort)
        if carta_jugador2 == "Sortir de la presó": # Jugador Blau guanya sortir de la presó
            jugador_b.add_carta_especial(carta_jugador2)
            cartes_sort.remove(carta_jugador2)
        else:
            if carta_jugador2 == "Anar a la presó": # Jugador Blau va a la presó
                Anr_pro()
            elif carta_jugador2 == "Anar a la sortida": # Jugador Blau va a la sortida 
                jugador_b.move_to(0, cells)
                print("Tornes a la casella de sortida")
            elif carta_jugador2 == "Anar tres espais endarrera": #  Jugador Blau va tres espais endarrera
                jugador_b.move(-3,cells)
                print("Retrocedeix  espais")
            elif carta_jugador2 == "Fer reparacions a les propietats": # Jugador Blau perd diners per reparacions a les propietats
                if len(jugador_b.propietats) != 0 :
                    jugador_b.diners -=25
                    if j == 1 :
                        jugador_b.diners -= 100 
                cell15= "B"
            elif carta_jugador2 == "Ets escollit alcalde": # Jugador Blau guanya diners per ser escollit alcalde
                jugador_b.diners += 150
                jugador_g.diners -= 50
                jugador_t.diners -= 50
                jugador_v.diners -= 50
                
            cartes_sort.remove(carta_jugador2)
            cartes_sort.index(carta_jugador2) 
                
    elif jugador_g.posicio == 3 or jugador_g.posicio == 15: #Jugador groc
        carta_jugador2 = random.choice(cartes_sort)
        if carta_jugador2 == "Sortir de la presó": # Jugador Groc guanya sortir de la presó
            jugador_g.add_carta_especial(carta_jugador2)
            cartes_sort.remove(carta_jugador2)
        else:
            if carta_jugador2 == "Anar a la presó": # Jugador Groc va a la presó
                Anr_pro()
            elif carta_jugador2 == "Anar a la sortida": # Jugador Groc va a la sortida 
                jugador_g.move_to(0, cells)
                print("Torna a la sortida")
            elif carta_jugador2 == "Anar tres espais endarrera": # Jugador Groc va tres espais endarrera
                jugador_g.move(-3,tauler)
                print("Retrocedeix 3 caselles")
            elif carta_jugador2 == "Fer reparacions a les propietats": # Jugador Groc perd diners per reparacions a les propietats
                if len(jugador_g.propietats) != 0 :
                    jugador_g.diners -=25
                    if j == 1 :
                        jugador_g.diners -= 100 
                

            elif carta_jugador2 == "Ets escollit alcalde": # Jugador Groc guanya diners per ser escollit alcalde
                jugador_b.diners -= 50
                jugador_g.diners += 150
                jugador_t.diners -= 50
                jugador_v.diners -= 50
            cartes_sort.remove(carta_jugador2)
            cartes_sort.index(carta_jugador2) 

    elif jugador_t.posicio == 3 or jugador_t.posicio == 15: #Jugador taronja
        carta_jugador2 = random.choice(cartes_sort)
        if carta_jugador2 == "Sortir de la presó": # Jugador Taronja guanya sortir de la presó
            jugador_t.add_carta_especial(carta_jugador2)
            cartes_sort.remove(carta_jugador2)
        else:
            if carta_jugador2 == "Anar a la presó": # Jugador Taronja va a la preso
                Anr_pro()
            elif carta_jugador2 == "Anar a la sortida": # Jugador Taronja va a la sortida 
                jugador_t.move_to(0, tauler)
                print("Torna a la casella de sortida")
            elif carta_jugador2 == "Anar tres espais endarrera": # Jugador Taronja va tres espais enderrera 
                jugador_t.move(-3,tauler)
                print("Retrocedeix 3 caselles")

            elif carta_jugador2 == "Fer reparacions a les propietats": # Jugador Taronja perd diners per reparacions a les propietats
                if len(jugador_t.propietats) != 0 :
                    jugador_t.diners -= 25
                    if j == 1 :
                        jugador_t.diners -= 100 
               
            elif carta_jugador2 == "Ets escollit alcalde": # Jugador Taronja guanya diners per ser escollit alcalde

                jugador_b.diners -= 50
                jugador_g.diners -= 50
                jugador_t.diners += 150
                jugador_v.diners -= 50
                
                
            cartes_sort.remove(carta_jugador2)
            cartes_sort.index(carta_jugador2)  

    elif jugador_v.posicio == 3 or jugador_v.posicio == 15: #Jugador vermell
        carta_jugador2 = random.choice(cartes_sort)
        if carta_jugador2 == "Sortir de la presó": # Jugador Vermell guanya sortir de la presó
            jugador_v.add_carta_especial(carta_jugador2)
            cartes_sort.remove(carta_jugador2)
        else:
            if carta_jugador2 == "Anar a la presó": # Jugador Vermell va a la presó
                Anr_pro()
                
            elif carta_jugador2 == "Anar a la sortida": # Jugador Vermell va la sortida 
                jugador_v.move_to(0, tauler)
                print("Torna a la casella de sortida")
            elif carta_jugador2 == "Anar tres espais endarrera": # Jugador Vermell va tres espais enderrera 
                jugador_v.move(-3,tauler)
                print("Retrocedeix 3 caselles")
            elif carta_jugador2 == "Fer reparacions a les propietats": # Jugador Vermell perd diners per reparacions a les propietats
                if len(jugador_v.propietats) != 0 :
                    jugador_v.diners -= 25
                    if j == 1 :
                        jugador_v.diners -= 100 
                
            elif carta_jugador2 == "Ets escollit alcalde": # Jugador Vermell guanya diners per ser escollit alcalde
                jugador_b.diners -= 50
                jugador_g.diners -= 50
                jugador_t.diners -= 50
                jugador_v.diners += 150
               

            cartes_sort.remove(carta_jugador2)
            cartes_sort.index(carta_jugador2) 

def Preso (): #Funció casella presó
    if jugador_b.a_preso ==  True:
        jugador_b.en_preso = True
        if jugador_b.show_especial_card() == True:
            jugador_b.en_preso = False
            return "El jugador \"B\" surt de la presó"
        elif valor_dau_1 == valor_dau_2:
            jugador_b.en_preso = True
            return "El jugador \"B\" ha tirat dobles i pot sortir de la presó"
    jugador_b.torns_a_preso += 1
    if jugador_b.torns_a_preso >= 3:
        jugador_b.en_preso = False
        return "El jugador \"B\" ha estat tres torns a presó i pot sortir"

"""
CASES I HOTELS
                -Afegir número cases i hotels en cada cas (3C1H) canviant (---) o  ("|")
"""
# Inicializamos las cantidades de casas (i) y hoteles (j)
i = 0
j = 0

# Función para intentar comprar un hotel
def comprar_j(cantidad):
    global i, j
    if j + cantidad > 2:
        print("No se pueden comprar más de 2 hoteles.")
    else:
        for _ in range(cantidad):
            if i >= 2:
                i -= 2  # Restar 2 casas por cada hotel comprado
                j += 1
                print(f"Compraste 1 hotel. Ahora tienes {i} casas y {j} hotel(es).")
            else:
                print("No tienes suficientes casas para comprar un hotel.")
                break

# Función para intentar comprar casas
def comprar_i(cantidad):
    global i, j
    if j == 2:
        print("No se pueden comprar casas porque ya tienes 2 hoteles.")
    elif j == 1 and i + cantidad > 2:
        print("No se pueden tener más de 2 casas con 1 hotel.")
    elif j == 0 and i + cantidad > 4:
        print("No se pueden comprar más de 4 casas.")
    else:
        i += cantidad
        print(f"Compraste {cantidad} casa(s). Ahora tienes {i} casas y {j} hotel(es).")




"""
INFORMACIÓ PARTIDA (CENTRE)
                            -Mostra les accions que passen a la partida
"""
def accions_partida():
    pass


"""
INFORMACIÓ PARTIDA (DRETA)
                            -Els jugadors es mostren per ordre de tirada
                            -Els carrers es mostren per ordre en el taulell
"""




"""
INFORMACIÓ PARTIDA (SOTA)
"""
def preu_terreny(casilla): #Definir el preu que ha de pagar per el terreny seleccionat
    if jugador_b.posicio == casilla: #Casilla igual al número de casella
        if casilla == [1,2,4,5]:
            return f"El preu del terreny és de:{diners_propietats[0]} "
        elif casilla == [7,8,10,11]:
            return f"El preu del terreny és de:{diners_propietats[1]}"
        elif casilla == [13,14,16,17]:
            return f"El preu del terreny és de:{diners_propietats[2]}"
        elif casilla == [19,20,22,23]:
            return f"El preu del terreny és de:{diners_propietats[3]}"
        else:
            pass
    
    if jugador_t.posicio == casilla: #Casilla igual al número de casella
        if casilla == [1,2,4,5]:
            return f"El preu del terreny és de:{diners_propietats[0]} "
        elif casilla == [7,8,10,11]:
            return f"El preu del terreny és de:{diners_propietats[1]}"
        elif casilla == [13,14,16,17]:
            return f"El preu del terreny és de:{diners_propietats[2]}"
        elif casilla == [19,20,22,23]:
            return f"El preu del terreny és de:{diners_propietats[3]}"
        else:
            pass

    if jugador_g.posicio == casilla: #Casilla igual al número de casella
        if casilla == [1,2,4,5]:
            return f"El preu del terreny és de:{diners_propietats[0]} "
        elif casilla == [7,8,10,11]:
            return f"El preu del terreny és de:{diners_propietats[1]}"
        elif casilla == [13,14,16,17]:
            return f"El preu del terreny és de:{diners_propietats[2]}"
        elif casilla == [19,20,22,23]:
            return f"El preu del terreny és de:{diners_propietats[3]}"
        else:
            pass
    
    if jugador_v.posicio == casilla: #Casilla igual al número de casella
        if casilla == [1,2,4,5]:
            return f"El preu del terreny és de:{diners_propietats[0]} "
        elif casilla == [7,8,10,11]:
            return f"El preu del terreny és de:{diners_propietats[1]}"
        elif casilla == [13,14,16,17]:
            return f"El preu del terreny és de:{diners_propietats[2]}"
        elif casilla == [19,20,22,23]:
            return f"El preu del terreny és de:{diners_propietats[3]}"
        else:
            pass


"""
Definir turno jugadores en los condicionales
"""




def accio_usuari(): # Funcio de les accions del usuari
    text = (f"Juga {jugador_b}, opcions: passar, comprar terreny, preus")
    text2 = (f"Juga {jugador_b}, opcions: passar, comprar casa, comprar hotel, preus")
    pass
"""
TABLERO
        -Variables casellas (cell(número))
        -Variables cases i hotels (casa(número))
"""




casa1,casa2,casa3,casa4,casa9,casa10,casa11,casa12 = "--","--","--","--","--","--","--","--"
casa5,casa6,casa7,casa8,casa13,casa14,casa15,casa16 = " |"," |"," |"," |"," |"," |"," |"," |"


    


# Definición de variables


def tablero(): #Funció imprimeix tauler
   
    texto0 = ""
    texto1 = ""
    texto2 = ""
    texto3 = ""
    texto4 = ""    
    texto5 = ""
    texto6 = ""
    texto7 = ""
    texto8 = ""
    texto9 = ""
    texto10 = ""
    texto11 = ""
    texto12 = ""
    texto13 = ""


    info_0 = jugador_t.propietat_info()
    info_1 = jugador_g.propietat_info()
    info_2 = jugador_b.propietat_info()
    info_3 = jugador_v.propietat_info()
    info_4 = jugador_t.diner_info()
    info_5 = jugador_g.diner_info()
    info_6  = jugador_b.diner_info()
    info_7 = jugador_v.diner_info()
    info_8 = jugador_t.especial_info()
    info_9 = jugador_g.especial_info()
    info_10 = jugador_b.especial_info()
    info_11 = jugador_v.especial_info()    

    print(f"+--------+----{casa9:<2}--+----{casa10:<2}--+--------+----{casa11:<2}--+----{casa12:<2}--+--------+ Banca:") 
    print(f"|Parking |Urqinoa |Fontan  |Sort    |Rambles |Pl.Cat  |Anr pró | Diners: {banca()}")                                           
    print(f"|{cell12:<8}|{cell13:<8}|{cell14:<8}|{cell15:<8}|{cell16:<8}|{cell17:<8}|{cell18:<8}|")
    print(f"+--------+--------+--------+--------+--------+--------+--------+ Jugador {Jugador_0}:")
    print(f"|Aragó  {casa8:<2}{texto13:<8}                                    | Angel {casa13:<2} {info_0}")
    print(f"|{cell11:<8}|{texto12:<8}                                    |{cell19:<8}| {info_4}")
    print(f"+--------+{texto11:<8}                                    +--------+ {info_8}")
    print(f"|S.Joan {casa7:<2}{texto10:<8}                                    |Augusta{casa14:<2} Jugador {Jugador_1}:")
    print(f"|{cell10:<8}|{texto9:<8}                                    |{cell20:<8}|  {info_1}")
    print(f"+--------+{texto8:<8}                                    +--------+ {info_5}")
    print(f"|Caixa   |{texto7:<8}                                    |Caixa   | {info_9}")
    print(f"|{cell9:<8}|{texto6:<8}                                    |{cell21:<8}| Jugador {Jugador_2}")
    print(f"+--------+{texto5:<8}                                    +--------+ {info_2}")
    print(f"|Aribau {casa6:<2}{texto4:<8}                                    |Balmes {casa15:<2} {info_6}")
    print(f"|{cell8:<8}|{texto3:<8}                                    |{cell22:<8}| {info_10}")
    print(f"+--------+{texto2:<8}                                    +--------+ Jugador {Jugador_3}")
    print(f"|Muntan {casa5:<2}{texto1:<8}                                    |Gracia {casa16:<2} {info_3}")
    print(f"|{cell7:<8}|{texto0:>8}                                    |{cell23:<8}| {info_7}")
    print(f"+--------+----{casa4:<2}--+----{casa3:<2}--+--------+----{casa2:<2}--+----{casa1:<2}--+--------+ {info_11}")
    print(f"|{cell6:<8}|{cell5:<8}|{cell4:<8}|{cell3:<8}|{cell2:<8}|{cell1:<8}|{cell0:<8}|")
    print(f"|Presó   |Consell |Marina  |Sort    |Rosell  |Lauria  |Sortida |")
    print(f"+--------+--------+--------+--------+--------+--------+--------+")
    








"""
INICI PARTIDA
                -Cada jugador comença amb 2000 euros
                -Mostra sempre a cada casella el primer jugador 
                -Barrejar les cartes de caixa i sort
"""
suma_daus, resultat_daus = llançar_daus()

def inici_partida():
  """Inicia la partida amb els jugadors tenint 2000 euros."""
 
  # Definir els jugadors
  random.shuffle(cartes_caixa) #Barreja les cartes de caixa
  random.shuffle(cartes_sort) #Barreja les cartes de sort
  ordre() #Crida la funció ordre
  tablero() #Crida la funció imprimeix tauler (imprimeix tauler)
  torn(torn_actual)
  llançar_daus()
  if torn_jugador_B():
    jugador_b.move(suma_daus,tauler)
  elif torn_jugador_G():
      jugador_g.move(suma_daus,tauler)
  elif torn_jugador_T():
      jugador_t.move(suma_daus,tauler)
  elif torn_jugador_V():
      jugador_v.move(suma_daus,tauler)
  opcions(jugador_actual)
 
"""
TRUCS
        -Anar a una casella
        -Afegir X cases
        -Afegir X hotels
        -Seguent X (jugador, saltar torn)
        -Diners X YY (Jugador, Quantitat)
        -Diners X banca
"""
def anar_casella():  # Funcio de trucs per escollir a quina casella anar
    next_cell = input("Escull una casella : ")
    jugador_b.move_to(next_cell,tauler)
    jugador_g.move_to(next_cell,tauler)
    jugador_t.move_to(next_cell,tauler)
    jugador_v.move_to(next_cell,tauler)
def afegir_cases():  # Funcio de trucs per afegir cases
    i  = input ("Indica les cases que vols afegir")
    comprar_i(i)
def afegir_hotels(): # Funcio de trucs per afegir hotels 
    j = input("Indica els hotels que vols afegir")
    comprar_j(j)
def next_player():   # Funcio de trucs per escollir el jugador que segueix
    canviar_torn = input("Indica el torn al que vols pasar")
    torn(canviar_torn)
def diners_player(): # Funcio de trucs per  afegir diners a un jugador
    afegir_diners = input("Indica els diners que vols afegir")
    if next_player == "B" :
        jugador_b.diners  += afegir_diners
    elif next_player == "V" :
        jugador_v.diners +=  afegir_diners
    elif  next_player == "T" :
        jugador_t.diners += afegir_diners
    elif next_player == "G" :
        jugador_g.diners += afegir_diners
    else  : 
        return "ERROR"

def diners_banca():  # Funcio de trucs per afegir diners a la banca
    afegir_diners_banca = input("Indica els diners que vols afegir a la banca")
    valor_banca = afegir_diners_banca
    return valor_banca
def trucs():
    print("1. Anar a una casella")
    print("2. Afegir X cases")
    print("3. Afegir X hotels")
    print("4. Seguent X (jugador, saltar torn)")
    print("5.  Diners X YY (Jugador, Quantitat)")
    print("6. Diners X banca")
    eleccio = input("Escull una opció : ")
    return eleccio


cell0 = orden[0] + orden[1] + orden[2]+ orden[3] #
print(orden)

"""if torn_jugador_B():
    casilla = tauler[0].replace("Lauria", "B")
    jugador_b.move(resultat_daus,tauler)
    jugador_b.posicio = 1
    cell1 = "B"
    cell0 = orden[1] + orden[2] + orden[3]
elif torn_jugador_V():
    casilla = tauler[0].replace("Lauria", "V")
    jugador_v.move(resultat_daus,tauler)
    jugador_v.posicio = 1
    cell1 = "V"
    cell0 = orden[1] + orden[2] + orden[3]
elif torn_jugador_T():
    casilla = tauler[0].replace("Lauria", "T")
    jugador_t.move(resultat_daus,tauler)
    jugador_t.posicio = 1
    cell1 = "T"
    cell0 = orden[1] + orden[2] + orden[3]
elif torn_jugador_G():
    casilla = tauler[0].replace("Lauria", "G")
    jugador_b.move(resultat_daus,tauler)
    jugador_b.posicio = resultat_daus
    if resultat_daus == 2:
        cell2 = "G"
   
    cell0 = orden[1] + orden[2] + orden[3]"""

inici_partida()

