def highest_volt(line: str):
    result = 0
    first_digit = 0
    n = len(line)

    for i in range(0, n - 1):
        first_digit = max(first_digit, int(line[i]))
        second_digit = 0
        for j in range(i + 1, n):
            second_digit = max(second_digit, int(line[j]))
            result = max(result, first_digit * 10 + second_digit)

    return result   


def highest_volt_part_2(line: str, number_of_battery: int):
    result = 0
    bank_size = len(line)

    start_index = 0
    for i in range(number_of_battery):
        battery_needed = (number_of_battery - i) 
        end_index = bank_size - battery_needed
        current_max = 0
        # print(f"start: {start_index}, end: {end_index}")
        for j in range(start_index, end_index+1):
            current_value = int(line[j])
            if current_value > current_max:
                current_max = current_value
                start_index = j + 1

        current_result = (current_max * (10 ** (battery_needed - 1)))
        # print(current_result)
        result =  current_result + result

    print(f"Line: {line}, Result: {result}")

    return result           


with open("input.txt", "r") as file:
    result = 0
    for line in file.read().splitlines():
        #print(line)
        result += highest_volt_part_2(line, 12)
    
    print("Result:", result)