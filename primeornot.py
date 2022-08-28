print("\t<Prime Number Program>")
num  = int(input("Enter a number : "))
count = 0
for i in range(1,num+1):
    if num%i == 0 :
         count+=1
if count == 2:
    print(f"{num} is Prime Number ")
else :
    print(f"{num} is NOT Prime ")