

with open("input.txt", "r") as file:
    position = 50
    password = 0
    for line in file:
        instruction = line.strip()
        direction = instruction[0]
        distance = int(instruction[1:])
        print(direction, distance)

        if direction == 'L':
            position = position - distance
            while position < 0:
                position = 100 + position
        else:
            position = position + distance
            position = position % 100

        print(position)
        if position == 0:
            password = password + 1

    
    print("Passsword:", password)