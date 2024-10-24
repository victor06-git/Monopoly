"""
DADOS
"""
import random
def llançar_daus(): #Funció daus: mostra el resultat aleatori dels dos daus
    global resultat_daus,suma_daus
    dau_1()
    dau_2()
    suma_daus = valor_dau_1 + valor_dau_2
    resultat_daus = print(f"Has tret {valor_dau_1} i {valor_dau_2} que suma: {suma_daus}")
    return suma_daus, resultat_daus
def dau_1():#Funció dau 1
    global valor_dau_1
    valor_dau_1 = random.randint(1,6)
def dau_2():#Funció dau 2
    global valor_dau_2
    valor_dau_2 = random.randint(1,6)