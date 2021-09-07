# -*- coding: utf-8 -*-
"""
 Aug 2021

@author: Pablo Abella
"""

import json

with open ("Json_test.json") as test: #abre archivo
    relato = json.load(test)
    
elemento = 0
print("")

while elemento < len(relato): #while es más complejo :c

#for elemento in relato: #recorre todas las partes del relato que pueden ser "texto unico", "decision" o "texto dependiente"
    
    if relato[elemento]["tipo"] == "texto unico": #si es texto unico simplemente lo muestra
        print(relato[elemento]["contenido"])
        elemento+=1    
    
        
    elif relato[elemento]["tipo"] == "decision": #si hay una decision debe mostrar todas las opciones al lector y permitirle escoger
        for opcion in relato[elemento]["contenido"]: #muestra opciones
            print(str(opcion["num"])+". "+opcion["opcion"])
        
        decision_valida = False #creo una variable para representar si la opción ingresada es valida, esta va a servir para que, hasta que lo sea, le pida al lector que escoja una opción
        while not decision_valida: #mientras que la opción no sea válida, hará todo lo que sigue. El curioso lector de este código se dará cuenta de que ninguno de los nombres de variables tiene tildes, esto es porque las letras con acentos son caracteres especiales que pueden generar errores, espero que no pase lo mismo con las cadenas de texto, es decir el relato y los poemas en sí, pero esperaría que no.
            decision_tomada = input("\n¿Qué opción escoges?: ") #esto le pide al usuario que introduzca una de las opciones
            if decision_tomada != "1" and decision_tomada != "2" and decision_tomada != "3": # con esto me aseguro de que la opción ingresada sea 1, 2 o 3.
                print("\nDebes escoger una de las opciones posibles introduciendo un número.")
            else:
                decision_valida = True #se escogió una decisión válida, así que puede continuar
                recorrido = relato[elemento]["contenido"][int(decision_tomada)-1]["recorrido"] #guarda el recorrido escogido para saber qué camino debe seguir el relato, "recorrido" es una propiedad de cada decision que dice el camino al que lleva la decisión. Es mejor hacer esto que usar el índice de la lista puesto que podría haber dos decisiones que lleven al mismo camino. -1 porque el indice de las listas empieza en 0.
                print("\nEscojiste: " + relato[elemento]["contenido"][int(decision_tomada)-1]["opcion"]) #repite la opción escogida
                
                if relato[elemento]["contenido"][int(decision_tomada)-1]["rebobinar"]>0: #si el número de "pasos" en el relato que se quieren rebobinar es mayor a cero, se imprime en consola el resultado de la decisión y se rebobina esa cantidad de pasos
                    print(relato[elemento+1]["contenido"][recorrido-1])
                    elemento-=relato[elemento]["contenido"][int(decision_tomada)-1]["rebobinar"]
                else:
                    elemento+=1 #si no hay que rebobinar simplemente pasa a la siguiente sección del relato
                
    #es importante que la revisión de si es una decisión esté primero que la revisión de si hay un texto que dependa de una decisión, pues la primera establece variables a las que la segunda se refiere. Además es el orden lógico, no podrá haber texto que dependa de decisiones si no se han tomado decisiones.
    elif relato[elemento]["tipo"] == "texto dependiente":
        print(relato[elemento]["contenido"][recorrido-1]) #imprime en consola el texto equivalente al recorrido que se escogió
        elemento +=1            
    
    #necesito mantener "recorrido" y "siguiente" pues hay cambios en el recorrido que tienen que guardarse en memoria (como el cambio que la primera decisión del primer relato genera en el final) y que no afectan necesariamente lo inmediatamente siguiente
      
    #era buena idea pero ya es obsoleto el uso de "elemento" para ir sumando de a uno y recorriendo el relato "linealmente", es mejor añadir a cada sección del relato un metadato que indique a qué sección se sigue desde cada una
    
    #no puedo ponerle tildes a las llaves o a los valores en el JSON o todo colapsa ._.
    input("ENTER para continuar \n")