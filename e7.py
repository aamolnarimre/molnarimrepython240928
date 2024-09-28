import math

def negyzetgyok():
    #7. feladat – NégyzetgyökA program számítsa ki egy beolvasott valós szám négyzetgyökét! A program adjon hibaüzenetet, ha a felhasználó negatív számból akar gyököt vonni!

    szam = float(input("Adj meg egy számot: "))
    if szam >= 0:
        gyok = math.sqrt(szam)
        print(gyok)
    else:
         print("HIBA: negatív szám gyökét akarja számolni")

