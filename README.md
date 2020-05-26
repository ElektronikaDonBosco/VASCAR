# Contenidos:
## Introducción	
## Funcionamiento
## Requerimientos	
## Especificaciones	
### Hardware del Proyecto	
### Esquema por Bloques	
### Fuente de Alimentación	
### Microcontrolador	
### Interfaces de Comunicación	
### Software	
## Desarrollo	
### Diseños FreeCad	
### Carro	
### Soporte de Batería	
### Soporte de QR	
### Caja de Led	
### Diseños Proteus	
### Sensores	
### Control de batería	
### Indicadores Led	
### Materiales	
### Motores	
### Pantalla táctil	
### Controladores de velocidad	
### Reguladores de tensión	
### Raspberry Pi	
### Arduino	
## Puesta a punto	
## Futuras mejoras	
## Conclusiones	
## Referencias	


# Introducción

Este proyecto a sido desarrollado por alumnos de Mantenimiento Electrónico de Don Bosco. La idea es crear una plataforma customizable y autónoma para poder cumplir diversas funciones. 

El proyecto consiste de un carro metálico el cual hemos automatizado para que mediante una página web podamos enviarlo a diferentes puntos. Estos puntos serán códigos QR ubicados al lado de una línea negra la cual seguirá el carro. Los códigos los leerá usando un lector de códigos QR ubicado en la parte de abajo y esta información pasará a una Raspberry la cual comparará el valor de la lectura con la página web utilizando un programa de python y, si ambos valores coinciden, mandará una señal a un Arduino que parará los motores del carro. El carro se moverá usando unos motores de Hoverboard alimentados por una batería de 36 V y seguirá una línea negra ubicada en el suelo utilizando unos sensores infrarrojos.

# Funcionamiento 

Lo primero que hacemos al llegar al carro es encender el interruptor e iniciar la Raspberry. Al encender la Raspberry, el programa de python se iniciará automáticamente, buscará el dispositivo que queremos usar (en este caso el lector de códigos QR) y hará que este solo pueda usarse en el programa. Para que este proceso se realice correctamente, debemos conectar el dispositivo antes de encender la Raspberry y cuando esté encendida debemos asegurarnos de que el servidor esté en funcionamiento.

Tras configurar la Raspberry, iremos a internet y entraremos en nuestra página web. Una vez allí, seleccionaremos el lugar al que queremos que vaya el carro. Esta información se pasará a la Raspberry mediante una API y comparará la lectura del lector de códigos QR con lo que reciba de la web. 
	
El siguiente paso será pulsar el botón de la parte de arriba del carro para iniciar su movimiento. Al hacer esto, el carro empezará a moverse y los LEDs de la parte superior pasarán de azul a blanco para indicar que está en movimiento. El carro seguirá la línea negra del suelo mediante unos sensores infrarrojos que detectarán la línea y harán que el carro siga recto. Seguirá esta línea hasta que el lector de códigos QR detecte el código que coincida con la información de la página web y, cuando esto suceda, la Raspberry enviará una orden al arduino mediante una conexión serie que hará que pare los motores y cambie los LEDs a azul indicando que está parado. 

Por último, si queremos seguir utilizando el carro, volveremos a la página web, indicaremos una nueva ubicación y pulsaremos el botón de la parte superior. Para más información, los programas se encuentran el la parte de código de este proyecto.

# Especificaciones

En este apartado explicaremos detalladamente las diferentes partes que forman este proyecto y las especificaciones de dichas partes.

## Hardware del Proyecto

### 1. Esquema por Bloques

