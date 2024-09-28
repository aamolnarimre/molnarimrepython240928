def harom():

    for i in range(0,21,1):
        print(i, end=" ")

def ot():
    for i in range(77,-77,-4):
        print(i, end=" ")

def hat():
    #6.	Kérj be 2 számot, majd írasd ki a számokat a legkisebbtől a legnagyobbig! (a legnagyobbat is! Ha az első szám nagyobb, abban az esetben is a legkisebbtől a legnagyobbig írasd ki!)

    def beolvas():
     szam1 = int(input("Első szám: "))
     szam2 = int(input("Első szám: "))

    #melyik a nagyonn?
        if szam2 < szam1:
            #csere
            atmenet = szam1
            szam1=szam2
            szam2 = atmenet

            for i in range(szam1, szam2+1, 1):
                print(i, end=" ")





