
def product(vals):
    d = {"forward" : 0, "up": 0, "down": 0}
    for cmd in vals:
        mv, amt = cmd.split(" ")
        d[mv] += int(amt)

    return d["forward"] * (d["down"]-d["up"])

def aim(vals):
    depth = 0
    horiz = 0
    aim = 0
    for cmd in vals:
        mv, amt = cmd.split(" ")
        amt = int(amt)
        aim += amt if mv == "down" else 0
        aim -= amt if mv == "up" else 0
        depth += amt*aim if mv == "forward" else 0
        horiz += amt if mv == "forward" else 0

    return depth*horiz


def main():
    with open("input.txt", "r") as fp:
        data = [x.strip("\n") for x in fp.readlines()]

    position = product(data)
    print(f"Position product: {product(data)}")
    print(f"Position aim: {aim(data)}")



if __name__ == '__main__':
    main()
