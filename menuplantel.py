import os
import modulos.menuEquipos as mp
def menuplantell (planteles:list):
    print("Este menu pertenece a el plantel")
    isvalid = True
    data= planteles
    planteles.append(data)
    jugadoress = []
    jugadoress.append
    while isvalid:
        print("1.Registrar tecnico\n 2.Ver Tecnico\n 3.Registrar Jugador\n 4.Ver jugadores\n 5.Volver\n")
        opc = int(input(": "))
        if (opc == 1):
            str(input("Ingrese el nombre del director tecnico: "))
        elif (opc ==2):
            pass
        elif (opc == 3):
            pass
        elif (opc == 4):
            print(f"los jugadores registrados son: {jugadoress}")
            input("presione cualquier letra para continuar...")
        elif (opc == 5):
            isvalid = False
def registrarjugador (equipos:list):
    print("Debe registrar los datos del jugador")