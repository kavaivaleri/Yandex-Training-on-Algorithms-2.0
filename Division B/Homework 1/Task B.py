# B. Кольцевая линия метро

lst0 = [int(i) for i in input().split()]
n, i, j = lst0[0], lst0[1], lst0[2]

if i > j:
    if i-j == 1:
        print(0)
    elif i-j <= j+(n-i):
        print(i-j-1)
    else:
        print(j+(n-i)-1)

elif j>i:
    if j-i == 1:
        print(0)
    elif j-i <= i+(n-j):
        print(j-i-1)
    else:
        print(i+(n-j)-1)
