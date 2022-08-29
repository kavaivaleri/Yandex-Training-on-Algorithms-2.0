# C. Даты

lst0 = [int(i) for i in input().split()]
num1, num2, num3 = lst0[0], lst0[1], lst0[2]

if num1 <= 12 and num2 <= 12 and num1!=num2:
    print(0)
else:
    print(1)
