def check_win(a, b, c):
    if (a % 2 == 0 and b % 2 == 0 and c % 2 == 0) or (a % 2 != 0 and b % 2 != 0 and c % 2 != 0):
        return "WIN"
    else:
        return "FAIL"


input = input("Введите три числа через пробел: ")
a, b, c = map(int, input.split())
result = check_win(a, b, c)
print(result)
