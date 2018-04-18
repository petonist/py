from random import randint

arvatav = randint(0, 51)
katseid = 0
sisend = int(input("sisesta nr (0-50): "))

while arvatav != sisend:
    print
    if sisend < arvatav:
        print ("suurem")
        katseid += 1
        sisend = int(input("Enter an integer from 1 to 99: "))
    elif sisend > arvatav:
        print ("väiksem")
        katseid += 1
        sisend = int(input("Enter an integer from 1 to 99: "))
    else:
        print (arvatav + " on õige. sul läks " + katseid)
        break
    print