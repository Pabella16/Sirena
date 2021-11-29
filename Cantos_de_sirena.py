# -*- coding: utf-8 -*-
"""
v.3.0, 2021-11-25

@author: Pablo Abella
"""
# Cantos de sirena es un proyecto creativo que explora la representación de la identidad de género, de la
# sexualidad y del carácter violento del deseo a través de una colección interactiva de cuentos y poemas
# presentada como programa de computador. Como experiencia interactiva, el proyecto busca dar cuenta de la
# crisis que la imposición de roles de género genera en alguien y presentar el género como una identidad fluida
# que se transforma y resignifica con los encuentros entre cuerpos y perspectivas. Me propuse mezclar ficción,
# poesía y programación para convertir al lector en jugador, editor y performer a través de la toma de decisiones
# en el contexto de lo narrado. Este programa referencia los archivos JSON en los que están estructurados los 
# relatos para recorrerlos, permitir al lector tomar decisiones y generar poemas.


# Primero que todo hay que invitar a JSON porque sin él no es una fiesta. Con esta instrucción traigo toda la 
# lógica escondida que maneja el tipo de archivo JSON, en el que estoy escribiendo los relatos. Escribirlos en 
# JSON me permite dejarlos previamente estructurados de manera que el programa "converse" con el relato y sepa
# navegarlo. ¡Así puedo escribir muchos relatos con la misma estructura y manejarlos todos con el mismo programa
# en vez de hacer un programa para cada relato! ¡Las maravillas de la tecnología! (Para más información sobre los
# JSON revisar comentarios en archivos .json).
import json

# Random me permite escoger algunos datos aleatoriamente, lo que uso para armar ciertos poemas y darles más variedad.
import random as random 

# Rich es un modulo para Python que permite organizar el texto en la pantalla fácilmente y cambiar el color y el
# formato. Aquí importo "console" la herramienta con la que muestro el texto de maneras bonitas, que se puede 
# encontrar a lo largo del código antes de la instrucción normal de Python para mostrar cosas en consola: "print()".
from rich.console import Console
console = Console()
    
