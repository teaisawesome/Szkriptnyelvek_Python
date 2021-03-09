#!/usr/bin/env python3


def get_tonality(word):
    deep_chars = ['a','á','o','ó','u','ú']
    high_chars = ['e','é','i','í','ö','ő','ü','ű']

    res = []

    for c in word:
        if c in deep_chars and "mély" not in res:
            res.append("mély")
        
        if c in high_chars and "magas" not in res:
            res.append("magas")

    if len(res) == 2:
        return "vegyes"
    
    if len(res) == 0:
        return "semmilyen"
    
    return res[0]
    

def main():
    word = input("Kérek egy szót: ")
    print(f"A(z) {word} szó hangrendje: {get_tonality(word)}")


if __name__ == "__main__":
    main()
