def parse_lines(file):
    with open("input.in") as file:
        lines = [i for i in file.read().strip().split('\n')]
    return lines

def tally_scores(scores):
    
    points = {'A': 1, 'B': 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
    
    total = []
   
    for score in scores:
        left,right = score.split(" ")
        tally = points[left] - points[right]
        
        if tally == 0:
             total.append(points[right] + 3)
        elif tally == 1 or tally == -2:
            total.append(points[right])
        else:
            total.append(points[right] + 6)

    return total

# Sometimes simplicity is more fun
def elf_guide(scores):
    scoring = { 
            # round score + shape score
        "A X" : 0 + 3,
        "A Y" : 3 + 1,
        "A Z" : 6 + 2,
        "B X" : 0 + 1,
        "B Y" : 3 + 2,
        "B Z" : 6 + 3,
        "C X" : 0 + 2,
        "C Y" : 3 + 3,
        "C Z" : 6 + 1
    }

    score = 0
    for hand in scores:
        score += scoring[hand]


    return score



print("Day2 part1:",sum(tally_scores(parse_lines("input.in"))))

print("Day2 part2:",elf_guide(parse_lines("input.in")))
