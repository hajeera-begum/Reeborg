#This is for 6*6 grid Storm2. A different approach

def turn_right():
    repeat 3:
        turn_left()
wall_count=0
def go_home():
    turn_left()
    move()
    turn_right()
    move()
    move()
    turn_right()
    move()
while not wall_count==7:
    if front_is_clear():
        move()
        while object_here():
            take()
    elif not front_is_clear():
        if wall_in_front():
            wall_count+=1
            if wall_count==1:
                turn_left()
            elif wall_count==7:
                while carries_object():
                    toss()
                go_home()
            elif wall_count>= 2 and wall_count%2==0:
                turn_left()
                move()
                while object_here():
                    take()
                turn_left()
            elif wall_count % 2!=0:
                turn_right()
                move()
                while object_here():
                    take()
                turn_right()
