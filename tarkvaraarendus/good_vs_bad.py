class Robots():
    def __init__(self):
        pass
    def WalkLikeARobot(self, WalkingStyle):
        self.WalkingStyle = WalkingStyle
        return self.WalkingStyle
    def CareLikeARobot(self):
        print("takes care like a robot")

class Humans():
    def __init__(self, nature = "good"):
        self.nature = nature
    def GoodHumanBeing(self):
        print("need not repeat, a good human being is always", self.nature)
    def BadHumanBeing(self):
        self.nature = "need not repeat, a bad human being is always bad"
        print(self.nature)
    def WalkLikeARobot(self, WalkingStyle):
        self.WalkingStyle = WalkingStyle
        return self.WalkingStyle

def main():
    robu = Robots()
    #robu.CareLikeARobot()
    #print("robu.WalkLikeARobot("a robot walks like a robot and nothing happens"))
    GoodMan = Humans()
    #print(GoodMan.nature)
    #GoodMan.GoodHumanBeing()
    BadMan = Humans()
    #BadMan.nature = "bad"
    #print(BadMan.nature)
    #BadMan.BadHumanBeing()
    #print(BadMan.WalkLikeARobot("he is human but walks like a robot"))
    
    #when a bad man walks like a robot many things happen
    WhenABadManWalksLikeARobot = BadMan.WalkLikeARobot(dict(change = "he becomes a monster inside",
        act = "he kills fellow people",
        feel = "he enjoys torturing animals",
        care = "he cares for none",
        look = "he looks a normal human being",
        state = "finally he destroys himself"))
    #there are a lot of actions that take place
    print("what happens when a Bad Man walks like a Robot?")
    change = input("tell us what kind of change may take place inside him?\nChoose between 'monster' and 'angel',"
    "and type here...>>>>")
    WhenABadManWalksLikeARobot['change'] = change
    reward = 0
    if change == 'monster':
        print("you have won the first round:", change)
        reward = 100
        print("you have won ", reward, "points")
        print("what does he do? :", WhenABadManWalksLikeARobot['act'])
        change = input("now tell us what the monster feels inside while killing people?\n choose between 'great' and 'sad',"
        "and type here...>>>>")
        WhenABadManWalksLikeARobot['change'] = change
        if change == 'great':
            print("you have won the second round:")
            reward = 1000
            print("you have won ", reward, "points")
            print("what he feels inside? :", WhenABadManWalksLikeARobot['feel'])
            change = input("tell us does the monster care for anyone\n choose between 'yes' and 'no',"
            "and type here...>>>>")
            WhenABadManWalksLikeARobot['change'] = change
            if change == 'no':
                print("you have won the third round:")
                reward = 100000
                print("you have won", reward, "points")
                print("what he feels inside? :", WhenABadManWalksLikeARobot['care'])
                change = input("tell us does the monster look like a normal human being\n choose between 'yes' and 'no',"
                "and type here...>>>>")
                WhenABadManWalksLikeARobot['change'] = change
                if change == 'yes':
                    print("you have won the fourth round:")
                    reward = 10000000
                    print("you have won ", reward, "points")
                    print("what does he look like? :", WhenABadManWalksLikeARobot['look'])
                    change = input("tell us what happens to the monster finally? does he destroy himself\n choose between 'yes' and 'no',"
                    "and type here...>>>>")
                    WhenABadManWalksLikeARobot['change'] = change
                    if change == 'yes':
                        print("you have won the fifth round:")
                        reward = 100000000
                        print("you have won jackpot", reward, "points")
                    else:
                        print("you have changed the course of game. it ends here. you have lost", reward - 100000, "points")
                else:
                    print("you have changed the course of game. it ends here. you have lost", reward - 1000, "points")
            else:
                print("you have changed the course of game. it ends here. you have lost", reward - 100, "points")
        else:
            print("you have the course of game. it ends here. you have lost", reward + 10, "points")
    else:
        print("you have changed the course of game. it ends here and you have won no points.")

main()