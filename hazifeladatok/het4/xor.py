#!/usr/bin/env python3


def true_or_false(var):
    return bool(var)


def main():
    str1 = "python"
    str2 = None
    li = ["python"]
    li2 = []
   
    print(f"A  str1 = 'python'  értéke: {true_or_false(str1)}")
    print(f"A  str2 = None  értéke: {true_or_false(str2)}")
    print(f"A  li = ['python']  értéke: {true_or_false(li)}")
    print(f"A  li = []  értéke: {true_or_false(li2)}")


if __name__ == "__main__":
    main()
