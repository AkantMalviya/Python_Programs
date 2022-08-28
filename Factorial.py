while (True):
    print("\t<Factorial Calculator> EXIT--> Press 0")
    num = int(input("Enter a Number : "))
    if num != 0:
        for i in range(num-1,0,-1):
            num*=i
        print("Factorial : ",num)
    else:
         print("Program Done")
         break    

