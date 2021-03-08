def main():
    # None olyen, mint C be a Null
    a = None # ez a változó már létezik, None az értéke
    # létezik  a változó csak nem mutat sehova

    print(a) # None

    bool() # megtudjunk nézni, hogy egy kifejezes igaznak vagy hamisnak számit e

    bool("") # False
    bool([]) # False
    bool("asd") # True

if __name__ == "__main__":
    main()