# Aquí defino mi primera función. Una función es como un mini programa contenido dentro del programa grande.
# Esto es útil para correr una sección de código cuando es necesario en vez de tener que reescribirla
# un montón de veces en el código cada vez que se quiere correr. Por ejemplo, aquí uso las funciones para que
# desde el menú se puedan activar diferentes secciones de código. Las variables que uno declara dentro de
# una función están limitadas solamente al reino de esa función. Es decir, si digo que la variable "número" es igual
# a 5 por fuera de una función y luego intento usar la variable "número", la función no tendrá ni idea de qué le estoy
# hablando, lo mismo si declaro la variable adentro y luego intento referenciarla por fuera, como si fuera un país
# aislado con sus propias costumbres en medio de un continente. ¡¡¡Sin embargo!!! Las funciones pueden recibir
# argumentos entre los paréntesis que siguen el nombre de la función. O sea, uno puede avisar desde el principio que
# la función va a importar una información de afuera cuando corra, e igualmente, al final, se puede exportar 
# información con la instrucción "return" seguida de los valores o variables que la función arroja. En este caso,
# la función que recorre los relatos recibe una lista con los datos sobre el jugador para editarla y registrar
# cuando se generan poemas o se descubren objetos coleccionables (explicaré esto con más detalle luego.)
def relatos(data):
    # Establezco la variable "volver_al_menu" como falsa desde el comienzo para que la siguiente serie de instruccciones,
    # que muestra los relatos, se repita hasta que se vuelva verdadera. Se vuelve verdadera si el lector lo indica al
    # terminar de leer un relato, y eso permite que se salga del ciclo y por tanto de la función.
    volver_al_menu = False
    while not volver_al_menu:
        # Misma lógica: mientras que una variable no sea verdadera (o sea mientras no se cumpla una condición),
        # no se saldrá del ciclo contenido por el "while". Esta misma construcción está varias veces en el programa,
        # la mayoría para no avanzar mientras que el lector no haya ingresado un valor válido, como en este caso.
        # De ahora en adelante me referiré al funcionamiento de esta sección como "lógica de menú".
        seleccion_valida = False
        console.print("[green]Selecciona el relato que deseas leer introduciendo un número: \n[/]")
        while not seleccion_valida:
            # Se muestran las opciones y se pide al usuario que ingrese un valor, que se guarda en "seleccion".
            console.print("1.[green] Muñecas \n[/]")
            console.print("2.[green] Presión \n[/]")
            console.print("3.[green] Hambre \n[/]")
            seleccion = input()
            
            # Esta estructura está mil veces más en el programa. Revisa que la selección ingresada sea una cifra y, si
            # lo es, revisa si es una de las cifras de las opciones.
            if seleccion.isdigit() and int(seleccion) == 1:
                # Por ejemplo, si la selección es "1", el lector escogió leer "Muñecas", y el programa abre el archivo 
                # de este relato (como utf-8 para evitar problemas de caracteres especiales). También vuelve verdadera
                # la variable "seleccion_valida" de manera que deje de repetirse el ciclo. Las siguientes dos secciones
                # hacen lo mismo con los otros dos relatos.
                seleccion_valida = True
                with open('MUNECAS.json', encoding='utf-8') as archivo: 
                    # Guarda el archivo como "relato", ahora la variable contiene la lista del relato entero.
                    relato = json.load(archivo) 
                
            elif seleccion.isdigit() and int(seleccion) == 2:
                seleccion_valida = True
                with open('PRESION.json', encoding='utf-8') as archivo: 
                    relato = json.load(archivo)
                    
            elif seleccion.isdigit() and int(seleccion) == 3:
                seleccion_valida = True
                with open('HAMBRE.json', encoding='utf-8') as archivo: 
                    relato = json.load(archivo)
            
            # Si no se cumplió ninguna de las anteriores condiciones, no se cambia el valor de "seleccion_valida" y
            # se muestra un pequeño regaño indicando qué valores se pueden ingresar, y se repite el ciclo del "while"
            # de arriba.
            else:
                # Decidí darle un color verde claro muy ameno a las "instrucciones" que muestra el programa, como cuando se 
                # debe presionar ENTER para continuar o se debe ingresar un número. Creo que esto ayuda a diferenciarlas del
                # relato en sí y ayuda a ubicarse en el texto que va apareciendo. Esas instrucciones son como otra voz además
                # del relato y del programa/comentarios. ¡Cuánta polifonía!
                console.print("[green]\nLa selección no es válida, por favor introduce un número del 1 al 3. \n[/]")
        
        
        # Hace falta inicializar la variable "preposicion", pues es una herramienta sorpresa que nos ayudará más tarde.
        # Cuando se combinan versos de poemas, es posible que se seleccione un verso que necesite una preoposicón 
        # específica para que el verso que lo sigue tenga sentido gramatical. Si hay más de una posibilidad de verso
        # (sea por variedad o para cuadrar gramaticalmente con el verso anterior), habra más de un verso guardado en
        # una lista ordenada [verso 1: "bla bla bla", verso 2: "bla bla"]. Así que, cuando se escoge un verso, está  
        # acompañado por una categoría llamada "preposición" que indica la posición en la lista del verso que debe 
        # seguir. Si no es necesario que siga un verso en particular, "preposición" es igual a 0. Creo la variable 
        # desde aquí pues la referencio cada que se añade un verso al poema que se está armando y la inicializo en
        # 0 puesto que el primer verso claramente no depende de un verso anterior. Así puedo usarla tranqulamente
        # más adelante la primera vez para después sí transformar su valor según el verso que se genere y la 
        #información del JSON. Fiu. Esta parte fue casi tan difícil de programar como de explicar.
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
        
            # Si la sección referenciada es un título pues... muestra el título ¿qué más esperabas? Mentira, hace algo
            # más, crea de una el poema como una lista vacía con el número de elementos correcto y guarda una lista
            # vacía en la que estarán las variaciones que generen las decisiones.
            if relato[elemento]["tipo"] == "TI":
                # Recibe el título del JSON y lo formatea bien bonito entre dos filas de signos de igualdad.
                titulo = relato[elemento]["contenido"]
                console.print("\n"+"="*64,justify="center")
                console.print(titulo, justify="center")
                console.print("="*64+"\n", end = "", justify="center")
                # Como todo poema, este tiene que empezar con un espacio en blanco. Excepto que este espacio en blanco 
                # tiene ya definido en cuántas partes está dividido el poema. El programa recibe una lista vacía del 
                # tamaño que tendrá el poema desde una de las propiedades del título en el JSON. Esto permite armar
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
                console.print("\n" + relato[elemento]["contenido"], end="", justify="full")                
                elemento = relato[elemento]["siguiente"]
                input()
                    
            
            # En cambio, si la sección es una decisón se pone bien peliaguda la cosa. Hay que mostrar las opciones,
            # permitir que se escoja una de ellas y regañar si se ingresa un valor inválido, registrar si tiene un 
            # efecto en el texto más adelante, guardar el verso que la decisión implica en el poema y mandar la 
            # lectura pa' donde debe seguir según la decisión escogida.
            elif relato[elemento]["tipo"] == "DE":
                # Cuando una sección del relato es una decisión, puede tener una especificación llamada "prompt", que
                # es una sección de texto para mostrar justo antes de la decisión que la contextualiza o incluye la 
                # parte inicial de la oración que la decisión completa. Esta instrucción revisa que "prompt" no sea
                # una cadena de texto vacía y muestra el valor guardado en "prompt".
                if relato[elemento]["prompt"] != "":
                   console.print("\n" + relato[elemento]["prompt"]+"\n", justify="full")
               
                for opcion in relato[elemento]["contenido"]:  # Muestra las opciones bonitas y ordenadas.
                    console.print(str(opcion["num"])+". "+opcion["opción"]+"\n", justify="full")
                    
                # Creo una variable para representar si la opción ingresada es valida, esta va a servir para que,
                # hasta que lo sea, le pida al lector que escoja una opción, como en la lógica de menú explicada
                # más arriba.
                decision_valida = False 
                
                # El curioso lector de este código se dará cuenta de que ninguno de los nombres de variables tiene tildes, 
                # esto es porque las letras con acentos son caracteres especiales que pueden generar errores, la verdad les
                # cogí miedo porque, gracias a los caracteres especiales, el JSON se rehusaba a llevarse bien con el
                # programa hasta que corregí el encoding. Pero más que eso, para las variables que uso en el programa,
                # me ayuda a evitar la confusión de accidentalmente ponerle a unas y a otras no.
                while not decision_valida:
                    # Esto le pide al usuario que introduzca una de las opciones
                    console.print("¿Qué opción escoges? (1 a " + str(len(relato[elemento]["contenido"]))+ "):",style="green",end="",justify="right",highlight=False)
                    decision_tomada = input()
                    # Con esto me aseguro de que la opción ingresada sea un número de las opciones posibles.
                    if not decision_tomada.isdigit() or int(decision_tomada)>len(relato[elemento]["contenido"]) or int(decision_tomada)<=0: 
                        console.print("[green]Debes escoger una de las opciones posibles introduciendo un número.[/]", end="", justify="right")
                    else:
                        # Este tipo de instrucción está en diferentes partes del programa. Simplemente salta una línea en
                        # el texto que se está mostrando. "\n" es como una instrucción dentro del texto que inserta un 
                        # salto de línea y no aparece literalmente como "\n" cuando se muestra un texto. Esto ayuda a 
                        # organizar el texto y evitar que se amontone.
                        console.print("\n", end="")
                        decision_valida = True  # Se escogió una decisión válida, así que puede continuar.
                        # Tonces, una vez la opción es válida se puede entrar a revisar si esa opción lleva a un objeto
                        # coleccionable. Esto se sabe si la categoría "coleccionable" está en la opción. De ser así, 
                        # cambia el valor de "encontrado" a verdadero en los datos sobre la lectura del relato, que se
                        # guardan en una lista llamada "data". Lo chevere es que una vez se encontró un coleccionable
                        # solo hay que volver la variable verdadero una vez, como precionar un switch, y queda activada
                        # la instrucción de mostrar el coleccionable.
                        if "coleccionable" in relato[elemento]["contenido"][int(decision_tomada) - 1]:
                            data[int(seleccion)-1]["encontrado"] = True
                            
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
                            # accedo a él, como está explicado más abajo sobre los índices de las listas).
                            num_verso = 1
                            # Algunos versos tienen variaciones que se escogen aleatoriamente para dar más variedad o se escogen
                            # deliberadamente para cuadrar gramaticalmente con el verso anterior. Esto revisa si existe más de
                            # una posibilidad para el verso registrando si el tamaño de la lista es mayor a 1. Entonces escoge
                            # un número aleatorio y se lo asigna al número del verso escogido o, si depende de una preposición
                            # determinada anteriormente, usa el número guardado en "preposición" para determinar el número del
                            # verso y reinicia la variable "preposición".
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
                            
                            # Si un verso requiere una preposición particular en el verso que le sigue, el valor de 
                            # "preposición" será mayor a 0 e indicará la parte que debe seguir, para revisar en el registro
                            # del siguiente verso.
                            if lista_verso[num_verso-1]["preposición"] > 0:
                                preposicion = lista_verso[num_verso-1]["preposición"]
                                                
                        # Algunas opciones permiten al lector ingresar una respuesta escrita. Este condicional revisa la 
                        # propiedad "input" de la decisión para saber si es o no el caso revisando si el valor de la clave es
                        # diferente a un string vacío. Si es el caso, usa el string que haya como valor para preguntar la respuesta
                         
                        # Cuando el lector escribe una respuesta, la registra en la variable "data" para poder mostrarla en uno de 
                        # los coleccionables: la tarjeta con el tema de conversación.                        
                        if relato[elemento]["contenido"][int(decision_tomada) - 1]["input"] != "":
                            data[0]["respuesta"] = console.input(relato[elemento]["contenido"][int(decision_tomada) - 1]["input"])
                            console.print("\n")
                        # Si no es necesario que el usuario ingrese una respuesta, sigue normal con la sección que indica
                        # la respuesta escogida.
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
                console.print("\n" + relato[elemento]["contenido"]["fijo"] + variaciones[relato[elemento]["contenido"]["parte"]-1], end="", justify="full")
                elemento = relato[elemento]["siguiente"]
                input()
        
            # Si el tipo de texto es "FIN", el programa muestra el poema que se armó y apague y vámonos. Relato relatado.
            elif relato[elemento]["tipo"] == "FIN":
                console.print("[green]\nPRESIONA ENTER PARA VER TU POEMA\n [/]",end="",justify="right")
                input()
                for i in poema:
                    print(i)         
                elemento = relato[elemento]["siguiente"]
                
        
        # input para que se presione ENTER después de que aparece el poema
        input()
        # Okey esta parte es chevere. Aquí se revisa si ya se ha guardado un poema generado por un relato viendo si el
        # tamaño de la lista que representa al poema en la variable "data" es mayor a cero. Si no es mayor a cero se 
        # guarda el poema generado sin preguntar, pero si sí es mayor a cero, hay que preguntar si se quiere cambiar el 
        # poema viejo.
        if len(data[int(seleccion)-1]["poema"])==0:
            data[int(seleccion)-1]["poema"] = poema
        else:
            console.print("[green]\n\nYa hay un poema guardado para este relato:[/]")
            
            # Muestra el poema viejo
            for v in data[int(seleccion)-1]["poema"]:
                print(v)
            # Aquí hay otra sección con lógica de menú que permite escoger si se cambia el poema guardado en "data" por 
            # el que se acaba de crear.
            seleccion_valida = False
            while not seleccion_valida:
                console.print("\n1.[green] Reemplazar el poema guardado\n[/]")
                console.print("2.[green] Mantener el poema guardado[/]")
                guardar_poema = console.input("[green]\n¿Qué quieres hacer?\n[/]")
                
                if guardar_poema.isdigit() and int(guardar_poema) == 1:
                    data[int(seleccion)-1]["poema"] = poema
                    seleccion_valida = True
                elif guardar_poema.isdigit() and int(guardar_poema) == 2:
                    seleccion_valida = True
                else:
                    console.print("[green]\nLa selección no es válida, por favor introduce 1 o 2. [/]")
        
        # Una vez más, lógica de menú. Aquí se cambia el valor de "volver_al_menu" a verdadero si el lector escoge volver
        # al menú principal. Esto hace que el ciclo del while de por allaaaa arriba se repita: vuelve a preguntar qué
        # relato se quiere leer y vuelve y muestra un relato completo. De lo contrario se continúa al "return" y se arroja
        # la variable "data" con todos los cambios que se han hecho.
        console.print("[green]\n\n\n¿Deseas leer otro relato o volver al menú principal?: \n[/]")
        seleccion_valida = False
        while not seleccion_valida:
            console.print("1.[green] Leer otro relato \n[/]")
            console.print("2.[green] Volver al menú principal \n[/]")
            menu_final_relato = input()
            
            if menu_final_relato.isdigit() and int(menu_final_relato) == 1:
                seleccion_valida = True
            elif menu_final_relato.isdigit() and int(menu_final_relato) == 2:
                seleccion_valida = True
                volver_al_menu = True
            else:
                console.print("[green]\nLa selección no es válida, por favor introduce un número del 1 al 2. [/]")
    return data

