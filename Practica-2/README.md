## Practica-2
Este programa permite dibujar un circulo y moverlo usando las flechas del teclado. La figura se mueve sin dejar rastro.

### Explicacion del codigo
import turtle
Importa la libreria turtle para dibujar y manipular la tortuga.

pantalla = turtle.Screen()
pantalla.bgcolor("white")
pantalla.title("Mover figura con flechas")
Crea la ventana de dibujo y la guarda en la variable pantalla.
Establece el color de fondo en blanco.
Asigna un titulo a la ventana.

t = turtle.Turtle()
t.pensize(2)
t.speed(0)
Crea una tortuga llamada t que dibujara la figura.
Define el grosor del lapiz en 2.
Ajusta la velocidad de dibujo a 0 (maxima velocidad).

x, y = 200, 50
radio = 50
Define las coordenadas iniciales del circulo (x e y).
radio indica el tamaño del circulo.

def dibujar_figura():
t.clear()
t.penup()
t.goto(x, y - radio)
t.pendown()
t.color("red")
t.circle(radio) -Esta funcion dibuja el circulo en la posicion actual.
t.clear() -borra cualquier dibujo previo para que no quede rastro.
penup() -levanta el lapiz para mover la tortuga sin dibujar.
goto(x, y - radio) -mueve la tortuga al centro del circulo ajustando la posicion.
pendown() -baja el lapiz para dibujar.
t.color("red") -define el color del circulo.
t.circle(radio) -dibuja el circulo con el radio definido.

def mover_izquierda():
global x
x -= 20
dibujar_figura()
Mueve el circulo hacia la izquierda.
global x permite modificar la variable x fuera de la funcion.
Disminuye x en 20 unidades y redibuja el circulo.

def mover_derecha():
global x
x += 20
dibujar_figura()
Mueve el circulo hacia la derecha aumentando x.

def mover_arriba():
global y
y += 20
dibujar_figura()
Mueve el circulo hacia arriba aumentando y.

def mover_abajo():
global y
y -= 20
dibujar_figura()
Mueve el circulo hacia abajo disminuyendo y.

dibujar_figura()
Dibuja el circulo por primera vez en la pantalla.

pantalla.listen()
pantalla.onkeypress(mover_izquierda, "Left")
pantalla.onkeypress(mover_derecha, "Right")
pantalla.onkeypress(mover_arriba, "Up")
pantalla.onkeypress(mover_abajo, "Down")
Activa la ventana para recibir entradas del teclado.
Asigna cada flecha del teclado a la funcion correspondiente para mover el circulo.

turtle.done()
Mantiene la ventana abierta hasta que el usuario la cierre manualmente.

(Se uso la ayuda de la inteligencia artificial para mejorar la explicacion de la funcionalidad del codigo)