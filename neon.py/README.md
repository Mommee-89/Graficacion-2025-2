# neon
Juego interactivo con control de un cubo y colisiones utilizando la librería pygame en Python  

## Descripcion  

Este proyecto es un juego desarrollado en **Python 3.12** utilizando la librería **pygame**.  
El objetivo es controlar un cubo en un entorno 2D, evitando que salga de la pantalla mediante colisiones con plataformas invisibles que actúan como límites.  
El jugador puede mover el cubo horizontal y verticalmente, y el sistema detecta las colisiones para impedir que atraviese los bordes del escenario.

Añadidos:  
- Implementación de colisiones verticales y laterales mediante detección de rectángulos (`Rect.colliderect`).  
- Movimiento fluido controlado por teclas del teclado.  
- Estructura modular del código para futuras ampliaciones del juego.  

---

## Requisitos  
- Python 3.12 instalado en tu sistema.  
- Librería **pygame** instalada (puede instalarse con el comando):  
  ```
  pip install pygame
  ```  

---

## Como ejecutar el programa  
1. Descarga o clona este repositorio en tu computadora.  
2. Abre una terminal en la carpeta del proyecto.  
3. Ejecuta el archivo principal con:  
   ```
   python neon.py
   ```  
4. Se abrirá una ventana de **pygame** donde podrás mover el cubo con las teclas de dirección.  
   Las plataformas laterales impiden que el jugador salga del área visible.  

---

## Estructura del proyecto  

```
neon.py           # Código fuente principal del juego
assets/           # Carpeta opcional para guardar imágenes o sonidos
README.md         # Documentación del proyecto
```

---

## Funciones principales  

- **clase Plataforma(x, y, ancho, alto)**  
  Crea una superficie rectangular que actúa como límite o superficie de colisión.  

- **clase Jugador(x, y)**  
  Controla la posición, movimiento y colisiones del cubo principal controlado por el jugador.  

- **update()**  
  Actualiza la posición del jugador en función de las teclas presionadas y comprueba las colisiones con las plataformas.  

- **draw()**  
  Dibuja en pantalla tanto el jugador como las plataformas de colisión.  

---

## Ejemplo de uso dentro del programa  

El juego crea cuatro plataformas invisibles alrededor de los bordes de la ventana:  

```
1. Plataforma superior
2. Plataforma inferior
3. Plataforma izquierda
4. Plataforma derecha
```

Cuando el cubo controlado por el jugador intenta salir del área visible, **pygame** detecta la colisión y detiene su movimiento.  
Esto simula paredes físicas invisibles que limitan el espacio de juego.  

---

## Lo que se aprende con este proyecto  
- Uso básico de **pygame** para crear ventanas y manejar eventos.  
- Implementación de colisiones usando rectángulos (`Rect`).  
- Control de movimiento y físicas simples.  
- Detección de límites en pantalla sin modificar la estructura base del código.  
- Principios fundamentales para el desarrollo de videojuegos 2D.  

---

## Posibles mejoras  
- Añadir físicas de salto o gravedad.  
- Incorporar animaciones o efectos visuales.  
- Detectar colisiones con objetos adicionales o enemigos.  
- Agregar sonido y música de fondo.  


---

### Autor  
**Diego Flores Ortiz** — Proyecto desarrollado como práctica de programación en **Python con pygame**.  
_(Se usó la ayuda de la inteligencia artificial para mejorar la explicación de la funcionalidad del código)_
