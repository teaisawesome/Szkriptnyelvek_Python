def rev(number):
    snumber = str(number)
    
    return int(snumber[::-1])


def main():
    print(f"1997 -> {rev(1997)}")
    print(f"2021 -> {rev(2021)}")
    print(f"1945 -> {rev(1945)}")


if __name__ == "__main__":
    main()