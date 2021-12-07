



def ints(file):
    inp = open(file, "r").readline().strip("\n").split(",")
    return list(map(int, inp))

