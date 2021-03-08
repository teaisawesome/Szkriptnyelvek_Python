def main():
    li = ['aaa','bbb','ccc']

    print(" ; ".join(li)) # szeparátor mentén összfuzi a tomb elemeit {szeparator}.join(tomb)


    s = "hell:nber"

    s_li = s.split(":") # a stringet feldarabolja a szepatár mentén

    print(s_li)

    s2 = "       asd         asdasd"

    s2_li = s2.split() # ha nem adunk meg semmit akkor a white spacek mentén vágja szét a stringet

    print(s2_li)

if __name__ == "__main__":
    main()