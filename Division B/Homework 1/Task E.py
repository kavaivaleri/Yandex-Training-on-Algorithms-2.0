# E. Точка и треугольник

d = int(input())
lst = [int(i) for i in input().split()]

x, y = lst[0], lst[1]

if 0<=x<=d and 0<=y<=d and x+y<=d:
    print(0)
else:
    a = x**2+y**2
    b = (x-d)**2+y**2
    c = x**2+(y-d)**2

    if a > b:
        if b > c:
            print(3)
        else:
            print(2)
    else:
        if c > b:
            print(1)
        else:
            if c>=a:
                print(1)
            else:
                print(3)
                
