import turtle

# Configuracion de la pantalla
pantalla = turtle.Screen()
pantalla.bgcolor("white")
pantalla.title("Mover figura con flechas")

# Tortuga para dibujar las figuras
t = turtle.Turtle()
t.pensize(2)
t.speed(0) 

# Coordenadas iniciales del circulo
x, y = 200, 50
radio = 50

# Funcion para dibujar el circulo
def dibujar_figura():
    t.clear()  # Borra la figura anterior
    t.penup()
    t.goto(x, y - radio)  # Ajuste para que el círculo se dibuje desde el centro
    t.pendown()
    t.color("red")
    t.circle(radio)

# Funciones para mover la figura
def mover_izquierda():
    global x
    x -= 20
    dibujar_figura()

def mover_derecha():
    global x
    x += 20
    dibujar_figura()

def mover_arriba():
    global y
    y += 20
    dibujar_figura()

def mover_abajo():
    global y
    y -= 20
    dibujar_figura()

# Dibujar la figura inicial
dibujar_figura()

# Asignar teclas de movimiento
pantalla.listen()
pantalla.onkeypress(mover_izquierda, "Left")
pantalla.onkeypress(mover_derecha, "Right")
pantalla.onkeypress(mover_arriba, "Up")
pantalla.onkeypress(mover_abajo, "Down")

# Mantener ventana abierta 
turtle.done()
