import turtle
t = turtle.Turtle()

t.up()
t.goto(0, -100)

t.begin_fill()
t.fillcolor("#fff700")
t.circle(100)
t.end_fill()

t.width(10)
t.fillcolor("black")




for i in range(-50, 105, 80):
    t.up()
    t.goto(i, 20)
    t.setheading(0)
    t.down()
    t.begin_fill()
    t.circle(10)
    t.end_fill()

t.hideturtle()
turtle.done()

