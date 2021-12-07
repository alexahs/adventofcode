



class Bag:
    def __init__(self, color, rule):
        self.color = color
        self.rule = rule
        self.contains = {}

    def add_to_contain(self, bag, amount):
        self.contains[bag] = amount


    def __repr__(self):
        string = f"BAG: color={self.color}, contains="
        for k, v in self.contains.items():
            string += f"{v} {k.color}, "
        string = string[:-2]
        return string



def build_bags(rules):
    bags = {}
    for rule in rules:
        idx = rule.find("bags")
        color = rule[:idx - 1]
        bag = Bag(color, rule)
        bags[color] = bag

    for bag in bags.values():
        sub_bags = bag.rule[len(bag.color)+len("bags contain "):].strip().split(",")
        for sub_bag in sub_bags:
            if "no other bags" in sub_bag:
                continue
            words = sub_bag.split()
            amt = int(words[0])
            color = ' '.join(words[1:3])
            bag.add_to_contain(bags[color], amt)


    return list(bags.values())

class ContainsGolden:
    def __init__(self):
        self.golden = False

    def check(self, bag):
        colors = [b.color for b in bag.contains.keys()]
        if "shiny gold" in colors:
            self.golden = True
        for sub_bag in bag.contains.keys():
            return self.check(sub_bag)

def main():
    data = open("in", "r").readlines()
    bags = build_bags(data)
    cnt = 0
    for bag in bags:
        golden = ContainsGolden()
        golden.check(bag)
        cnt += 1 if golden.golden else 0

    print(f"Colors containing at least one golden bag: {cnt}")


if __name__ == '__main__':
    main()


        
