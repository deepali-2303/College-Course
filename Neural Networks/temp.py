import turtle


t = turtle.Turtle()
t.speed(0) 


t.begin_fill()
t.fillcolor("red")
t.left(50)
t.forward(133)
t.circle(50, 200)
t.right(140)
t.circle(50, 200)
t.forward(133)
t.end_fill()


text_x = t.xcor()
text_y = t.ycor() - 60 


t.penup()
t.goto(text_x, text_y)
t.pendown()
t.color("black")
t.write("I Love You Jayant", align="center", font=("Arial", 12, "bold"))


t.hideturtle()
turtle.done()
