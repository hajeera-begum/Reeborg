#Works for Tokens1, Tokens2, Tokens3, Tokens4 
def collect_all():
    while object_here():
        take()
        move()
def put_down_all_and_move():
    while carries_object():
        put()
    move()
while not at_goal():
    if object_here():
        collect_all()
    elif carries_object():
        put_down_all_and_move()
    else:
        move()
    
        
        
