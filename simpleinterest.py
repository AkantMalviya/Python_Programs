print("\t<Simple Interest>")
p = int(input("principal amount : "))
r = float(input("rate% of interest  : "))
t = int(input("Time (years) : "))
si = (p*r*t)/100
print("Simple Interest : ",si)
a = si + p
print("Compound amount : ",a)
ci = p*(1+r/100)**t
print("Compund Interest : ", ci)





