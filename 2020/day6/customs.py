


def build_grps(inp):
    groups = []
    tmp_grp = ""
    grp_size = 0
    for i, line in enumerate(inp):
        if line == "\n":
            groups.append((grp_size, tmp_grp))
            tmp_grp = ""
            grp_size = 0
            continue
        tmp_grp += line.strip("\n")
        grp_size += 1
    groups.append((grp_size, tmp_grp))
    return groups

def sum_yes(inp):
    cnt = 0 
    for grp in build_grps(inp):
        cnt += len(set(grp[1]))

    print(f"Counts: {cnt}")


def sum_all_yes(inp):
    
    final_cnt = 0
    for grp in build_grps(inp):
        questions = grp[1]
        size = grp[0]
        counts = {}
        for q in questions:
            counts[q] = counts.get(q, 0) + 1
        for count in counts.values():
            final_cnt += 1 if count == size else 0

    print(f"Counts: {final_cnt}")
            



def main():

    with open("in", "r") as fp:
        data = fp.readlines()

    sum_yes(data)
    sum_all_yes(data)




if __name__ == '__main__':
    main()
