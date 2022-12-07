def parse_lines(file):
    with open("input.in") as file:
        lines = [i for i in file.read().strip().split('\n')]
    return lines

# TODO:Hardcoded parser, refactor to be dynamic for any amount of input
lines = parse_lines("input.in")
stack_input= lines[:8]
movement_input =lines[10:]

# TODO: Refactor stack builder to be dynamic. See above!
# Stacks are built into a list of list based on size. '9'
stacks = [[] for _ in range (9)]
print(stacks)
# Four characters = one 'crate'
for row in stack_input:
    for i in range(0, len(row), 4):
        # Stack posistion based on multiples of four.
        #[W] [Z]
        #12341234
        index = i // 4
        moving_crate = row[i:i+4] 
        if moving_crate[1] != " ":  
            # Append to stacks list at 'index' with char value
            stacks[index].append(moving_crate[1])
        
print(stacks)





#print(stack_input)
#print(movement_input)