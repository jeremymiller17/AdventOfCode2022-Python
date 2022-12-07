
with open("input.in") as file:
    calories = [i for i in file.read().strip().split('\n')]

def calorie_counter(calories):
    inventory = []  
    counter = 0
    for line in calories:
        if line == "":
            inventory.append(counter)
            counter = 0
            
        else:
            counter += int(line)
    
    inventory.sort()
    return inventory

# Results
print("Part 1:",calorie_counter(calories)[-1])
print("Part 2:",sum(sorted(calorie_counter(calories),reverse=True)[:3]))
