# A script megvizsgálja, hogy az inputként bejövő url string {instancename}.service-now.com formájú-e.


def main():
    ins = input()
    if ins.endswith('.service-now.com'):
        print('Valid Service Now instance.')
    else:
        print('Invalid Service Now instance.')


if __name__ == "__main__":
    main()