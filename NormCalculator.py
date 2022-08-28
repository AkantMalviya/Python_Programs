print("\t---------------")
print("\t  Calculator")
print("\t---------------")
fn = int(input(": "))
op = input(": ")
sn = int(input(": "))
if op=="+":
    print("Sum : ",fn+sn)
elif op=="-":
    print("Difference : ",fn-sn)
elif op=="*":
    print("Multiply : ",fn*sn)
elif op=="/":
    print("Division : ",fn/sn)
elif op=="//":
    print("Quotient : ",fn//sn)
elif op=="%":
    print("Remainder: ",fn%sn)
elif op=="**":
    print("Exponent: ",fn**sn)
else :
    print("Invalid Operator")
