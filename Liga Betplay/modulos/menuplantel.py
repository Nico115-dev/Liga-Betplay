import os
import modulos.menuEquipos as mp

def menuplantell(planteles: list):
    print("Este menú pertenece al plantel")
    isvalid = True
    directores_tecnicos = [] 
    jugadoress = []  
    while isvalid:
        print("1. Registrar técnico\n2. Ver Técnicos\n3. Registrar Jugador\n4. Ver Jugadores\n5. Volver")
        opc = int(input(": "))
        if (opc == 1):
            nombre_dt = input("Ingrese el nombre del director técnico: ")
            directores_tecnicos.append({'nombre': nombre_dt})
            print(f"Director técnico {nombre_dt} registrado.")
        elif (opc == 2):
            if directores_tecnicos:
                print("Los directores técnicos registrados son:")
                for dt in directores_tecnicos:
                    print(f"Nombre: {dt['nombre']}")
            else:
                print("No hay directores técnicos registrados.")
            input("Presione cualquier tecla para continuar...")
        elif (opc == 3):
            nombre_jugador = input("Ingrese el nombre del jugador: ")
            dorsal = input("Ingrese el dorsal del jugador: ")
            posicion = input("Ingrese la posición del jugador: ")
            jugadoress.append({'nombre': nombre_jugador, 'dorsal': dorsal, 'posicion': posicion})
            print(f"Jugador {nombre_jugador} registrado.")
        elif (opc == 4):
            if jugadoress:
                print("Los jugadores registrados son:")
                for jugador in jugadoress:
                    print(f"Nombre: {jugador['nombre']}, Dorsal: {jugador['dorsal']}, Posición: {jugador['posicion']}")
            else:
                print("No hay jugadores registrados.")
            input("Presione cualquier tecla para continuar...")
        elif (opc == 5):
            isvalid = False
        else:
            print("Opción no válida.")

    
    
    
    