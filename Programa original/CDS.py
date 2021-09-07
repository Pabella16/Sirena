# -*- coding: utf-8 -*-
"""
@author: Pablo Abella
"""
#Bienvenido, desocupado lector, al código que maneja a "Cantos de sirena". Lo que tenga el símbolo "#" es un comentario hecho por el autor, algunas veces con pedazos de código obsoleto que se tuvo que descartar, para dar cuenta de algunos de los problemas de desarrollo y de intenciones fosilizadas que yacen estériles como recuerdo de lo que pudo ser.

import random as random 


"""
CONSOLA - CONSOLA - CONSOLA - CONSOLA - CONSOLA - CONSOLA - CONSOLA - CONSOLA - CONSOLA - CONSOLA - CONSOLA
"""
#Normalmente, por lo menos según mi experiencia, los programas están separados en un archivo en el que está toda la interfaz de usuario, el código que se encarga de darle las opciones al usuario y de hacer al programa algo legible, y otro en el que está la lógica de fondo. Por lo que este programa se correrá en línea y no puede haber más de un archivo, simplemente habrá una sección dedicada a la consola y otra dedicada a la lógica.
def iniciar_lectura ()->None: # esta función, que es como una especie de mini programa que se puede llamar para que corra lo que está adentro en cualquier momento, inicia una nueva lectura de la colección
    print("\n"+"_"*64)
    print("="*64)
    print("{:^64}".format("CANTOS DE SIRENA"))
    print("\nUna colección interactiva de poemas (¡y cuentos!) como respuesta y reescritura de la representación del género y el deseo en _Sirena Selena, vestida de pena_ de Mayra Santos-Febres")
    # no es posible ponerle cursiva al texto que muestra Python, por lo que las palabras en cursivas aparecerán con rayas al piso alrededor así: _cursivas_
    print("="*64)
    
    input("Nota del autor: este programa es un prototipo que por ahora incluye solamente un cuento. En próximas versiones habrá un indice en este punto del programa que permitirá al lector escoger qué cuento quiere leer o si quiere acceder a una galería con los poemas que ha hecho hasta ahora. \n\nMuchas gracias estimado Mario por el ánimo, la oportunidad de experimentar con un producto como este en el espacio del seminario y por introducirme a los autores que inspiraron este proyecto, que van desde Mayra Santos Febres y Luis Negrón a Leonardo Padura, Junot Díaz, Rita Hernandez, Wendy Guerra y un mundo de salseros, merengueros y soneros. \n \nPresione ENTER para comenzar con el cuento 'Muñecas'.")
    munecas()



"""
LÓGICA - LÓGICA - LÓGICA - LÓGICA - LÓGICA - LÓGICA - LÓGICA - LÓGICA - LÓGICA - LÓGICA - LÓGICA
"""

