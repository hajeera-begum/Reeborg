#This code works for Center1 and all edge cases i.e., x=1,y=N & x=N,y=1, x=1,y=1
height=0
width=0

def found_centre():
    if front_is_clear() and wall_on_right(): 
        w=round(width/2)
        for i in range(w):
            move()
        put()
        done()
    
    turn_left()
    w=round(width/2)
    for i in range(w):
        move()
    turn_left()
    h=round(height/2)
    for i in range(h):
        move()
    put()
    done()
while True:
    if wall_in_front():
        turn_left()
        if wall_in_front():
            turn_left()
            height=1
            if front_is_clear():
                found_centre()
            if wall_in_front():
                width=1
            if height==width:
                found_centre()

    elif not is_facing_north():
         move()
         width+=1
    elif is_facing_north():
         move()
         height+=1
         if wall_in_front():
            found_centre()
