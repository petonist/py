#trips-traps-trull
#15.04.18
######################

#ruudustiku koordinaadid
koordinaat_x = [1,2,3]
koordinaat_y = [1,2,3]

#user input
print("Hint: X-koordinaat -> vasak-parem ja Y -> ülesse-alla")

#mängija X
while True:
    mängija_xx = int(input("Mängija X: sisesta x-koordinaat vahemikus 1-3: "))
    if mängija_xx != 1-3:
        print("sa sisestasid",mängija_xx,". sisesta number vahemikus 1-3!")
    elif mängija_xx == 1-3:
        break

while True:        
    mängija_xy = int(input("Mängija X: sisesta y-koordinaat vahemikus 1-3: "))
    if mängija_xy != 1-3:
        print("sisesta number vahemikus 1-3!")
    elif mängija_xy == 1-3:
        break

#mängija O
while True:
    mängija_ox = int(input("Mängija O: sisesta x-koordinaat vahemikus 1-3: "))
    if mängija_ox != 1-3:
        print("sisesta number vahemikus 1-3!")
    elif mängija_ox == 1-3:
        break

while True:
    mängija_oy = int(input("Mängija O: sisesta y-koordinaat vahemikus 1-3: "))
    if mängija_oy != 1-3:
        print("sisesta number vahemikus 1-3!")
    elif mängija_oy == 1-3:
        break

