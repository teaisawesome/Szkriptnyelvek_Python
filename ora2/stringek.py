s = "hello"
print(s)

s = 'hello'
print(s)

# string hossza
len(s)


# ' karakter levédése - jobb a "" -al megadott string
s = "isn't"

s = 'isn\'t'

# ha idézés van a stringbe akkor ' ' közé tesszük
s = 'she said: "Get out!"'

s = "she said: \"Get out!\""


# batman
s = "batman"

# s string legelso karaktere
s[0]

# s string masodik karaktere - ha tulidexelunk akkor IndexError
s[1]

# !! Pythonban a string egy immutable (nem módositható)
s[0] = 'B' # nem mukodik
s + '!' # nem mukodik


## elkészit egy uj string objektumot
s = "joker"
# JOKER - elkészit egy uj string objektumot és azt adja vissza
s = s.upper()

s = s.lower()

# rá tudunk keresni egy rész stringre - return index
s.find('k')

s.find('ke')

s.find('x') # ha nincs benne akkor -1 -et ad vissza


# néhány gyakori string metódus
s.lower() # a string kisbetujevel ter vissza
s.upper() # a string nagybetujevel ter vissza
s.strip() # a white space karaktereket levágja a sztring elejéről és végéről
s.isalpha(), s.isdigit(), s.isspace() # megnézi, hogy a string vmennyi karaktere az adott karakterosztályba tartozik-e
s.startswith('other'), s.endswith('oter') # megnézi, hogy a string a másik stringel kezdodik / vegzodik-e
s.find('other')  # A stringben szerepel-e a parameter string. Ha igen visszater az index-el, ha nincs akkor -1
s.replace('old', 'new') # a stringben az 'old' vmennyi előfordulását 'new'-ra cseréli
s.split('delim') # a stringet a megadott határoló mentén feldarabolja egy listába.
'_'.join(list) # A split ellentéte. Egy adott lista elemeit fuzi össze a megadott szeparátorral. 

