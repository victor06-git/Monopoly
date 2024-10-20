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
        valor_banca = valor_inicial + 1000000 #Afegeix 1M d'euros a la banca si té 500mil o menys 
        return valor_banca
    else:
        valor_banca = valor_inicial
        return valor_banca # Retorna el valor en diners que te la banca en aquell moment
"""
JUGADORS
            -Class Jugador
            -Jugadors definits per color
"""
class Jugador:
    def __init__(self,name,color):
        self.name = name
        self.color = color
        self.posicio = 0 #Comença a la casella "sortida"
        self.propietats = [] #Lista de les propietats que té l'usuari
        self.carta_especial = [] #Lista de les cartes especials (Sortir de la presó)
        self.diners = 2000
        self.a_preso = False
        self.torns_a_preso = 0
    def en_preso(self):
        return self.a_preso()
    def move(self,passos,tauler):
        if self.a_preso == True:
            print("Jugador a presó, no pot tirar")
            return None
        else:
            self.posicio = (self.posicio + passos) % len(tauler) #Passos == resultat_daus
            casella_actual = tauler[self.posicio]
            return casella_actual
        
    def move_to(self, casella, tauler):  #Funció anar a presó
        if 0 <= casella < len(tauler):
            self.posicio = casella
            return tauler[self.posicio]
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
    def diners_propietat(self, diners_propietat): #Definir els diners que té després de comprar un terreny, casa o hotel
        self.diners = (self.diners - diners_propietat)  
   
    def diners_sortida(self, sortida):#Definir els diners que té després de passar per la casella de sortida
        self.diners = (self.diners + sortida)
   
    def jugador_info(self):#Definir informació que es mostra en la pantalla
        info = {
            "Propietats": self.propietats,
            "Diners": self.diners,
            "Especial": self.carta_especial
        }
        salts_de_linea = "\n".join([f"{key}: {value}" for key, value in info.items()])
        return salts_de_linea

jugador_v = Jugador("V", "Vermell")
jugador_b =Jugador("B", "Blau")
jugador_g = Jugador("G", "Groc")
jugador_t = Jugador("T","Taronja")



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
    #Ordre tirada jugadors
    global Jugador_0, Jugador_1, Jugador_2, Jugador_3
    Jugador_0 = None
    Jugador_1 = None
    Jugador_2 = None
    Jugador_3 = None
#Defineixo per variables els jugadors
    if orden[0] == "V":#Si vermell es troba al primer lloc de la llista orden
        jugador_v = Jugador_0 #Defineixo el jugador amb una variable
        Jugador_0 = "Vermell"
        if orden[1] == "T":##Segona posició
            jugador_t = Jugador_1
            Jugador_1 = "Taronja"
            if orden[2] == "B":###tercera posició
                jugador_b = Jugador_2
                Jugador_2 = "Blau"
            elif orden[2] == "G":###
                jugador_g = Jugador_2
                Jugador_2 = "Groc"
        elif orden[1] == "G":##
            jugador_g = Jugador_1
            Jugador_1 = "Groc"
            if orden[2] == "B":###
                jugador_b = Jugador_2
                Jugador_2 = "Blau"
            elif orden[2] == "T":###
                jugador_t = Jugador_2
                Jugador_2 = "Taronja"
        elif orden[1] == "B":##
            jugador_b = Jugador_1
            Jugador_1 = "Blau"
            if orden[2] == "T":###
                jugador_t = Jugador_2
                Jugador_2 = "Taronja"
            elif orden[2] == "G":###
                jugador_g = Jugador_2
                Jugador_2 = "Groc"
    elif orden[0] == "T":#Si taronja es troba al primer lloc de la llista orden
        jugador_t = Jugador_0
        Jugador_0 = "Taronja"
        if orden[1] == "V":##
            jugador_v = Jugador_1
            Jugador_1 = "Vermell"
            if orden[2] == "B":###
                jugador_b = Jugador_2
                Jugador_2 = "Blau"
            elif orden[2] == "G":###
                jugador_g = Jugador_2
                Jugador_2 = "Groc"
        elif orden[1] == "G":##
            jugador_g == Jugador_1
            Jugador_1 = "Groc"
            if orden[2] == "B":###
                jugador_b = Jugador_2
                Jugador_2 = "Blau"
            elif orden[2] == "V":###
                jugador_v = Jugador_2
                Jugador_2 = "Vermell"
        elif orden[1] == "B":##
            jugador_b = Jugador_1
            Jugador_1 = "Blau"
            if orden[2] == "V":###
                jugador_v = Jugador_2
                Jugador_2 = "Vermell" 
            elif orden[2] == "G":###
                jugador_g = Jugador_2
                Jugador_2 = "Groc"
    elif  orden[0] == "G":#Si groc es troba al primer lloc de la llista orden
        jugador_g == Jugador_0
        Jugador_0 = "Groc"
        if orden[1] == "T":##
            jugador_t = Jugador_1
            Jugador_1 = "Taronja"
            if orden[2] == "B":###
                jugador_b = Jugador_2
                Jugador_2 = "Blau"
            elif orden[2] == "V":###
                jugador_v = Jugador_2
                Jugador_2 = "Vermell"
        elif orden[1] == "V":##
            jugador_v = Jugador_1
            Jugador_1 = "Vermell"
            if orden[2] == "B":###
                jugador_b = Jugador_2
                Jugador_2 = "Blau"
            elif orden[2] == "T":###
                jugador_t = Jugador_2
                Jugador_2 = "Taronja"
        elif orden[1] == "B":##
            jugador_b = Jugador_1
            Jugador_1 = "Blau"
            if orden[2] == "V":###
                jugador_v = Jugador_2
                Jugador_2 = "Vermell"
            elif orden[2] == "T":###
                jugador_t = Jugador_2
                Jugador_2 = "Taronja"
    elif orden[0] == "B":#Si blau es troba al primer lloc de la llista orden
        jugador_b = Jugador_0
        Jugador_0 = "Blau"
        if orden[1] == "T":##
            jugador_t = Jugador_1
            Jugador_1 = "Taronja"
            if orden[2] == "V":###
                jugador_v = Jugador_2
                Jugador_2 = "Vermell"
            elif orden[2] == "G":###
                jugador_g = Jugador_2
                Jugador_2 = "Groc"
        elif orden[1] == "G":##
            jugador_g = Jugador_1
            Jugador_1 = "Groc"
            if orden[2] == "T":###
                jugador_t = Jugador_2
                Jugador_2 = "Taronja"
            elif orden[2] == "V":###
                jugador_v = Jugador_2
                Jugador_2 = "Vermell"
        elif orden[1] == "V":##
            jugador_v = Jugador_1
            Jugador_1 = "Vermell"
            if orden[2] == "T":###
                jugador_t = Jugador_2
                Jugador_2 = "Taronja"
            elif orden[2] == "G":###
                jugador_g = Jugador_2
                Jugador_2 = "Groc"
    if orden[3] == "V":####
        jugador_v = Jugador_3
        Jugador_3 = "Vermell"
    elif orden[3] == "G":####
        jugador_g = Jugador_3
        Jugador_3 = "Groc"
    elif orden[3] == "T":####
        jugador_t = Jugador_3
        Jugador_3 = "Taronja"
    else:####
        jugador_b = Jugador_3
        Jugador_3 = "Blau"
    

