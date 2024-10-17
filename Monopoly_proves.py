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


from tauler import *
from llistes import *


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
        return f"--- Banc:\nDiners: {valor_banca}\n---"
    else:
        valor_banca = valor_inicial
    # Imprimimos el tablero
    return f"--- Banc:\nDiners: {valor_banca}\n---"




"""
DADOS
"""
import random
def daus(): #Funció daus: mostra el resultat aleatori dels dos daus
    global resultat
    dau_1()
    dau_2()
    suma = valor_dau_1 + valor_dau_2
    resultat = print(f"Has tret {valor_dau_1} i {valor_dau_2} que suma: {suma}")
def dau_1():#Funció dau 1
    global valor_dau_1
    valor_dau_1 = random.randint(1,6)
def dau_2():#Funció dau 2
    global valor_dau_2
    valor_dau_2 = random.randint(1,6)



"""
ORDRE TIRADA
                -Aleatoriament selecciona al principi de cada partida
"""
def ordre():#Funció mostra els jugadors a l'atzar
    players = ["V","T","G","B"]
    for _ in range(4):    
        eleccio = random.choice(players)
        print(eleccio, end="")
        players.remove(eleccio)
    print()
ordre()


"""
JUGADORS
"""
def groc():
    Carrers = []
    Diners = []
    Caselles = []
    return Carrers,Diners,Caselles
def taronja():
    Carrers = []
    Diners = []
    Caselles = []
    return Carrers,Diners,Caselles
def blau():
    Carrers = []
    Diners = []
    Caselles = []
    return Carrers,Diners,Caselles
def vermell():
    Carrers = []
    Diners = []
    Caselles = []
    return Carrers,Diners,Caselles



# Imprimimos la información de cada jugador
jugadores = [groc, taronja, blau, vermell]
#for jugador in jugadores:
    #print(f"Jugador: {jugador} \nCarrers: {jugadores[jugador]['Carrers']} \nDiners: {jugadores[jugador]['Diners']} \n Especial: {jugadores[jugador]['Especial']}\n---")


"""
CARRERS(CASELLES)
"""

def carrers():
    
    pass

"""
CASELLES ESPECIALS
"""

Caselles = ["Sortida","Anr pró","Caixa","Sort","Presó"]
def Sortida ():
    sortida = Caselles[0]
    return sortida
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
  jugadors = {
      "T": 2000,
      "V": 2000,
      "G": 2000,
      "B": 2000,
  }
  return jugadors

# Inici de la partida
jugadors = inici_partida()
print(f"Jugadors: {jugadors}")

