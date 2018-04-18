import random               #random mooduli importimine

def suvaMõõt():             #suvalise numbri genereerimine mõõtude jaoks
    number = random.randint(0, 1000)
    return(number)

class mööbel:                   #main class
    pikkus = ''
    kõrgus = ''
    laius = ''
    kaal = ''
    värvus = ''
    materjal = ''

    def __init__(self):
        pass
    def joonista(self, pikkus, kõrgus, laius, kaal, värvus, materjal):
        print(f"siin on objekti {self} graafika")   #graafika joonistamine koos objekti argumendi väljastamisega
        print("eseme mõõdud:")          #objekti atribuutide väljastamine
        print(f"pikkus: {pikkus}(cm)")
        print(f"kõrgus: {kõrgus}(cm)")
        print(f"laius: {laius}(cm)")
        print(f"kaal: {kaal}(g)")
        print(f"värvus: {värvus}")
        print(f"materjal: {materjal}")
        
class istumiseks(mööbel):       #subclass
    def __init__(self):
        pass
class hoiustamiseks(mööbel):
    def __init__(self):
        pass     

class toolid(istumiseks):       #sub_subclass
    def __init__(self):
        pass
class voodid(istumiseks):
    def __init__(self):
        pass
class kapid_lauad(hoiustamiseks):
    def __init__(self):
        pass    

def main():             #main funktsioon
    mööbel1 = ["tool", "taburett", "tumba", "baaritool", "diivan"]      #mööbliesemed jaotatud vastavateks massiivideks
    for tool in mööbel1:                                                #for tsükliga kõik elemendid läbi käidud 
        tool = toolid()                                                 #määratud iga elemendi kuuluvus
        tool.joonista(suvaMõõt(), suvaMõõt(), suvaMõõt(), suvaMõõt(), "kollane", "puit")                                                 #joonista funktsioon iga elemendiga

    mööbel2 = ["voodi", "välivoodi"]
    for voodi in mööbel2:
        voodi = voodid()
        voodi.joonista(suvaMõõt(), suvaMõõt(), suvaMõõt(), suvaMõõt(), "roheline", "kivi")

    mööbel3 = ["laud", "kapp"]
    for laud_kapp in mööbel3:
        laud_kapp = kapid_lauad()
        laud_kapp.joonista(suvaMõõt(), suvaMõõt(), suvaMõõt(), suvaMõõt(), "punane", "plastik")

main()                  #maini väljakutsumine

#tee suvalise värvi genekas[10]



