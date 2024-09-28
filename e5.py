def honap():
    #5. feladat – HónapNév A program  olvasson be a konzolról egy egész számot!
# Ha a szám 1 és 12 közötti, akkor legyen a beolvasott szám egy hónap sorszáma!
# A program írja ki a konzolra a sorszámmal megadott hónap nevét! Hiba esetén legyen hibaüzenet!

    szam =    int(input("Adj meg egy hónap sorszámát számot: "))

    if (szam >= 1) and (szam <=12):
        #print("A hónap sorszáma:" + str(szam))
        if szam ==1:
            print("A hónap sorszáma: " + str(szam), 'Ez a hónap január')
        elif szam ==2:
            print("A hónap sorszáma: " + str(szam), 'Ez a hónap a február')
        elif szam == 3:
            print("A hónap sorszáma: " + str(szam), 'Ez a hónap a március')
        elif szam == 4:
            print("A hónap sorszáma: " + str(szam), 'Ez a hónap a április')
        elif szam == 5:
            print("A hónap sorszáma: " + str(szam), 'Ez a hónap a május')
        elif szam == 6:
            print("A hónap sorszáma: " + str(szam), 'Ez a hónap a június')
        elif szam == 7:
            print("A hónap sorszáma: " + str(szam), 'Ez a hónap a július')
        elif szam == 8:
            print("A hónap sorszáma: " + str(szam), 'Ez a hónap az augusztus')
        elif szam == 9:
            print("A hónap sorszáma: " + str(szam), 'Ez a hónap a szeptember')
        elif szam == 10:
            print("A hónap sorszáma: " + str(szam), 'Ez a hónap az október')
        elif szam == 11:
            print("A hónap sorszáma: " + str(szam), 'Ez a hónap a november')
        elif szam == 12:
            print("A hónap sorszáma: " + str(szam), 'Ez a hónap a december')
        else:
            print("Hiba: A megadott szám nincs a tartományban")





