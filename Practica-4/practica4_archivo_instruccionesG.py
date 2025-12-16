import turtle

pantalla = turtle.Screen()
pantalla.setup(600, 600)
pantalla.bgcolor("white")
pantalla.title("Practica 4 - Lector de instrucciones")
t = turtle.Turtle()
t.pensize(2)
t.speed(3)

# Funciones de figuras
def cuadrado(x, y, lado, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    for i in range(4):
        t.forward(lado)
        t.right(90)

def triangulo(x, y, lado, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    for i in range(3):
        t.forward(lado)
        t.right(120)

def circulo(x, y, radio, color):
    t.penup()
    t.goto(x, y - radio)
    t.pendown()
    t.color(color)
    t.circle(radio)

def linea(x, y, longitud, color):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.color(color)
    t.forward(longitud)

def teleport(x, y, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.dot(20)

# Funcion para leer archivo
def lee_archivo():
    filename = "dibujante.txt"
    for line in open(filename):
        datos = line.split()
        if not datos:
            continue

        comando = datos[0].upper()

        try:
            if comando == "CUADRADO":
                cuadrado(int(datos[1]), int(datos[2]), int(datos[3]), datos[4])
            elif comando == "TRIANGULO":
                triangulo(int(datos[1]), int(datos[2]), int(datos[3]), datos[4])
            elif comando == "CIRCULO":
                circulo(int(datos[1]), int(datos[2]), int(datos[3]), datos[4])
            elif comando == "LINEA":
                linea(int(datos[1]), int(datos[2]), int(datos[3]), datos[4])
            elif comando == "TELEPORT":
                teleport(int(datos[1]), int(datos[2]), datos[3])
            else:
                print("⚠️ Instruccion invalida:", line.strip())
        except:
            print("⚠️ Error procesando:", line.strip())

# Llamar la funcion para leer y ejecutar
lee_archivo()
turtle.done()