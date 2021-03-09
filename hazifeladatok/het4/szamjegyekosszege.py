#!/usr/bin/env python3


def sums_in_range():
    sum_nums = 0

    for n in range(1,100+1):
        n_li = list(str(n))
        
        sum_n_digits = 0

        for d in n_li:
            sum_n_digits += int(d)
        
        sum_nums += sum_n_digits
    
    return sum_nums


def main():
    print("Számjegyek összege: ", sums_in_range())


if __name__ == "__main__":
    main()
