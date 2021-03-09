#!/usr/bin/env python3


def diamond_draw(height):
    if height % 2 == 0:
        print("Csak páratlan magasság a megengedett!")
    else:
        count = 1
        for i in range(1, height+1):
            star_li = ['*'] * count
            stars = "".join(star_li)
            
            if i >= (height // 2 + 1):
                count -= 2
            else:
                count += 2
         
            print(stars.center(height))



def main():
    h = input("Kérem a gyémánt magasságát: ")
    diamond_draw(int(h))

if __name__ == "__main__":
    main()