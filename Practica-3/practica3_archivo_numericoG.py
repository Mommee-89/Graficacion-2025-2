import turtle
import os


PIXEL_SIZE = 5

COLORES = {
    0: "black",
    1: "red",
    2: "green",
    3: "blue",
    4: "yellow",
    5: "orange",
    6: "purple",
    7: "brown",
    8: "pink",
    9: "gray"
}


def leer_matriz():
    ruta_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(ruta_actual, "matriz.txt")

    matriz = []

    with open(ruta_archivo, "r") as archivo:
        for linea in archivo:
            fila = [int(numero) for numero in linea.strip().split()]
            matriz.append(fila)

    return matriz


def pintar_pixel(x, y, size, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()

    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)

    turtle.end_fill()


def dibujar_matriz(matriz, pixel=5):
    turtle.speed(0)
    turtle.hideturtle()
    turtle.tracer(0, 0)

    filas = len(matriz)
    columnas = len(matriz[0])

    inicio_x = -columnas * pixel / 2
    inicio_y = filas * pixel / 2

    for i in range(filas):
        for j in range(columnas):
            valor = matriz[i][j]
            color = COLORES.get(valor, "black")

            x = inicio_x + j * pixel
            y = inicio_y - i * pixel

            pintar_pixel(x, y, pixel, color)

    turtle.update()


def main():
    turtle.setup(width=800, height=800)
    turtle.bgcolor("white")
    turtle.title("Práctica 3 - Pixel Art con Turtle")

    matriz = leer_matriz()
    dibujar_matriz(matriz, PIXEL_SIZE)

    turtle.done()


if __name__ == "__main__":
    main()
