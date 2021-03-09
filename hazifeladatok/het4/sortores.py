#!/usr/bin/env python3


import sys
import random as r

UPTO = 100


def main():
    for i in range(1, UPTO+1):
        if i % 10 == 0:
            print(r.randint(0, 9), end="\n")
        else:
            print(r.randint(0, 9), end="")


if __name__ == "__main__":
    main()
