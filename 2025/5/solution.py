import _io

class Interval:
    def __init__(self, start: int, end: int):
        self.start: int = start
        self.end: int = end

    def __str__(self):
        return f"{self.start}-{self.end}"
    
    def merge(self, interval: "Interval"):
        self.start = min(self.start, interval.start)
        self.end = max(self.end, interval.end)

    def is_overlap(self, interval: "Interval") -> bool:
        return (interval.start <= self.end and interval.start >= self.start) or (self.start <= interval.end and self.start >= interval.start) 
    
    def in_the_interval(self, value: int) -> bool:
        return value >= self.start and value <= self.end
    

    __repr__ = __str__

def read_input(file: _io.TextIOWrapper) -> tuple[list[Interval], list[int]]:
    fresh_ids = []
    ids = []
    parse_fresh = True

    for line in file.read().splitlines():
        if line == "":
            parse_fresh = False
            continue

        if parse_fresh:
            interval = line.split("-")
            fresh_ids.append(Interval(int(interval[0]), int(interval[1])))
        else:
            ids.append(int(line))
    return fresh_ids, ids

def merge_interval(intervals:list[Interval]) -> list[Interval]:

    sorted_intervlas = sorted(intervals, key=lambda interval: interval.start)

    print(sorted_intervlas)

    result: list[Interval] = []
    result.append(sorted_intervlas[0])

    for interval in sorted_intervlas[1:]:
        if result[-1].is_overlap(interval):
            result[-1].merge(interval)
        else:
            result.append(interval)

    return result

with open("input.txt", "r") as file:    
    fresh_ids, ids = read_input(file)
    
    print(f"Fresh: {fresh_ids}")
    print(f"Ids: {ids}")

    merged_interval = merge_interval(fresh_ids)
    print(f"Merged: {merged_interval}")

    result: int = 0
    for id in ids:
        for interval in merged_interval:
            if interval.in_the_interval(id):
                result += 1
                break
            
    print(f"Result: {result}")