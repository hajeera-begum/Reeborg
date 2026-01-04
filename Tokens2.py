while not at_goal():
    move()
    if object_here():
        take()
    elif carries_object():
        put()
