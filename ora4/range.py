def main():
    # python 2-be!
    r = range(20) # csak a felso limitet adom meg 0-20
    print(r) # [0,1,2,...,20]

    r2 = range(5,20) # also és felso limit megadva
    print(r2) # [5,6,7...,20]

    #python3 ba:

    print(list(range(5)))

    print(list(range(23,36+1))) # 23-36 

    print(list(range(76,63-1, -1))) # 76-63


    sums = sum(range(1,100+1)) # az iterátorral végigmegy az elemeken és összeadja őket

    print(sums)

if __name__ == "__main__":
    main()