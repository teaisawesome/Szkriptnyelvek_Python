#!/usr/bin/env python3
# encoding: utf-8


TEXT = """Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb"""


def decoder(text):
    c_table = {
        'A' : 'C',
        'B' : 'D',
        'C' : 'E',
        'D' : 'F',
        'E' : 'G',
        'F' : 'H',
        'G' : 'I',
        'H' : 'J',
        'I' : 'K',
        'J' : 'L',
        'K' : 'M',
        'L' : 'N',
        'M' : 'O',
        'N' : 'P',
        'O' : 'Q',
        'P' : 'R',
        'Q' : 'S',
        'R' : 'T',
        'S' : 'U',
        'T' : 'V',
        'U' : 'W',
        'V' : 'X',
        'W' : 'Y',
        'X' : 'Z',
        'Y' : 'A',
        'Z' : 'B'
    }

    parts = list(text)

    for i in range(0, len(parts)):
        if parts[i].isalpha():
            if parts[i].isupper():
                parts[i] = c_table[parts[i]]
            else:
                parts[i] = c_table[parts[i].upper()].lower()
    
    
    return "".join(parts)


def main():
    print(decoder(TEXT))


if __name__ == "__main__":
    main()