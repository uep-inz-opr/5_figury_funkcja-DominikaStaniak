import random
import math
liczba_figur=[]

il_figur=int(input())
for linia in range (il_figur):
  figura_n=input().split()
  figura_n = [float(y) for y in figura_n]
  liczba_figur.append(figura_n)


def suma_pol(figury):
  suma = 0
  for linia in figury:
    if len(linia) == 1:
      pole = math.pi * linia[0] ** 2
    elif len(linia) == 2:
      pole = linia[0] * linia[1]
    elif len(linia) == 3:
      pole = math.sqrt(((linia[0]+linia[1]+linia[2])/2)*(((linia[0]+linia[1]+linia[2])/2)-linia[0])*(((linia[0]+linia[1]+linia[2])/2)-linia[1])*(((linia[0]+linia[1]+linia[2])/2)-linia[2]))
    else:
      return("Błąd: można podać maksymalnie 3 liczby")
    suma = suma + pole
  return round(suma, 2)


print(suma_pol(liczba_figur))
