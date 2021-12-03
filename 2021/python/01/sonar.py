


def depth(vals):
    return len([i for i in range(1, len(vals)) if vals[i] > vals[i-1]])

def moving_avg(vals):
    return len([i for i in range(3, len(vals)) if sum(vals[i-3:i]) < sum(vals[i-2:i+1])])


def main():
    with open("input.txt", "r") as fp:
        vals = [int(x.strip("\n")) for x in fp.readlines() if x != "\n"]

    print(f"Number of larger measurements: {depth(vals)}")
    print(f"Number of larger averaged measurements: {moving_avg(vals)}")


if __name__ == '__main__':
    main()
