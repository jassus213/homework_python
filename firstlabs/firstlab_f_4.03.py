def find_extra_char(s, t):
    result = 0

    for char in s + t:
        result ^= ord(char)

    return chr(result)

# Ввод строк s и t
s = input().strip()
t = input().strip()

# Вывод лишней буквы
result = find_extra_char(s, t)
print(result)