put()
for side in range(5):
    while front_is_clear():
        move()
        if object_here():
            take()
            done()
    turn_left()
