import os
import modulos.menuEquipos as me
def encuentros(partidos_programados: list):
    print("Este menú permite programar partidos")
    isvalid = True
    while isvalid:
        print("1. Programar Partidos\n2. Ver partidos programados\n3. Ver Equipos Registrados en el torneo\n4. Volver")
        opc = int(input(": "))
        if opc == 1:
            equipos = me.obtener_equipos()  
            if not equipos:
                print("No hay equipos registrados. Por favor, registre equipos primero.")
                continue
            print("Equipos disponibles:")
            for idx, equipo in enumerate(equipos):
                print(f"{idx + 1}. {equipo}")
            try:
                equipo1_idx = int(input("Seleccione el primer equipo (número): ")) - 1
                equipo2_idx = int(input("Seleccione el segundo equipo (número): ")) - 1
                if (equipo1_idx < 0 or equipo1_idx >= len(equipos) or 
                        equipo2_idx < 0 or equipo2_idx >= len(equipos)):
                    print("Selección inválida, intente nuevamente.")
                    continue
                equipo1 = equipos[equipo1_idx]
                equipo2 = equipos[equipo2_idx]
                partidos_programados.append((equipo1, equipo2)) 
                print(f"Partido programado: {equipo1} vs {equipo2}")
            except ValueError:
                print("Entrada no válida, por favor ingrese un número.")
        elif opc == 2:
            if partidos_programados:
                print("Partidos programados:")
                for partido in partidos_programados:
                    print(f"{partido[0]} vs {partido[1]}")
            else:
                print("No hay partidos programados.")
        elif opc == 3:
            equipos = me.obtener_equipos()
            print("Equipos Registrados:")
            for equipo in equipos:
                print(equipo)
        elif opc == 4:
            isvalid = False
        else:
            print("Opción no válida, intente nuevamente.")