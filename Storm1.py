def turn_right():
    repeat 3:
        turn_left()
move()
repeat 5:
    while object_here():
        take()
    
    if wall_in_front():
        turn_left()
        turn_left()
        repeat 5:
            move()
        turn_right()
        while carries_object():
            toss()
        break
    move()
