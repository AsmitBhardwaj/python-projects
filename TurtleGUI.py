from turtle import Turtle, Screen   

#create a new turtle who is gonna run in a square
evylen_turtle = Turtle()
evylen_turtle.shape("turtle")
evylen_turtle.color("blue")


#square for tutrle
#evylen_turtle.forward(100)
#turn it 90 degree right
#evylen_turtle.right(90)
#move it forward
#evylen_turtle.forward(100)
#evylen_turtle.right(90)
#evylen_turtle.forward(100)
#evylen_turtle.right(90)
#evylen_turtle.forward(100)


#we will use a loop to make the square
for i in range(4):
    evylen_turtle.forward(100)
    evylen_turtle.left(90)

#closes the screen as soon as we click it
Screen().exitonclick()


