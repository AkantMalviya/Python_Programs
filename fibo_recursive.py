print("\t<Fibonacci Series using Recursion>")
def fibo(n):
    if n==0:
        print("enter value greater than 0")
        return
    if n==1:
        return 0
    if n==2:
        return 1 
    else:    
        return fibo(n-1)+ fibo(n-2)

num = int(input("How many elements of fibonacci series: "))
for i in range(1,num+1):
    print(fibo(i),end=" ")

num = int(input("\nEnter nth Fibonacci number :"))
print("The number : ",fibo(num))
