def regEquipo(eq:list):
    equipo = eq
    print("Su equipo es: ", equipo)
    
def pedirDatos ():
    name = str(input("Ingrese el nombre de su equipo: "))
    pj = int(input(f"ingrese la cantidad de partidos jugados para {name}: "))
    pg = int(input(f"ingrese la cantidad de partidos ganados para {name}: "))
    pp = int(input(f"ingrese la cantidad de partidos perdidos para {name}: "))
    pe = int(input(f"ingrese la cantidad de partidos empatados para {name}: "))
    gf = int(input(f"ingrese la cantidad goles a favor para {name}: "))
    gc = int(input(f"ingrese la cantidad goles en contra para {name}: "))
    datos = [name, pj, pg,pp,pe,gf,gc]
    return datos
def submenu(equipos:list):
    isvalid = True
    while isvalid:
        print("1.Ingresar Equipo nuevo\n 2.Ver equipos\n 3.Salir\n")
        opc = int(input(": "))
        if (opc == 1):
            data= pedirDatos()
            equipos.append(data)
            print("Se ha registrado correctamente su equipo")
        elif (opc == 2):
            print(f"los equipos registrados son: {equipos}")
            input("presione cualquier letra para continuar...")
        elif (opc == 3):
            isvalid = False
    else:
        print("Opcion no valida")
