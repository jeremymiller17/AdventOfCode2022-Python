def parse_lines(file):
    with open("input.in") as file:
        lines = [i for i in file.read().strip().split('\n')]
    return lines

file_input = parse_lines("input.in")
current_directory = ["/"]
total_size = {}


for line in file_input:
    line = line.split(" ")
    if line[0] == "$":
        if line[1] == "cd" and line[2] != "..":
            current_directory.append(line[2])
        elif line[1] == "cd" and line[2] == "..":
            current_directory.pop()
    else:
        if line[0] != "dir":
            for directory in current_directory:
                if directory == "/":
                    path = directory
                else:
                    path += directory + "/"
                if path in total_size:
                    total_size[path] += int(line[0])
                else:
                    total_size[path] = int(line[0])

# Sums all file sizes in 'total_size' that are less than or equal to 100000
def part1(size_dict):
    total_memory = 0
    for path in size_dict:
        if size_dict[path] <= 100000:
            total_memory += size_dict[path]
    
    print("Day7 part1:",total_memory)

# Compares values of 'total_size' if file size is greater than space required for update. Appends to list
# of possible files to delete which is then sorted returning the first index.
def part2(size_dict):
    potential_del = []
    memory_quota = (70000000 - size_dict["/"] - 30000000 ) * -1;
    
    for path in size_dict:
        sorted(size_dict.values())
        if size_dict[path] > memory_quota:
            potential_del.append(size_dict[path])
    
    potential_del.sort()
    print("Day7 part2:", potential_del[-1])

   

part1(total_size)
part2(total_size)