# Esta es la función del tutorial. Es muy parecida a la que corre los relatos y es completamente independiente. No necesita
# información exterior ni bota información. También se basa en un JSON y hace un simulacro interactivo de lo que es recorrer
# los relatos.
def tutorial():
    with open('tutorial.json', encoding='utf-8') as archivo: 
        tut = json.load(archivo) # guarda el archivo como "tut"
    # Como la anterior función, recorre las secciones del archivo y lleva a cabo ciertas instrucciones dependiendo del tipo 
    # de sección.
    elemento = 0
    while elemento < len(tut):
        if tut[elemento]["tipo"] == "TU":
            # Esta partecita sirve para justificar el texto a la derecha de la pantalla en una de las secciones.
            if tut[elemento]["dir"] == "R":
                console.print(tut[elemento]["contenido"], style="green", end="", justify="right")
            else:    
                console.print(tut[elemento]["contenido"], style="green", end="", justify="full")
            # Esta parte "responde" a lo que el usuario ingresa en la explicación de cómo ciertas decisiones reciben texto
            # escrito por el usuario. Dependiendo de lo que responde a la pregunta "¿cuál es el título de esta monografía?"
            # da una respuesta.
            if "input" in tut[elemento]:
                console.print(tut[elemento]["input"], style="green", end="", justify="full")
                titulo_ingresado = str(input()).strip().lower() 
                if titulo_ingresado == "cantos de sirena":
                    console.print("\n\nExactamente, veo que estás poniendo atención.\n", style="green", end="", justify="full")
                else:
                    console.print("\nEsa no es la respuesta correcta pero ¿sabes? tal vez '" + titulo_ingresado + "' habría sido un mejor título.\n", style="green", end="", justify="full")
            elemento = tut[elemento]["siguiente"]
            input()

        elif tut[elemento]["tipo"] == "DE": 
            for opcion in tut[elemento]["contenido"]:  # muestra las opciones bonitas y ordenadas.
                console.print(str(opcion["num"])+". "+opcion["opción"]+"\n", justify="full")
                    
            # La misma estructura de menú de las decisiones de los relatos.
            decision_valida = False 
            while not decision_valida:
                console.print("¿Qué opción escoges? (1 a " + str(len(tut[elemento]["contenido"]))+ "):",style="green",end="",justify="full",highlight=False)
                decision_tomada = input()
                # Aquí muestra regaños personalizados si se ingresa un valor que no corresponde a las opciones o ni siquiera
                # es un número.
                if not decision_tomada.isdigit(): 
                    console.print("[green]Eso... Eso ni siquiera es una cifra ¿estás jugando conmigo? Necesito que pongas una cifra correspondiente a una de las opciones: 1, 2 o 3. Ten cuidado de no poner espacios ni caracteres adicionales.[/]", end="", justify="full")
                elif int(decision_tomada)>len(tut[elemento]["contenido"]) or int(decision_tomada)<=0:
                    console.print("[green]Qué agradable número, lástima que no es 1, 2 o 3, que son los números correspondientes a las opciones que te mostré. Igual gracias, es bueno saber que conoces más números.[/]", style="green", end="", justify="full")
                else:
                    console.print("\n", end="")
                    decision_valida = True  # se escogió una decisión válida, así que puede continuar.
            elemento = tut[elemento]["contenido"][int(decision_tomada) - 1]["siguiente"]

