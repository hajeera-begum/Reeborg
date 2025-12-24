def turn_right():
    turn_left()
    turn_left()
    turn_left()
turn_left()
move()
move()
turn_right()
move()

def object():
    if object_here():
        take()
def harvest_one_row(num):
    for i in range(num):
        move()
        object()

harvest_one_row(6)
for i in range(2):
    turn_left()
    move()
    turn_left()
    object()
    harvest_one_row(5)
    turn_right()
    move()
    turn_right()
    object()
    harvest_one_row(5)
turn_left()
move()
turn_left()
object()
harvest_one_row(5)
