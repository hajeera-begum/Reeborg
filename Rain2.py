def turn_right():
    repeat 3:
        turn_left()
    
while True:
    if not at_goal():
        move()
    else:
        turn_right()
        move()
        break
while True:
    if not right_is_clear() and front_is_clear():
        move()
    elif not right_is_clear() and not front_is_clear():
        turn_left()
    elif wall_in_front() and right_is_clear():
        turn_right()
        move()
    elif not wall_on_right() and at_goal() and not is_facing_north():
        turn_right()
        build_wall()
        turn_left()
        break
    elif not wall_on_right():
        turn_right()
        build_wall()
        turn_left()
        move()
        if right_is_clear() and not wall_in_front():
            build_wall()
            turn_right()
            move()
            turn_right()
            move()
