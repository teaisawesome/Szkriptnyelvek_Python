a = "Batman"

print(a[1])

# szeleteles: a[start_poz : end_poz] az end pozicio nem lesz benne csak end_poz - 1
a[1:4] # atm
a[0:4] # Batm
a[3:6] # man
a[3:] # 3 - tobbi "man"
a[:3] #  elozoek - 3 "Bat"
a[:] # Batman

# minusz indexelés
# " B  a  t  m  a  n"
# "-6 -5 -4 -3- 2 -1"

a[-1] # -1 a legutolso karakter  'n'
a[-2] # utolso elotti  'a'
a[-3:] # -3 indexpoziciotol a végéig 'man'
a[:-3] # -3 tól barla lévő 'Bat'

print(a[-5:-2]) # atm

# lehet keverni a pozitiv és a negativ indexelést a[+:-]
print(a[1:-2]) # atm

# a[start_poz : end_poz : lepes_koz]
a[::-1] # megforditja a stringet
a = 'python programming'
a[:6:2] # pto
a[::2] # pto rgramn

# palindrom fuggveny - oda vissza olvasva ugyanaz pl.: abba
def is_palindrome(s):
    # ...
    return True

# pythonba NINCS ++ --
a = 5
++a # eredmeny 5, mert igy bezarojelezi - (+(+a))
--a # eredmeny 5, mert igy bezarojelezi - (-(-a))

a += 1 # 6
a -= 1 # 5 (elotte 6 volt)