def munecas()->None: #todo lo que está aquí adentro es el cuento y las partes que construyen al poema
    poema=[] # como todo poema, este tiene que empezar como un espacio en blanco
    print("\n"+"="*64)
    print("{:^64}".format("MUÑECAS"))
    print("="*64)
    print("\nNueva York se abre ante tus ojos como una de las primeras muestras que recibes de que el mundo es demasiado grande como para que algún día logres conocerlo realmente. En once años de vida jamás te habías sentido como cuando, por primera vez, ")

    print("\n1. te paraste en frente de un rascacielos y casi quedas tendido ahí en la calle al mirar hacia arriba.")
    print("\n2. viste a la ciudad transformarse cuando la cobijó la nieve que sentiste caer como una caricia gélida.")
    print("\n3. te deslumbraron las luces y pantallas de colores que instalaron un brillo nuevo en tus ojos.") 
    #Hasta aquí el programa solamente muestra el título, el principio del cuento y la primera decisión en la que el lector escoge una de tres opciones insertando el número de alguna.
    
    opcion_valida = False #creo una variable para representar si la opción ingresada es valida, esta va a servir para que, hasta que lo sea, le pida al lector que escoja una opción
    while not opcion_valida: #mientras que la opción no sea válida, hará todo lo que sigue. El curioso lector de este código se dará cuenta de que ninguno de los nombres de variables tiene tildes, esto es porque las letras con acentos son caracteres especiales que pueden generar errores, espero que no pase lo mismo con las cadenas de texto, es decir el cuento y los poemas en sí, pero esperaría que no.
        opcion = input("\n¿Qué opción escoges?: ") #esto le pide al usuario que introduzca una de las opciones
        if opcion != "1" and opcion != "2" and opcion != "3": # con esto me aseguro de que la opción ingresada sea 1, 2 o 3.
            print("\nDebes escoger una de las opciones posibles introduciendo un número.")
        else:
           opcion_valida = True #cuando la opción sí es válida cambia el valor de esta variable a True para frenar el ciclo que pide al lector que introduzca una opción
           preposicion = "" #esto crea la variable "preposición" para guardar cuándo debe ser "a" y cuándo debe ser "de" para el poema.
           opcion = (int(opcion),random.randint(1,2)) #el programa hace uso de "random" para generar un número aleatorio que define cúal de dos posibles versos para cada opción se escoge. 
           if opcion[0] == 1: # si la opción escogida es la primera, muestra de nuevo el texto y guarda en la lista que representa al poema los versos correspondientes a la opcion escogida, los siguientes dos condicionales hacen lo mismo para la opción 2 y la 3. Además guardan qué preposición es la apropiada de manera que después pueda ponerse en el poema.
                print("\nte paraste en frente de un rascacielos y casi quedas tendido ahí en la calle al mirar hacia arriba.")
                ednilu = "a los edificios gigantes que te hacen sentir atrapado." #de lo que el usuario escoja en esta primera decisión depende el final del cuento, que tendrá edificios, nieve o luces dependiendo de lo que se escoja.
                if opcion[1] == 1: #dependiendo de qué número aleatorio salió, se guarda un verso distinto. Estos son condicionales anidados, primero define qué opción introdujo el usuario y luego revisa qué número aleatorio se produjo y así va concretando el verso adecuado.
                    preposicion = "a"
                    poema.append("Paredes gruesas de alturas imposibles\nsostienen lejos y fuera de tu alcance")
                if opcion[1] == 2:
                    preposicion = "de"
                    poema.append("Paredes gruesas de alturas imposibles\nse alzan y te aíslan ")                    
           elif opcion[0] == 2:
                print("\nviste a la ciudad transformarse cuando la cobijó la nieve que sentiste caer como una caricia gélida.")
                ednilu = "a la nieve cayendo pesada, cruel e indiferente."
                preposicion = "a"
                if opcion[1] == 1:
                    poema.append("Capas de nieve espesa e intransitable\ncubren, borran y asfixian")
                if opcion[1] == 2:
                    poema.append("Capas de nieve espesa e intransitable\ntragan tus pies e impiden el camino")
           else:
                print("\nte deslumbraron las luces y pantallas de colores que instalaron un brillo nuevo en tus ojos.")
                ednilu = "los destellos de neón que vuelven todo borroso."
                preposicion = "de"
                if opcion[1] == 1:
                    poema.append("Primero titila, luego muere\nla luz que revelaba una esperanza\ny en lo oscuro solo queda el olvido")
                if opcion[1] == 2:
                    poema.append("Primero titila, luego muere\nel brillo del asombro en ojos grandes\ny en lo oscuro solo queda el olvido")
           
           input("Presiona ENTER para continuar.") # esto es simplemente una pausa en el programa para que no se muestre todo el texto repentinamente
    
    print("\nPero esta noche tu hermana escogió a donde iban, por lo que, en vez de ir a la tienda de juguetes gigantesca, que tiene hasta una rueda de la fortuna adentro y un ferrocarril suspendido con un trencito de juguete que la recorre como si fuera la mismísima fábrica de Papá Noel, van a una de magnitud similar pero sola y exclusivamente de muñecas. Como todo sitio por el que han pasado hasta ahora, la tienda es otra pequeña ciudad contenida dentro de la gran ciudad, con una peluquería para las niñas y sus muñecas, con tiendas de ropa para las niñas y sus muñecas, y con juguetes y accesorios como los que tienen las niñas pero del tamaño de las muñecas. Y allá van las niñas con sus muñecas que tienen exactamente su misma cara, su misma piel y su mismo pelo a comprarles todo lo que tienen de verdad, como los útiles del colegio y el celular, y también lo que no tienen o sueñan tener, como un carro o un caballo.")
    input("Presiona ENTER para continuar.")
    print("\nLas niñas que aún no tienen muñeca, como tu hermana, van a depositar su imagen, sus sueños y su alma en aquellos montoncitos de plástico y poliéster. Aquí las niñas se hacen muñecas y las muñecas se hacen niñas. Tu hermana dice que esto les da el famoso título de “American Girls”. Tu hermana aún no es una de ellas, pero ese día va a ")
    
    print("\n1. completar esa transformación.")
    print("\n2. comenzar esa transformación.")
    print("\n3. pretender esa transformación.")
    
    opcion_valida = False 
    while not opcion_valida: #cada montón de estos que comienza con "while" es bastante parecido al primero y tiene la misma función de recibir la decisión del jugador, mostrarla cuando la toma, e ir construyendo por detrás el poema para poder mostrarlo al final
        opcion = input("\n¿Qué opción escoges?: ") 
        if opcion != "1" and opcion != "2" and opcion != "3":
            print("\nDebes escoger una de las opciones posibles introduciendo un número.")
        else:
           opcion_valida = True
           opcion = int(opcion)
           if opcion == 1:
                print("\ncompletar esa transformación.")
                if preposicion == "a":
                    poema.append("al sueño de ser de aquellos cuerpos\nhechos de polvo de estrella.")
                elif preposicion == "de":
                    poema.append("del sueño de ser de aquellos cuerpos\nhechos de polvo de estrella.")
           elif opcion == 2:
                print("\ncomenzar esa transformación.")
                if preposicion == "a":
                    poema.append("a la promesa de vivir en la inocencia\nque no acaba y siempre se renueva.")
                elif preposicion == "de":
                    poema.append("de la promesa de vivir en la inocencia\nque no acaba y siempre se renueva.")
           else:
                print("\npretender esa transformación.")
                if preposicion == "a":
                    poema.append("al juego inofensivo \nde ser muchas voces \ny una sola canción.")
                elif preposicion == "de":
                    poema.append("del juego inofensivo \nde ser muchas voces \ny una sola canción.")
                        
           input("Presiona ENTER para continuar.")
    
    print("\nTal vez por eso el proceso se parece tanto a lo que tú y tu familia tuvieron que hacer en el aeropuerto. Hay que tomarse fotos, intercambiar documentos, leer folletos, seguir instrucciones y dar información de origen, identidad e intención. Mientras tu hermana lo hace, miras a tu alrededor, pero te sientes observado. Decenas de ojos de girls y sus moms te miran al pasar y sabes que se preguntan qué haces ahí si no es hacerte muñeca. Piensas en tus amigos y en lo importante que es que no se enteren nunca en la vida de que pasaste por ese sitio. No sabrías cómo explicarlo, cómo justificarte, como tampoco sabrías explicar la manera en que tu mirada salta entre los artículos de exhibición y se detiene sobre ")
    print("\n1. el parecido entre las sonrisas de las muñecas y las de sus dueñas, que aparecen en fotos al lado de cada muñeca.")
    print("\n2. los kits de maquillaje para las niñas, y los kits de juguete para las muñecas.")
    print("\n3. la ropa que venden para las niñas y las pequeñas versiones para muñecas.")
    
    opcion_valida = False 
    while not opcion_valida: 
        opcion = input("\n¿Qué opción escoges?: ") 
        if opcion != "1" and opcion != "2" and opcion != "3":
            print("\nDebes escoger una de las opciones posibles introduciendo un número.")
        else:
           opcion_valida = True
           opcion = int(opcion)
           if opcion == 1:
                print("\nel parecido entre las sonrisas de las muñecas y las de sus dueñas, que aparecen en fotos al lado de cada muñeca.")
                enfoque = "las sonrisas" #¿qué es esto? ¿una variable nueva? Así es, y sirve para que en el cuento aparezca la opción que el usuario haya escogido. Cuando el personaje piensa en lo que estaba mirando, aparecerá lo que se escogió.
                poema.append("La dicha impresa en un rostro\nque a sí mismo se ha dibujado")
           elif opcion == 2:
                print("\nlos kits de maquillaje para las niñas, y los kits de juguete para las muñecas.")
                enfoque = "el maquillaje"
                poema.append("La máscara cambiante que haría\na una vida un carnaval")
           else:
                print("\nla ropa que venden para las niñas y las pequeñas versiones para muñecas.")
                enfoque = "la ropa"
                poema.append("La imagen que tejiste en tus adentros\nde tu autenticidad replicada")
                        
           input("Presiona ENTER para continuar.")
    
    print("\nTe das cuenta de que alguien podría pensar que te interesa lo que estás mirando e intentas fingir distracción mientras sigues pensando en {} y en lo mucho que se asemeja la versión real a la de juguete. Tomas el folleto en frente tuyo disimulando indiferencia y aburrimiento pero registrando mentalmente las prendas anunciadas. Montones de parejas de niñas y muñecas disfrazadas igual se esparcen por páginas moradas y sigues revisando con curiosidad los trajes de doctoras y de surfistas, los pijamas y vestidos elegantes. En las últimas páginas del folleto las páginas tienen un fondo azul y te das cuenta de que las muñecas ahora son muñecos, y usan camisas con pantalones elegantes, y aparecen niños vestidos igual. Ves que aparece la misma marca en la parte superior de cada hoja y te preguntas si igual se llamarían “American Girls” o qué pasaría entonces. Y si consiguieras uno ¿también podrían vestirse igual? ¿tener las mismas cosas? ¿qué pasaría si le pusieras la ropa de la de tu hermana? ¿eso se puede? Te quedas enfrascado en tus pensamientos y no notas que tu hermana terminó de diseñar su muñeca. Para cuando te das cuenta es muy tarde, tu padre ya te ha visto con los ojos fijos en las páginas azules y te sorprende al preguntarte con tono de burla si los muñecos te gustan.".format(enfoque)) #En este montón de texto aparece lo que el usuario haya escogido en la decisión anterior, lo interesante es que es un cambio que puede ser difícil de detectar, pues son solo un par de palabras y lo lógico es que aparezca lo que uno escogió, así que cuando sucede el lector no le pone mucho misterio, pero esto, me parece, lo hace aún más interesante y, de hecho, me da la idea de cambiar el final del cuento, lo que haré en este momento.
    input("Presiona ENTER para continuar.")
    print("\n	-¿Quere que le conshiga el shuyo como a shu hermanita? \nHablándote de “usted” como a veces lo hacía, como si hablara de ti en tercera persona, como si no estuvieras ahí, y con voz infantil, apunta a uno. \n	-¿Qué tal ese? ¡Son igualiticos! \nSientes clavarse como una espina dentro de ti el sarcasmo con el que lo dice y su sonrisa maliciosa es como una cachetada que amarra con fuerza un nudo en tu garganta. Te estruja demasiado fuerte contra él como si hicieras parte del chiste y se voltea hacia el resto de tu familia como diciendo “Nos vamos”, por lo que no ve cómo comienzan a aguarse tus ojos mientras")
    
    print("\n1. dejas caer el folleto ")
    print("\n2. guardas el folleto en tu bolsillo ")
    print("\n3. devuelves el folleto a su lugar ")
    
    opcion_valida = False 
    while not opcion_valida: 
        opcion = input("\n¿Qué opción escoges?: ") 
        if opcion != "1" and opcion != "2" and opcion != "3":
            print("\nDebes escoger una de las opciones posibles introduciendo un número.")
        else:
           opcion_valida = True
           opcion = int(opcion)
           if opcion == 1:
                print("\ndejas caer el folleto y ves por la ventana {}".format(ednilu)) # cada final usa "format" para remplazar "{}" con una imagen de nieve, edificios o luces que se determinó al principio, con la primera decisión del lector.
                poema.append("es sepultada bajo el dolor \ndel sueño que muere ahogado.")
           elif opcion == 2:
                print("\nguardas el folleto en tu bolsillo y ves por la ventana {}".format(ednilu))
                poema.append("queda esperando tu regreso \nen un secreto que tomas prestado.")
           else:
                print("\ndevuelves el folleto a su lugar y ves por la ventana {}".format(ednilu))
                poema.append("vuelve a perderse en el silencio \nde las páginas de un libro cerrado.")
           
           
           input("\nPresiona ENTER para terminar el cuento y ver tu poema.")
    
    print("\n") #aquí aparece el poema mostrando una a una cada parte que se fue guardando en la lista a medida que se determinó con lo que escogió el lector
    print(poema[0])
    print(poema[1])
    print("\n")
    print(poema[2])
    print(poema[3])



iniciar_lectura() #esto hace que comience el programa corriendo la primera función, que muestra el título de la colección. Es bonito que tenga que leer todo el código primero para ahí sí correrlo e iniciar la lectura.
