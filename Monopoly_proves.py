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


def cambiar_turno():
    global torn_actual
    torn_actual = (torn_actual + 1) % 4  # Hay 4 jugadores
    return torn(torn_actual)  # Devuelve el nuevo jugador
    
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
    if jugador.propietats != 0:   
        opcion_jugador = input(f"Torn \"{jugador_actual}\", opcions --> (passar, compra terreny, preus):  ")
        if opcion_jugador == 1 or opcion_jugador == "comprar  terreny":
            if torn_jugador_B():
                jugador_b.compra_propietat(cells[jugador_b.posicio])
            elif torn_jugador_G():
                jugador_g.compra_propietat(cells[jugador_g.posicio])
            elif torn_jugador_T():
                jugador_t.compra_propietat(cells[jugador_t.posicio])
            elif  torn_jugador_V():
                jugador_v.compra_propietat(cells[jugador_v.posicio])

        elif opcion_jugador == "preus" or opcion_jugador == 2:
            return preu_terreny(jugador.posicio)
        elif opcion_jugador == "trucs".lower():
            trucs()
        elif opcion_jugador == "passar".lower() or opcion_jugador == 0:
            # Pasar al siguiente jugador
            cambiar_turno()
            return jugador_actual  # Retornar el nuevo jugador y su índice

    

    elif jugador.propietats >= 1:
        opcion_jugador = input(f"Juga {jugador_actual}, opcions: passar, comprar casa, comprar hotel, preus: ")
        if opcion_jugador == 1 or opcion_jugador == "comprar  terreny":
            if torn_jugador_B():
                jugador_b.compra_propietat(cells[jugador_b.posicio])
            elif torn_jugador_G():
                jugador_g.compra_propietat(cells[jugador_g.posicio])
            elif torn_jugador_T():
                jugador_t.compra_propietat(cells[jugador_t.posicio])
            elif  torn_jugador_V():
                jugador_v.compra_propietat(cells[jugador_v.posicio])

        elif opcion_jugador == "preus" or opcion_jugador == 2:
            return preu_terreny(jugador.posicio)
        elif opcion_jugador == "trucs".lower():
            trucs()
        elif opcion_jugador == "passar".lower() or opcion_jugador == 0:
            # Pasar al siguiente jugador
            cambiar_turno()
            
            return jugador_actual  # Retornar el nuevo jugador y su índice


"""
CASELLAS EN LLISTA
"""
cells = ["", "", "", "", "", "", "", "", "", "", "",
         "", "", "", "", "", "", "", "", "", "",
         "", "", ""]

"""
JUGADORS
            -Class Jugador
            -Jugadors definits per color
"""
  


