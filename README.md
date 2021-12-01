![](https://i.imgur.com/bsxgluh.jpeg)
# Advertencia:
Este proyecto está pensado para el formato de programa de computador para Windows. Usé Python para hacer una experiencia interactiva que luego convertí en un archivo ejecutable (.exe). El archivo no es malicioso ni es una amenaza para el equipo que lo corre. Solamente interactúa con los archivos de texto (.json) que vienen con el proyecto. El único archivo que se edita es "data.json" para guardar los poemas que genera el lector, los demás archivos solamente se leen.

Es posible que el antivirus de su equipo bloquee la ejecución del programa y detecte una amenaza. Esto es un falso positivo. En la mayoría de los casos es posible seleccionar una opción de "correr de todas formas", pero ciertos antivirus más agresivos eliminan el programa tan pronto hay un intento de correrlo. Una solución para esto es crear una "exclusión" en la configuración del antivirus para que no analice un archivo o carpeta particular, la manera exacta de hacerlo depende del antivirus. No estoy pidiendo que tome esta medida si usted no desea desactivar la protección de su antivirus ni espero que lo haga si duda de la procedencia o integridad del archivo. Sin embargo, incluyo esta aclaración para dar cuenta de que el programa no es malicioso, de que la inaccesibilidad no es a causa de un problema en el código que escribí y de que existe una forma de acceder al programa.

Si definitivamente no puede correr el ejecutable incluyo las siguientes alternativas:
1.  En [github.com/Pabella16/Sirena](https://github.com/Pabella16/Sirena) podrá encontrar el código de Python y los archivos JSON que aparecen en el listado de códigos. Es posible descargarlos y correr el programa con un [intérprete](https://hackr.io/blog/best-python-ide) de Python (tambiíen hay que instalar el módulo [Rich](https://rich.readthedocs.io/en/stable/introduction.html)). Además, encontrará un archivo "README.md" que incluye pantallazos del funcionamiento del programa y la versión PDF de los tres relatos. El proyecto no está diseñado para leerse en el formato lineal del PDF y leer así el contenido puede ser decepcionante. Están incluidos para evitar que, en el peor de los casos, el contenido literario sea completamente inaccesible para los evaluadores.
2.  En [youtu.be/jcTaIFuNiHY](https://youtu.be/jcTaIFuNiHY) podrá encontrar un video que muestra el funcionamiento del programa.

# Presentación:

*Cantos de sirena* es un proyecto creativo que explora la representación de la identidad de género, de la sexualidad y del carácter violento del deseo a través de una colección interactiva de cuentos y poemas presentada como programa de computador. Como experiencia interactiva, el proyecto busca dar cuenta de la crisis que la imposición de roles de género genera en alguien y presentar el género como una identidad fluida que se transforma y resignifica con los encuentros entre cuerpos y perspectivas. Me propuse mezclar ficción, poesía y programación para convertir al lector en jugador, editor y performer a través de la toma de decisiones en el contexto de lo narrado. Este programa referencia los archivos JSON en los que están estructurados los relatos para recorrerlos, permitir al lector tomar decisiones y generar poemas.

Según las opciones que el lector escoge introduciendo un número, la obra puede sufrir una serie de transformaciones. Los principales cambios suceden en el desarrollo de los relatos y en la generación de los poemas. El lector transforma el texto y escoge qué escenas se presentarán con ciertas decisiones. También escoge (sin saberlo) qué versos combinan para completar el poema que se presentará al final de cada relato. Adicionalmente, puede afectar detalles menores que aparecen en el texto. Esto hace a la lectura personalizada natural y consecuente, pues el relato “recuerda” la opción escogida y la refleja. Por último, ciertas decisiones permiten al lector llevarse una especie de objeto coleccionable relacionado con cada relato. Con este formato, el texto en sí es fluido y cambiante, como las nociones del deseo y la identidad que explora, y la participación del lector en la propuesta es activa y necesaria. De esta manera, el proyecto permite una lectura coherente en términos ludo-narrativos con la representación del género y el deseo como un “durante” constante, múltiple y variable.

# Instrucciones:
Extraer el contenido del archivo comprimido y correr el archivo .exe

# Archivos:
El proyecto incluye:
1.  Un archivo "Cantos\_de\_sirena.exe".
2.  Cinco archivos .json. Tres relatos, un tutorial y un archivo de datos:
    1.  "data.json"
    2.  "MUNECAS.json"
    3.  "PRESION.json"
    4.  "HAMBRE.json"
    5.  "tutorial.json"
3.  Un archivo PDF con el "Arte poética".
4.  Un archivo PDF con el listado de códigos.
5.  Este archivo "README.md"


# Pantallazos:
![](https://i.imgur.com/z4D2LzY.jpg)

![](https://i.imgur.com/3GheVR9.jpg)

![](https://i.imgur.com/CuzKlEb.jpg)

![](https://i.imgur.com/sk0pkI5.jpg)

# Más información sobre el ejecutable:
Para crear un ejecutable a partir del código de Python usé un módulo llamado "PyInstaller". Esta es una de las formas más sencillas de crear un programa a partir de un código, pero el resultado tiene algunos problemas con que los antivirus detectan un falso positivo por el ejecutable. Estos problemas han sido reportados por diferentes usuarios en internet y existen algunas soluciones (como la que se describe [aquí](https://python.plainenglish.io/pyinstaller-exe-false-positive-trojan-virus-resolved-b33842bd3184)). Probé las soluciones más rápidas, pero el archivo siguió siendo detectado como un virus, probablemente porque no tiene una "firma", que se puede comprar para certificar que un programa no es un virus. El proceso de la firma es largo y costoso. Hay otras alternativas para hacer que el código se pueda correr por internet o para crear un ejecutable, pero son muy complejas. Por la limitación de tiempo para este proyecto lo dejé como ejecutable aunque algunos antivirus lo bloquean.
