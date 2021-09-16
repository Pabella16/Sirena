# -*- coding: utf-8 -*-
"""
Sept. 2021

@author: Pablo Abella
"""

import json

# abre archivo (como utf-8 para evitar problemas de caracteres especiales)
with open('Munecas.json', encoding='utf-8') as archivo: 
    relato = json.load(archivo)  # y lo guarda como "relato"
    
elemento = 0
print("")

while elemento < len(relato): # while es más complejo :c
    print("\033[1;37;m",end="") #restablece el color del texto al pasar cada sección
    # for elemento in relato: # recorre todas las partes del relato que pueden ser "texto unico", "decision" o "texto dependiente"
    #print(relato[elemento])
    
    if relato[elemento]["tipo"] == "TI":  
        titulo = relato[elemento]["contenido"]
        print("\n"+"="*64)
        print("{:^64}".format(titulo))
        print("="*64)
        elemento = relato[elemento]["siguiente"]
        input("\033[1;32;mENTER PARA CONTINUAR\n")
        
        
    elif relato[elemento]["tipo"] == "TU":  # si es texto unico simplemente lo muestra
        print(relato[elemento]["contenido"])
        elemento = relato[elemento]["siguiente"] 
        input("\033[1;32;mENTER PARA CONTINUAR\n")
    
    # si hay una decision debe mostrar todas las opciones al lector y permitirle escoger
    elif relato[elemento]["tipo"] == "DE":
       
        for opcion in relato[elemento]["contenido"]:  # muestra opciones
            print(str(opcion["num"])+". "+opcion["opción"] + "\n")
            # También es posible la siguiente manera, que crea variables para "num" y "opcion"
            # num = str(opcion["num"])
            # opcion = opcion["opción"]
            # print(f"{num}. {opcion}")
            
        # Creo una variable para representar si la opción ingresada es valida, esta va a 
        # servir para que, hasta que lo sea, le pida al lector que escoja una opción
        decision_valida = False 
        
        # Mientras que la opción no sea válida, hará todo lo que sigue. El curioso lector
        # de este código se dará cuenta de que ninguno de los nombres de variables tiene tildes, esto es
        # porque las letras con acentos son caracteres especiales que pueden generar errores, espero que no 
        # pase lo mismo con las cadenas de texto, es decir el relato y los poemas en sí, pero esperaría que no.
        while not decision_valida:
            # esto le pide al usuario que introduzca una de las opciones
            decision_tomada = input("\033[1;32;m¿Qué opción escoges? " + "(1 a " + str(len(relato[elemento]["contenido"]))+ "): ")
            # con esto me aseguro de que la opción ingresada sea un número de las opciones posibles.
            if not decision_tomada.isdigit() or int(decision_tomada)>len(relato[elemento]["contenido"]) or int(decision_tomada)<=0: 
                print("\033[1;32;m\nDebes escoger una de las opciones posibles introduciendo un número.")
            else:
                decision_valida = True  # se escogió una decisión válida, así que puede continuar
                
                # guarda el recorrido escogido para saber qué camino debe seguir el relato, "detalle" es una
                # propiedad de cada decision que dice el índice de la lista de variaciones en el texto dependiente
                # que contiene el detalle que coincide con la decisión tomada. 
                # -1 porque el indice de las listas empieza en 0.
                
                # hay que mejorar este condicional y la mecánica general del "detalle" porque, como está, una
                # decisión del principio puede no lograr determinar la variación de un texto dependiente al final
                # porque otra decisión tenga "detalle" y cambie el registrado. Mi idea para esto es que el valor
                # de la clave "detalle" no sea un número, sino un string que se añade a una variable lista guardada
                # en el programa, y que cada texto independiente tenga el metadato de a qué índice de la lista debe
                # referirse para el detalle que le toca usar (esto reemplazaría el valor de la llave "variación").
                # luego el print sería simplemente el fijo + lista[índice]
                if int(relato[elemento]["contenido"][int(decision_tomada) - 1]["detalle"])>0:
                    detalle = relato[elemento]["contenido"][int(decision_tomada) - 1]["detalle"]
                if relato[elemento]["contenido"][int(decision_tomada) - 1]["input"] != None:
                    respuesta = input("\033[1;37;m" + relato[elemento]["contenido"][int(decision_tomada) - 1]["input"])
                else:
                    # con esto se revisa qué frase es la anterior a la decisión para repetirla con ella.
                    repetir = relato[elemento]["repetir"]
                    # repite la opción escogida con la última frase antes de la decisión
                    respuesta = relato[elemento]["contenido"][int(decision_tomada) - 1]["opción"]
                    print("\033[1;37;m \n" + repetir + " " + respuesta) 
                elemento = relato[elemento]["contenido"][int(decision_tomada) - 1]["siguiente"]  
        input("\033[1;32;mENTER PARA CONTINUAR\n")
        
                
    # es importante que la revisión de si es una decisión esté primero que la revisión de si hay un texto que
    # dependa de una decisión, pues la primera establece variables a las que la segunda se refiere. Además es
    # el orden lógico, no podrá haber texto que dependa de decisiones si no se han tomado decisiones.
    elif relato[elemento]["tipo"] == "TD":
        #imprime en consola el texto equivalente al recorrido que se escogió, -1 por los índices que empiezan en 0
        print(relato[elemento]["contenido"]["fijo"] + relato[elemento]["contenido"]["variación"][detalle-1], end = "") 
        elemento = relato[elemento]["siguiente"]  

    elif relato[elemento]["tipo"] == "comentario":
        #print("\033[1;34;m" + relato[elemento]["contenido"])
        #print("\033[1;37;m ")          
        elemento = relato[elemento]["siguiente"]
    
    
    
    # necesito mantener "recorrido" y "siguiente" pues hay cambios en el recorrido que tienen que guardarse en
    # memoria (como el cambio que la primera decisión del primer relato genera en el final) y que no afectan
    # necesariamente lo inmediatamente siguiente
      
    # era buena idea pero ya es obsoleto el uso de "elemento" para ir sumando de a uno y recorriendo el relato
    # "linealmente", es mejor añadir a cada sección del relato un metadato que indique a qué sección se sigue
    # desde cada una
    
