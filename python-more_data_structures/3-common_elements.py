#!/usr/bin/python3
def common_elements(set_1, set_2):
    lst=[]
for i in set_1:
    if i not in set_2:
        lst.append(i)
for i in set_2:
    if i in set_1:
        lst.append(i)
return lst
