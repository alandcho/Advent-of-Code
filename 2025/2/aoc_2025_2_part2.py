

def is_invalid_id(id: str):
    id_len = len(id) 
    max_number_per_section = int(id_len / 2)
    for number_per_section in range(max_number_per_section, 0, -1):
        if id_len % number_per_section != 0: # if cannot equally divide into n part continue
            continue
        parts = [id[i:i+number_per_section] for i in range(0, id_len, number_per_section)]
        # print(parts)
        
        if all(x == parts[0] for x in parts):
            return False
        
    return True



with open("input.txt", "r") as file:
    result = 0
    id_ranges = file.read().split(sep=",")

    for id_range in id_ranges:
        id_range_arr:str = id_range.split(sep="-")
        start_range:str = id_range_arr[0]
        end_range:str = id_range_arr[1]
        # print(f"raw:{id_range} start: {start_range} end: {end_range}")

        for i in range(int(start_range), int(end_range) + 1):
            is_valid = is_invalid_id(str(i))
            if not is_valid:
                #print(f"{i} is not valid id")
                result = result + i

    print(f"Result {result}")





    