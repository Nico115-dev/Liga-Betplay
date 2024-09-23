import modulos.menu as mn
import modulos.menuEquipos as me
import modulos.menuplantel as mp
if (__name__ == "__main__"):

    equipos=[]
    planteles = []
    activeMenu = True
    while activeMenu:
        res =  mn.crearMenu()
        
        print (res)
        if(res == 1):
            try:
              me.submenu(equipos)
            except:
                print("Ha ocurrido un error intentelo despues")
                
        elif(res == 2):
            try:
                mp.menuplantell(planteles)
            except ValueError:
                print("Ha ocurrido un error")
        if(res == 3 ):
            pass
        elif(res == 4):
            pass
        elif(res == 5):
            activeMenu = False