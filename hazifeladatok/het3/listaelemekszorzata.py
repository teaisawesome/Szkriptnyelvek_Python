#!/usr/bin/env python3


def product(numbers):
    result = 1
    
    for n in numbers:
        result = result * n

    return result
    

def main():
    li = []
    li2 = [1,2,3]
    li3 = [5,5,5,5]

    print(f"Üres listára: {product(li)}")
    print(f"[1,2,3] listára: {product(li2)}")
    print(f"[5,5,5,5] listára: {product(li3)}")


if __name__ == "__main__":
    main()