ordre()


# Imprimimos la información de cada jugador
#jugadores = ["", taronja, blau, vermell]
#for jugador in jugadores:
    #print(f"Jugador: {jugador} \nCarrers: {jugadores[jugador]['Carrers']} \nDiners: {jugadores[jugador]['Diners']} \n Especial: {jugadores[jugador]['Especial']}\n---")


"""
CASELLES
            -Definir caselles com números ( exemple: Sortida == 0)
            -Per la seva posició en la llista tauler
"""


"""
CASELLES ESPECIALS
"""


def Sortida ():
    diners_sortida = 200
    if jugador_g  in tauler[0]: #Si el jugador groc es troba en la casella sortida
        jugador_g.diners_sortida(diners_sortida) #El jugador guanya 200 euros
    elif jugador_b in tauler[0]:
        jugador_b.diners_sortida(diners_sortida)
    elif jugador_t in tauler[0]:
        jugador_t.diners_sortida(diners_sortida)
    elif jugador_v in tauler[0]:
        jugador_v.diners_sortida(diners_sortida)
    else:
        pass

def Anr_pro  ():
    anar_preso = tauler[18]
    if jugador_b in anar_preso:
        jugador_b.move_to(6,tauler)
    elif jugador_g in anar_preso:
        jugador_g.move_to(6, tauler)
    elif jugador_t in anar_preso:
        jugador_t.move_to(6,tauler)
    elif jugador_v in anar_preso:
        jugador_v.move_to(6,tauler)

def Caixa (): #Casella caixa
    caixa1 = tauler[9]
    caixa2 = tauler[21]
    if jugador_b in caixa1 or caixa2:# Jugador blau
        carta_jugador = random.choice(cartes_caixa)
        if carta_jugador == "Sortir de la presó":
            jugador_b.add_carta_especial(carta_jugador)
            cartes_caixa.remove(carta_jugador)
        else:
            cartes_caixa.remove(carta_jugador)
            cartes_caixa.index(carta_jugador)   
    elif jugador_g in caixa1 or caixa2:#Jugador groc
        carta_jugador = random.choice(cartes_caixa)
        if carta_jugador == "Sortir de la presó":
            jugador_g.add_carta_especial(carta_jugador)
            cartes_caixa.remove(carta_jugador)
        else:
            cartes_caixa.remove(carta_jugador)
            cartes_caixa.index(carta_jugador)
    elif jugador_t in caixa1 or caixa2: #Jugador taronja
        carta_jugador = random.choice(cartes_caixa)
        if carta_jugador == "Sortir de la presó":
            jugador_t.add_carta_especial(carta_jugador)
            cartes_caixa.remove(carta_jugador)
        else:
            cartes_caixa.remove(carta_jugador)
            cartes_caixa.index(carta_jugador) 
    elif jugador_v in caixa1 or caixa2: #Jugador vermell
        carta_jugador = random.choice(cartes_caixa)
        if carta_jugador == "Sortir de la presó":
            jugador_v.add_carta_especial(carta_jugador)
            cartes_caixa.remove(carta_jugador)
        else:
            cartes_caixa.remove(carta_jugador)
            cartes_caixa.index(carta_jugador) 
