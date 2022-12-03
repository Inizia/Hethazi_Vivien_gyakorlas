import random
szorozat = [-3, 5, 11, -2, 4]

def kiir(kiir):
    i = 0
    ures = " "
    while (i < len(szorozat) - 1):
        ures += str(szorozat[i]) + kiir
        i += 1
    print(ures + str(i))


def veletlen():
    vel = int(random.random() * 7) + 5
    print(vel + szorozat[0])
    szorozat[0] += vel
    print(kiir("*"))


def utolso():
    szam = int(input("Adj meg egy 3-al osztható kétjegyű páratlan számot!: "))

    while not ((szam >= 10) and (szam <= 99) and (szam%2==1) and (szam%3==0)):
        szam = int(input("+-mal osztható nem páros kétjegyű szám: "))
    print(szam)

    szorozat[len(szorozat)-1] = szam
    print(szorozat)


def prim():
#Egy paraméterében megadott számról eldönti, hogy prím-e?
    szam = int(input("Adj meg egy prím számot!: "))






