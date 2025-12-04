def read_input(file):
    map = []
    for line in file.read().splitlines():
        row = [c for c in line]
        map.append(row)

    return map

def count_neighbor(input_map, i, j, n, m):
    neighbor = 0

    for y in range(i-1, i+2):
        for x in range(j-1, j+2):
            if y < 0 or y >= n or x < 0 or x >= m:
                continue
            if x == j and y == i:
                continue
            if input_map[y][x] == '@':
                neighbor += 1

    return neighbor

def count_accessible_rolls(input_map):
    result = 0
    n = len(input_map)
    m = len(input_map[0])

    for i in range(n):
        for j in range(m):
            if input_map[i][j] == '@' and count_neighbor(input_map, i, j, n, m) < 4:
                input_map[i][j] = 'X'
                result += 1

    return result


with open("input.txt", "r") as file:    
    input_map = read_input(file)
    all_result = 0 
    result = count_accessible_rolls(input_map)
    all_result += result
    while result != 0:
        result = count_accessible_rolls(input_map)
        all_result += result

    print("Result:", all_result)