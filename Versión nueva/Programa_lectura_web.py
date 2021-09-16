# -*- coding: utf-8 -*-
"""
Sept. 2021

@author: Pablo Abella
"""

# Primero que todo hay que invitar a JSON porque sin él no es una fiesta. Con esta instrucción traigo toda la 
# lógica escondida que maneja el tipo de archivo JSON, en el que estoy escribiendo los relatos. Escribirlos en 
# JSON me permite dejarlos previamente estructurados de manera que el programa "converse" con el relato y sepa
# navegarlo. ¡Así puedo escribir muchos relatos con la misma estructura y manejarlos todos con el mismo programa
# en vez de hacer un programa para cada relato! ¡Las maravillas de la tecnología! Solo tendría que devolverme a
# este único programa y cambiar lo que haga falta si decido complicarme la vida cambiando la estructura.

# Nota: Como esta es la versión Web no se usa nada de JSON, pero dejo el anterior comentario para dar cuenta de cómo
# funciona en la versión normal. La versión normal abre el archivo JSON y lo lee sin necesitar incluirlo en el programa.
import json
# random me permite escoger algunos datos aleatoriamente, lo que uso para armar los poemas y darles más variedad.
import random as random 

# Esta es la versión de lectura Web, que no tiene el relato separado, de manera que es simplemente copiar el código,
# que ahora incluye el relato, y correrlo en cualquier compilador en línea.
relato= [

  {
    "comentario":"Hay cinco tipos de texto en este archivo de JSON: 'titulo' (TI), 'texto único' (TU), 'decisión'(DE), 'texto dependiente'(TD) y FIN. Todos son objetos de JSON e incluyen su tipo entre sus características. El programa sabe qué hacer con cada elemento de este archivo JSON dependiendo del tipo que tiene registrado. Todo elemento tendrá un 'tipo', un 'índice', que indique su posición en la lista, un 'siguiente' que indique qué elemento le sigue, y un 'contenido'. También pueden tener dentro de sí un 'comentario' sobre esa sección. En el caso del título también incluí 'poema', que le dice al programa desde el principio cuantas secciones tiene el poema que se va a armar.",
    "tipo": "TI",
    "indice": 0,
    "contenido": "MUÑECAS",
    "poema": ["","","",""],
    "siguiente": 1
  },

  {
    "comentario":"Este archivo en particular funciona como una lista de las secciones del relato. Es un arreglo de objetos de JSON. ¿Qué rayos significa eso? Pues un arreglo es básicamente una lista que puede contener cualquier otro tipo de dato separado por comas, incluso más listas, y un objeto es una serie de claves (títulos o categorías) con valores correspondientes; se organizan con dos puntos (clave:valor) y también se separan por comas. Los objetos de JSON se escriben entre corchetes {}, y los arreglos entre paréntesis cuadrados []. Es posible que me refiera a los arreglos como 'listas' y a los objetos como 'diccionarios', pues estos son los equivalentes en Python. La mejor manera de pensarlos es como un directorio telefónico, el directorio es el arreglo (lista) de objetos, y cada objeto es un contacto con toda la información organizada. Se ven así:\n \n[{“nombre”:“Pablo”, “apellido”:“Abella”, “número”: 123456789, “país”: “Colombia”}, {“nombre”:“Mayra”, “apellido”:“Santos-Febres”, “número”: 987654321, “país”: “Puerto Rico”}] \n \nEsto sería un directorio [arreglo] con dos contactos {objetos}, cada uno con su serie de parejas de clave:valor. El lenguaje permite anidar objetos y arreglos entre sí, es decir puede haber un arreglo de arreglos o un objeto con más objetos adentro, o un arreglo con objetos con objetos con arreglos con arreglos con… ¿De qué hablaba? Ah, sí. Todo esto permite que el cuento se vuelva más o menos inteligente. A medida que construya el relato en este JSON, incluiré explicaciones sobre cómo está organizado.",
    "tipo": "TU",
    "indice": 1,
    "contenido": "Nueva York se abre ante tus ojos como una de las primeras muestras que recibes de que el mundo es demasiado grande como para que algún día logres conocerlo realmente. Cada día te sorprende más que el anterior. Montaste en metro subterráneo, diste vueltas por Central Park sobre una carroza jalada por caballos, patinaste sobre hielo, conociste la tienda de chocolates más grande que has visitado y viste esqueletos de dinosaurios tan altos que parecían tocar los techos altísimos del museo de historia natural. Pero ni eso ni ninguna otra experiencia de tus once años de vida se compara a cómo te sentiste cuando",
    "siguiente": 2
  },

  {
    "comentario":"En 'contenido' cada decisión tendrá el número de la decisión ('num'), el texto en sí de ese camino ('opción'), el número del detalle que debe aparecer en el texto más adelante según la decisión ('detalle'), si el ususario debe ingresar texto o no ('input'), el respectivo verso de esa decisión, que puede tener más de una versión, ('verso') y el elemento al que se debe pasar desde esa decisión ('siguiente'). Es importante que el 'siguiente' sea una propiedad de cada decisión particular puesto que algunas necesariamente llevan por diferentes caminos. La clave 'verso' a su vez es un arreglo de objetos pues puede haber diferentes versiones posibles de un verso, y hace falta anotar la preposición que esa versión exigiría para mantener la lógica gramática con el siguiente verso al igual que la parte del poema a la que corresponde. Por fuera de 'contenido' también está 'repetir' que guarda la frase que debe repetirse con la respuesta escogida para darle fluidez a la lectura.",
    "tipo": "DE",
    "indice": 2,
    "repetir":"Pero ni eso ni ninguna otra experiencia de tus once años de vida se compara a cómo te sentiste cuando",
    "contenido": [
      {
        "num": 1,
        "opción": "te paraste en frente de un rascacielos y casi quedas tendido ahí en la calle al mirar hacia arriba.",
        "detalle": 1,
        "input":"",
        "verso": [{"v":"Paredes gruesas de alturas imposibles\nalejan de ti", "preposición":2, "parte":1},{"v":"Paredes gruesas de alturas imposibles\nse alzan y te aíslan","preposición":1, "parte":1}
        ],
        "siguiente": 3
      },
      {
        "num": 2,
        "opción": "viste a la ciudad transformarse cuando la cobijó la caricia gélida de la primera nevada de tu vida.",
        "detalle": 2,
        "input":"",
        "verso": [{"v":"Capas de nieve espesa e intransitable\ncubren, borran y asfixian", "preposición":2, "parte":1},{"v":"Capas de nieve espesa e intransitable\ntragan tus pies e impiden el camino", "preposición":1, "parte":1}
        ],
        "siguiente": 3
      },
      {
        "num": 3,
        "opción": "te deslumbró el universo de luces y pantallas de colores que instaló un brillo nuevo en tus ojos.",
        "detalle": 3,
        "input":"",
        "verso": [{"v":"Primero titilan, luego mueren\nlas gotas de luz\ny en lo oscuro solo queda olvidar", "preposición":2, "parte":1},{"v":"Primero titila, luego muere\nel brillo del asombro en ojos nuevos\ny en lo oscuro solo queda olvidar","preposición":2, "parte":1}
        ],
        "siguiente": 3
      }
    ] 
  },

  {
    "comentario":"El TD o 'texto dependiente' incluye un detalle que depende de una decisión anterior. Por eso tiene más categorías dentro de 'contenido'. El 'fijo' es el texto que no cambia, y la 'variación', el arreglo, es el texto que cambia.",
    "tipo": "TD",
    "indice": 3,
    "contenido": {
      "fijo":"Te sentiste ligero y diminuto ante el espectáculo, como si flotaras ",
      "variación":["y el vértigo te elevara hacia la punta del edificio. ", "con la misma suavidad y elegancia de los copos de nieve. ", "en un mar de neón. "]
    },
    "siguiente": 4
  },

  {
    "tipo": "TD",
    "indice": 4,
    "contenido": {
      "fijo":"Nació en ti una nueva fascinación, una sensación de estarte renovando. \n\n   Ahora sueñas con visitar una tienda de juguetes gigantesca que viste antes de pasada. Desde afuera se veía una rueda de la fortuna en medio de la tienda, un ferrocarril suspendido con un trencito de juguete recorriéndola como si fuera la mismísima fábrica de Papá Noel y pisos al parecer interminables llenos de marcas de juguetes que ni sabías que existían. Algo te dice que conocerla por dentro incluso podría superar haber visto ",
      "variación":["el rascacielos.\n\n", "la nieve.\n\n", "la iluminación de los avisos en Times Square.\n\n"]
    },
    "siguiente": 5
  },

  {
    "tipo": "TU",
    "indice": 5,
    "contenido": "    Sin embargo, esta noche tu hermana escogió el destino. Por eso, en vez de ir a una tienda inmensa de juguetes tú y tu familia van a una tienda inmensa pero sola y exclusivamente de muñecas. Es una pequeña ciudad contenida dentro de la gran ciudad. Tiene una peluquería para las niñas y sus muñecas, tiendas de ropa para las niñas y sus muñecas, y juguetes y accesorios como los que tienen las niñas pero del tamaño de las muñecas. Es a donde van las niñas con muñecas que tienen exactamente su misma cara, su misma piel y su mismo pelo a comprarles todo lo que tienen de verdad, una silla de ruedas, los útiles del colegio o el celular, y también lo que no tienen o sueñan tener, como un carro o un caballo. Las niñas que aún no tienen muñeca, como tu hermana, van a depositar su imagen, sus sueños y su alma en aquellos montoncitos de plástico y poliéster. Aquí las niñas se hacen muñecas y las muñecas se hacen niñas. \n\n   -“Son American Girls”, te dice tu hermana. \n\n   Ella aún no es una American Girl, pero ese día va a… ¿completar esa transformación? ¿comenzarla? ¿o solamente a pretenderla? No sabes exactamente cuál es el resultado, porque además ustedes vienen de Colombia y eso a veces complica las cosas.",
    "siguiente": 6

  },

  {
    "tipo": "TU",
    "indice": 6,
    "contenido": "    El proceso se parece a lo que tú y tu familia tuvieron que hacer en el aeropuerto. Hay que tomarse fotos, intercambiar documentos, leer folletos, seguir instrucciones, dar información de origen, identidad e intención y pagar, claro. Mientras tu hermana lo hace, miras a tu alrededor, pero te sientes observado. Montones de ojos de girls y sus moms te miran al pasar y sabes que se preguntan qué haces ahí si no es hacerte muñeca. Piensas en tus amigos y en lo importante que es que no se enteren nunca en la vida de que pasaste por ese sitio. No sabrías cómo explicarlo, cómo justificarte, como tampoco sabrías explicar la manera en que tu mirada salta entre los artículos de exhibición y registra con cuidado",
    "siguiente": 7
  },

  {
    "tipo": "DE",
    "indice": 7,
    "repetir":"tu mirada salta entre los artículos de exhibición y registra con cuidado",
    "contenido": [
      {
        "num": 1,
        "opción": "las fotografías de niñas sonrientes acompañadas de muñecas.",
        "detalle": 0,
        "input":"",
        "verso": [{"v":"La alegría impresa en un rostro\nque a sí mismo se ha dibujado", "preposición":0, "parte":3}],
        "siguiente": 8
      },
      {
        "num": 2,
        "opción": "los kits de maquillaje para las niñas y los kits de juguete para las muñecas.",
        "detalle": 0,
        "input":"",
        "verso": [{"v":"La máscara cambiante que haría\na la vida un carnaval", "preposición":0, "parte":3}],
        "siguiente": 8
      },
      {
        "num": 3,
        "opción": "la ropa que venden para las niñas y las versiones pequeñas para muñecas.",
        "detalle": 0,
        "input":"",
        "verso": [{"v":"La imagen que tejiste en tus adentros\nde tu autenticidad replicada", "preposición":0, "parte":3}],
        "siguiente": 8
      }
    ]
  },

  {
    "tipo": "TU",
    "indice": 8,
    "contenido": "Te das cuenta de que alguien podría pensar que te interesan demasiado e intentas fingir indiferencia mientras sigues recorriendo el espacio a tu alrededor con la mirada. Ves uniformes de doctora, trajes de surfista, pijamas y vestidos elegantes esparcidos por un panorama cubierto por todos lados con el color magenta de la marca. Sientes que todo es demasiado rosado, demasiado otro, y que estás contemplando un mundo que no es para ti. Entonces tu recorrido visual te lleva a una muñeca con el pelo corto y frenas en seco. Tras examinarla un poco más te das cuenta que parece ser un niño, lo que la haría un muñeco en vez de una muñeca ¿o no? No ves que diga “niño” en ninguna parte y su ubicación tampoco te dice nada, pues está al lado de una muñeca pelilarga como cualquier otra. Dudas. Tiene puesta una camiseta polo de rayas y unos pantalones beige sueltos a diferencia de todas las demás, que usan faldas y vestidos. No puede ser una coincidencia que además tenga el pelo corto. Tiene que ser una American Boy, o sea, un American Boy. Te quedas mirándolo y te preguntas: ¿te conseguirían uno? ¿podrías vestirlo igual a ti? Nunca habías pensado realmente en tu ropa, siempre has usado la ropa que alguien más ya ha escogido para ti. \n\n    Ves a tu American Boy atrapado dentro de la vitrina vestido con la única ropa de niño que parece haber en toda la tienda. No sabes si se supone que lo vistas con las prendas que tienes a tu alrededor ¿le quedaría la ropa de la muñeca de tu hermana? Sientes que te llaman y te sacan de dentro de tu cabeza. Te quedas congelado por un momento. No puedes evitar sentir pena y hasta miedo de que te hayan descubierto en el trance en el que estabas. Al parecer te salvaste, solamente te avisan que tu hermana terminó de diseñar su muñeca y que la siguiente parada es el American Girl Café. Te diriges hacia allá con tu familia.",
    "siguiente": 9
  },

  {
    "tipo": "TU",
    "indice": 9,
    "contenido": "El restaurante te parece feo. Rayas blancas y negras bajan por las paredes y continúan sobre las cortinas recogidas encima de las ventanas. Ciertas secciones de los muros rompen el patrón con acentos y decoraciones del mismo color magenta que te ha perseguido toda la tienda. Las sillas son grandes y acolchadas, de un color morado oscuro decorado con filas de pepitas rosadas y hay demasiadas mesas para un espacio tan pequeño. Te sientes atrapado. Ves una cajita en medio de la mesa y la abres por curiosidad, como si fueras Alicia en el país de las maravillas, pero, en vez de pastelillos con la palabra “CÓMEME”, está llena de tarjetitas con temas de conversación. Algunas tienen manchas de la comida de clientes anteriores, pero leerlas es una buena manera de pasar el tiempo. La primera que sacas dice “What is your earliest memory?” Intentas entender: “early” significa temprano ¿o sea pregunta por tu primer recuerdo de esa mañana? ¿o por tu recuerdo más reciente? Sería una pregunta muy boba, tiene que ser por tu recuerdo más antiguo. Tienes que pensarlo por un momento, organizar tus recuerdos e intentar reconocer cuáles podrías estarte inventando. Decides que tu primer recuerdo ",
    "siguiente": 10
  },

  {"comentario":"aunque no definen una parte siguiente, es importante que los versos en esta decisión vuelvan a decir su preposición, pues al pasarlos el programa la registra como cero de lo contrario, y si se usa la siguiente opción para volver esto puede generar un error gramatical en el que no se usa la preposición correcta sino que se escoge aleatoriamente.",
    "tipo": "DE",
    "indice": 10,
    "repetir":"Decides que tu primer recuerdo",
    "contenido": [
      {
        "num": 1,
        "opción": "es una mezcla confusa de imágenes de tu jardín infantil: las manualidades, los juegos en los descansos y las izadas de bandera.",
        "detalle": 0,
        "input":"",
        "verso": [{"v":"del sueño de ser de aquellos cuerpos\nhechos de polvo de estrella.\n", "preposición":1, "parte":2},{"v":"el sueño de ser de aquellos cuerpos\nhechos de polvo de estrella.\n","preposición":2, "parte":2}],
        "siguiente": 12
      },
      {
        "num": 2,
        "opción": "es una de tus primeras navidades, cuando tus papás te regalaron unos carritos tallados en madera.",
        "detalle": 0,
        "input":"",
        "verso": [{"v":"de la promesa de vivir en la inocencia.\n", "preposición":1, "parte":2},{"v":"la promesa de vivir en la inocencia.\n","preposición":0, "parte":2}],
        "siguiente": 12
      },
      {
        "num": 3,
        "opción": "es difícil de escoger, así que te esfuerzas un poco más, intentando que se te ocurra algo distinto.",
        "detalle": 0,
        "input":"",
        "verso": [{"v":"del juego inofensivo\nde ser muchas voces\ny una sola canción.\n", "preposición":1, "parte":2},{"v":"el juego inofensivo\nde ser muchas voces\ny una sola canción.\n","preposición":2, "parte":2}],
        "siguiente": 11
      }
    ]
  },

  {
    "tipo": "DE",
    "indice": 11,
    "repetir":"",
    "contenido": [
      {
        "num": 1,
        "opción": "Cierras los ojos, te concentras e intentas devolverte en tu memoria lo que más puedes, hasta determinar que _______ (ESCRIBE TU PROPIA RESPUESTA)",
        "detalle": 0,
        "input":"(ESCRIBE AQUÍ) tu primer recuerdo es: ",
        "verso": [],
        "siguiente": 12
      },
      {
        "num": 2,
        "opción": "Te concentras mucho pero es imposible recordar más, así que te decides por una de tus primeras opciones. (VUELVE A LAS OPCIONES ANTERIORES)",
        "detalle": 0,
        "input":"",
        "verso": [],
        "siguiente": 10
      }
    ]
  },

  {
    "tipo": "TU",
    "indice": 12,
    "contenido": "¡Ajá! Tiene que ser eso. Intentas anotarlo mentalmente, pues se siente como algo que no debes olvidar de ti mismo, como si en ese momento acabaras de definir quién eres.\n\n    Vas a seguir mirando las tarjetas para ver qué más te dicen de ti mismo, pero llega una mesera y les avisa que, como no traen muñeca, pueden tomar prestada una para comer junto a ella. La mesera señala hacia un lado del restaurante, donde hay mesas con filas de muñecas y sillitas que se pueden encajar en las mesas para sentarlas. No habías notado las que ya estaban puestas en otras mesas al lado de sus dueñas, con plato y taza propios. Descubres tres muñecos de pelo corto entre las muñecas, vestidos como el que antes habías encontrado. Tu hermana se levanta a escoger su muñeca y tú resuelves ",
    "siguiente": 13
  },

  {
    "tipo": "DE",
    "indice": 13,
    "repetir":"Tu hermana se levanta a escoger su muñeca y tú resuelves",
    "contenido": [
      {
        "num": 1,
        "opción": "quedarte mirando desde la mesa para ver cuáles hay y cuál escoge.",
        "detalle": 0,
        "input":"",
        "verso": [{"v":"es sepultada bajo el dolor\ndel sueño que muere ahogado.", "preposición":0, "parte":4}],
        "siguiente": 14
      },
      {
        "num": 2,
        "opción": "acompañarla y ver las muñecas más de cerca.",
        "detalle": 0,
        "input":"",
        "verso": [{"v":"queda esperando tu regreso\nen un secreto que tomas prestado.", "preposición":0, "parte":4}],
        "siguiente": 15
      },
      {
        "num": 3,
        "opción": "desviar la mirada y volverte a concentrar en las tarjetas.",
        "detalle": 0,
        "input":"",
        "verso": [{"v":"vuelve a perderse en el silencio\nde las páginas de un libro cerrado.", "preposición":0, "parte":4}],
        "siguiente": 17
      }
    ]
  },

  {
    "tipo": "TU",
    "indice": 14,
    "contenido": "Tu hermana revisa las muñecas cuidadosamente. La ves revisando los diferentes atuendos, tipos de pelo y estilos. Notas la variedad de colores en la ropa, que contrasta con la monotonía de la ropa de los muñecos, que aparentemente tu hermana ni considera. Entre ellos hay uno que se parece a ti. Ves a tu hermana escoger una muñeca de pelo negro, con un saco rosado, blue jeans y botas. Se devuelve con ella a la mesa. ",
    "siguiente": 21
  },

  {
    "tipo": "TU",
    "indice": 15,
    "contenido": "    Te levantas y sin darte cuenta te guardas la tarjetita que estabas leyendo en el bolsillo en vez de devolverla a la caja. Vas con tu hermana aunque no parece estar muy contenta de que la acompañes. Puedes ver los atuendos de las muñecas detalladamente. La mayoría son rosados, pero hay algo de variedad. Algunas usan pantalones, otras faldas y otras vestido. También tienen diferentes peinados, colores de pelo y tonos de piel. Tu hermana parece preferir una de pelo negro con blue jeans, saco rosado y botas. Tiene el saco puesto al revés, de manera que la capucha le queda en cambio como un babero. Ves a tu hermana revisar si se le puede quitar para ponérselo correctamente antes de llevársela. Le muestras una que tiene un vestido azul claro con flores blancas y rojas y unos zapatos negros con medias rojas. Te parece linda. \n\n   -“No me gusta,” te responde simplemente. ",
    "siguiente": 16
  },

  {
    "tipo": "TU",
    "indice": 16,
    "contenido": "    Intentas convencerla diciéndole que el castaño claro de su pelo es más parecido al de esta que al de la otra. \n\n   -“No quiero una con vestido. Llévala tú si quieres pero yo no la quiero llevar,” te dice, y se va con la muñeca de pelo negro, dejándote solo con las filas de muñecas. \n\n   No te la vas a llevar, pero miras a los tres muñecos. Su ropa se ve aburrida en comparación a la diversidad de la de las muñecas, pero uno de ellos tiene tu mismo tono de piel y color de pelo. Consideras por un instante devolverte con él a la mesa. Te atrae su materialidad, la posibilidad de tocarlo, su existencia por fuera de la vitrina. Descartas rápidamente la idea, estás imaginando cosas imposibles. Vuelves a la mesa antes de que sea demasiado sospechoso. ",
    "siguiente": 21
  },

  {
    "tipo": "TU",
    "indice": 17,
    "contenido": "    Sacas la siguiente tarjeta. “If you owned a horse, what would you name it?” Esperabas una pregunta un poco más profunda, y además no te gustan los caballos. Piensas y recuerdas que en la finca de tu abuelo tienen uno llamado Topacio. Es el nombre perfecto para un caballo. Decides que lo llamarías igual. Siguiente tarjeta. “What is your very favorite sandwich combination?” Esta te da un poco más en qué pensar, pero en realidad no sueles ponerle nada distinto que jamón y queso a tus sándwiches. Entre más verduras menos te gustan y tampoco conoces más variedades. “Would you rather vacation on the beach or in the mountains?” Comienzas a aburrirte.  ",
    "siguiente": 18
  },

  {
    "tipo": "TU",
    "indice": 18,
    "contenido": "    Entonces tu hermana vuelve con la muñeca que escogió y cuelga la silla en la mesa. Intentas aprovechar los temas de conversación y hacerle las preguntas a tu familia pero no les interesa. Tus papás quieren tomarle fotos a tu hermana y planear qué harán los días que les quedan en Nueva York. Te quedas solo con tus tarjetitas y pasas algunas más que te parecen aburridas o que no sabes cómo responder. Entonces comienzan a repetirse, y vuelves a encontrar la primera que sacaste. “What is your earliest memory?” Decides  ",
    "siguiente": 19
  },

  {
    "tipo": "DE",
    "indice": 19,
    "repetir":"Decides",
    "contenido": [
      {
        "num": 1,
        "opción": "devolver todas las tarjetas y dejar de leerlas.",
        "detalle": 0,
        "input":"",
        "verso": [],
        "siguiente": 20
      },
      {
        "num": 2,
        "opción": "devolver todas las tarjetas excepto esa y te la guardas en el bolsillo.",
        "detalle": 0,
        "input":"",
        "verso": [],
        "siguiente": 20
      }
    ]
  },

  {
    "tipo": "TU",
    "indice": 20,
    "contenido": "    El resto de la comida pasa de manera ordinaria. Intentas convencer a tus papás de que vayan a la tienda de juguetes, pero están concentrados en buscar una iglesia cercana que valga la pena visitar. Qué aburrimiento. Ya más bien quieres volver al hotel. ",
    "siguiente": 24
  }, 

  {
    "tipo": "TU",
    "indice": 21,
    "contenido": "    -“¿Quere que le conshiga el shuyo como a shu hermanita?” Te sorprende tu papá al preguntarte con burla. \n\n    Hablándote de “usted” como a veces lo hace, como si hablara de ti en tercera persona, como si no estuvieras ahí, y con voz infantil, apunta hacia las muñecas. \n\n    -“¿Qué tal ese? ¡Son igualiticos!” ",
    "siguiente": 22
  },

  {
    "tipo": "TD",
    "indice": 22,
    "contenido": {
      "fijo":"Sientes clavarse dentro de ti el sarcasmo con el que lo dice y su sonrisa maliciosa es como una cachetada que amarra con fuerza un nudo en tu garganta. Te estruja demasiado fuerte contra él como si hicieras parte del chiste. Te volteas hacia las ventanas para que no vea cómo se te comienzan a aguar los ojos. Te sientes vulnerable y observado, como si todas las mesas a tu alrededor supieran que no perteneces allí. Sientes que odias las cosas de niñas, odias a las muñecas y más aún a los muñecos. Intentas fijarte en lo que se ve por fuera de las ventanas, más allá de las líneas blancas y negras de las paredes, y solamente logras ver ",
      "variación":["los edificios gigantes que te hacen sentir atrapado.", "la nieve cayendo pesada, cruel e indiferente.", "los destellos de neón que vuelven todo borroso."]
    },
    "siguiente": 23
  },

  {
    "tipo": "TU",
    "indice": 23,
    "contenido": "",
    "siguiente": 24
  },

  {
    "tipo": "FIN",
    "indice": 24,
    "contenido": "FIN",
    "siguiente": 25
  }

] 


