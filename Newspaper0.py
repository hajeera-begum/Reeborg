def turn_right():
    for i in range(3):
        turn_left()
def climb_up():
    for i in range(2):
        move()
   
take()

def movement(steps):
    for i in range(steps):
        turn_left()
        move()
        turn_right()
        climb_up()
movement(3)
put()
turn_left()
turn_left()
def climb_down():
    climb_up()
    movement(2)

climb_down()
turn_left()
move()
