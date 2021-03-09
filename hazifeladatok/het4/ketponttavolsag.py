#!/usr/bin/env python3

import math


def distance(p1, p2):
    a_side, b_side = 0, 0

    if p1[0] > p2[0]:
        a_side = p1[0] - p2[0]
    else:
        a_side = p2[0] - p1[0]

    if p1[1] > p2[1]:
        b_side = p1[1] - p2[1]
    else:
        b_side = p2[1] - p1[1]
    
    return math.sqrt(a_side**2 + b_side**2)


def main():
    p1 = (1, 2)
    p2 = (6, 5)
    print('A ket pont kozti tavolsag:', distance(p1, p2))

#############################################################################

if __name__ == "__main__":
    main()
