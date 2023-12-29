import turtle

def draw_side(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        draw_side(length / 3, depth - 1)
        turtle.left(60)
        draw_side(length / 3, depth - 1)
        turtle.right(120)
        draw_side(length / 3, depth - 1)
        turtle.left(60)
        draw_side(length / 3, depth - 1)

def draw_snowflake(length, depth):
    for _ in range(3):
        draw_side(length, depth)
        turtle.right(120)

turtle.speed(0)
turtle.penup()
turtle.goto(-200, 100)
turtle.pendown()

draw_snowflake(400, 4)

turtle.hideturtle()
turtle.done()