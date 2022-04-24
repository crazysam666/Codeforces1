""" 158 A """
import re
s1 = input()
s2 = input()
s1 = [int(s) for s in re.findall(r'-?\d+\.?\d*', s1)]
s2 = [int(s) for s in re.findall(r'-?\d+\.?\d*', s2)]
n = s1[0]
k = s1[1]
a = s2[k-1]
p = 0
for i in s2:
    if i >= a and i != 0:
        p += 1
print(p)