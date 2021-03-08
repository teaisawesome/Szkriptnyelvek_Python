# Akkor használjuk, ha egy nagy stringet akarunk összerakni darabokból.


#Példa: vegyük az egész számokat 1-től 15-ig s irjuk le őket egymás mellé.
# Az eredményt sztringként kezeljük: ,,1234567891112131415".

# naiv:

def main():
    # naiv:
    res = ""
    for i in range(1, 15+1):
        res += str(i)

    print(res)
    
    # Sztringbuffer alkalmazása:
    parts = []
    for i in range(1, 15+1):
        parts.append(str(i))

    res = "".join(parts)

    print(res)
    

if __name__ == "__main__":
    main()