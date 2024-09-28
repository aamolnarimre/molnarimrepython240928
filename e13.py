import math

def kor():
    #13. feladat – Kör A program olvassa be a konzolról egy kör sugarát! Ha a sugár nem pozitív, akkor a program írja ki konzolra, hogy "Hiba: a kör sugara nem pozitív!"; egyébként a program számítsa ki és írja ki a kör kerületét, területét a konzolra!

    r = float(input("Adj meg egy kör sugár értékét"))
    if r>0:
        terulet = r**2 * math.pi
        terulet2 = r*r *math.pi
        terulet3 = math.pow(r, _y:2) *math.pi
        terulet4 = pow(r, 2)*math.pi
        kerulet = 2 * r * math.pi

        print("A kör területe:"+str(terulet)+", a kör területe: " +str(kerulet))
