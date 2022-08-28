print("\t<Prime Numbers>")
print("Enter two numbers of interval ")
fn = int(input(":"))
print("To")
sn = int(input(":"))
print("prime numbers : ")
count = 0 
for i in range(fn,sn+1):
    count = 0
    for j in range(1,i+1): 
        if i==1:
            print(i,", ",end="")
        if i%j==0:
            count+=1
    if count==2:
            print(i,", ",end="")    
            count = 0         



