def turn_right():
    for i in range(3):
        turn_left()
while not at_goal():
    if wall_in_front():
        turn_left()
    elif is_facing_north():
        move()
        if right_is_clear():
           turn_right()
           move()
           turn_right()
           move()
    else:
        move()
