import turtle
turtle.goto(0,0)

turtle.direction = None

def on_move():
    position = turtle.pos()
    x = position[0]
    y = position[1]    
    if turtle.direction == "Up":
        turtle.goto(x, y + 50)
    if turtle.direction == "Down":
        turtle.goto(x, y - 50)
    if turtle.direction == "Right":
        turtle.goto(x + 50, y)
    if turtle.direction == "Left":
        turtle.goto(x - 50, y)

def up():
    turtle.direction = "Up"
    on_move()
    print("you pressed the up key")
turtle.onkey(up, "Up")


def down():
    turtle.direction = "Down"
    on_move()
    print("you pressed the down key")  
turtle.onkey(down, "Down")

def left():
    turtle.direction = "Left"
    on_move()
    print("you pressed the left key")  
turtle.onkey(left, "Left")


def right():
    turtle.direction = "Right"
    on_move()
    print("you pressed the right key")  
turtle.onkey(right, "Right")
turtle.listen()

turtle.mainloop()
