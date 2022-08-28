print("\t<Fibonacci Series using iteration>")
num = int(input("How many elements you want: "))
fn = 0 
sn = 1 
tn = 0 
print(f"Fibonacci Series:\n{fn},{sn}",end="")
for i in range(num-2):
    tn = fn + sn  
    fn = sn
    sn = tn
    print(f", {tn}",end="")
