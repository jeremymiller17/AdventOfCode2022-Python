def parse_lines_from_input(file):
    with open("input.in") as file:
        lines = [i for i in file.read().strip().split('\n')]
    return lines


lines = parse_lines_from_input("input.in")

part1_counter = 0
part2_counter = 0

for line in lines:
    left,right = line.split(",")
    l1,l2 = left.split("-")
    r1,r2 = right.split("-")
    l1,l2,r1,r2 = [int(x) for x in [l1,l2,r1,r2]]
    if not (l2 < r1 or r2 < l1):
        part2_counter += 1
    if (l1 <= r1 and r2 <= l2) or (r1 <= l1 and l2<= r2):
        part1_counter += 1

print("Day4 part 1:",part1_counter)
print("Day4 part 2:",part2_counter)

