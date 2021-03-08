import sys


def check(length):
    if length == 3:
        print(f"A két szám összege: {sum(sys.argv[1], sys.argv[2])}")
    else:
        print("Hiba! Kérem adjon meg két számot argumentumként!")

def sum(number1, number2):
    return int(number1) + int(number2)


def main():
    check(len(sys.argv))


if __name__ == "__main__":
    main()