# Programa para imitar el funcionamiento de un caleidoscopio con espejos separados 90 grados
import turtle
import random

# Función para dibujar un triángulo


def dibujarTriangulo(x, y, tamaño, color, orientacion):
    turtle.penup()
    turtle.pensize(10)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)

    if orientacion == 'UR':
        direccion = 0
        giro = 120
    elif orientacion == 'UL':
        direccion = 240
        giro = 120
    elif orientacion == 'DR':
        direccion = 0
        giro = 240
    elif orientacion == 'DL':
        direccion = 180
        giro = 120

    turtle.setheading(direccion)

    for _ in range(3):
        turtle.forward(tamaño)
        turtle.right(giro)

# Función para dibujar un pentágono


def dibujarPentagono(x, y, tamaño, color, orientacion):
    turtle.penup()
    turtle.pensize(10)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)

    if orientacion == 'UR':
        direccion = 0
        giro = 72
    elif orientacion == 'UL':
        direccion = 180
        giro = 288
    elif orientacion == 'DR':
        direccion = 0
        giro = 288
    elif orientacion == 'DL':
        direccion = 180
        giro = 72

    turtle.setheading(direccion)

    for _ in range(5):
        turtle.forward(tamaño)
        turtle.right(giro)

# Función para dibujar un hexágono


def dibujarHexagono(x, y, tamaño, color, orientacion):
    turtle.penup()
    turtle.pensize(10)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)

    if orientacion == 'UR':
        direccion = 0
        giro = 60
    elif orientacion == 'UL':
        direccion = 180
        giro = 300
    elif orientacion == 'DR':
        direccion = 0
        giro = 300
    elif orientacion == 'DL':
        direccion = 180
        giro = 60

    turtle.setheading(direccion)

    for _ in range(6):
        turtle.forward(tamaño)
        turtle.right(giro)

# Función para dibujar un cuadrado


def dibujarCuadrado(x, y, tamaño, color, orientacion):
    turtle.penup()
    turtle.pensize(10)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)

    if orientacion == 'UR':
        direccion = 0
        giro = 90
    elif orientacion == 'UL':
        direccion = 270
        giro = 90
    elif orientacion == 'DR':
        direccion = 90
        giro = 90
    elif orientacion == 'DL':
        direccion = 180
        giro = 90

    turtle.setheading(direccion)

    for _ in range(4):
        turtle.forward(tamaño)
        turtle.right(giro)


# Configuración  de la ventana
turtle.setup(800, 800)
turtle.speed(0)
turtle.hideturtle()

# Configuración de los ejes
turtle.penup()
turtle.goto(0, 300)
turtle.pendown()
turtle.goto(0, -300)
turtle.penup()
turtle.goto(300, 0)
turtle.pendown()
turtle.goto(-300, 0)

# Generando valores aleatorios para el hexagono
x_hex = random.randint(50, 300)
y_hex = random.randint(50, 300)
tamaño_hex = random.randint(50, 150)
color_hex = random.choice(
    ['plum', 'mediumslateblue', 'deeppink', 'magenta', 'blueviolet', 'pink'])

# Dibujando hexagono en el primer cuadrante
dibujarHexagono(x_hex, y_hex, tamaño_hex, color_hex, 'UR')

# Dibujando hexagono en el segundo cuadrante
dibujarHexagono(-x_hex, y_hex, tamaño_hex, color_hex, 'UL')

# Dibujando hexagono en el tercer cuadrante
dibujarHexagono(x_hex, -y_hex, tamaño_hex, color_hex, 'DR')

# Dibujando hexagono en el cuarto cuadrante
dibujarHexagono(-x_hex, -y_hex, tamaño_hex, color_hex, 'DL')

# Generando valores aleatorios para el pentagono
x_pen = random.randint(50, 300)
y_pen = random.randint(50, 300)
tamaño_pen = random.randint(50, 150)
color_pen = random.choice(
    ['cornflowerblue', 'royalblue', 'dodgerblue', 'deepskyblue', 'skyblue', 'darkturquoise'])

# Dibujando pentagono en el primer cuadrante
dibujarPentagono(x_pen, y_pen, tamaño_pen, color_pen, 'UR')

# Dibujando pentagono en el segundo cuadrante
dibujarPentagono(-x_pen, y_pen, tamaño_pen, color_pen, 'UL')

# Dibujando pentagono en el tercer cuadrante
dibujarPentagono(x_pen, -y_pen, tamaño_pen, color_pen, 'DR')

# Dibujando pentagono en el cuarto cuadrante
dibujarPentagono(-x_pen, -y_pen, tamaño_pen, color_pen, 'DL')

# Generando valores aleatorios para el cuadrado
x_cua = random.randint(50, 300)
y_cua = random.randint(50, 300)
tamaño_cua = random.randint(50, 150)
color_cua = random.choice(
    ['limegreen', 'springgreen', 'aquamarine', 'palegreen', 'lightgreen', 'mediumseagreen'])

# Dibujando cuadrado en el primer cuadrante
dibujarCuadrado(x_cua, y_cua, tamaño_cua, color_cua, 'UR')

# Dibujando cuadrado en el segundo cuadrante
dibujarCuadrado(-x_cua, y_cua, tamaño_cua, color_cua, 'UL')

# Dibujando cuadrado en el tercer cuadrante
dibujarCuadrado(x_cua, -y_cua, tamaño_cua, color_cua, 'DR')

# Dibujando cuadrado en el cuarto cuadrante
dibujarCuadrado(-x_cua, -y_cua, tamaño_cua, color_cua, 'DL')

# Generando valores aleatorios para el triangulo
x_tri = random.randint(50, 300)
y_tri = random.randint(50, 300)
tamaño_tri = random.randint(50, 150)
color_tri = random.choice(
    ['crimson', 'coral', 'orangered', 'lightcoral', 'firebrick', 'tomato'])

# Dibujando triangulo en el primer cuadrante
dibujarTriangulo(x_tri, y_tri, tamaño_tri, color_tri, 'UR')

# Dibujando triangulo en el segundo cuadrante
dibujarTriangulo(-x_tri, y_tri, tamaño_tri, color_tri, 'UL')

# Dibujando triangulo en el tercer cuadrante
dibujarTriangulo(x_tri, -y_tri, tamaño_tri, color_tri, 'DR')

# Dibujando triangulo en el cuarto cuadrante
dibujarTriangulo(-x_tri, -y_tri, tamaño_tri, color_tri, 'DL')

# Mantener la ventana abierta hasta cierre manual
turtle.done()
