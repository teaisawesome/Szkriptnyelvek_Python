# standard adattipusok
# szám, {sztring, lista, tuple}>szekvenciáknak nevezzuk, szótár, halmaz


def hello(name, color, what):
    # geza, kek az eg!
    # C-ben: printf("%s, %s az %s!\n", name, color, what);
    # v1 itt egy változóra többször is tudunk hivatkozni
    print("{0}, {1} az {2}! ki? {0}".format(name, color, what))
    # v2 nem tudok visszautalni az értékekre
    print("{}, {} az {}!".format(name, color, what))
    # v3 
    print("{nev}, {szin} az {mi}!".format(nev=name, szin=color, mi=what))
    # v4 f-et kell rakni a string elejére...a kapcsok közötti kifejezés kiértékelődik
    print(f"1 + 1 = {1+1}")
    print("1 + 1 = {1+1}") # f nelkul
    print(f"{name}, {color} az {what}!")
    # Geza kék az ég . ezt szeretném elérni ugy hogy nem modositom a maint
    print("{0}, {1} az {2}! ki? {0}".format(name.capitalize(), color, what))
    # negyven hosszusagu elvalasztojel:
    print("-" * 40)

def main():
    hello("geza", "kek", "eg")


if __name__ == "__main__":
    main()