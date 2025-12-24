def turn_right():
    for i in range(3):
        turn_left()
    
turn_left()
move()
move()
turn_right()
move()

def collect():
    if object_here():
        take()
def harvest(num):
    for i in range(num):
        move()
        collect()
def step_up(direction):
    direction()
    move()
    direction()
    collect()
harvest(6)
for i in range(2):
    step_up(turn_left)
    harvest(5)
    step_up(turn_right)
    harvest(5)
step_up(turn_left)
harvest(5)
