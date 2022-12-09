#Excited to try numpy for this problem.
import numpy as np

tree_patch = np.array(
    #Posistional arguement. Key arguements must go after posistional.
    [
        list(trees)
        #Reads through input, strips, and splits into list
        for trees in open("input.in", "r")
        .read()
        .strip()
        .splitlines()
    ],
    #key array arguement
    dtype=int,
    
)




#Checks the sum of elements remaining directionally in the row >= current_tree .
# then checks result is >= 1. If >= return false, else tree is visisble. 
def isVis(row,col):
    current_tree = tree_patch[row,col]
    # Check row  east
    if (np.sum(tree_patch[row,col + 1 :] >= current_tree) >= 1 and
        # Check row west
        np.sum(tree_patch[row,:col] >= current_tree) >= 1 and
            # Check colum  north
            np.sum(tree_patch[:row,col] >= current_tree) >= 1 and
                # Check colum south
                np.sum(tree_patch[row + 1 :,col] >= current_tree) >= 1
    ):
        return False
    else:
        return True

size = len(tree_patch) -1

# Starting visible tree counter with edges included
vis = 4 * (size)

# Run each element excluding edges
for row in range(1,size):
    for col in range (1,size):
        if isVis(row,col):
            vis += 1

print(vis)

def tree_scores(row,col):
    current_tree = tree_patch[row,col]
    East = tree_patch[row, col + 1:] >= current_tree
    West = tree_patch[row,:col] >= current_tree
    North = tree_patch[:row,col] >= current_tree
    South = tree_patch[row +1 :, col] >= current_tree

    # Iterate through each direction from tree, and generate score
    points,score = 0,1
    #Check trees to the east
    for i in range(len(East)):
        if len(East) < 1:
            break
        points += 1
        if East[i] == True:
            break
    score *= points
    points = 0

    #Check trees to the west
    for i in range(len(West)-1,-1,-1): #Reverse the range
        if len(West) < 1:
            break
        points += 1
        if West[i] == True:
            break
    score *= points
    points = 0
    
    #Check trees to the north
    for i in range(len(North)-1,-1,-1): # Reverse the range
        if len(North) < 1:
            break
        points += 1
        if North[i] == True:
            break
    score *= points
    points = 0

    #Check trees to the south
    for i in range(len(South)):
        if len(South) < 1:
            break
        points += 1
        if South[i] == True:
            break
    score *= points

    return [score]
    
trees = []   

size = len(tree_patch)
for row in range(size):
    for col in range(size):
        trees+=tree_scores(row,col)

print(max(trees))





