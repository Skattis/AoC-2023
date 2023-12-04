from time import perf_counter as pfc

def read_puzzle(file):
    with open(file) as f:
        return [row.strip() for row in f]
    
def solve(puzzle):
    answer = []
    for line in puzzle:
        line = line.split(':')
        game = line[1].split('|')
        winningNumbers, pickedNumbers = game[0].split(), game[1].split()
        matchingNumbers, found = 0, False
        for p in pickedNumbers:
            if p in winningNumbers:
                matchingNumbers += 1
                found = True
        points = 1 * 2**(matchingNumbers-1) if found else 0
        answer.append(points)
    part1 = sum(answer)

    answer = []
    cardDictCopys = {}
    
    for i, line in enumerate(puzzle, 1):
        line = line.split(':')
        game = line[1].split('|')
        winningNumbers, pickedNumbers = game[0].split(), game[1].split()
        matchingNumbers = 0
        cardDictCopys[i] = cardDictCopys.get(i, 0)
        
        for p in pickedNumbers:
            if p in winningNumbers:
                matchingNumbers += 1

        for c in range(i+1, matchingNumbers+i+1):
            extra = cardDictCopys[i]
            cardDictCopys[c] = cardDictCopys.get(c, 0)+ 1 + extra
    
    part2 = sum(v+1 for v in cardDictCopys.values())

    return part1, part2

if __name__ == '__main__':
    print(solve(read_puzzle("day4.txt")))
