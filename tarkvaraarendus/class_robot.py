class Robots:
    def __init__(self):
        pass
    def WalkLikeARobot(self, style): #polymorphism
        self.style = style
        return self.style
        #print("walks like a robot")
    def CareLikeARobot(self):
        print("takes care like a robot")

class Humans:
    def __init__(self, nature = "good"): #default väärtus nature = good
        self.nature = nature    #kui ei anta muud väärtust võetakse default väärtus
    def GoodHumanBeing(self):
        print("need not repeat, a good human being is always", self.nature)
    def BadHumanBeing(self):
        self.nature = "need not repeat, bad human being is always bad"
        print(self.nature)
    def WalkLikeARobot(self, style): #polymorphism
        self.style = style
        return self.style

def main():
    robu = Robots()
    robu.CareLikeARobot()
    print(robu.WalkLikeARobot("walks like a robot"))
    GoodMan = Humans()
    print(GoodMan.nature)
    GoodMan.GoodHumanBeing()
    BadMan = Humans()
    BadMan.nature = "bad"
    print(BadMan.nature)
    BadMan.BadHumanBeing()
    print(BadMan.WalkLikeARobot("he is human but walks like a robot"))

main()