![Arduino](https://github.com/asieriglesias/VASCAR/blob/master/Imagenes/Bloques.png)

### 2. Fuente de Alimentación

Para alimentar este proyecto, hemos utilizado una batería de 36V y 4000mA. Hemos elegido esta batería ya que los motores se alimentan a 36V y con 4000mA la batería durará suficiente como para que este proyecto sea útil. Para poder alimentar los controladores (Max 36V), hemos usado un regulador de tensión LM2596 ya que la batería al máximo de carga tiene 42V y de esta forma nos ahorraremos posibles fallos.

Además de esta batería, hemos usado una segunda batería de 7.4V y 3600mA para alimentar la Raspberry. Hemos utilizado otro regulador en esta parte para bajar esta tensión a 5V y evitar fallos por exceso de tensión.

### 3. Interfaces de Comunicación

En este proyecto contamos con diferentes partes que se comunican entre sí y, para ello, hemos usado diversas tecnologías. Para la comunicación entre la Raspberry y el servidor API, hemos usado una conexión wifi mediante la cual la Raspberry se conecta a internet y accede al servidor. La comunicación entre Raspberry y Arduino se realiza mediante una conexión serie por USB. Por esta conexión se pasará la orden de parada que envía la Raspberry al Arduino cuando el carro tiene que detenerse y se alimenta el Arduino. Además del Arduino, la Raspberry tiene conectados otros dos USB: uno es el lector de códigos QR encargado de detectar la posición de parada del carro y otro es de la pantalla que permite usar la función táctil de la misma. Por último, la pantalla se conecta a la Raspberry usando un cable HDMI para poder visualizar la interfaz de la misma.

## Software

### * Python 

Python es un software de programación centrado en que el código sea fácil de leer. Es una herramienta fácil de usar y de aprender pero permite realizar programas complejos. En este proyecto, lo hemos usado para hacer el programa que llevará la raspberry y que se encargará de controlar el lector de QR.

### * Trello

Trello es una herramienta que utiliza el método canvas para gestión de proyectos online. Esta nos permitirá organizar rutinas de trabajo, priorizar tareas, generar avisos y muchas otras opciones. La aplicación es un tablero muy intuitivo el cual se distribuye en columnas o listas fijas personalizadas, donde reflejaremos las distintas fases de cada tarea en nuestro proyecto. Estas estarán subdivididas en entradas o tarjetas, las cuales harán referencia a cada una de las tareas o labores del proyecto.

### * Arduino

Este software nos permite poder configurar nuestro controlador ATMega , de nuestra placa de arduino. 
Este software utiliza un lenguaje de programación basado en C++.

### * Github 

Este software es una página web donde nos permite subir diferentes tipo de archivo creando un usuario. 

### * Proteus

Con este programa podremos crear los diferentes circuitos que necesitamos y podremos simularlos en ello, de esta forma podremos comprobar de antemano que posibles fallos nos pueden aparecer, además de un apartado donde podemos crear un archivo LPKF que nos permite generar nuestro circuito en PCB. 

### * FreeCad

Mediante este programa conseguiremos hacer los diseños 3D para los soportes del carro junto a su diseño.

# Desarrollo

## Diseños FreeCad 

A lo largo del proyecto hemos tenido que diseñar varias piezas para diferentes funciones, en este apartado se explicaran sus usos y las medidas que hemos utilizado. 

### Carro

Para la creación del proyecto tuvimos que hacer nuestro propio diseño del carro, para que posteriormente sería soldado en el departamento de soldadura. 

Las medidas que utilizamos fueron adaptadas desde un carro que vimos en internet donde cada plancha es de 500 x 400 mm, el carro tiene una altura 980 mm y los tubos tienen un diámetro de 40 mm 

![Arduino](https://github.com/asieriglesias/VASCAR/blob/master/Imagenes/Carro.png)

### Soporte de Batería 

Para poder sujetar la batería  a la plataforma tuvimos que hacerle un soporte que se pudiera atornillar  a la placa de metacrilato, para ello hicimos agujeros compatibles con tornillos de cabeza plana de 2 mm de radio, por otra parte tiene una altura de 2 mm para que no se moviera, y tiene unas dimensiones de 134 x 75 mm.

![Arduino](https://github.com/asieriglesias/VASCAR/blob/master/Imagenes/Soporte%20Bater%C3%ADa.png)

### Soporte de QR 

Una vez que empezamos a montar todo el carro vimos que necesitábamos  un soporte donde poder sujetar el lector QR. Para ello intentamos hacer un tipo de caja donde introduciremos el QR.

![Arduino](https://github.com/asieriglesias/VASCAR/blob/master/Imagenes/Soporte%20QR.png)

### Caja de Led

Por último hicimos una caja para introducir la placa de los led dentro. De esta forma solo se verán los led, el diseño será enganchado mediante bridas al carro.

![Arduino](https://github.com/asieriglesias/VASCAR/blob/master/Imagenes/Caja%20Leds.png)

## Diseños Proteus

Durante la creación del carro hicimos un total de tres PCBs: para los sensores,  el control de batería y el circuito de LEDs.

### Sensores 

La primera PCB se basa en sensores QTR y su función era detectar la línea. Hicimos dos versiones de esta placa. La primera fue una placa con dos sensores separados por 60 mm ya que nuestra línea es de 50 mm. Después de probar este diseño, concluimos que no tenía la suficiente precisión y por ello hicimos la segunda versión, esta vez con cuatro sensores. Estos sensores están separados los unos de los otros por 15 mm y gracias a esto y unos cambios en el programa conseguimos una precisión bastante mejor.
![Arduino](https://github.com/asieriglesias/VASCAR/blob/master/Imagenes/Sensores.png)

### Control de batería 

La siguiente PCB es un divisor de tensión que nos permite saber el nivel de voltaje de la batería. Con este circuito, obtenemos una tensión de salida equivalente a la tensión de la batería, es decir, cuando la batería está al 100% tendremos 5V de salida y según baje, esta tensión será equivalente.
![Arduino](https://github.com/asieriglesias/VASCAR/blob/master/Imagenes/Control%20Bater%C3%ADa.png)

### Indicadores Led 

La última PCB son una serie de LEDs conectados al arduino, estos indican diferentes situaciones en las que se puede encontrar el carro, encendiéndose el blanco cuando no hay ningún tipo de problema, el azul cuando este se sale de la línea y el rojo cuando la batería cae de cierto punto.

![Arduino](https://github.com/asieriglesias/VASCAR/blob/master/Imagenes/LEDs.png)

## Materiales

### Motores 

Los motores que hemos utilizado en este proyecto son unos motores de hoverboard de 36V, estos motores tienen 3 pines de alimentación y 5 de realimentación que van a 5V. Mediante estos pines se generan 2 impulsos diferentes que entran por los pines Ha y Hc donde entre ellos tienen 90º de retardo y el tercer pin Hb va a la par de Ha. 

### Pantalla táctil

La pantalla táctil utilizada en este proyecto es una pantalla de 7 pulgadas LCD. Esta pantalla se conecta a la Raspberry utilizando el puerto display y se alimenta conectandola a los pines GPIO. Tiene una resolución de 800x480 y soporta hasta 10 puntos simultáneos táctiles.

### Controladores de velocidad 	

Mediante estos controladores conseguiremos regular la velocidad de los motores mediante un pin VR que está alimentado a 5V, por otro lado nos permiten controlar la dirección de los motores. 

La placa se alimenta a 36V y se encarga de alimentar los motores, aparte tendrá unos pines que nos permitirán hacer una realimentación a +5V. 

### Reguladores de tensión 	

Los reguladores de tensión que hemos utilizado son los LM2596. Estos reguladores convierten la tensión de entrada en una tensión de salida inferior. Esta tensión se ajusta mediante un potenciómetro integrado en la placa. La tensión de salida de la placa será constante una vez ajustada ya que utilizan transistores en conmutación, lo cual hace que estos reguladores sean muy eficientes (73%). Su datasheet se encuentra en este enlace.  

### Raspberry Pi

La Raspberry que hemos usado en este proyecto es una Raspberry Pi 3 b+. Este modelo es la última versión de la Raspberry Pi 3, cuenta con un procesador de cuatro núcleos 1.4GHz 64 bits, LAN inalámbrico de doble banda y Bluetooth 4.2. Además de esto, cuenta con las siguientes conexiones: cuatro puertos USB, un puerto HDMI, un puerto Ethernet, un puerto Jack, un puerto USB micro B, 40 pines GPIO, un puerto display y un puerto para cámaras.

![Arduino](https://github.com/asieriglesias/VASCAR/blob/master/Imagenes/Raspberry.png)

En este proyecto, la Raspberry será la encargada de conectarse al servidor API para poder saber la localización en la que debe pararse el carro. Para esto, usaremos un programa de Python que se encargará de controlar el lector de códigos QR y comparar su lectura con la del servidor. Cuando la lectura del código QR y el valor cogido del servidor API coincidan, la Raspberry enviará una orden de parada al Arduino mediante una conexión serie.

### Arduino

Arduino es una placa de software y hardware libre el cual nos permite crear una diversidad de proyectos.  La placa que hemos utilizado a sido un Arduino Leonardo, esta placa contiene 20 pines de entrada / salidas digitales (de los cuales 7 se pueden usar como salidas PWM y 12 como entradas analógicas), un oscilador de cristal de 16MHz, una conexión micro USB que nos permite alimentar la placa a +5V, un conector de alimentación jack de +7V -  +12V, 2 pines de Vin y +5V que nos permiten alimentar y proporcionar alimentación,  un encabezado ICSP y un botón de reinicio.

![Arduino](https://github.com/asieriglesias/VASCAR/blob/master/Imagenes/Partes%20Arduino.png)

Por otra parte el Arduino es el encargado de hacer un control sobre la plataforma, para ello ejecutará diferentes funciones dependiendo de su importancia, esto se entenderá mejor mediante el próximo diagrama de flujo. 

![Arduino](https://github.com/asieriglesias/VASCAR/blob/master/Imagenes/Diagrama%20Arduino.png)

Para empezar haremos una lectura del nivel de batería para tener en cuenta cuando hay que cargarla, tras eso el Arduino recogerá los datos que reciba de los sensores que estarán en todo momento leyendo la línea, mediante estos valores el arduino ejecutara su parte de control. 

Esta parte de control dependerá de los valores que recogemos de los sensores, dependiendo en qué caso nos encontremos los motores se ejecutarán con diferente velocidad. 

![Arduino](https://github.com/asieriglesias/VASCAR/blob/master/Imagenes/Tabla%20Arduino.png)

Este funcionamiento se puede ver mediante el siguiente dibujo: 

![Arduino](https://github.com/asieriglesias/VASCAR/blob/master/Imagenes/Linea.png)

Como se puede apreciar en la figura, cuando uno de los dos sensores centrales  detecta que está fuera de la línea, se gira en el sentido contrario, para volver a colocarse en la línea. El giro se efectúa mediante una diferencia de velocidad entre ambas ruedas, y en el caso de que los sensores estén fuera de la línea esa diferencia será mayor.

Por otro lado una vez que el arduino reciba la orden de parada, habremos llegado a la habitación, se pararan todos los sistema y se encenderá un led el cual nos indicará que el sistema está apagado, para volver a ejecutar el programa tendremos que elegir una habitación y pulsar el botón de arranque.

## Esquemas

### Divisor de tensión: 

Este circuito fue diseñado con la intención de medir el voltaje de la batería. La batería tiene un voltaje que varía entre 30 y 42 voltios, por lo que para medir esto hicimos un divisor de tensión que tendría un voltaje de salida equivalente en todo momento, para enviarlo al arduino y que este lo detecta correctamente. El voltaje con la batería completamente llena, sería de 5 voltios y con la batería descargada serían 3.5 voltios.

![Arduino](https://github.com/asieriglesias/VASCAR/blob/master/Imagenes/Divisor%20de%20Tensi%C3%B3n.png)

### Sensores  QTR: 

Los sensores QTR están conformados por un diodo-led y un fototransistor. El led se ilumina y la luz de este rebota en la superficie, la cual dependiendo de la intensidad de éste será detectado en mayor o menor medida por el fototransistor.

Hicimos uso de 4 de estos para tener mayor precisión y control de estos, y los separamos unos de otros con un espacio de 60 milímetros ya que la cinta que guiaría el camino media 50mm.

![Arduino](https://github.com/asieriglesias/VASCAR/blob/master/Imagenes/Esquema%20Sensores.png)

# Puesta a punto

En este punto explicaremos el proceso que hemos seguido para el montaje de este proyecto. Como en todo proyecto, empezamos por recaudar la información necesaria para saber con que material íbamos a trabajar y cómo funcionaba cada componente. 

Una vez hecho eso empezamos a crear una maqueta con la que trabajar hasta que nos llegara el carro, esta maqueta fue una placa de metacrilato en la cual tuvimos que hacer  agujeros y cortes. En esta maqueta probamos principalmente los motores, controladores y batería. Para ello tuvimos que ir haciendo varias pruebas debido a la poca información que teníamos de las placas. Lo primero que hicimos fue medir cada pin de la placa. Tras descubrir los pines de alimentación empezamos a hacer pruebas conectando la rueda y buscando cual era el pin encargado de regular la velocidad, tras eso buscamos el pin para el control de dirección y conectamos cada pin a una de las salidas del arduino.
 
Después de esto, comenzamos a diseñar los sensores QTR y empezamos a desarrollar el programa de python que iría en la raspberry. Cuando diseñamos los sensores QTR y comprobamos que las simulaciones daban buenos resultados, imprimimos la PCB e hicimos varias pruebas para comprobar que los sensores daban los valores correctos. Una vez hecho esto, probamos los sensores con un programa de Arduino y conseguimos controlar la velocidad de éstos usando los sensores.
 
En la parte del programa de Raspberry, primero se hizo un programa para enviar información al Arduino por serie y que el Arduino encendiera un LED. Después, se creó la forma de controlar el lector de códigos QR y guardar su lectura. Por último, hicimos un programa para enviar y recibir datos desde la página web y enviar una orden al Arduino basados en la respuesta. Tras crear estos programas, juntamos las diferentes partes en un mismo programa, añadimos el inicio automático y comprobamos que funcionase correctamente.

Una vez que nos llegó el carro, creamos una nueva placa de metacrilato en la que hicimos nuevas medidas para poder poner todos los componentes de una forma ordenada. Tras instalar todos los componentes empezamos a hacer pruebas para que todo funcionara correctamente juntando todas las pruebas individuales que habíamos hecho hasta ahora. Cuando comprobamos que todo funcionaba correctamente, nos centramos en dejar el proyecto con un aspecto más presentable y lo dimos por finalizado.

# Futuras mejoras 

Mediante este apartado explicaremos cambios importantes que habría que realizar para tener una mejor funcionalidad del proyecto.  

### Sensores CCD

Una de las cosas a mejoras que habría que implementar sería un sustituto de los sensores QTR por sensores CCD, este cambio nos proporciona un campo de visión del los sensores mayor junto a una mejor sensibilidad para detectar la línea, además de menos peso de lo que proporcionan los sensores actuales. 

### Motores 

Otra de las mejoras a implementar sería la sustitución de los motores debido a que los motores que teníamos no nos permiten hacer una realimentación, esto se debía a que a la hora de hacerla se genera un alto campo electromagnético y nos impedía tener el control sobre el motor. Entonces mediante esta mejora conseguiremos tener un precisión más exacta sobre el carro para dirigirlo sobre la línea. 

### Ultrasonido

Inicialmente teníamos pensado usar un sistema de ultrasonidos para detectar los alrededores del carro y que este se detuviese en el caso de que hubiera algún obstáculo. Aunque no lo metimos aún pensamos que es una buena aplicación para el proyecto ya que aporta una medida de seguridad.

# Conclusiones 

En conclusión, nos gustaría decir que, a pesar de ser un desafío ambicioso, ha sido gratificante para todos trabajar en este proyecto. Nos ha aportado conocimientos que hemos obtenido unos de otros.

Al compilar todos los procesos, podemos concluir que el proceso ha sido positivo en todos los aspectos. El trabajo realizado ha dado como resultado una aplicación con varias funcionalidades y un carro autómata práctico.  




