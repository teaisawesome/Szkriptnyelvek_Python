#!/usr/bin/env python3


def dec_to_bin(number):
    reminders = []

    while number != 0:
        reminders.append(str(number % 2))
        number = number // 2
    
    return "".join(reminders[::-1])


def main():
    dec_num = input("Kérek egy decimális számot: ")
    print("A megadott szám bináris alakja: ", dec_to_bin(int(dec_num)))

#############################################################################

if __name__ == "__main__":
    main()
