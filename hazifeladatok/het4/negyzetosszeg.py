#!/usr/bin/env python3


def nums_diff():
    nums_square_sum = 0 # 1^2 + ... + n^2
    
    for i in range(1, 100+1):
        nums_square_sum += i**2

    nums_sums_square = sum(range(1,100+1)) ** 2 # (1 + ... + n)^2

    return nums_sums_square - nums_square_sum


def main():
    print("Az első száz természetes szám összegének a négyzete és az első száz természetes szám négyzetösszege közti különbség:", nums_diff())


if __name__ == "__main__":
    main()
