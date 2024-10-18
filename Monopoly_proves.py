"""
Monopoly --> grupo: Manel y Víctor

1 -- Dibuixar tauler i fer funció daus individualment
2 -- Tauler amb noms
3 -- Definir banca quan doni diners als jugadors i es quedi amb 500.000 euros (Fer que s'afegeixin 1M d'euros).
4 -- Definir ordre tirada (amb random) fer que apareixin les inicials dels colors
       que comencen en ordre ( exemple: VGTB)
5 -- Definir inici_partida(); Els jugadors comencen amb 2000 euros.
6 -- Definir els jugadors amb 4 funcions diferents; (Els color taronja, groc, blava i vermell)
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
Coses fetes:
       /
daus \/

"""

"""
IMPORTS
"""
from tauler import *
from llistes import *
from daus import *
import random


"""
BANCA
        -Si el valor de la banca es menor que 500.000 euros suma a la banca 1M
        -Retorna el valor de la banca
"""
valor_banca = None

def banca():#Funció diners banca
    valor_inicial = 1000000
    valor = 500000
    if valor_inicial <= valor:
        valor_banca = valor_inicial + 1000000
        return valor_banca
    else:
        valor_banca = valor_inicial
    # Retorna el valor en diners que te la banca en aquell moment
    return valor_banca
"""
JUGADORS
"""

def jugador_groc(): #Funció jugador groc
    diners_groc= 2000
    jugador_g = None
    Carrers_g = []
    Diners_g = []
    Caselles_g = []
    return Carrers_g,Diners_g,Caselles_g, diners_groc,jugador_g
def jugador_taronja():#Funció jugador taonja
    diners_taronja= 2000
    jugador_t = None
    Carrers_t = []
    Diners_t = []
    Caselles_t = []
    return Carrers_t,Diners_t,Caselles_t, diners_taronja, jugador_t
def jugador_blau():#Funció jugador blau
    diners_blau= 2000
    jugador_b = None
    Carrers_b = []
    Diners_b = []
    Caselles_b = []
    return Carrers_b,Diners_b,Caselles_b, diners_blau, jugador_b
def jugador_vermell():#Funció jugador vermell
    diners_vermell = 2000
    jugador_v = None
    Carrers_v = []
    Diners_v = []
    Caselles_v = []
    return Carrers_v,Diners_v,Caselles_v, diners_vermell, jugador_v

"""
ORDRE TIRADA
                -Aleatoriament selecciona al principi de cada partida
                -Condicional para saber que valores entre el 0 i el 3 tienen los jugadores
                -
"""
def ordre(): #Funció mostra els jugadors a l'atzar
    players = ["V","T","G","B"]
    orden = []
    for _ in range(4):    
        eleccio = random.choice(players)
        orden.append(eleccio)
        print(eleccio, end="")
        players.remove(eleccio)
    print()
    global jugador_v, jugador_t, jugador_g, jugador_b
