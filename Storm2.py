#This works for Storm1 too
def turn_right():
    repeat 3:
        turn_left()
def collect():
    while object_here():
        take()
    move()
def roam(steps):
    for i in range(steps):
        collect()
while not wall_in_front():
    move()
turn_left()
roam(5)
repeat 2:
    turn_left()
    collect()
    turn_left()
    collect()
    roam(4)
    turn_right()
    collect()
    turn_right()
    collect()
    roam(4)
turn_left()
collect()
turn_left()
roam(3)
while object_here():
    take()
while carries_object():
    toss()
    
turn_left()
collect()
turn_right()
move()
move()
turn_right()
move()
