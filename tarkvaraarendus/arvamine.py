from random import randint

arvatav = randint(0, 51)
katseid = 0
sisend = int(input("sisesta nr (0-50): "))

while arvatav != sisend:
    print
    if sisend < arvatav:
        katseid += 1
        print("suurem!")
        sisend = int(input("sisesta nr (0-50): "))
    elif sisend > arvatav:
        katseid += 1
        print("väiksem!")
        sisend = int(input("sisesta nr (0-50): "))
    elif sisend == arvatav:
        print(arvatav, " on õige.", katseid, " korda pakkusid")
    else:
        break