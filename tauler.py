"""
TABLERO
        -Modificar una parte para que en el centro no se impriman "|" y solo espacio.
"""


cell0 = ""
cell1 = ""
cell2 = ""
cell3 = ""
cell4 = ""
cell5 = ""
cell6 = ""
cell7 = ""
cell8 = ""
cell9 = ""
cell10 = ""
cell11 = ""
cell12 = ""
cell13 = ""
cell14 = ""
cell15 = ""
cell16 = ""
cell17 = ""
cell18 = ""
cell19 = ""
cell20 = ""
cell21 = ""
cell22 = ""
cell23 = ""
casa1 = "--"
casa2 = "--"
casa3 = "--"
casa4 = "--"
casa5 = " |"
casa6 = " |"
casa7 = " |"
casa8 = " |"
casa9 = "--"
casa10 = "--"
casa11 = "--"
casa12 = "--"
casa13 = " |"
casa14 = " |"
casa15 = " |"
casa16 = " |"
def tablero():
    print(f"+--------+----{casa9:<2}--+----{casa10:<2}--+--------+----{casa11:<2}--+----{casa12:<2}--+--------+")
    print("|Parking |Urqinoa |Fontan  |Sort    |Rambles |Pl.Cat  |Anr pró |")
    print(f"|{cell12:<8}|{cell13:<8}|{cell14:<8}|{cell15:<8}|{cell16:<8}|{cell17:<8}|{cell18:<8}|")
    print("+--------+--------+--------+--------+--------+--------+--------+")
    print(f"|Aragó  {casa8:<2}                                            | Angel {casa13:<2}")
    print(f"|{cell11:<8}|                                            |{cell19:<8}|")
    print("+--------+                                            +--------+")
    print(f"|S.Joan {casa7:<2}                                            |Augusta{casa14:<2}")
    print(f"|{cell10:<8}|                                            |{cell20:<8}|")
    print("+--------+                                            +--------+")
    print(f"|Caixa   |                                            |Caixa   |")
    print(f"|{cell9:<8}|                                            |{cell21:<8}|")
    print("+--------+                                            +--------+")
    print(f"|Aribau {casa6:<2}                                            |Balmes {casa15:<2}")
    print(f"|{cell8:<8}|                                            |{cell22:<8}|")
    print("+--------+                                            +--------+")
    print(f"|Muntan {casa5:<2}                                            |Gracia {casa16:<2}")
    print(f"|{cell7:<8}|                                            |{cell23:<8}|")
    print(f"+--------+----{casa4:<2}--+----{casa3:<2}--+--------+----{casa2:<2}--+----{casa1:<2}--+--------+")
    print(f"|{cell6:<8}|{cell5:<8}|{cell4:<8}|{cell3:<8}|{cell2:<8}|{cell1:<8}|{cell0:<8}|")
    print("|Presó   |Consell |Marina  |Sort    |Rosell  |Lauria  |Sortida |")
    print("+--------+--------+--------+--------+--------+--------+--------+")


