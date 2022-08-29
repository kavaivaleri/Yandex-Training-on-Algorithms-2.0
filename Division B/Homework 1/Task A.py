# A. Interactor

r = int(input()) #целое число, код завершения задачи
i = int(input()) #целое число, вердикт интерактора
c = int(input()) #целое число, вердикт чекера

if i == 0:
    if r != 0:
        result = 3
    else:
        result = c
elif i == 1:
    result = c
elif i == 4:
    if r != 0:
        result = 3
    else:
        result = 4
elif i == 6:
    result = 0
elif i == 7:
    result = 1
else:
    result = i

print(result)
