def digitNumber(number):
    
    return len(str(number))


def main():
    print(f"2^256 number of digits: {digitNumber(2**256)}")


if __name__ == "__main__":
    main()