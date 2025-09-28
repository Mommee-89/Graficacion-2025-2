# practica-4
Lector de instrucciones para dibujar figuras con la librería turtle en Python

## Descripcion

Este proyecto es una práctica en Python 3.10 utilizando la librería turtle.
El objetivo es leer un archivo externo (dibujante.txt) que contiene instrucciones para dibujar figuras geométricas y ejecutar cada instrucción en pantalla.
Cada línea del archivo indica un comando con parámetros (posición, tamaño, color) y la tortuga dibuja la figura correspondiente.

Añadidos:
- Manejo de errores: si la instrucción es inválida, se muestra un warning y se continúa con la siguiente línea.
- Soporte para múltiples figuras: cuadrado, triángulo, círculo, línea y teleport.

---

## Requisitos
- Python 3.10 instalado en tu sistema.
- No se requieren librerías externas, solo el módulo estándar turtle.

---

## Como ejecutar el programa
1. Descarga o clona este repositorio en tu computadora.
2. Abre una terminal en la carpeta del proyecto.
3. Ejecuta el archivo principal con:
4. python practica4_archivo_instruccionesG.py
5. Se abrirá una ventana de turtle de 600x600 px donde se ejecutarán las instrucciones del archivo dibujante.txt.

---

## Estructura del proyecto

practica4_archivo_instruccionesG.py  # Código fuente principal
dibujante.txt                        # Archivo con instrucciones de figuras
README.md                            # Documentación del proyecto

---

## Funciones principales
- cuadrado(x, y, lado, color)
Dibuja un cuadrado de tamaño y color especificado en la posición indicada.

- triangulo(x, y, lado, color)
Dibuja un triángulo de tamaño y color especificado en la posición indicada.

- circulo(x, y, radio, color)
Dibuja un círculo con radio y color especificado centrado en la posición indicada.

- linea(x, y, longitud, color)
Dibuja una línea de la longitud y color indicados comenzando en la posición indicada.

- teleport(x, y, color)
Marca un punto en la posición indicada con el color especificado.

- lee_archivo()
Lee el archivo dibujante.txt, identifica cada comando y llama a la función correspondiente.
Muestra un warning en la consola si la instrucción es inválida o genera un error.

---

## Ejemplo de uso dentro del programa
El archivo dibujante.txt contiene instrucciones como:

1. CUADRADO -200 100 100 blue
2. TRIANGULO 0 100 100 green
3. CIRCULO 200 50 50 red
4. LINEA -100 -100 200 black
5. TELEPORT 100 -200 purple
6. ESTRELLA 0 0 yellow

- Cada instrucción válida dibuja la figura correspondiente en la ventana de Turtle.
- La instrucción ESTRELLA se considera inválida y genera un warning en la consola, pero no detiene la ejecución.

---

## Lo que se aprende con este proyecto
- Lectura de archivos externos en Python.
- Manejo de cadenas y parámetros numéricos.
- Uso de la librería turtle para dibujar figuras geométricas.
- Manejo de errores y validación de comandos.
- Posibles mejoras
- Soporte para más figuras geométricas, como estrellas o pentágonos.
- Permitir cambiar colores o tamaños mediante comandos adicionales.
- Validar automáticamente colores y parámetros numéricos antes de dibujar.
- Permitir comentarios dentro del archivo de instrucciones.

---

## Fuentes de información
- Python Software Foundation. (2023). turtle — Gráficos con Turtle. Documentación oficial de Python 3.9.23. Recuperado de https://docs.python.org/es/3.9/library/turtle.html
- Stack Overflow. (2019). Manejo de excepciones en Python. Recuperado de https://es.stackoverflow.com

---

### Autor
Diego Flores Ortiz - Proyecto desarrollado como práctica de programación en Python.
- (Se uso la ayuda de la inteligencia artificial para mejorar la explicacion de la funcionalidad del codigo)