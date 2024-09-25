def registrar_resultado(partido):
    print(f"Ingrese el resultado para el partido: {partido[0]} vs {partido[1]}")
    goles_equipo1 = int(input(f"¿Cuántos goles marcó {partido[0]}? "))
    goles_equipo2 = int(input(f"¿Cuántos goles marcó {partido[1]}? "))
    return (partido[0], goles_equipo1, partido[1], goles_equipo2)
def mostrar_resultados(resultados):
    if resultados:
        print("Resultados de los partidos:")
        for resultado in resultados:
            print(f"{resultado[0]} {resultado[1]} - {resultado[2]} {resultado[3]}")
    else:
        print("No hay resultados registrados.")
