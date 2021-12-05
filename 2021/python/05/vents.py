import numpy as np
import matplotlib.pyplot as plt


class Line:
    def __init__(self, inp):
        self.inp = inp

    def __repr__(self):
        return self.inp

    def formatted_coords(self):
        start, stop = self.inp.split("->")
        x0, y0 = tuple(map(int, start.split(",")))
        x1, y1 = tuple(map(int, stop.split(",")))
        """
        if y0 > y1:
            y1, y0 = y0, y1
        if x0 > x1:
            x1, x0 = x0, x1
        """
        return y0, x0, y1, x1
        #return x0, y0, x1, y1

    def draw(self, ocean_map, diag):
        x0, y0, x1, y1 = self.formatted_coords()
        if x0 == x1:
            if y0 > y1:
                y1, y0 = y0, y1
            ocean_map[x0, y0:y1+1]+= 1
        elif y0 == y1:
            if x0 > x1:
                x1, x0 = x0, x1
            ocean_map[x0:x1+1, y0]+= 1
        elif diag:
            step_x = 1 if x0 < x1 else -1
            step_y = 1 if y0 < y1 else -1
            xx = range(x0, x1+step_x, step_x) 
            yy = range(y0, y1+step_y, step_y)
            for i, j in zip(xx, yy):
                ocean_map[i, j] += 1

        return ocean_map

def straight(data):
    n = 1000
    ocean_map = np.zeros((n, n))
    for coords in data:
        line = Line(coords)
        ocean_map = line.draw(ocean_map, diag=False)

    num_danger = len(np.where(ocean_map > 1)[0])
    print(f"Point with atleast 2 vents: {num_danger}")
    plt.imshow(ocean_map)
    plt.show()

def diag(data):
    n = 1000
    ocean_map = np.zeros((n, n))
    for coords in data:
        line = Line(coords)
        ocean_map = line.draw(ocean_map, diag=True)

    num_danger = len(np.where(ocean_map > 1)[0])
    print(f"Point with atleast 2 vents: {num_danger}")
    plt.imshow(ocean_map)
    plt.show()

def main():
    with open("in", "r") as fp:
        data = fp.readlines()

    straight(data)
    diag(data)


if __name__ == '__main__':
    main()