def Sort  (): #Casella sort
    sort1 = tauler[3]
    sort2 = tauler[15]
    if jugador_b in sort1 or sort2: #Jugador blau
        carta_jugador2 = random.choice(cartes_sort)
        if carta_jugador2 == "Sortir de la presó":
            jugador_b.add_carta_especial(carta_jugador2)
            cartes_sort.remove(carta_jugador2)
        else:
            cartes_sort.remove(carta_jugador2)
            cartes_sort.index(carta_jugador2) 
    elif jugador_g in sort1 or sort2: #Jugador groc
        carta_jugador2 = random.choice(cartes_sort)
        if carta_jugador2 == "Sortir de la presó":
            jugador_g.add_carta_especial(carta_jugador2)
            cartes_sort.remove(carta_jugador2)
        else:
            cartes_sort.remove(carta_jugador2)
            cartes_sort.index(carta_jugador2) 
    elif jugador_t in sort1 or sort2: #Jugador taronja
        carta_jugador2 = random.choice(cartes_sort)
        if carta_jugador2 == "Sortir de la presó":
            jugador_t.add_carta_especial(carta_jugador2)
            cartes_sort.remove(carta_jugador2)
        else:
            cartes_sort.remove(carta_jugador2)
            cartes_sort.index(carta_jugador2)  
    elif jugador_v in sort1 or sort2: #Jugador vermell
        carta_jugador2 = random.choice(cartes_sort)
        if carta_jugador2 == "Sortir de la presó":
            jugador_v.add_carta_especial(carta_jugador2)
            cartes_sort.remove(carta_jugador2)
        else:
            if carta_jugador2 == "Anar a la presó":
                jugador_v.move_to(6, tauler)
            elif carta_jugador2 == "Anar a la sortida":
                jugador_v.move_to(0, tauler)
            elif carta_jugador2 == "Anar tres espais endarrera":
                jugador_v.move(-3,tauler)
            elif carta_jugador2 == "Fer reparacions a les propietats":
                pass
            elif carta_jugador2 == "Ets escollit alcalde":
                pass
            cartes_sort.remove(carta_jugador2)
            cartes_sort.index(carta_jugador2) 

def Preso ():
    preso = tauler[6]
    if jugador_b in preso:
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
                -Afegir número cases i hotels en cada cas (3C2H) canviant (---) o  ("|")
"""





"""
INFORMACIÓ PARTIDA (CENTRE)
"""
def accions_partida():
    pass


"""
INFORMACIÓ PARTIDA (DRETA)
                            -Els jugadors es mostren per ordre de tirada
                            -Els carrers es mostren per ordre en el taulell
"""

def informacio_usuari():
    info_0 = jugador_t.jugador_info()
    info_1 = jugador_g.jugador_info()
    info_2 = jugador_b.jugador_info()
    info_3 = jugador_v.jugador_info()
    print(f"""
Banca:
Diners: 
Jugador {Jugador_0}:
{info_0}
Jugador {Jugador_1}:
{info_1}
Jugador {Jugador_2}:
{info_2}
Jugador {Jugador_3}:
{info_3}
    """)
informacio_usuari()

"""
INFORMACIÓ PARTIDA (SOTA)
"""
def accio_usuari():
    text = (f"Juga {jugador_b}, opcions: passar, comprar terreny, preus")
    text2 = (f"Juga {jugador_b}, opcions: passar, comprar casa, comprar hotel, preus")
    pass
def opcions():
    opcion = ["passar", "comprar terreny", "preus"]
    if opcion == "comprar terreny" or 1:
        print("Compres terreny")
    elif opcion == "preus" or 2:
        print(preu_terreny)
def preu_terreny(casilla):
    precios = [50,60,70,80]
    if jugador_b in tauler[0]:
        pass
    """
    Definir las caselles por números como los jugadores, 
    desde el array caselles del archivo tauler.py según la posició del tablero empezará 
    desde 0 con la sortida dando la vuelta en sentido de las agujas del reloj
    """
casellas_num = ["Sortida","Lauria","Roselló","Sort","Marina","Consell de Cent","Presó","Muntaner","Aribau","Sant Joan","Aragó","Parking","Urquinaona","Fontana","Sort","Les Rambles","Plaça Catalunya","Anar presó","Portal de l'Àngel", "Via Augusta","Caixa","Balmes","Passeig de Gràcia"]
"""
INICI PARTIDA
                -Cada jugador comença amb 2000 euros
                -Mostra sempre a cada casella el primer jugador 
                -Barrejar les cartes de caixa i sort
"""
def inici_partida():
  """Inicia la partida amb els jugadors tenint 2000 euros."""
  # Definir els jugadors
  random.shuffle(cartes_caixa) #Barreja les cartes de caixa
  random.shuffle(cartes_sort) #Barreja les cartes de sort