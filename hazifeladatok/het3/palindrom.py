#!/usr/bin/env python3


def trivial(sample):
    if sample == sample[::-1]:
        return True
    
    return False


def iterative(sample):
    i = 0

    while i < len(sample)/2:
        if sample[i] != sample[-(i+1)]:
            return False
        i += 1

    return True


def recursive(sample):
    if len(sample) < 2:
        return True

    if sample[0] != sample[-1]:
        return False
    
    return recursive(sample[1:-1])

def main():
    sample = input("Kérem a szöveget: ")

    print(f"Triviális módszerrel: {trivial(sample)}")

    print(f"Iteratív módszerrel: {trivial(sample)}")

    print(f"Rekurzív módszerrel: {trivial(sample)}")


if __name__ == "__main__":
    main()