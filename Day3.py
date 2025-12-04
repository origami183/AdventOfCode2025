file = 'day3_input.txt'
# file = 'temp.txt'

def part1():
    with open(file) as f:
        biggest = {}
        index = 0
        for line in f:
            biggest[index] = 0
            lineLength = len(line)
            for i in range(lineLength-1):
                digitOne = line[i:i+1]
                rest = line[i+1:]
                for j in range(len(rest)):
                    digitTwo = rest[j:j+1]
                    merge = int(f"{digitOne}{digitTwo}")
                    if merge > biggest[index]:
                        biggest[index] = merge
            index += 1
        total = 0
        for value in biggest:
            total += biggest[value]
        print(total)

def part2():
    with open(file) as f:
        biggest = {}
        index = 0
        numLen = 12
        for line in f:
            line = line.strip()
            biggest[index] = 0
            temp = ""
            lineLength = len(line)
            start = 0
            for _ in range(numLen):
                remain = numLen-len(temp)
                end = lineLength - remain
                best = '0'
                best_index = start
                for i in range(start, end+1):
                    if line[i] > best:
                        best = line[i]
                        best_index = i
                temp += best
                start = best_index + 1
            biggest[index] = int(temp)
            index += 1
        total = 0
        for value in biggest:
            total += biggest[value]
        print(total)


part1()
part2()