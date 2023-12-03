import re
import math as m

def read_puzzle(file):
    with open(file) as f:
        return [row.strip() for row in f]

def solve(puzzle):
    configuration = {"red": 12, "green": 13, "blue": 14}
    lstPart1 = []

    for row in puzzle:
        colours = re.findall("red|green|blue", row)
        amounts = re.findall(r"\d+", row)
        ids = amounts.pop(0)
        add = True

        for cols, ams in zip(colours, amounts):
            if configuration[cols] < int(ams):
                add = False
                break
        if add:
            lstPart1.append(int(ids))
    
    part1 = sum(lstPart1)

    lstPart2 = []
    for row in puzzle:
        maxAmountsPart2 = {"red": 0, "green": 0, "blue": 0}
        colours = re.findall("red|green|blue", row)
        amounts = re.findall(r"\d+", row)
        ids = amounts.pop(0)

        for cols, ams in zip(colours, amounts):
            if maxAmountsPart2[cols] < int(ams):
                maxAmountsPart2[cols] = int(ams)
        lstPart2.append(m.prod([int(v) for v in maxAmountsPart2.values()]))

    part2 = sum(lstPart2)
    return part1, part2

if __name__ == "__main__":
    print(solve(read_puzzle("day2.txt")))
