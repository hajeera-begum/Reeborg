put()
move()
​
def turn_right():
    turn_left()
    turn_left()
    turn_left()
​
while not object_here():
    if front_is_clear():
        move()
    if wall_in_front():
        turn_left()
    if right_is_clear():
        turn_right()
​
take()
