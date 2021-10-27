""""
1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *

from freegames import vector


def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circulo(start, end):
    "Draw circle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    
    import turtle
    turtle.circle(end.x - start.x)

    end_fill()


def rectangle(start, end):
    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for i in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)
    
    end_fill()


def triangle(start, end):
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3):
        forward(end.x - start.x)
        left(360/3)

    end_fill()


def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    "Store value in state at key."
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K') #color negro para las figuras
onkey(lambda: color('white'), 'W') #color blanco para las figuras
onkey(lambda: color('green'), 'G') #color verde para las figuras
onkey(lambda: color('blue'), 'B') #color azul para las figuras
onkey(lambda: color('red'), 'R') #color rojo para las figuras
onkey(lambda: color('purple'), 'P') #color morado para las figuras
onkey(lambda: store('shape', line), 'l') #tipo de figura a dibujar: línea
onkey(lambda: store('shape', square), 's') #tipo de figura a dibujar: cuadrado
onkey(lambda: store('shape', circulo), 'c') #tipo de figura a dibujar: círculo
onkey(lambda: store('shape', rectangle), 'r') #tipo de figura a dibujar: rectángulo
onkey(lambda: store('shape', triangle), 't') #tipo de figura a dibujar: triángulo
done()