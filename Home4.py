def jump():
    move()
    move()
    move()
​
def inner_wall():
    turn_left()
    jump()
​
def turn_right():
    turn_left()
    turn_left()
    turn_left()
​
def outer_wall():
    turn_right()
    move()
    turn_right()
​
for i in range(3):
    jump()
    inner_wall()
    outer_wall()
​
jump()
inner_wall()
    
