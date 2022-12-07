def parse_lines(file):
    with open("input.in") as file:
        lines = file.read()
    return lines

def find_sequence(size):
    input = parse_lines("input.in")
    for i,char in enumerate(input):
        # Sets must have unique values.
        #If length of set = specified sequence size, return 'true'.
        if len(set(input[i:i+ size])) == size:
            return i+ size

print("Day6 part1 :",find_sequence(4))
print("Day6 part2 :",find_sequence(14))


    

