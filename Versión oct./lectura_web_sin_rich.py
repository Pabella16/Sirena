# -*- coding: utf-8 -*-
"""
Oct. 2021

@author: Pablo Abella
"""


# Primero que todo hay que invitar a JSON porque sin él no es una fiesta. Con esta instrucción traigo toda la 
# lógica escondida que maneja el tipo de archivo JSON, en el que estoy escribiendo los relatos. Escribirlos en 
# JSON me permite dejarlos previamente estructurados de manera que el programa "converse" con el relato y sepa
# navegarlo. ¡Así puedo escribir muchos relatos con la misma estructura y manejarlos todos con el mismo programa
# en vez de hacer un programa para cada relato! ¡Las maravillas de la tecnología! Solo tendría que devolverme a
# este único programa y cambiar lo que haga falta si decido complicarme la vida cambiando la estructura.
import json
# random me permite escoger algunos datos aleatoriamente, lo que uso para armar los poemas y darles más variedad.
import random as random 


correr = True

print("\nBienvenidx.")
while correr:
    seleccion_relato = False
    print("Selecciona el relato que deseas leer introduciendo un número: \n")
    while not seleccion_relato:
        print("1. Muñecas \n")
        print("2. Hambre \n")
        seleccion = input()
    
        if seleccion.isdigit() and int(seleccion) == 1:
            # abre el archivo (como utf-8 para evitar problemas de caracteres especiales)
            seleccion_relato = True
            with open('MUNECAS.json', encoding='utf-8') as archivo: 
                relato = json.load(archivo) # guarda el archivo como "relato"
            
        elif seleccion.isdigit() and int(seleccion) == 2:
            seleccion_relato = True
            with open('HAMBRE.json', encoding='utf-8') as archivo: 
                relato = json.load(archivo)        
        else:
            print("La selección no es válida, por favor introduce un número del 1 al 2. ")
    
    # Hace falta inicializar la variable "preposicion", pues es una herramienta sorpresa que nos ayudará más tarde.
    preposicion = 0
    
    # Esta pequeña instrucción es, básicamente, lo que pasa las páginas. Es un ciclo que dice "mientras que no se haya
    # pasado el número de elementos que hay en el relato, siga leyendo". Dentro de él se recorren todas las partes del
    # relato, que pueden ser "título", "texto único", "decisión" o "texto dependiente". Cada una significa un set 
    # diferente de instrucciones. En Python, las instrucciones que se ejecutan solamente después de un condicional (if)  
    # o que se repiten en un ciclo (como while o for) están más indentadas que el condicional o el ciclo del que 
    # dependen. Luego, para volver al nivel de instrucciones exterior al ciclo o condicional, se vuelve al grado de 
    # indentación original. Por eso hace falta que todo esté indentado dentro del "while".
    elemento = 0
    while elemento < len(relato):
        # Decidí darle un color verde claro muy ameno a las "instrucciones" que muestra el programa, como cuando se 
        # debe presionar Enter para continuar o se debe ingresar un número. La siguiente instrucción reestablece el 
        # color del texto para que no se vuelva todo verde. Creo que esto ayuda a diferenciar una parte de la otra 
        # y ayuda a ubicarse en el texto que va apareciendo. Esas instrucciones son como otra voz además del relato
        # y del programa/comentarios. ¡Cuánta polifonía! 
    
        # Si la sección referenciada es un título pues... muestra el título ¿qué más esperabas? Mentira, hace algo
        # más, crea de una el poema como una lista vacía con el número de elementos correcto.
        if relato[elemento]["tipo"] == "TI":
            # Recibe el título del JSON y lo formatea bien bonito entre dos filas de signos de igualdad.
            titulo = relato[elemento]["contenido"]
            print("\n"+"="*64,)
            print(titulo, )
            print("="*64+"\n", end = "", )
            # Como todo poema, este tiene que empezar con un espacio en blanco. Excepto que este espacio en blanco 
            # tiene ya definido en cuántas partes está dividido el poema. El programa recibe una lista vacía del 
            # tamaño que tendrá el poema desde el una de las propiedades del título en el JSON. Esto permite armar
            # la lista con antelación para definir el número de partes y simplemente editarlas en su momento (en vez
            # de ir armando el poema bloque por bloque, que ya no me funciona porque, como una de las opciones permite
            # devolverse a otra decisión, una parte del poema se añadiría más de una vez.
            poema = relato[elemento]["poema"]
            # Junto al poema, se crea la lista de variaciones. A esta se le irán añadiendo todos los detalles que una
            # decisión "cause". Por ejemplo, si un personaje rompe un jarrón en una decisión, el jarrón debe aparecer
            # roto más adelante en el relato o debe aparecer intacto si no. Cuando se toma la decisión, se añade a la 
            # lista el texto concreto que debe aparecer más adelante en el relato en las partes que cambian según
            # la decisión.
            variaciones = relato[elemento]["variaciones"]
            # La siguiente instrucción toma de la sección que se está revisando el índice en la lista de la sección
            # que sigue, así se navega el cuento como debe ser, serpenteando según la voluntad del lector.
            elemento = relato[elemento]["siguiente"]
            
            
        # Elif (no confundir con la popular telenovela turca) es una contracción de "else if", o sea "de lo contrario,
        # si no se cumplió el anterior condicional, entonces si este sí se cumple haga tales cosas". Es decir, se hacen
        # las instrucciones de aquí adentro solamente si no se entraron a las instrucciones anteriores y el texto no es
        # de la categoría "título", y así sucesivamente con las otras categorías que tienen "elif", solo se ejecutan si
        # no se cumplió una categoría anterior. En este caso es texto único que solamente muestra y no pasa más na'    
        elif relato[elemento]["tipo"] == "TU":
            print(relato[elemento]["contenido"], end="", )
            elemento = relato[elemento]["siguiente"]
            # Con este condicional permito que al final se muuestre un "ENTER PARA TERMINAR..." que indique que el relato
            # terminó sin que se repita después de un "ENTER PARA CONTINUAR" normal. No hace falta sumarle 1 al elemento
            # en el que va pues la anterior instrucción ya estableció el valor de "elemento" como el siguiente.
            if relato[elemento]["tipo"] != "FIN":
                print("\n\nENTER PARA CONTINUAR")
                input()
                
        
        # En cambio, si la sección es una decisón se pone bien peliaguda la cosa. Hay que mostrar las opciones,
        # permitir que se escoja una de ellas y regañar si se ingresa un valor inválido, registrar si tiene un 
        # efecto en el texto más adelante, guardar el verso que la decisión implica en el poema y mandar la 
        # lectura pa' donde debe seguir según la decisión escogida.
        elif relato[elemento]["tipo"] == "DE":
       #TODO añadí un par de \n pa que funcione mejor en cmd, hay que ver si funciona en los .exe    
            if relato[elemento]["prompt"] != "":
               print(relato[elemento]["prompt"]+"\n", )
           
            for opcion in relato[elemento]["contenido"]:  # muestra las opciones bonitas y ordenadas.
                print(str(opcion["num"])+". "+opcion["opción"]+"\n", )
                
            # Creo una variable para representar si la opción ingresada es valida, esta va a servir para que,
            # hasta que lo sea, le pida al lector que escoja una opción.
            decision_valida = False 
            
            # Mientras que la opción no sea válida, hará todo lo que sigue. El curioso lector
            # de este código se dará cuenta de que ninguno de los nombres de variables tiene tildes, esto es
            # porque las letras con acentos son caracteres especiales que pueden generar errores, la verdad les
            # cogí miedo porque, gracias a los caracteres especiales, el JSON se rehusaba a llevarse bien con el
            # programa hasta que corregí el encoding. Pero más que eso, para las variables que uso en el programa,
            # me ayuda a evitar la confusión de accidentalmente ponerle a unas y a otras no.
            while not decision_valida:
                # esto le pide al usuario que introduzca una de las opciones
                print("¿Qué opción escoges? " + "(1 a " + str(len(relato[elemento]["contenido"]))+ "): ",end="",)
                decision_tomada = input()
                # con esto me aseguro de que la opción ingresada sea un número de las opciones posibles.
                if not decision_tomada.isdigit() or int(decision_tomada)>len(relato[elemento]["contenido"]) or int(decision_tomada)<=0: 
                    print("Debes escoger una de las opciones posibles introduciendo un número.", end="", )
                else:
                    print("\n", end="")
                    decision_valida = True  # se escogió una decisión válida, así que puede continuar.
                                 
                    
                    # Esto guarda los detalles que luego debe incluir el relato en textos dependientes. Para saber si la 
                    # decisión significa cambios en el texto, revisa si la lista guardada como valor de la llave "detalle"
                    # tiene un tamaño mayor a 0. Puede que la decisión cause más de un detalle, por lo que hace falta que
                    # se trate de una lista de diccionarios, cada uno de los cuales contiene el detalle particular que la
                    # decisión "causa" y la posición que debe llevar en la lista de variaciones. Estas instrucciones
                    # recorren todos los diccionarios y anotan cada variacion dentro de la lista prestablecida de
                    # "variaciones" en la posición correcta. Más adelante cuando haya un Texto Dependiente podrá 
                    # completarse con la variación adecuada revisando la lista "variaciones" en la parte adecuada,
                    # que está indicada como valor de la llave "parte" en cada Texto Dependiente. O sea, el detalle
                    # cifrado en cada opción y cada texto dependiente trabajan juntos para construir el texto de manera
                    # consecuente.
                    # -1 porque el indice de las listas empieza en 0.
                    if len(relato[elemento]["contenido"][int(decision_tomada) - 1]["detalle"])>0:
                        for variación in relato[elemento]["contenido"][int(decision_tomada) - 1]["detalle"]:
                            variaciones[variación["posición"]-1] = variación["variación"]
                        
                    # Este condicional revisa si la decisión incluye un verso confirmando si la propiedad "verso" tiene
                    # como valor una lista con un tamaño mayor a 0. Ese larguero de paréntesis cuadrados que sigue a "relato"
                    # es la manera de acceder a cada propiedad específica. En cristiano, lo que dice ahí es "en el relato,
                    # en el elemento número tal, hay una propiedad llamada contenido, dentro de ella están las tres opciones,
                    # acceda a la del número de la decisión tomada y, dentro de ella, revise el tamaño de la lista que es el
                    # valor de la propiedad "verso". Así están anidados los datos de los tipos de texto, y hay que recorrer
                    # todo desde el cajón más general hasta el más específico para encontrar el dato que se está buscando,
                    # pero el camino se puede guardar en una variable, como hago aquí, para que sirva como una especie de atajo.
                    lista_verso = relato[elemento]["contenido"][int(decision_tomada) - 1]["verso"]
                    # Ciertas decisiones no añaden un verso al poema. Estas son las que tienen una lista vacía, de tamaño 0. 
                    # Esto es lo que el condicional revisa para confirmar si no debe entrar a buscar verso donde no hay.
                    # En realidad "verso" se refiere en la mayoría de los casos a una sección del poema de más de un verso, pero 
                    # ese nombre es la forma más fácil de expresar y entender la manera en que se arma el poema.
                    if len(lista_verso) > 0:
                        # El número del verso escogido se inicializa en 1 puesto que, si no hay más de uno, sirve para 
                        # referenciar el primer y único verso de la lista. (No en cero puesto que después igual resto 1 cuando
                        # accedo a él, como está explicado más abajo).
                        num_verso = 1
                        # Algunos versos tienen variaciones que se escogen aleatoriamente para dar más variedad, esto revisa
                        # si existe más de una posibilidad para el verso registrando si el tamaño de la lista es mayor a 1.
                        # Entonces escoge un número aleatorio y se lo asigna al número del verso escogido o, si depende de
                        # una preposición determinada anteriormente, guarda ese como el número del verso y reinicia la variable.
                        if len(lista_verso) > 1 and preposicion==0:
                            num_verso = random.randint(1,len(lista_verso))
                        elif len(lista_verso) > 1 and preposicion>0:
                            num_verso = preposicion
                            preposicion = 0
    
                        
                        # Una vez ha escogido el verso, puede añadirlo a la lista "poema" en la sección indicada por la 
                        # propiedad "parte" del verso. Le debe restar uno a este valor, igual que en otros casos, pues los 
                        # indices de las listas empiezan en 0 [0,1,2,3], así que siempre cuando se usa otro número para hablar 
                        # de la posición en la lista hay que tener en cuenta que la primera posición es 0 y, por lo tanto,
                        # se puede estar dando un indice una unidad mayor a lo propuesto.
                        poema[lista_verso[num_verso-1]["parte"]-1] = lista_verso[num_verso-1]["v"]
                        
                        # Existe la posibilidad de que un verso, por una variación, requiera una preposición particular en
                        # el verso que le sigue. De ser así, el valor de "preposición" será mayor a 0 e indicará
                        # qué parte debe seguir.
                        if lista_verso[num_verso-1]["preposición"] > 0:
                            preposicion = lista_verso[num_verso-1]["preposición"]
                                            
                    # Algunas opciones permiten al lector ingresar una respuesta escrita. Este condicional revisa la 
                    # propiedad "input" de la decisión para saber si es o no el caso revisando si el valor de la clave es
                    # diferente a un string vacío. Si es el caso, usa el string que haya como valor para preguntar la respuesta
                    if relato[elemento]["contenido"][int(decision_tomada) - 1]["input"] != "":
                        respuesta = input(relato[elemento]["contenido"][int(decision_tomada) - 1]["input"])
                        print("\n")
                    # Si no es necesario que el usuario ingrese una respuesta, sigue normal con las respuesta escogida.
                    elemento = relato[elemento]["contenido"][int(decision_tomada) - 1]["siguiente"]  
            
            
        # El "texto dependiente", como dice su nombre, depende de una decisión. Estas instrucciones muestran el texto
        # apropiado según lo que se eligió antes. Hay un texto fijo y una variación. Cada Texto Dependiente incluye
        # en la llave "parte" de sus propiedades el número de la lista de "variaciones" del que debe sacar su
        # variación. Esta la añade al texto fijo para mostrar la oración completa que se ha determinado antes en una
        # toma de decisón. Esta parte fue bien compleja.
        # Es importante que la revisión de si es una decisión esté primero que la revisión de si hay un texto que
        # dependa de una decisión, pues la primera establece variables a las que la segunda se refiere. Además es
        # el orden lógico, no podrá haber texto que dependa de decisiones si no se han tomado decisiones.
        elif relato[elemento]["tipo"] == "TD":
            # Imprime en consola el texto equivalente al recorrido que se escogió, -1 por los índices que empiezan en 0
            print(relato[elemento]["contenido"]["fijo"] + variaciones[relato[elemento]["contenido"]["parte"]-1], end="", )
            elemento = relato[elemento]["siguiente"]
            
            if relato[elemento]["tipo"] != "FIN":
                print("\n\nENTER PARA CONTINUAR")
                input()
    
        # Si el tipo de texto es "FIN", el programa muestra el poema que se armó y apague y vámonos. Relato relatado.
        elif relato[elemento]["tipo"] == "FIN":
            print("\n\nENTER PARA TERMINAR EL CUENTO Y VER TU POEMA\n ",end="",)
            input()
            for i in poema:
                print(i)         
            elemento = relato[elemento]["siguiente"]
    
    print("\n\n\n¿Deseas leer otro relato o salir?: \n")
    seleccion_final = False
    while not seleccion_final:
        print("1. Leer otro relato \n")
        print("2. Salir \n")
        menu_final = input()
        
        if menu_final.isdigit() and int(menu_final) == 1:
            seleccion_final = True
        elif menu_final.isdigit() and int(menu_final) == 2:
            seleccion_final = True
            correr = False
        else:
            print("La selección no es válida, por favor introduce un número del 1 al 2. ")

  
