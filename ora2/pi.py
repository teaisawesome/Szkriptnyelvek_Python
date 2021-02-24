PI = 3.14

def main():
    # print("PI értéke: " + PI)  hiba: egy stringet és egy számot nem lehet összefuzni
    print("PI értéke: " + str(PI))
    print("PI értéke:", PI) # igy minden értéket szóközökkel választ el
    print("aa", 45, True, 3.14)

# nyomtassuk ki a PI értékét stringformázással
if __name__ == "__main__":
    main()