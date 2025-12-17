move()
while not at_goal():
    if object_here():
        take()
    
    if wall_in_front():
        turn_left()
    move()
