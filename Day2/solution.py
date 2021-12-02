# Solution to puzzle 1

# Will handle reading file and setting up directions
def read_input():
    with open('input.txt') as file:        
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        print(lines)

        return lines
read_input()

def get_position():
    directions = read_input()
    # accounts for forward command; keeps track of horizontal pos
    location = 0
    # accounts for up and down commands; up decreases and down increases depth
    depth = 0

    #iterating thru directions
    for i in range(0, len(directions)):

        if ('forward' in directions[i]):
            # gets command from directions list and then casts last char which is amount to go
            location += int(directions[i][-1])

        if ('down' in directions[i]):
            depth += int(directions[i][-1])

        if ('up' in directions[i]):
            depth -= int(directions[i][-1])

    print(location * depth)
get_position()

def get_position_advanced():
    directions = read_input()
    
    aim = 0
    # accounts for forward command; keeps track of horizontal pos
    location = 0
    # accounts for up and down commands; up decreases and down increases depth
    depth = 0

    #iterating thru directions
    for i in range(0, len(directions)):

        if ('forward' in directions[i]):
            # gets command from directions list and then casts last char which is amount to go
            location += int(directions[i][-1])
            depth += (aim * int(directions[i][-1]))
        
        if ('down' in directions[i]):
            aim += int(directions[i][-1])

        if ('up' in directions[i]):
            aim -= int(directions[i][-1])

    print(location * depth)
get_position_advanced()