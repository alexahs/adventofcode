import sys
sys.path.append("../")
from utils import *


def fuel(arr):
    max_pos = max(arr)
    min_pos = min(arr)
    fuel_cnts = {i:0 for i in range(min_pos, max_pos)}
    fuel_cnts_2= {i:0 for i in range(min_pos, max_pos)}
    for i in range(min_pos, max_pos):
        for pos in arr:
            diff = abs(pos-i)
            fuel_cnts[i] += diff
            fuel_cnts_2[i] += diff*(diff + 1)//2

    print(f"Least fuel: {min(fuel_cnts.values())}")
    print(f"Least fuel 2: {min(fuel_cnts_2.values())}")

inp = ints("in")
fuel(inp)
