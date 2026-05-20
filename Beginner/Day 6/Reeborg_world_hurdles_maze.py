#HURDLE 1: JUMPING OVER HURDLES (WHILE LOOP)
# REEBORG WORLD (RUN THIS CODE THERE AS PARTICULAR FUNCTIONS ARE DEFINED THERE.

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1


HURDLE 2: VARYING HURDLE COMPLETION POSITION
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while at_goal() != True:
    jump()

HURDLE 3: VARYING HURDLE POSITION AND VARYING HURDLE NUMBERS
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while at_goal() != True:
    if front_is_clear() == True:
        move()
    else:
        jump()


HURDLE 4: ALL PREVIOUS CONDITIONS AND HURDLES OF VARYING LENGTH
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while front_is_clear():
        if wall_on_right() == True:
            move()
        else:
            turn_right()
            move()
            turn_right()
            move()
    turn_left()


while at_goal() != True:
    if front_is_clear() == True:
        move()
    else:
        jump()



MAZE PROJECT:
def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if not wall_on_right():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()