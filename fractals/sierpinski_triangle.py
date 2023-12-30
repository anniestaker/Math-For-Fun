import turtle

def draw_triangle(length, depth):
    if depth == 0:
        turtle.forward(length)
        turtle.left(120)
        turtle.forward(length)
        turtle.left(120)
        turtle.forward(length)
        turtle.left(120)
    else:
        draw_triangle(length / 2, depth - 1)
        turtle.forward(length / 2)
        draw_triangle(length / 2, depth - 1)
        turtle.left(180)
        turtle.forward(length / 2)
        turtle.right(120)
        turtle.forward(length / 2)
        turtle.right(60)
        draw_triangle(length / 2, depth - 1)
        turtle.right(120)
        turtle.forward(length / 2)
        turtle.left(120)

startingX = -200
startingY = -100
length = 400
depth = 6

turtle.speed(0)
turtle.penup()
turtle.goto(startingX, startingY)
turtle.pendown()

draw_triangle(length, depth)

turtle.hideturtle()
turtle.done()