#Works for Tokens1, Tokens2
def turn_around():
    repeat 2:
        turn_left()
while not at_goal():
    if object_here():
        take()
    move()
turn_around()
while carries_object():
    toss()
