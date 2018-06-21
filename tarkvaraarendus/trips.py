import sys

def print_game(game):
    print("\n")
    for i in range(3):
        print("  |  ".join(str(x) for x in game[i]))
        if i < 2:
            print("-------------")
        
def game_winner(game):
    for i in range(3):
        row = set(game[i])
        if(len(row) == 1 and game[i][2] != 0):
            return game[i][2]
        
    for j in range(3):
        column = set([game[0][j], game[1][j], game[2][j]])
        if(len(column) == 1 and game[1][j] != 0):
            return game[1][j]
        
    diag1 = set([game[0][0], game[1][1], game[2][2]])
    diag2 = set([game[0][2], game[1][1], game[2][0]])
    if(len(diag1) == 1 or len(diag2) == 1 and game[1][1] != 0):
        return game[1][1]
    
    return "viik!"

def game_main():  
    ans = 'y'
    count_x = 0
    count_o = 0
        
    while ans != 'n':
        game = [[" "," "," "], [" "," "," "], [" "," "," "]]

        print_game(game)

        count = 0
        chance = True

        while chance:
            spot = input("sisesta rida,veerg: ")
            spot = spot.split(",")
                
            row = int(spot[0]) -1
            column = int(spot[1]) -1

            if(count % 2 == 0):
                print("\n ---=== Mängija X ===---")
                if(game[row][column] == " "):
                    game[row][column] = 'X'
                else:
                    print("koht on võetud! vali uus!")
                    count-=1
                print_game(game)
            else:
                print("\n ---=== Mängija O ===---")
                if(game[row][column] == " "):
                    game[row][column] = 'O'
                else:
                    print("koht on võetud! vali uus!")
                    count-=1
                print_game(game)

            count+=1
           
            if(" " in game[0] or " " in game[1] or " " in game[2]):
                chance = True
            else:
                chance = False
                print("käigukorrad otsas!")
        
            if(game_winner(game) == 'X'): 
                print("võitja on", game_winner(game))
                count_x+=1
                break
            elif(game_winner(game) == 'O'):
                print("võitja on", game_winner(game))
                count_o+=1
                break
            
        ans = input("soovid uuesti mängida?(y/n): ")
    
    print("Seis on ->>> \nmängija X: %s \nmängija O: %s"%(count_x, count_o))

try:
    game_main()
except ValueError:
    print("quit!")
    sys.exit(0)
except IndexError:
    print("sisesta väärtus vahemikus 1-3 kujul x,o")
else:
    game_main()
