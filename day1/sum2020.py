import numpy as np
input = np.loadtxt('input.txt', dtype='int64')
n = len(input)

def part1():
    for i in range(n-1):
        for j in range(i + 1, n):
            if input[i] + input[j] == 2020:
                prod = input[i] * input[j]
                print("Answer:", prod)


def part2():
    for i in range(n-2):
        for j in range(i + 1, n-1):
            for k in range(j + 1, n):
                if input[i] + input[j] + input[k] == 2020:
                    prod = input[i] * input[j] * input[k]
                    print("Answer:", prod)


# part1()
part2()
