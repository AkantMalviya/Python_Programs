# phone number validator using regular expression
import re
num = input(":")
pattern = r"(^1|^8|^9\d)"
matched = re.match(pattern,num)
if len(num)==8:
    if matched:
        print("Valid")
    else:
        print("Invalid")
else:
    print("Invalid")