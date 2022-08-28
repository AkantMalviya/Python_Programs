#Method1
str = input("Enter a String : ")
if str == str[::-1] :
     print("Palindrome")
else :
    print("Not Palindrome")
#Method2
def ispalindrome(str):
    for i in range(int(len(str)/2)):
        if str[i]!=str[len(str)-i-1]:
            return False
    return True
str = input("Enter a String : ")
ans = ispalindrome(str)
if (ans):
    print("Palindrome")
else :
    print("Not Palindrome")
