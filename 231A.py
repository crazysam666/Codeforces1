n = int(input())
s = 0
pivot = 0
for i in range(n):
    i = input()
    s = int(i[0]) + int(i[2]) + int(i[4])
    if s >= 2:
        pivot += 1
print(pivot)