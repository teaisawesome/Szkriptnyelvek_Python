# tuple is immutable - pont ugy mint a string
# lehet benne különböző tipusu elemeket is tarolni
# ugyanugy van lekérés elemekre: tup[0]
# ugyanugy van szeletelés - utolso ketto tup[:2]

def get_movie_info():
    return ("Total Recall", 1990, 7.5)


def main():
    title, year, score = get_movie_info()  # <- value unpacking

    print(title,year,score)

    # két változó felcserélése tuple el
    a = 3
    b = 9

    (a, b) = (b, a)

    print(a,b) # 9 3
    

if __name__ == "__main__":
    main()