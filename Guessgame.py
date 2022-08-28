print("\t<Guess Game>")
print("You have only Three chances>>")
print("Enter three random digits>>")
Lottery = "121"
chance = 0 
while True:
    if chance!=3:
        g = input("Guess : ")
        if g==Lottery:
            print("Win lottery Game")
            break
    else :
        print("Game Over")
        break
    chance+=1