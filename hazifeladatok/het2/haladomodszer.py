lang_info =  [('Fortran', 1954, 0.435), ('Cobol', 1959, 0.391),
              ('C', 1972, 16.076), ('C++', 1980, 9.014), 
              ('Python', 1991, 6.482), 
              ('Java', 1995, 17.99), ('C#', 2001, 6.687)]


def select():
    print("{0:<12} {1:^16} {2:>16}".format("Language", 
                                            "Year Developed", 
                                            "TIOBE rating"))
    print("-" * 46)
    for element in lang_info:
        print("{0:12} {1:^16} {2:16.2f}".format(element[0], 
                                                element[1], 
                                                element[2]))

def is_valid(query):
    if query == 'SELECT * FROM database':
        select()
    else:
        print("Invalid query!")


def main():
    query = input('> ')

    # SELECT * FROM database
    is_valid(query)
    

if __name__ == "__main__":
    main()
