import turtle
tao = turtle.Pen()
tao.shape('turtle')
tao.color('green')

turtle.bgcolor('light blue')
def Circle():
    for i in range(8):
        tao.circle(60)
        tao.left(40)

def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

Go(200,200)
Circle()
Go(200,-200)
Circle()
Go(-200,200)
Circle()
Go(-200,-200)
Circle()



