file = 'day5_input.txt'
# file = 'temp.txt'

def getData():
    freshIDs = []
    available = []
    with open(file) as f:
        blank = False
        for line in f:
            if len(line) < 2:
                blank = True
                continue
            
            if blank:
                available.append(int(line))
            else:
                values = line.strip().split("-")
                idRange = [int(values[0]), int(values[1])]
                freshIDs.append(idRange)
    return freshIDs, available

def part1():
    freshIDs, avail = getData()
    freshIngred = 0
    for ingred in avail:
        for idRange in freshIDs:
            if idRange[0] <= ingred <= idRange[1]:
                freshIngred += 1
                break
    print(freshIngred)

def part2():
    freshIDs, _ = getData()
    freshIDs.sort()
    merge = []
    start, end = freshIDs[0]

    for tempStart, tempEnd in freshIDs[1:]:
        if tempStart <= end + 1:
            end = max(end, tempEnd)
        else:
            merge.append((start, end))
            start, end = tempStart, tempEnd
    
    merge.append((start, end))
    total = 0
    for s, e in merge:
        total += (e - s + 1)
    print(total)            

part1()
part2()