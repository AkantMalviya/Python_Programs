print("\t<Check Armstrong Number>")
num1 =  input("Enter a number : ")
num = list(num1)
sum = 0 
for i in range(len(num)):
    m = int(num[i])
    n  = m**3
    sum+=n
if sum==int(num1):
    print(f"Yes\n{num1} is a Armstrong Number")
else :
     print(f"No\n{num1} is Not Armstrong Number")

