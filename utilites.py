"""
This is a package or file module which is create to import or reuse
in other python files
"""


def find_max(list1):
    max1 = -1
    for i in range(len(list1)):
        if list1[i] > max1:
            max1 = list1[i]
    return max1
