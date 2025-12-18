def jump():
    move()
    move()
    move()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def L_shape():
    jump()
    turn_left()
    jump()
    while at_goal():
        done()
    turn_right()
    move()
    turn_right()
for i in range(4):
        L_shape()
