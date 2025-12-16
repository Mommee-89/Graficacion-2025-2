## Practica-1
### Requerimientos
Esta practica fue hecha en python 3.10 en la distribucion de linux Ubuntu. Para que esta practica funcione debe cumplir con ciertos puntos:
- Haber instalado Python en su version 3.10 para que se asegure de que no haya errores.
- Asegurarse de tener instalado tkinder para que el codigo pueda funcionar

### Explicacion del codigo
El primer paso es importar el modulo turtle, que es una herramienta en Python para dibujar graficos. Luego, se crea una pantalla o ventana de dibujo con el comando pantalla = turtle.Screen(), y se cambia el color de fondo de la ventana a blanco con pantalla.bgcolor("white").

Despues se crea una tortuga, que es el objeto que dibuja en la pantalla, con t = turtle.Turtle(). A esta tortuga se le puede configurar cosas como el tamaño del lapiz (con t.pensize(2)) y la velocidad a la que dibuja (con t.speed(3)). En este caso, el lapiz tiene un grosor de 2 y la tortuga dibuja a una velocidad moderada (3).

Luego, se levanta el lapiz con t.penup(), lo que hace que la tortuga se mueva sin dibujar. Se mueve a las coordenadas (-200, 100) usando t.goto(-200, 100) y luego se baja el lapiz con t.pendown() para comenzar a dibujar.

Se cambia el color del lapiz a azul con t.color("blue") y se comienza a dibujar un cuadrado. La tortuga dibuja una linea de 100 unidades hacia adelante con t.forward(100), luego gira 90 grados hacia la derecha con t.right(90) y repite este proceso cuatro veces para completar el cuadrado.

Despues de dibujar el cuadrado, se mueve la tortuga a las coordenadas (0, 100) usando t.goto(0, 100), y se cambia el color del lapiz a verde con t.color("green"). Ahora, la tortuga dibuja un triangulo equilatero. Dibuja una linea de 100 unidades, luego gira 120 grados a la derecha y repite esto tres veces para completar el triángulo.

A continuación, la tortuga se mueve a las coordenadas (200, 50) con t.goto(200, 50), y se cambia el color del lapiz a rojo con t.color("red"). En este caso, la tortuga dibuja un círculo de radio 50 usando el comando t.circle(50).

Finalmente, la tortuga se mueve a las coordenadas (-100, -100) con t.goto(-100, -100), se orienta hacia la derecha con t.setheading(0) y dibuja una linea horizontal de 200 unidades de largo en color negro con t.forward(200).

El código termina con turtle.done(), lo cual indica que el dibujo ha terminado y mantiene la ventana abierta para que puedas ver el resultado.

(Se uso la ayuda de la inteligencia artificial para mejorar la explicacion de la funcionalidad del codigo)