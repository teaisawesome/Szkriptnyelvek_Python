#!/usr/bin/env python3
# encoding: utf-8

def getURL(url):
    return "".join(url.split()) # split clean all white space


def main():
    s1 = "192.20.246.138:\n 6666"
    s2 = "206.130.99.82:\n8080"

    print(f"Megtisztított URL s1-re: {getURL(s1)}")
    print(f"Megtisztított URL s2-re: {getURL(s2)}")
##############################################################################


if __name__ == "__main__":
    main()