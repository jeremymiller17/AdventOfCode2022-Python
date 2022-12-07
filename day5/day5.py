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
stacks = [stack[::-1]for stack in stacks]
        

    # Parse movement_input and find each digit per line.
    # Each line carries three digits, and append them to a list
crane_op = []
for movement in movement_input:
    digits = [int(num) for num in movement.split() if num.isdigit()]
    crane_op.append(digits)

for op in crane_op:
     #correct index
    op[1] -= 1
    op[2] -= 1
    # Operation moves crate from starting stack to desto stack
    for _ in range(op[0]):
         # if starting stack is empty
        if stacks[op[1]]:
            # remove top crate
            crate = stacks[op[1]].pop()
            # Append to desto stack
            stacks[op[2]].append(crate)

print(''.join([stack[-1]for stack in stacks]))

stacks = [[] for _ in range (9)]
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
stacks = [stack[::-1]for stack in stacks]
   
   
   
     # Parse movement_input and find each digit per line.
    # Each line carries three digits, and append them to a list
crane_op = []
for movement in movement_input:
     # number of crates to move -> source -> desto
    digits = [int(num) for num in movement.split() if num.isdigit()]
    crane_op.append(digits)

for op in crane_op:
    #correct index
    op[1] -= 1
    op[2] -= 1
    # Move crates as grop from source ->desto
    if stacks[op[1]]:
        # Pick up crates
        crates = stacks[op[1]][-op[0]:]
        # Remove crates from source
        stacks[op[1]] = stacks[op[1]][:-op[0]]
        # Move crates to desto
        stacks[op[2]] += crates


print(''.join([stack[-1]for stack in stacks]))










#print(stack_input)
#print(movement_input)