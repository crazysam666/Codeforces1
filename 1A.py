import re
s = input()
s = [int(s) for s in re.findall(r'-?\d+\.?\d*', s)]
m = s[0]
n = s[1]
a = s[2]
if m % a > 0:
    k1 = (m // a) + 1
else:
    k1 = m // a
if n % a > 0:
    k2 = (n // a) + 1
else:
    k2 = n // a
r = k1 * k2
print(r)