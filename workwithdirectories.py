"""
Program to Print all files in a directory or project
"""
from pathlib import Path

path1 = Path()
# path1.mkdir()
# path1.rmdir()
count = 0
for file in path1.glob("*.py"):
    print(file)
    count+=1
print("\nTotal number of file : ",count)