class Jugador:#Definir class Jugador

    def __init__(self,name,color):
        self.name = name
        self.color = color
        self.posicio = None #Comença a la casella "sortida"
        self.propietats = [] #Lista de les propietats que té l'usuari
        self.carta_especial = [] #Lista de les cartes especials (Sortir de la presó)
        self.diners = 2000 #Diners amb els que comença cada partida els jugadors
        self.a_preso = False #False per definir que el jugador no es troba a presó
        self.torns_a_preso = 0 #Número torns a preso
    
    def daus(self):
        suma_dados()
        llançar_daus()
        self.posicio = (self.posicio + suma_daus) % len(cells)
        return self.posicio
    def en_preso(self):
        return self.a_preso()
    
    def move(self):
        global suma_daus
        """if self.a_preso == True:
            print("Jugador a presó, no pot jugar")"""
        
        cells[self.posicio] = ""
        
        self.posicio2 = (self.posicio + suma_daus) % len(cells)
        

        if cells[self.posicio2] == "":
            if torn_jugador_B():
                cells[self.posicio2] = "B"
            elif torn_jugador_G():
                cells[self.posicio2] = "G"
            elif torn_jugador_T():
                cells[self.posicio2] = "T"
            elif torn_jugador_V():
                cells[self.posicio2] = "V"
            else:
                return ""
        else:
            if torn_jugador_V():
                cells[self.posicio2] += "V"
            elif torn_jugador_B():
                cells[self.posicio2] += "B"
            elif  torn_jugador_G():
                cells[self.posicio2]  += "G"
            elif  torn_jugador_T():
                cells[self.posicio2]   += "T"
            else:
                return ""
                

    
        
    def move_to(self, casella):
        if 0 <= casella < len(cells):
            cells[self.posicio]  = ""
            
                                  
            if cells[casella] == "":
                if torn_jugador_B():
                    cells[casella] = "B"
                elif torn_jugador_G():
                    cells[casella] = "G"
                elif torn_jugador_T():
                    cells[casella] = "T"
                elif torn_jugador_V():
                    cells[casella] = "V"
            else:
                if torn_jugador_B():
                    cells[casella] += "B"
                elif torn_jugador_G():
                    cells[casella] += "G"
                elif torn_jugador_T():
                    cells[casella] += "T"
                elif torn_jugador_V():
                    cells[casella] += "V"
                else:
                    return ""

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
                    if hotels == 1 :
                        jugador_b.diners -= 100 
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
                    if hotels == 1 :
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
                    if hotels == 1 :
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
                    if hotels == 1 :
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
            jugador_b.a_preso = False
            return "El jugador \"B\" surt de la presó"
        elif valor_dau_1 == valor_dau_2:
            jugador_b.a_preso = False
            return "El jugador \"B\" ha tirat dobles i pot sortir de la presó"
            
    elif jugador_v.a_preso ==  True:
        jugador_v.en_preso = True
        if jugador_v.show_especial_card() == True:
            jugador_v.a_preso = False
            return "El jugador \"V\" surt de la presó"
        elif valor_dau_1 == valor_dau_2:
            jugador_v.a_preso = False
            return "El jugador \"V\" ha tirat dobles i pot sortir de la presó"
    
   
    elif jugador_g.a_preso ==  True:
        jugador_g.en_preso = True
        if jugador_g.show_especial_card() == True:
            jugador_g.a_preso = False
            return "El jugador \"G\" surt de la presó"
        elif valor_dau_1 == valor_dau_2:
            jugador_g.a_preso = False
            return "El jugador \"G\" ha tirat dobles i pot sortir de la presó"
    
    
    elif jugador_t.a_preso ==  True:
        jugador_t.en_preso = True
        if jugador_t.show_especial_card() == True:
            jugador_t.a_preso = False
            return "El jugador \"T\" surt de la presó"
        elif valor_dau_1 == valor_dau_2:
            jugador_t.a_preso = False
            return "El jugador \"T\" ha tirat dobles i pot sortir de la presó"
    

        jugador_b.torns_a_preso += 1 
        jugador_t.torns_a_preso += 1 
        jugador_v.torns_a_preso += 1 
        jugador_g.torns_a_preso += 1 
        if jugador_b.torns_a_preso >= 3:
            jugador_b.a_preso = False
            return "El jugador \"B\" ha estat tres torns a presó i pot sortir"
        elif jugador_v.torns_a_preso >= 3:
            jugador_v.a_preso = False
            return "El jugador \"V\" ha estat tres torns a presó i pot sortir"
        elif jugador_g.torns_a_preso >= 3:
            jugador_g.a_preso = False
            return "El jugador \"G\" ha estat tres torns a presó i pot sortir"
        elif jugador_t.torns_a_preso >= 3:
            jugador_t.a_preso = False
            return "El jugador \"T\" ha estat tres torns a presó i pot sortir"


"""     
CASES I HOTELS
                -Afegir número cases i hotels en cada cas (3C1H) canviant (---) o  ("|")
"""
# Inicializamos las cantidades de casas (i) y hoteles (j)
cases = 0
hotels = 0

# Función para intentar comprar un hotel
def comprar_hotels(cantidad):
    global cases, hotels
    if hotels + cantidad > 2:
        print("No se pueden comprar más de 2 hoteles.")
    else:
        for _ in range(cantidad):
            if cases >= 2:
                cases -= 2  # Restar 2 casas por cada hotel comprado
                hotels += 1
                print(f"Compraste 1 hotel. Ahora tienes {cases} casas y {hotels} hotel(es).")
            else:
                print("No tienes suficientes casas para comprar un hotel.")
                

