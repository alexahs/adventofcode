with open("input.txt", "r") as infile:
    data = []
    for line in infile:
        data.append(line.rstrip("\n"))
    m = len(data[0])

def task1():
    k = 0
    count = 0
    for i in range(len(data)):
        j = k % m
        count += False or data[i][j] == '#'
        k += 3
    print(f"(1) Number of tree encounters: {count}")

def task2():
    jumps = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    prod = 1
    for y, x in jumps:
        count = 0
        k = 0
        for i in range(0, len(data), x):
            j = k % m
            count += False or data[i][j] == '#'
            k += y
        prod *= count
    print(f"(2) Product of tree encounters: {prod}")

task1()
task2()
