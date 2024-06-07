import turtle

# Set up the screen
win = turtle.Screen()
win.bgcolor("white")

# Create a turtle object
flag = turtle.Turtle()
flag.speed(1)  # Set the speed of the turtle

# Draw the saffron color (top stripe)
flag.penup()
flag.goto(-150, 75)
flag.pendown()
flag.color("orange")
flag.begin_fill()
for _ in range(2):
    flag.forward(300)
    flag.right(90)
    flag.forward(50)
    flag.right(90)
flag.end_fill()

# Draw the white color (middle stripe)
flag.penup()
flag.goto(-150, 25)
flag.pendown()
flag.color("white")
flag.begin_fill()
for _ in range(2):
    flag.forward(300)
    flag.right(90)
    flag.forward(50)
    flag.right(90)
flag.end_fill()

# Draw the green color (bottom stripe)
flag.penup()
flag.goto(-150, -25)
flag.pendown()
flag.color("green")
flag.begin_fill()
for _ in range(2):
    flag.forward(300)
    flag.right(90)
    flag.forward(50)
    flag.right(90)
flag.end_fill()

# Draw the blue chakra (wheel)
flag.penup()
flag.goto(-25, -25)
flag.pendown()
flag.color("blue")
flag.begin_fill()
flag.circle(25)
flag.end_fill()

# Draw the 24 spokes of the chakra
flag.color("white")
for _ in range(24):
    flag.penup()
    flag.goto(0, -25)
    flag.pendown()
    flag.forward(25)
    flag.penup()
    flag.goto(0, -25)
    flag.right(15)

# Hide the turtle and close the window
flag.hideturtle()
win.mainloop()
