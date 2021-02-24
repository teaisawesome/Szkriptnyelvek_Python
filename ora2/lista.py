# Listák - dinamikus tömb

a = [2, 4, 6]

print(type(a)) # <class 'list'>

b = [] # lista, aminek a mérete 0
len(b) # 0

c = [2, 3, 14.5, "kiscica", True] # lehet kulonbozo tipusokat tömbbe rakni

# lista összefuzes
a = [1, 2] + [3, 4] 
print(a)

# lista elem lekérdezés - szeletelés
a[:2] # 0-1 indexen levo elemek  result: [1, 2]
a[-2] # utolso ket elemet adja vissza result: [3, 4]

# Lista összehasonlitas - tartalmilag
[1, 2] == [1, 3] # False
[1, 2] == [1, 2] # True

a = [1,2,3]
b = a
b[0] = 100

print(a[0]) # Vajon a[0] értéke 100 vagy 1? Válasz: 100-mert, mert a és b is ugyanoda a területre mutat. 
# Előbb pedig b megvaltoztatta 100-ra az elso erteket.

# Hogyan lehetne visszakapni az 1-est? a[0] = 1
# Másolatot keszitunk
a = [1,2,3]
b = a[:] # másolat új objektum
b[0] = 100
a[0] # 1

# Dinamikus tomb bovitheto

a.append(5)
print(a)

# Listába mennyi elemet tudunk betenni? Ameddig van szabad memória, addig lehet boviteni.