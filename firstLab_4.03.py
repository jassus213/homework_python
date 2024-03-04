def calculate_quadratic_function(a, b, c, x):
    return a * x ** 2 + b * x + c


input_values = input("Введите a, x, b, c через пробел: ")
a, x, b, c = map(float, input_values.split())

result = calculate_quadratic_function(a, b, c, x)
print(f"Результат = {result}")
