def parse_lines(file):
    with open("input.in") as file:
        lines = [i for i in file.read().strip().split('\n')]
    return lines

def rummage_bag(inventory):
    totals = []
    for rucksack in inventory:
        left,right = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
        common =list(set(left)&set(right))
        totals.append(case_check(common[0]))
    
    return totals

def find_badge(inventory):
    priority_sum = 0
    
    for three_rucks in range(int(len(inventory)/3)):
        bag1 = inventory[three_rucks*3]
        bag2 = inventory[1 + three_rucks*3]
        bag3= inventory[2 + three_rucks*3]
        common = set(bag1).intersection(set(bag2)).intersection(set(bag3))
        
        priority_sum += case_check(next(iter(common)))
    return priority_sum
    
    
# Found shift value by subtracting ascii value from request value.S
def case_check(character):
    lowercase_shift = 96
    uppercase_shift = 38
    if ord(character) < ord('a'):
        return ord(character) - uppercase_shift
    else:
        return ord(character) - lowercase_shift



print("Day3 part 1:",sum(rummage_bag(parse_lines("input.in"))))
print("Day3 part 2:",find_badge(parse_lines("input.in")))