import turtle


window = turtle.Screen()
window.bgcolor('black')
turtle.title("John Lorenz Leonor BSCS 1A")


t = turtle.Turtle()
t.speed(0)
penSize = 4
t.pensize(penSize)
outrad = 300


t.up()
t.goto(0,-(outrad))
t.down()
t.color('white')
t.circle(outrad)


for i in range(15):
    for colors in ("red", "yellow", "blue"):
        t.goto(0,0)
        t.color(colors)
        t.pensize(3)
        t.left(12)
        t.forward(220)
        t.left(90)
        t.forward(220)
        t.left(90)
        t.forward(220)
        t.left(90)


t.pensize(3)
t.goto(0,0)
t.down()
t.pencolor("green")
for j in range(20): 
	t.right(360/20)
	t.color('green')
	for i in range(4):
		t.forward(210)
		t.left(90)
	t.end_fill()

t.up()
t.goto(0,0)
t.down()
t.pencolor("blue")
for j in range(10): 
	t.right(360/10)
	for i in range(8):
		t.forward(75)
		t.left(360/8)
	t.end_fill()


t.up()
t.pensize(3)
t.goto(0,0)
t.down()
t.pencolor('red')
for i in range (40):
        t.circle(100-i,90)
        t.left(90)
        t.circle(100-i,90)
        t.left(15)
t.end_fill()



turtle.exitonclick()
