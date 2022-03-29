

def HexToDec (b):
    r = 0
    d = 0
    list_hex = list(range(10,16))
    list_hex_l = ["A","B","C","D","E","F"]
    tab = list(str(b))
    tab.reverse()
    while  r < len(tab) :
        if tab[r] in list_hex_l :
             tab[r] = int(list_hex[list_hex_l.index(tab[r])]) * 16 ** r
             d += (tab[r])
        else :
            tab[r] = int(tab[r]) * 16 ** r
            d += (tab[r])
        r = r + 1
    return d
"""
Fonction permettant de convertir des nombres en base 16 en base 10,
fait correspondre les valeurs A,B,C,D,E et F à leurs équivalent en base 10,
et additionne les membres convertie en base 10.
"""

def DecToBin (dec):
    b = []
    c = 0
    a = str()
    quotient = dec
    while quotient != 0 :
        reste = quotient % 2
        quotient = quotient // 2
        if reste == 0 :
            b.append(0)
        elif reste == 1 :
            b.append(1)
    b.reverse()
    while c < len(b) :
        a += str(b[c])
        c += 1
    return a

"""
Fonction permettant de convertir des nombres en base 10 en base 2,
en utilisant les divisions successives. 
"""
def DecToHex (dec) :
    b = []
    list_dec = list(range(0,10))
    lis_hex = list(range(10,16))
    lis_hex_l = ["A","B","C","D","E","F"]
    quotient = dec
    while quotient != 0:
        reste = quotient % 16
        quotient = quotient // 16
        if reste in list_dec:
            b.append(reste)
        elif reste in lis_hex:
            b.append(lis_hex_l[lis_hex.index(reste)])
    b.reverse()
    return b
"""
Fonction permettant de convertir des nombres en base 10 en base 16,
en utilisant les divisions successives
"""
def HexToBin (hex):
    h = HexToDec(hex)
    a = DecToBin(h)
    return a
"""
Fonction permettant de convertir des nombres en base 16 en base 2,
en utilisant les fonctions HexToDec et DecToHex.
"""

def BinToDec (bin) :
    bin = str(bin)
    b = list(bin)
    b.reverse()
    c = 0
    a = 0
    if (b.count("0")+b.count("1") == len(b)) :
     while c != len(b) :
        a += int(b[c]) * 2**c
        c = c+1
    else :
        a = str()
    return a

"""
Fonction permettant de convertir des nombres en base 2 en base 10,
en fesant la somme des x*2**n (n = rang ; x = valeur associer à ce rang)
"""

def BinToHex (bin) :
    d = BinToDec(bin)
    return DecToHex(d)


"""
Fonction permettant de convertir des nombres en bases 16 en base 2,
en utilisant les fonction HexToDec et DecToBin. 
"""

b1 = 2

while b1 == b1 :
  print("Menu\n"
      "1 : conversion hexadecimale en binaire\n"
      "2 : conversion decimale en binaire\n"
      "3 : conversion hexadecimale en decimale\n"
      "4 : conversion decimale en hexadecimale\n"
      "5 : conversion binaire en decimale\n"
      "6 : conversion binaire en hexadecimale\n"
      "0 : quitter le programme")
  choix = int(input("choix = "))

  if choix == 1 :
     h = str(input("hexadecimale = "))
     print(f"La conversion de {h} en hexadecimale est égale à {HexToBin(h)} ")
     continue
  elif choix == 2 :
     d = int(input("decimale = "))
     print(f"La conversion de {d} en binaire est égale à {DecToBin(d)} ")
     continue
  elif choix == 3 :
      h = str(input("hexadecimale = "))
      print(f"La conversion de {h} en decimale est égale à {HexToDec(h)} ")
      continue
  elif choix == 4 :
      d = int(input("decimale = "))
      print(f"La conversion de {d} en hexadecimale est égale à {DecToHex(d)} ")
      continue
  elif choix == 5 :
      b = int(input("binaire ="))
      if BinToDec(b) == str() :
          print("Veuillez entrer un nombre binaire")
      else :
          print(f"La conversion de {b} en decimale est égale à {BinToDec(b)} ")
      continue
  elif choix == 6 :
      b = int(input("binaire ="))
      if BinToDec(b) == str() :
          print("Veuillez entrer un nombre binaire")
      else :
          print(f"La conversion de {b} en hexadecimale est égale à {BinToHex(b)} ")
      continue
  elif choix == 0 :
      break
  else :
      print("Veuillez entrer un chiffre entre 0 et 6")

"""
Menu du programme
"""






