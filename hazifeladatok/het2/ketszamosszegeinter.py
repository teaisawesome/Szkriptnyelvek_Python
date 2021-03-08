import sys


def sum(numbers):
    if(len(numbers) == 2):
        return f"A két szám összege: {int(numbers[0]) + int(numbers[1])}"
    else:
        return "Hiba! Kérem adjon meg két számot!"


def main():
    numbers = input('Kérem adjon meg 2 számot: ')
    print(sum(numbers.split()))


if __name__ == "__main__":
    main()