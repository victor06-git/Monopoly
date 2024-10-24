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