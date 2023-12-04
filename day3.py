import re, math

def read_puzzle(file):
    with open(file) as f:
        return [row.strip() for row in f]

def numPos(matches):
    return [(int(match.group()), match.span()) for match in matches]

def isValid(puzzle, row, col):
    return row >= 0 and col >= 0 and row < len(puzzle) and col < len(puzzle[0])

def adjacents(puzzle, row, col):
    indices = [(row - 1, col), (row + 1, col), (row + 1, col - 1), (row + 1, col + 1), 
                (row, col - 1), (row, col + 1), (row - 1, col - 1), (row - 1, col + 1)]
    return [(row, col) for row, col in indices if isValid(puzzle, row, col)]

def isSymbol(s):
    lst = re.findall(r'[^0-9.\n]', s)
    return True if lst else False


def solve(puzzle):
    part1 = []
    for row, line in enumerate(puzzle):
        numbers = numPos(re.finditer(r'\d+', line))
        for number, (start, end) in numbers:
            isPartNumber = False
            for col in range(start, end):
                adj = adjacents(puzzle, row, col)
                if isPartNumber: break
                for r, c in adj:
                    if isSymbol(puzzle[r][c]):
                      isPartNumber = True
                      part1.append(int(number))
                      break
    part1 = sum(part1)

    answer2 = []
    for row, line in enumerate(puzzle):
        gears = re.finditer(r'\*', line)

        for pos in gears:
            col = pos.span()[1]-1
            rowLst = [row]
            if row-1 >= 0: rowLst.append(row-1)
            if row+1 < len(puzzle): rowLst.append(row+1)
            tmpLst = []
            for rrr in rowLst:
                numbers = numPos(re.finditer(r'\d+', puzzle[rrr]))
                for n, (start, end) in numbers:
                    if rrr == row:
                        if col-1 in range(start,end) or col+1 in range(start,end):
                            tmpLst.append(int(n))
                    else:
                        if col-1 in range(start,end) or col+1 in range(start,end):
                            tmpLst.append(int(n))
            if len(tmpLst) == 2:
                answer2.append(math.prod(tmpLst))
    part2 = sum(answer2)

    return part1, part2

if __name__ == "__main__":
    print(solve(read_puzzle("day3.txt")))
