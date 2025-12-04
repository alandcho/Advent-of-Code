

def is_invalid_id(id: str):
    id_len = len(id) 
    if id_len % 2 != 0:
        return True
    
    mid = int(id_len / 2)
    print(f"id: {id} mid: {mid}")
    
    print(f"digit: {id[0:mid]} {id[mid:]}")

    return id[0:mid] != id[mid:]

with open("input.txt", "r") as file:
    result = 0
    id_ranges = file.read().split(sep=",")

    for id_range in id_ranges:
        id_range_arr:str = id_range.split(sep="-")
        start_range:str = id_range_arr[0]
        end_range:str = id_range_arr[1]
        print(f"raw:{id_range} start: {start_range} end: {end_range}")

        for i in range(int(start_range), int(end_range) + 1):
            is_valid = is_invalid_id(str(i))
            if not is_valid:
                print(f"{i} is not valid id")
                result = result + i

    print(f"Result {result}")





    