#Defineixo per variables els jugadors
    if orden[0] == "V":#Si vermell es troba al primer lloc de la llista orden
        jugador_v = 0 #Defineixo el jugador amb una variable
        if orden[1] == "T":##
            jugador_t = 1
            if orden[2] == "B":###
                jugador_b = 2
            elif orden[2] == "G":###
                jugador_g = 2
        elif orden[1] == "G":##
            print("groc juga segon")
            if orden[2] == "B":###
                print("blau juga tercer")
            elif orden[2] == "T":###
                print("taronja juga tercer")
        elif orden[1] == "B":##
            print("blau juga segon")
            if orden[2] == "T":###
                print("taronja juga tercer")
            elif orden[2] == "G":###
                print("groc juga tercer")
    elif orden[0] == "T":#Si taronja es troba al primer lloc de la llista orden
        print("taronja juga primer")
        if orden[1] == "V":##
            print("vermell juga segon")
            if orden[2] == "B":###
                print("blau juga tercer")
            elif orden[2] == "G":###
                print("groc juga tercer")
        elif orden[1] == "G":##
            print("groc juga segon")
            if orden[2] == "B":###
                print("blau juga tercer")
            elif orden[2] == "V":###
                print("vermell juga tercer")
        elif orden[1] == "B":##
            print("blau juga segon")
            if orden[2] == "V":###
                print("vermell juga tercer")
            elif orden[2] == "G":###
                print("groc juga tercer")
    elif  orden[0] == "G":#Si groc es troba al primer lloc de la llista orden
        print("groc juga primer")
        if orden[1] == "T":##
            print("taronja juga segon")
            if orden[2] == "B":###
                print("blau juga tercer")
            elif orden[2] == "V":###
                print("vermell juga tercer")
        elif orden[1] == "V":##
            print("vermell juga segon")
            if orden[2] == "B":###
                print("blau juga tercer")
            elif orden[2] == "T":###
                print("taronja juga tercer")
        elif orden[1] == "B":##
            print("blau juga segon")
            if orden[2] == "V":###
                print("vermell juga tercer")
            elif orden[2] == "T":###
                print("taronja juga tercer")
    elif orden[0] == "B":#Si blau es troba al primer lloc de la llista orden
        print("blau juga primer")
        if orden[1] == "T":##
            print("taronja juga segon")
            if orden[2] == "V":###
                print("vermell juga tercer")
            elif orden[2] == "G":###
                print("groc juga tercer")
        elif orden[1] == "G":##
            print("groc juga segon")
            if orden[2] == "T":###
                print("taronja juga tercer")
            elif orden[2] == "V":###
                print("vermell juga tercer")
        elif orden[1] == "V":##
            print("vermell juga segon")
            if orden[2] == "T":###
                print("taronja juga tercer")
            elif orden[2] == "G":###
                print("groc juga tercer")
    if orden[3] == "V":####
        print("vermell juga últim")
    elif orden[3] == "G":####
        print("groc juga últim")
    elif orden[3] == "T":####
        print("taronja juga últim")
    else:####
        print("blau juga últim")

ordre()


# Imprimimos la información de cada jugador
#jugadores = ["", taronja, blau, vermell]
#for jugador in jugadores:
    #print(f"Jugador: {jugador} \nCarrers: {jugadores[jugador]['Carrers']} \nDiners: {jugadores[jugador]['Diners']} \n Especial: {jugadores[jugador]['Especial']}\n---")


"""
CARRERS(CASELLES)
"""

"""
CASELLES ESPECIALS
"""


def Sortida ():
    diners_groc, jugador_g = jugador_groc()
    diners_blau, jugador_b = jugador_blau()
    diners_vermell, jugador_v = jugador_vermell()
    diners_taronja, jugador_t = jugador_taronja()
    if jugador_g  in "sortida": #Si el jugador groc es troba en la casella sortida
        diners_groc += 200 #El jugador guanya 200 euros
    elif jugador_b in "sortida":
        diners_blau += 200
    elif jugador_t in "sortida":
        diners_taronja += 200
    elif jugador_v in "sortida":
        diners_vermell += 200
    else:
        pass

def Anr_pro  ():
    pro = Caselles[1]
    return pro
def Caixa ():
    caixa = Caselles[2]
    return caixa
def Sort  ():
    sort =  Caselles[3]
    return sort
def Preso ():
    preso = Caselles[4]
    return preso






"""
INFORMACIÓ PARTIDA (CENTRE)
"""
def accions_partida():
    pass


"""
INFORMACIÓ PARTIDA (DRETA)
"""
def informacio_usuari():
    pass

"""
INFORMACIÓ PARTIDA (SOTA)
"""
def accio_usuari():
    pass


"""
INICI PARTIDA
"""
def inici_partida():
  """Inicia la partida amb els jugadors tenint 2000 euros."""
  # Definir els jugadors
  ordre()
  



