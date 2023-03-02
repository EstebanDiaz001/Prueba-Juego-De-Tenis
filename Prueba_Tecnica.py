#-----------------------------------------------Prueba técnica juego de tenis por Esteban Díaz-----------------------------------------------#

#Validación para acceder al menú de configuarciones
x=1

# Clase del jugador
class jugador:
    def __init__(self, nombre = "", punto_partido = 0):
        self.nombre = nombre                                            #Creación del atributo nombre
        self.punto_partido = punto_partido                              #Creación del atributo punto_partido
        return
      
        

jugador1 = jugador()
jugador2 = jugador()

print(jugador1.nombre)
#Creación del menú y la variable opción_menu, seleccionar jugador
opcion_menu : int
seleccionar_jugador: int
while x == 1:

    #Se pide opción del menú a elegir
    
    opcion_menu = int(input("\n\nMenú: \n"+ 
        "1. Perzonalizar nomrbes de jugadores\n"+
        "2. Jugar\n"+
        "3. Salir\n\n"))
    
    if opcion_menu == 1:

        #seleccionar jugador

        seleccionar_jugador = int(input("Seleccione un jugador: \n"+
                                "1. Jugador #1\n"+
                                "2. Jugador #2\n"))
        if seleccionar_jugador == 1:

            #Cambiar nombre del jugador #1

            nombre_nuevo = input("Ingrese un nombre nuevo para el jugador #1    Nombre actual ->"+ jugador1.nombre + "\n")
            jugador1.nombre = nombre_nuevo
            print("Nombre del jugador #1 acualizado a :" + jugador1.nombre)
            
            
        if seleccionar_jugador == 2:

            #Cambiar nombre del jugador #2

            nombre_nuevo = input("Ingrese un nombre nuevo para el jugador #2    Nombre actual ->"+ jugador2.nombre + "\n")
            jugador2.nombre = nombre_nuevo
            print("Nombre del jugador #2 acualizado a :" + jugador2.nombre)


    #Game

    if opcion_menu == 2 and (jugador1.nombre != "" and jugador2.nombre != ""):

        #Se instancian las variable que se usarán para el juego

        Marcador = ""
        opcion_juego = ""
        jugador1ventaja = ""
        jugador2ventaja = ""
        while opcion_menu == 2:

        #Se crea el menú del juego
            print("\n\nmarcador:\n"+
            "Jugador " + jugador1.nombre + " " + str(jugador1.punto_partido) + " " + jugador1ventaja + "\n" +
            "Jugador " + jugador2.nombre + " " + str(jugador2.punto_partido) + " " + jugador2ventaja)

            opcion_juego = int(input( "1. Jugador "+ jugador1.nombre +" anotó un punto\n"+
                            "2. Jugador "+ jugador2.nombre+ " anotó un punto\n"))

            ################################################### OPCIONES DEL JUGADOR 1 ###################################################
            if opcion_juego==1:
                
            #El jugador 1 ha ganado y se reinician los valores de los punto y punto_partido


                if jugador1ventaja == "Ventaja" and jugador1.punto_partido == 40:
                                print("El jugador " + jugador1.nombre + " ha ganado el partido")
                                jugador1.punto_partido = 0
                                jugador2.punto_partido = 0
                                jugador1ventaja = ""
                                jugador2ventaja = ""
                                opcion_menu = 0


                    #Se le quita la ventaja al jugador 2

                else:
                    if jugador2ventaja == "Ventaja":
                                jugador2ventaja = ""
                    



                    else:
                        
                #Adición de puntos cuando tiene 40 puntos, se le pone el estado a ventaja

                        if jugador1.punto_partido == 40 and jugador1ventaja == "":
                                    jugador1ventaja = "Ventaja"

                #Adición de puntos cuando tiene 30 puntos en el marcador

                        else:
                            if jugador1.punto_partido == 30:
                                jugador1.punto_partido += 10

                    #Adición de puntos cuando tiene menos de 30 puntos en el marcador

                            else:
                                if jugador1.punto_partido < 30:
                                    jugador1.punto_partido += 15


            ################################################### OPCIONES DEL JUGADOR 2 ###################################################
            if opcion_juego==2:
                
            #El jugador 1 ha ganado y se reinician los valores de los punto y punto_partido


                if jugador2ventaja == "Ventaja" and jugador2.punto_partido == 40:
                                print("El jugador " + jugador1.nombre + " ha ganado el partido")
                                jugador1.punto_partido = 0
                                jugador2.punto_partido = 0
                                jugador1ventaja = ""
                                jugador2ventaja = ""
                                opcion_menu = 0


            #Se le quita la ventaja al jugador 1

                else:
                    if jugador1ventaja == "Ventaja":
                                jugador1ventaja = ""
                    
                    # #Adición de puntos cuando tiene 30 puntos en el marcador


                    else:
                        
                #Adición de puntos cuando tiene 40 puntos, se le pone el estado a ventaja

                        if jugador2.punto_partido == 40 and jugador2ventaja == "":
                                    jugador2ventaja = "Ventaja"


                        else:
                            if jugador2.punto_partido == 30:
                                jugador2.punto_partido += 10

                    #Adición de puntos cuando tiene menos de 30 puntos en el marcador

                            else:
                                if jugador2.punto_partido < 30:
                                    jugador2.punto_partido += 15
                                    
        #Se pide que modifiquen los nombres de los 2 jugadores
    if opcion_menu == 2 and (jugador1.nombre == "" or jugador2.nombre == ""):
            
            print("Elige un nombre para ambos jugadores antes")

    if opcion_menu == 3:
        exit()