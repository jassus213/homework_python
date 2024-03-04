def add_binary_numbers(a, b):
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    result = ''
    carry = 0

    for i in range(max_len - 1, -1, -1):
        bit_sum = int(a[i]) + int(b[i]) + carry
        result = str(bit_sum % 2) + result
        carry = bit_sum // 2

    if carry:
        result = '1' + result

    return result


binary_number1 = input().strip()
binary_number2 = input().strip()

# Вывод суммы чисел
result = add_binary_numbers(binary_number1, binary_number2)
print(result)
