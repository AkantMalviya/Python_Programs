print("\t<GUI CAR Game>")
print("Type help")
while True:
    n = input(">>")
    if n=="help":
        print("start --> accelarate the car")
        print("stop --> stop the car")
        print("quit --> for exit")
    elif n=="start":
        print("Car speeding up")
    elif n=="stop":
        print("car stopped")
    elif n=="quit":
        print("Game Exited")
        break
    else:
        print("Enter a right command")
