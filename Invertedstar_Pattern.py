print("\t<Inverted Star Pattern>")
n = int(input("Enter a Number : "))
i=0
for j in range(n,0,-1):
    print((j+i)*" ",end="")
    print(j*"*")
    i+=2
       