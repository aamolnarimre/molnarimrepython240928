def szog():

#6. feladat – SzögtípusA program  kérjen be a
# konzolról egy valós számot! Ha ez a szám 0 és
# 360 közé esik, akkor legyen egy szög mértéke (pl. 60 fok),
# egyébként a program adjon hibaüzenetet! Ha lehet, a program írja ki
# a szög mértéke alapján a szög típusát (pl.: 60 -> hegyesszög)!

    vSzam = float(input('Adj meg egy való számot'))

    if (vSzam >= 0 and vSzam<=360):
        if vSzam == 0:
             print(str(vSzam)+" -> nullszög")
        elif (vSzam>0) and (vSzam<90):
            print(str(vSzam)+" -> hegyesszög")