# Esta es la función de la galería de poemas. Recibe la variable "data" y una lista prestablecida con el tamaño correcto
# para organizar los poemas. Originalmentequería mostrar los tres poemas uno al lado del otro pero fueron muy difíciles de
# organizar. Creo que no hay mucho más que decir: muestra los poemas que se han generado.
def galeria_poemas(data,poemas):
    # Este par de whiles tenían el propósito de organizar los poemas en una especie de matríz para poderlos mostrar uno
    # al lado del otro. Esto me resultó imposible, pero la matríz me sirvió para guardar los poemas como si estuvieran 
    # organizados en una tabla, que es la lista "poemas".
    contador_r = 0
    while contador_r < 3:
        if len(data[contador_r]["poema"])>0:
            contador_p = 0
            while contador_p < len(data[contador_r]["poema"]):
                poemas[contador_p][contador_r] = data[contador_r]["poema"][contador_p]
                contador_p+=1 
        contador_r+=1
    
    # Aquí uso la lógica de menú para mostrar los distintos poemas con unos ciclos que recorren la "tabla" de la variable
    # "poemas" por sus columnas, que son equivalentes a los poemas.
    seleccion_valida = False
    volver_al_menu = False
    while not (seleccion_valida and volver_al_menu):
        console.print("[green]\n¿Qué quieres hacer?: \n[/]")
        console.print("1.[green] Ver poema de 'Muñecas'\n[/]")
        console.print("2.[green] Ver poema de 'Presión' \n[/]")
        console.print("3.[green] Ver poema de 'Hambre'\n[/]")
        console.print("4.[green] Volver al menú principal[/]")
        seleccion = input()
        print("\n")
        if seleccion.isdigit() and int(seleccion) == 1:
            seleccion_valida = True
            for fila in poemas:
                console.print("\n{}".format(fila[0]),end="")
            console.input("[green]\nPresiona ENTER para volver\n[/]")
            
        elif seleccion.isdigit() and int(seleccion) == 2:
            seleccion_valida = True
            for fila in poemas:
                console.print("\n{}".format(fila[1]),end="")
            console.input("[green]\nPresiona ENTER para volver\n[/]")
            
        elif seleccion.isdigit() and int(seleccion) == 3:
            seleccion_valida = True
            for fila in poemas:
                console.print("\n{}".format(fila[2]),end="")
            console.input("[green]\nPresiona ENTER para volver\n[/]")
            
        elif seleccion.isdigit() and int(seleccion) == 4:
            seleccion_valida = True
            volver_al_menu = True
        
        else:
            console.print("[green]\nLa selección no es válida, por favor introduce un número del 1 al 4. \n[/]")

              
