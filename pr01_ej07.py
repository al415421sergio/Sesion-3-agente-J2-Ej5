from turtle import *
pan = Screen()
pan.setup(425,225)
pan.screensize(400,200)
#datos y calculos
tortuga = Turtle()
sus = int(input('Dime el numAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAe sus: '))
aprobados = int(input('Dime el numero de aprobados: '))
notables = int(input('Dime el numero de notables: '))
sobresalientes = int(input('Dime el numero de sobresalientes: '))
total = sus+aprobados+notables+sobresalientes
p_sus = (sus/total)*100
p_aprobados = (aprobados/total)*100
p_notables = (notables/total)*100
p_sobresalientes = (sobresalientes/total)*100
#angulos
angulo_sus = p_sus*360/100
angulo_apr = p_aprobados*360/100
angulo_not = p_notables*360/100
angulo_sob = p_sobresalientes*360/100
#sus
tortuga.penup()
tortuga.goto(0,0)
tortuga.pencolor('red')
tortuga.pendown()
tortuga.forward(150)
tortuga.left(90)
tortuga.circle(150,angulo_sus)
tortuga.penup()
tortuga.goto(0,0)

tortuga.right(90+angulo_sus/2)
tortuga.forward(150/2)
tortuga.write('sus')
tortuga.backward(150/2)
tortuga.left(90+angulo_sus/2)
tortuga.right(90)

#aprobados
tortuga.pencolor('green')
tortuga.pendown()
tortuga.forward(150)
tortuga.left(90)
tortuga.circle(150,angulo_apr)
tortuga.penup()
tortuga.goto(0,0)

tortuga.right(90+angulo_apr/2)
tortuga.forward(150/2)
tortuga.write('aprobados')
tortuga.backward(150/2)
tortuga.left(90+angulo_apr/2)
tortuga.right(90)

#notables
tortuga.pencolor('yellow')
tortuga.pendown()
tortuga.forward(150)
tortuga.left(90)
tortuga.circle(150,angulo_not)
tortuga.penup()
tortuga.goto(0,0)

tortuga.right(90+angulo_not/2)
tortuga.forward(150/2)
tortuga.write('notables')
tortuga.backward(150/2)
tortuga.left(90+angulo_not/2)
tortuga.right(90)

#sobresalientes
tortuga.pencolor('blue')
tortuga.pendown()
tortuga.forward(150)
tortuga.left(90)
tortuga.circle(150,angulo_sob)
tortuga.penup()
tortuga.goto(0,0)

tortuga.right(90+angulo_sob/2)
tortuga.forward(150/2)
tortuga.write('sobresalientes')
tortuga.backward(150/2)
tortuga.left(90+angulo_sob/2)
tortuga.right(90)
