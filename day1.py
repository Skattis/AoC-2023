import re

def read_puzzle(file):
    with open(file) as f:
        return [row.strip() for row in f]
    
def solve(puzzle):
    digit_lists = [re.findall(r'\d', line) for line in puzzle]
    part1 = sum(int(digit[0]+digit[-1])for digit in digit_lists)

    number_mapping = {"one": '1',"two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9", 
               "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9"}
    digit_lists_from_words = []

    for line in puzzle:
        digits_from_words = []
        for i in range(len(line)):
            for word, digit in number_mapping.items():
                if line[i:].startswith(word):
                    digits_from_words.append(digit)
                    break
        digit_lists_from_words.append(digits_from_words)

    part2 = sum(int(digits[0] + digits[-1]) for digits in digit_lists_from_words)

    return part1, part2

if __name__ == "__main__":
    print(solve(read_puzzle("day1.txt")))