# La galería de coleccionables es muy simple. Usa "data" para revisar si en los datos de cada relato "encontrado" es
# verdadero y, si lo es, muestra la información del coleccionable. De lo contrario muestra "???".             
def galeria_coleccionables(data):
    console.print("\nColeccionable de 'Muñecas':\n",highlight=False) 
    if data[0]["encontrado"]:
        console.print("{:>5}".format(data[0]["coleccionable"]))
        # Esto es algo especial del coleccionable de "Muñecas", si se dio una respuesta perzonalizada a "What is your
        # earliest memory", esta se va a haber guardado en los datos de "Muñecas" en la categoría "respuesta" y se
        # mostrará junto a la información del coleccionable. Es cool, en el futuro quiero hacer más mecánicas así, que
        # recuerden este tipo de detalles.
        if data[0]["respuesta"] != "":
            console.print("A la pregunta de la tarjeta respondiste: " + data[0]["respuesta"])
    else:
        console.print("{:>5}".format("???"))
    console.print("\nColeccionable de 'Presión':\n",highlight=False)
    if data[1]["encontrado"]:
        console.print("{:>5}".format(data[1]["coleccionable"]))
    else:
        console.print("{:>5}".format("???"))    
    console.print("\nColeccionable de 'Hambre':\n",highlight=False)
    if data[2]["encontrado"]:
        console.print("{:>5}".format(data[2]["coleccionable"]))
    else:
        console.print("{:>5}".format("???"))

    console.input("[green]\n\nPresiona ENTER para volver al menú principal\n[/]")

