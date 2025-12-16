# practica-3
Lectura de archivo numérico y visualización tipo Pixel Art con la librería turtle en Python

## Descripcion

Este proyecto es una práctica en Python 3.10 utilizando la librería turtle.
El objetivo es leer un archivo externo (matriz.txt) que contiene una matriz de 100x100 con valores numéricos del 0 al 9.
Cada número representa un color distinto y se dibuja un cuadrado que simula un píxel en la pantalla.

El programa recorre la matriz y posiciona la tortuga en la coordenada correspondiente para pintar cada píxel, formando una imagen tipo mosaico o pixel art.

Añadidos:
- Uso de os.path para asegurar la lectura correcta del archivo sin importar desde dónde se ejecute el programa.
- Optimización de dibujo usando tracer para mejorar el rendimiento.
- Manejo seguro de la matriz para evitar errores de índices.

---

## Requisitos
- Python 3.10 instalado en tu sistema.
- No se requieren librerías externas, solo el módulo estándar turtle.

---

## Como ejecutar el programa
1. Descarga o clona este repositorio en tu computadora.
2. Abre una terminal en la carpeta del proyecto.
3. Ejecuta el archivo principal con:
4. python practica3_archivo_numericoG.py
5. Se abrirá una ventana de turtle donde se dibujará la matriz de colores.

---

## Estructura del proyecto

practica3_archivo_numericoG.py   # Código fuente principal
matriz.txt                      # Archivo con la matriz 100x100
README.md                       # Documentación del proyecto

---

## Funciones principales
- leer_matriz()
Lee el archivo matriz.txt y devuelve la matriz como una lista de listas de enteros.

- pintar_pixel(x, y, size, color)
Dibuja un cuadrado relleno simulando un píxel del tamaño y color indicados en la posición especificada.

- dibujar_matriz(matriz, pixel)
Recorre la matriz y dibuja cada número utilizando el color asignado, formando el pixel art completo.

---

## Ejemplo de uso dentro del programa
El archivo matriz.txt contiene números del 0 al 9 separados por espacios.
Cada número corresponde a un color específico definido dentro del programa.

Ejemplo de una fila del archivo:
0 1 2 3 4 5 6 7 8 9 ...

Al ejecutar el programa:
- Se lee el archivo matriz.txt.
- Cada número se traduce a un color.
- Se dibuja un mosaico de 100x100 píxeles en la ventana de Turtle.

---

## Lo que se aprende con este proyecto
- Lectura de archivos externos en Python.
- Manejo de listas y matrices bidimensionales.
- Uso de la librería turtle para representar datos gráficamente.
- Relación entre datos numéricos y visualización en pantalla.
- Organización de proyectos y archivos en Python.

---

## Posibles mejoras
- Soporte para matrices de distinto tamaño.
- Lectura dinámica de colores desde un archivo.
- Escalado automático del tamaño de los píxeles.
- Animación del proceso de dibujado.

---

## Fuentes de información
- Python Software Foundation. (2023). turtle — Gráficos con Turtle. Documentación oficial de Python. Recuperado de https://docs.python.org/es/3/library/turtle.html
- Python Software Foundation. (2023). os — Interfaces del sistema operativo. Recuperado de https://docs.python.org/es/3/library/os.html

---

### Autor
Diego Flores Ortiz - Proyecto desarrollado como práctica de programación en Python.
- (Se usó la ayuda de la inteligencia artificial para mejorar la explicación de la funcionalidad del código)