import re

'''
Here . ^ and $ are the metacharacters which make regular expression more powerful than a normal string
. = matches any character in a string
^ = matches when start with character
$ = matches when ends with character 
Another feature is Character classes 
create this by putting characters inside a [] of raw string
'''
'''


'''
pattern = r"^gr.y$"
if re.match(pattern, "grey"):
    print("match1")
if re.match(pattern, "gray"):
    print("match2")
if re.match(pattern, "blue"):
    print("match3")

'''
Character classes can also match ranges of characters. 
Some examples:
The class [a-z] matches any lowercase alphabetic character.
The class [G-P] matches any uppercase character from G to P.
The class [0-9] matches any digit. 
Multiple ranges can be included in one class. For example, [A-Za-z] matches a letter of any case.
'''
pattern2 = r"[aeiou]"
if re.match(pattern2, "aeipo"):
    print("match3")
if re.match(pattern2, "qwertyuiop"):
    print("match4")
if re.match(pattern2, "rhythm myths"):
    print("match5")

pattern3 = r"[a-z][A-Z][0-9]"
if re.match(pattern3, "aM6"):
    print("match6")
if re.match(pattern3, "cR7"):
    print("match7")
if re.match(pattern3, "et6"):
    print("match8")

# only ^ metacharacter can use in character class at the begining
pattern4 = r"[^A-Z]"
if re.match(pattern4, "thisisallcorrect"):
    print("Match is found")
# Their are more metacharacters * + ? { and } for their different uses
'''
*  =  zero or more repetitions 
+  =  one or more repetitions
?  =  zero or one repetitions
of characters in raw string
{ } = and curly braces used to represent the number of repetitions between two numbers
here (spam) is a group of characters
'''
pattern5 = r"egg(spam)*"
if re.match(pattern5, "egg"):
    print("match9")
if re.match(pattern5, "eggspamspamegg"):
    print("match10")
if re.match(pattern5, "spam"):
    print("match11")

pattern6 = r"g+"
if re.match(pattern6, "g"):
    print("match12")
if re.match(pattern6, "ggggggggggggggg"):
    print("match13")
if re.match(pattern6, "abc"):
    print("match14")

pattern6 = r"g+"
if re.match(pattern6, "g"):
    print("match12")
if re.match(pattern6, "ggggggggggggggg"):
    print("match13")
if re.match(pattern6, "abc"):
    print("match14")

pattern7 = r"ice(-)?cream"
if re.match(pattern7, "ice-cream"):
    print("match15")
if re.match(pattern7, "icecream"):
    print("match16")
if re.match(pattern7, "sausages"):
    print("match17")
if re.match(pattern7, "ice--ice"):
    print("match18")

pattern8 = r"9{1,3}$"
if re.match(pattern8, "99"):
    print("match19")
if re.match(pattern8, "999"):
    print("match20")
if re.match(pattern8, "99999"):
    print("match21")

pattern9 = r"a(bc)(de)(f(g)h)i"
match = re.match(pattern9, "abcdefghijklmnop")
if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))
    print(match.group())

'''
There are two types of groups 
(?P<name>...) = named group , can be accessed by group method 
(?:...)  = non-capturing group, this can't be accessed by group method
'''

pattern10 = r"(?P<first>abc)(?:def)(ghi)"
match = re.match(pattern10, "abcdefghi")
if match:
    print(match.group("first"))
    print(match.groups())

# Another metacharacter is |
pattern11 = r"gr(a|e)y"
match = re.match(pattern11, "gray")
if match:
    print("match25")
match = re.match(pattern11, "grey")
if match:
    print("match26")
match = re.match(pattern11, "griy")
if match:
    print("match27")
'''
their are special sequences in regex they are written as blackslash followed by a character or number
\1 to \99
\d : digits [0-9]                          \D
\s  : whitespaces [\t\n\r\f\v]                  \S
\w :  word and number character [a-zA-Z0-9]        \W
the special sequences that are opposite to lowercase version are written below
'''
pattern12 = r"(.+)\1"
match = re.match(pattern12, "word word")
if match:
    print("match28")

match = re.match(pattern12, "abc cde")
if match:
    print("match29")

match = re.match(pattern12, "?! ?!")
if match:
    print("match30")

pattern13 = r"(\D+\d)"
match = re.match(pattern13, "Hi 999!")
if match:
    print("match31")

match = re.match(pattern13, "1, 23, 456!")
if match:
    print("match32")

match = re.match(pattern13, " ! $?")
if match:
    print("match33")

pattern14 = r"\b(cat)\b"
match = re.match(pattern14, "The cat sat!")
if match:
    print("match34")

match = re.match(pattern14, "Wes>cat<tered?")
if match:
    print("match35")

match = re.match(pattern14, "We scattered.")
if match:
    print("match36")
