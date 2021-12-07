import numpy as np




def num_fish(arr, days):
    next_spawn = 0
    for i in range(0, days):
        new_fish = 0
        print(f"Day {i}")
        for j in range(len(arr)):
            if arr[j] > 0:
                arr[j] -= 1
            else:
                arr[j] = 6
                new_fish += 1
        for j in range(new_fish):
            arr.append(8)
            
    print(f"Num fish after {days} days: {len(arr)}")

def num_fish_opt(arr, days):

    counts = {i:0 for i in range(9)}
    for x in arr:
        counts[x] += 1
    for day in range(days):
        new_counts = {i:0 for i in range(9)}
        for k, v in counts.items():
            if k == 0:
                new_counts[6] += v
                new_counts[8] += v
            else:
                new_counts[k-1] += v
        counts = new_counts

    final_count = sum([c for c in counts.values()])
    print(f"Num fish after {days} days: {final_count}")



def main():
    inp = open("in", "r").readlines()[0].strip()
    inp = list(map(int, inp.split(",")))
    num_fish_opt(inp, 256)



if __name__ == '__main__':
    main()