# Función para intentar comprar casas
def comprar_cases(cantidad):
    global cases, hotels
    if hotels == 2:
        print("No se pueden comprar casas porque ya tienes 2 hoteles.")
    elif hotels == 1 and cases + cantidad > 2:
        print("No se pueden tener más de 2 casas con 1 hotel.")
    elif hotels == 0 and cases + cantidad > 4:
        print("No se pueden comprar más de 4 casas.")
    else:
        cases += cantidad
        print(f"Compraste {cantidad} casa(s). Ahora tienes {cases} casas y {hotels} hotel(es).")




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
    print(f"|{cells[12]:<8}|{cells[13]:<8}|{cells[14]:<8}|{cells[15]:<8}|{cells[16]:<8}|{cells[17]:<8}|{cells[18]:<8}|")
    print(f"+--------+--------+--------+--------+--------+--------+--------+ Jugador {Jugador_0}:")
    print(f"|Aragó  {casa8:<2}{texto13:<8}                                    | Angel {casa13:<2} {info_0}")
    print(f"|{cells[11]:<8}|{texto12:<8}                                    |{cells[19]:<8}| {info_4}")
    print(f"+--------+{texto11:<8}                                    +--------+ {info_8}")
    print(f"|S.Joan {casa7:<2}{texto10:<8}                                    |Augusta{casa14:<2} Jugador {Jugador_1}:")
    print(f"|{cells[10]:<8}|{texto9:<8}                                    |{cells[20]:<8}|  {info_1}")
    print(f"+--------+{texto8:<8}                                    +--------+ {info_5}")
    print(f"|Caixa   |{texto7:<8}                                    |Caixa   | {info_9}")
    print(f"|{cells[9]:<8}|{texto6:<8}                                    |{cells[21]:<8}| Jugador {Jugador_2}")
    print(f"+--------+{texto5:<8}                                    +--------+ {info_2}")
    print(f"|Aribau {casa6:<2}{texto4:<8}                                    |Balmes {casa15:<2} {info_6}")
    print(f"|{cells[8]:<8}|{texto3:<8}                                    |{cells[22]:<8}| {info_10}")
    print(f"+--------+{texto2:<8}                                    +--------+ Jugador {Jugador_3}")
    print(f"|Muntan {casa5:<2}{texto1:<8}                                    |Gracia {casa16:<2} {info_3}")
    print(f"|{cells[7]:<8}|{texto0:>8}                                    |{cells[23]:<8}| {info_7}")
    print(f"+--------+----{casa4:<2}--+----{casa3:<2}--+--------+----{casa2:<2}--+----{casa1:<2}--+--------+ {info_11}")
    print(f"|{cells[6]:<8}|{cells[5]:<8}|{cells[4]:<8}|{cells[3]:<8}|{cells[2]:<8}|{cells[1]:<8}|{cells[0]:<8}|")
    print(f"|Presó   |Consell |Marina  |Sort    |Rosell  |Lauria  |Sortida |")
    print(f"+--------+--------+--------+--------+--------+--------+--------+")
    

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
    casas  = input ("Indica les cases que vols afegir")
    comprar_cases(casas)
def afegir_hotels(): # Funcio de trucs per afegir hotels 
    hoteles = input("Indica els hotels que vols afegir")
    comprar_hotels(hoteles)
def next_player():   # Funcio de trucs per escollir el jugador que segueix
    canviar_torn = input("Indica el torn al que vols pasar")
    torn(canviar_torn)
def diners_player(): # Funcio de trucs per  afegir diners a un jugador
    afegir_diners = input("Indica els diners que vols afegir")
    if torn_jugador_B():
        jugador_b.diners  += afegir_diners
    elif torn_jugador_V():
        jugador_v.diners +=  afegir_diners
    elif  torn_jugador_T() :
        jugador_t.diners += afegir_diners
    elif torn_jugador_G():
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
    if eleccio == 1 or  eleccio == "Anar a una casella" :
        anar_casella()
    elif eleccio == 2 or eleccio == "Afegir X cases":
        afegir_cases()
    elif  eleccio == 3 or eleccio == "Afegir X hotels":
        afegir_hotels()
    elif eleccio == 4 or eleccio == "Seguent X (jugador, saltar torn)":
        next_player()
    elif  eleccio == 5 or eleccio == "Diners X YY (Jugador, Quantitat)":
        diners_player()
    elif eleccio == 6 or eleccio ==  "Diners X banca":
        diners_banca()
    elif eleccio == "trucs": 
        trucs()
    else:
        pass

"""
INICI PARTIDA
                -Cada jugador comença amb 2000 euros
                -Mostra sempre a cada casella el primer jugador 
                -Barrejar les cartes de caixa i sort
"""


def inici_partida():
    jugador_t.posicio = 0
    jugador_g.posicio = 0
    jugador_v.posicio = 0
    jugador_b.posicio = 0    
    """Inicia la partida amb els jugadors tenint 2000 euros."""
    cells[0] = orden[0] + orden[1] + orden[2]+ orden[3]
    # Definir els jugadors
  
    random.shuffle(cartes_caixa) #Barreja les cartes de caixa
    random.shuffle(cartes_sort) #Barreja les cartes de sort
    ordre() #Crida la funció ordre
    tablero() #Crida la funció imprimeix tauler (imprimeix tauler)
    torn(torn_actual)
  
  


inici_partida()

if torn_jugador_B():
    jugador_b.daus()
    jugador_b.move()
elif torn_jugador_V():
    jugador_v.daus()
    jugador_v.move()
elif  torn_jugador_G():
    jugador_g.daus()
    jugador_g.move()
elif  torn_jugador_T():
    jugador_t.daus()
    jugador_t.move()
else:
    print("None detected") 

opcions(torn_actual)