def menu_principal(): # Esta función solamente muestra las opciones del menú principal
    console.print("[green]\n¿Qué quieres hacer? Introduce un número y presiona ENTER: \n[/]")
    console.print("1.[green] Leer relatos \n[/]")
    console.print("2.[green] Ver galería de poemas \n[/]")
    console.print("3.[green] Ver objetos coleccionables \n[/]")
    console.print("4.[green] Ver tutorial \n[/]")
    console.print("5.[green] Salir \n[/]")


# Esta función es el ciclo general del programa al que siempre se vuelve para seleccionar una opcion del menú principal,
# incluye la introducción en la que se muestra el título, la información, los epígrafes y la dedicatoria una sola vez,
# da la opción de ver el tutorial antes de seguir al menú principal y luego entra a un ciclo de mostrar el menú hasta
# que se haya escogido la opción salir. Es como si todo el programa estuviera contenido en esta función que permite
# correr todas las otras opciones una y otra vez volviendo al menú principal cada vez que las termina de correr.

def Cantos_de_sirena(): 
    console.print("\n\n[bold black]PRESIONA ENTER[/]",justify="center")
    input()
    console.print("\n   _____            _                  _            _                  v.3.0\n  / ____|          | |                | |          (_)              dic.2021\n| |     __ _ _ __ | |_ ___  ___    __| | ___   ___ _ _ __ ___ _ __   __ _ \n | |    / _` | '_ \| __/ _ \/ __|  / _` |/ _ \ / __| | '__/ _ \ '_ \ / _` |\n | |___| (_| | | | | || (_) \__ \ | (_| |  __/ \__ \ | | |  __/ | | | (_| |\n  \_____\__,_|_| |_|\__\___/|___/  \__,_|\___| |___/_|_|  \___|_| |_|\__,_|\n\n",style="cyan bold",justify="center",highlight=False)
    # Versión del título con puntos negros en vez de fecha y versión:
    # console.print("\n\n[bold]   _____            _                  _            _                      [/][black].[/]\n[bold]  / ____|          | |                | |          (_)                     [/][black].[/]\n[bold]| |     __ _ _ __ | |_ ___  ___    __| | ___   ___ _ _ __ ___ _ __   __ _ \n | |    / _` | '_ \| __/ _ \/ __|  / _` |/ _ \ / __| | '__/ _ \ '_ \ / _` |\n | |___| (_| | | | | || (_) \__ \ | (_| |  __/ \__ \ | | |  __/ | | | (_| |\n  \_____\__,_|_| |_|\__\___/|___/  \__,_|\___| |___/_|_|  \___|_| |_|\__,_|\n\n[/]",style="cyan",justify="center",highlight=False)
    console.print("Pablo Abella Calle\n\nMonografía en creación para optar al título de Literato\n\n\n",style="bold",justify="center")
    console.print("Dirigida por Mario Barrero Fajardo y Nicolás Vaughan Caro\n\nCoordinada por Fernanda Trías Patrón\n\n\n",style="bold",justify="center")
    console.print("Universidad de los Andes\nFacultad de Artes y Humanidades\nDepartamento de Humanidades y Literatura\nBogotá\nDiciembre de 2021\n\n",style="bold",justify="center",highlight=False)
    console.print("~"*119,justify="center")
    console.print("[green]\nPRESIONA ENTER PARA CONTINUAR[/]",justify="center")
    input()
    console.print("\n\n\n" + " "*39 + "A mi familia. Son mi inspiración, mi fuerza y mi luz.",justify="right")
    console.print("\n\n" + " "*39 + "A Andrea, que me ha dado más amor del que creí que cabía en el mundo.",justify="right")
    console.print("\n\n" + " "*39 + "A mis amigos Tomás, David, Juan, Lena, Laura, Sofía, Melissa y Abraham, que me recuerdan cada día lo hermoso que es estar vivo.\n",justify="right")

    console.print("\n\n\n" + " "*39 + "Gracias a Mario y a Nicolás, por guíarme y motivarme.",justify="right")
    console.print("\n\n" + " "*39 + "Gracias a Fernanda, por sus consejos y su atención.",justify="right")
    console.print("\n\n" + " "*39 + "Gracias a Laura, Maria José, Camila y Maria Alejandra, por sus textos y su compañía.",justify="right")
    console.print("\n\n" + " "*39 + "Gracias a Juan Diego, por creer en mí y compartirme sus palabras.\n\n",justify="right")
    console.print("~"*119,justify="center")
    console.print("[green]\nPRESIONA ENTER PARA CONTINUAR[/]",justify="center")
    input()
    
    console.print("\n\n\n" + " "*39 + "\"[i]Quién no se ha preguntado alguna vez ¿soy un monstruo o es esto ser una persona?[/]\"\nClarice Lispector,[i]La hora de la estrella[/]",justify="right",highlight=False)
    console.print("\n\n" + " "*39 + "\"[i]Todos eran el chofer; él, el pasajero.[/]\"\nMayra Santos-Febres,[i]Sirena Selena, vestida de pena[/]",justify="right",highlight=False)
    console.print("\n\n" + " "*39 + "\"[i]When Stanley came to a set of two open doors, he entered the door on his left.[/]\"\n[i]The Stanley Parable[/]\n\n",justify="right",highlight=False)
    console.print("~"*119,justify="center")
    console.print("[green]\nPRESIONA ENTER PARA CONTINUAR[/]",justify="center")
    input()
    
    console.print("[green]\n\n\nBienvenidx.[/]")    
    seleccion_valida = False
    console.print("[green]¿Deseas ver el tutorial? Introduce el número correspondiente a una opción y presiona ENTER para continuar: \n[/]")
    while not seleccion_valida:
        console.print("1.[green] Sí, ver el tutorial \n[/]")
        console.print("2.[green] No, omitir el tutorial \n[/]")
        seleccion = input()
        if seleccion.isdigit() and int(seleccion) == 1:
            seleccion_valida = True
            tutorial()
            
        elif seleccion.isdigit() and int(seleccion) == 2:
            seleccion_valida = True
        
        else:
            console.print("[green]La selección no es válida, por favor introduce 1 o 2. [/]")
    
    # Abre el archivo JSON data y lo guarda en una variable para editarlo y guardar los avances y los poemas generados.
    with open('data.json', 'r', encoding='utf-8') as archivo_data:
        data = json.load(archivo_data)
    # Crea la "tabla" (matriz) del tamaño indicado para registrar los poemas.
    poemas = [["(No has generado este poema)","(No has generado este poema)","(No has generado este poema)"],["","",""],["","",""],["","",""],["","",""]]    
    
    # Esta parte es el papá de las lógicas de menú. Según la opción que se escoja, corre una función con los parámetros
    # necesarios o simplemente cambia el valor de "seguir" a falso cuando se selecciona "salir" esto significa que el 
    # ciclo de mostrar el menú principal se interrumpe y el programa se acaba.
    seguir = True
    while seguir:
        menu_principal()
        seleccion = input()
        if seleccion.isdigit() and int(seleccion) == 1:
            data = relatos(data)
            
        elif seleccion.isdigit() and int(seleccion) == 2:
            galeria_poemas(data,poemas)

        elif seleccion.isdigit() and int(seleccion) == 3:
            galeria_coleccionables(data)

        elif seleccion.isdigit() and int(seleccion) == 4:
            tutorial()
                
        elif seleccion.isdigit() and int(seleccion) == 5:
            seguir = False
            
        else:
            console.print("[green]La selección no es válida, por favor introduce un número del 1 al 5. [/]")
            
    return data

