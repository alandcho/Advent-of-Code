

with open("input.txt", "r") as file:
    position = 50
    password = 0
    for line in file:
        instruction = line.strip()
        direction = instruction[0]
        distance = int(instruction[1:])
        print(direction, distance)

        if direction == 'L':
            prev_position = position
            position = position - distance
            while position < 0:
                position = 100 + position
                if prev_position != 0 and distance % 100 != 0:
                    password += 1
                prev_position = position
        else:
            position = position + distance

            if position >= 100:
                password = password + int(position / 100)
                if (position % 100 == 0):
                    password = password - 1

            position = position % 100

        if position == 0:
            password = password + 1

        print(f"position: {position} password:{password}")

    
    print("Passsword:", password)