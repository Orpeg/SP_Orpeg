import turtle
bob = turtle.Turtle()
bob.color('blue', 'red')
bob.pu()
bob.goto(0,0)
bob.pd()
bob.begin_fill()
bob.forward(55)
bob.left(90)
bob.forward(110)
bob.end_fill()
bob.pu()

bob.goto(200,0)
bob.pd()
bob.circle(100,50)
bob.pu()

turtle.done()