# Hace falta inicializar la variable "preposicion", pues es una herramienta sorpresa que nos ayudará más tarde.
preposicion = 0

# Esta pequeña instrucción es, básicamente, lo que pasa las páginas. Es un ciclo que dice "mientras que no se haya
# pasado el número de elementos que hay en el relato, siga leyendo". Dentro de él se recorren todas las partes del
# relato, que pueden ser "título", "texto único", "decisión" o "texto dependiente". Cada una significa un set 
# diferente de instrucciones.
elemento = 0
while elemento < len(relato):
    # Decidí darle un color verde claro muy ameno a las "instrucciones" que muestra el programa, como cuando se 
    # debe presionar Enter para continuar o se debe ingresar un número. La siguiente instrucción reestablece el 
    # color del texto para que no se vuelva todo verde. Creo que esto ayuda a diferenciar una parte de la otra 
    # y ayuda a ubicarse en el texto que va apareciendo. Esas instrucciones son como otra voz además del relato
    # y del programa/comentarios. ¡Cuánta polifonía! 
    print("\033[1;37;m",end="")

    # Si la sección referenciada es un título pues... muestra el título ¿qué más esperabas? Mentira, hace algo
    # más, crea de una el poema como una lista vacía con el número de elementos correcto.
    if relato[elemento]["tipo"] == "TI":
        # Recibe el título del JSON y lo formatea bien bonito entre dos filas de signos de igualdad.
        titulo = relato[elemento]["contenido"]
        print("\n"+"="*64)
        print("{:^64}".format(titulo))
        print("="*64)
        # Como todo poema, este tiene que empezar con un espacio en blanco. Excepto que este espacio en blanco 
        # tiene ya definido en cuántas partes está dividido el poema. El programa recibe una lista vacía del 
        # tamaño que tendrá el poema desde el una de las propiedades del título en el JSON. Esto permite armar
        # la lista con antelación para definir el número de partes y simplemente editarlas en su momento (en vez
        # de ir armando el poema bloque por bloque, que ya no me funciona porque, como una de las opciones permite
        # devolverse a otra decisión, una parte del poema se añadiría más de una vez.
        poema = relato[elemento]["poema"]
        # la siguiente instrucción toma de la sección que se está revisando el índice en la lista de la sección
        # que sigue, así se navega el cuento como debe ser, serpenteando según la voluntad del lector.
        elemento = relato[elemento]["siguiente"]
        input("\033[1;32;mENTER PARA CONTINUAR\n")
        
    # Ahora sí, sí es texto único solamente lo muestra y no pasa más na'    
    elif relato[elemento]["tipo"] == "TU":
        print(relato[elemento]["contenido"])
        elemento = relato[elemento]["siguiente"] 
        input("\033[1;32;mENTER PARA CONTINUAR\n")
    
    # En cambio, sí la sección es una decisón se pone bien peliaguda la cosa. Hay que mostrar las opciones,
    # permitir que se escoja una de ellas y regañar si se ingresa un valor inválido, registrar si tiene un 
    # efecto en el texto más adelante, guardar el verso que la decisión implica en el poema y mandar la 
    # lectura pa' donde debe seguir según la decisión escogida.
    elif relato[elemento]["tipo"] == "DE":
       
        for opcion in relato[elemento]["contenido"]:  # muestra las opciones bonitas y ordenadas.
            print(str(opcion["num"])+". "+opcion["opción"] + "\n")
            # También es posible la siguiente manera, que crea variables para "num" y "opcion" y usa f string
            # por ahora no he aprovechado f string porque no he podido leer la referencia al respecto, así que
            # me he mantenido con mi técnica a la antigua. Más adelante revisaré y corregiré con f string.
            # num = str(opcion["num"])
            # opcion = opcion["opción"]
            # print(f"{num}. {opcion}")
            
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
            decision_tomada = input("\033[1;32;m¿Qué opción escoges? " + "(1 a " + str(len(relato[elemento]["contenido"]))+ "): ")
            # con esto me aseguro de que la opción ingresada sea un número de las opciones posibles.
            if not decision_tomada.isdigit() or int(decision_tomada)>len(relato[elemento]["contenido"]) or int(decision_tomada)<=0: 
                print("\033[1;32;m\nDebes escoger una de las opciones posibles introduciendo un número.")
            else:
                decision_valida = True  # se escogió una decisión válida, así que puede continuar
                             
                # Ok, voy a contarte un secreto pero solo porque creo que eres de mis lectorxs favoritxs: está parte de
                # "detalle" no está programada de la mejor manera. Hay que mejorar este condicional y la mecánica 
                # general del "detalle" porque, como está, una decisión del principio puede no lograr determinar
                # la variación de un texto dependiente al final porque otra decisión puede cambiar "detalle" y por tanto
                # la variación. Mi idea para esto es que el valor de la clave "detalle" no sea un número, sino un
                # string con el detalle y el número de ese detalle. Entonces el detalle concreto puede añadirse a una
                # lista guardada en el programa en el puesto que le registra su número. Así cada texto independiente
                # puede tener el metadato de a qué índice de esa lista debe referirse para el detalle que le toca usar 
                # (esto reemplazaría el valor de la llave "variación"). Luego el print sería simplemente el texto fijo
                # con lista[indice]. Podría hacerlo igual que como hago el poema, con la lista previamente iniciada con
                # el número correcto de partes. No lo he hecho porque este programa funciona bien con esta instrucción
                # y la fecha de la 1a entrega está peligrosamente cerca, así que prefiero terminar el resto más 
                # indispensable del programa, pero dejo todo el concepto escrito para mi yo del futuro.
                
                # Esto guarda el recorrido escogido para saber qué detalle debe usar el relato, "detalle" es una
                # propiedad de cada decision que dice el índice de la lista de variaciones en el texto dependiente
                # que contiene el detalle que coincide con la decisión tomada.
                # -1 porque el indice de las listas empieza en 0.
                if int(relato[elemento]["contenido"][int(decision_tomada) - 1]["detalle"])>0:
                    detalle = relato[elemento]["contenido"][int(decision_tomada) - 1]["detalle"]
                # Este condicional revisa si la decisión incluye un verso confirmando si la propiedad "verso" tiene
                # como valor una lista con un tamaño mayor a 0. Ese larguero que sigue a "relato" es la manera de acceder
                # a cada propiedad específica. En cristiano, lo que dice ahí es "en el relato, en el elemento número tal,
                # hay una propiedad llamada contenido, dentro de ella están las tres opciones, acceda a la del número de
                # la decisión tomada y, dentro de ella, revise el tamaño de la lista que es el valor de la propiedad 
                # "verso". Así están anidados los datos de los tipos de texto, y hay que recorrer todo desde el cajón más
                # general hasta el más específico para encontrar el dato que se está buscando, pero el camino se puede 
                #guardar en una variable, como hago aquí, para que sirva como una especie de atajo.
                lista_verso = relato[elemento]["contenido"][int(decision_tomada) - 1]["verso"]
                # Ciertas decisiones no añaden un verso al poema. Estas son las que tienen una lista vacía, de tamaño 0. 
                # Esto es lo que el condicional revisa para confirmar si no debe entrar a buscar verso donde no hay.
                # En realidad "verso" se refiere en la mayoría de los casos a una sección del poema de más de un verso, pero 
                # ese nombre es la forma más fácil de expresar y entender la manera en que se arma el poema.
                if len(lista_verso) > 0:
                    # El número del verso escogido se inicializa en 1 puesto que, si no hay más de uno, sirve para 
                    # referenciar el primer y único verso de la lista.
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
                    # la parte del poema que le sigue. De ser así, el valor de "preposición" será mayor a 0 e indicará
                    # qué parte debe seguir.
                    if lista_verso[num_verso-1]["preposición"] > 0:
                        preposicion = lista_verso[num_verso-1]["preposición"]
                                        
                # Algunas opciones permiten al lector ingresar una respuesta escrita. Este condicional revisa la 
                # propiedad "input" de la decisión para saber si es o no el caso revisando si el valor de la clave es
                # diferente a un string vacío. Si es el caso, usa el string que haya como valor para pregntar la respuesta
                if relato[elemento]["contenido"][int(decision_tomada) - 1]["input"] != "":
                    respuesta = input("\033[1;37;m" + relato[elemento]["contenido"][int(decision_tomada) - 1]["input"])
                # Si no es necesario que el usuario ingrese una respuesta, sigue normal con las respuesta escogida.
                else:
                    # Las decisiones tienen la propiedad "repetir" para guardar qué frase es la anterior a la decisión 
                    # para repetirla con ella.
                    repetir = relato[elemento]["repetir"]
                    # Repite la opción escogida con la última frase antes de la decisión
                    respuesta = relato[elemento]["contenido"][int(decision_tomada) - 1]["opción"]
                    print("\033[1;37;m \n" + repetir + " " + respuesta) 
                elemento = relato[elemento]["contenido"][int(decision_tomada) - 1]["siguiente"]  
        input("\033[1;32;mENTER PARA CONTINUAR\n")
        
    # El "texto dependiente", como dice su nombre, depende de una decisión. Estas instrucciones muestran el texto
    # apropiado según lo que se eligió antes. Hay un texto fijo y una "variación", esto es lo que escoge el valor de
    # "detalle" y es lo que tengo que cambiar más adelante para permitir que diferentes decisiones puedan tener
    # diferentes efectos en partes cruzadas del texto sin afectarse entre sí.
    # Es importante que la revisión de si es una decisión esté primero que la revisión de si hay un texto que
    # dependa de una decisión, pues la primera establece variables a las que la segunda se refiere. Además es
    # el orden lógico, no podrá haber texto que dependa de decisiones si no se han tomado decisiones.
    elif relato[elemento]["tipo"] == "TD":
        # Imprime en consola el texto equivalente al recorrido que se escogió, -1 por los índices que empiezan en 0
        print(relato[elemento]["contenido"]["fijo"] + relato[elemento]["contenido"]["variación"][detalle-1], end = "") 
        elemento = relato[elemento]["siguiente"]  

    # Si el tipo de texto es "FIN", el programa muestra el poema que se armó y apague y vámonos. Relato relatado.
    elif relato[elemento]["tipo"] == "FIN":
        print("\033[1;32;mENTER PARA TERMINAR EL CUENTO Y VER TU POEMA\n")
        for i in poema:
            print("\033[1;37;m" + i)         
        elemento = relato[elemento]["siguiente"]
    
       
