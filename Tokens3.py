#Works for Tokens1, Tokens2 aswell
while not at_goal():
    move()
    if object_here():
        take()
    elif carries_object():
        put()