# Algo curioso de las funciones es que no se ejecutan cuando se definen (como en todos los anteriores instantes que
# dicen "def nombre_función():") sino solamente cuando se "llaman" entonces, hasta este punto, el programa no ha hecho 
# nada más que importar las herramientas del principio, y no ha mostrado nada, pero cuando se llega a la siguiente 
# instrucción ahí si se activa la cosa, se pone bueno. Dice: "en la variable "data" guarde lo que sea que retorne la
# función "Cantos_de_sirena", y lo que sale de esa función es lo que, si se han recorrido relatos, se ha editado para
# incluir los poemas generados y los objetos encontrados. O sea, "data" se viaja todito el programa para ser cambiada 
# y mostrada y luego, cuando el lector escoge "salir", sale del reino de las funciones y se guarda en esta variable.
data = Cantos_de_sirena()
 
# Pero que se guardara en una variable no sirve para nada si se cierra el programa, así que el archivo que originalmente
# se tomó para organizar los datos de las lecturas se reescribe con los nuevos datos (poemas generados y objetos 
# encontrados) y se guarda en el computer sano y salvo, feliz y gordito.   
with open("data.json", "w") as outfile:
    json.dump(data, outfile)

# ¡Gracias por leer los comentarios! O por solo leer este comentario, no tengo cómo saber qué leíste ni te voy a juzgar 
# porque sé que es algo largo y confuso en ciertas partes. Pero espero que hayan servido para explicar el código, que 
# te hayan enseñado algo o al menos algunos hayan sido entretenidos. <3