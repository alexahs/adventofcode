
def power_consumption(vals):
    most_common = [0]*len(vals[0])
    for bits in vals:
        for i in range(len(bits)):
            most_common[i] += 1 if bits[i] == "1" else 0

    gamma = 0
    epsilon = 0
    for i, num_bits in enumerate(reversed(most_common)):
        if num_bits > len(vals)/2:
            gamma += 2**i
        else:
            epsilon += 2**i
    return gamma*epsilon

def get_rating_number(bits_list, idx, keep_set_bit):
    if len(bits_list) == 1:
        return bits_list

    num_set_bits = 0
    for bits in bits_list:
        num_set_bits += int(bits[idx]) 

    most_common = 1 if num_set_bits >= len(bits_list)/2 else 0
    least_common = 1 - most_common
    criteria = most_common if keep_set_bit else least_common

    to_keep = [b for b in bits_list if int(b[idx]) == criteria]

    return get_rating_number(to_keep, idx+1, keep_set_bit)


def life_support(vals):
    bits1 = get_rating_number(vals, 0, True)
    bits2 = get_rating_number(vals, 0, False)
    return int(bits1[0], 2)*int(bits2[0], 2)


def main():
    with open("input.txt", "r") as fp:
        data = [x.strip("\n") for x in fp.readlines()]

    print(f"power consumption: {power_consumption(data)}")
    print(f"life support rating: {life_support(data)}")



if __name__ == '__main__':
    main()
