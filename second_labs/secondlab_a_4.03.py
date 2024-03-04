def transpose_matrix(matrix):
    zipped_matrix = zip(*matrix)
    transposed_matrix = list(zipped_matrix)
    return transposed_matrix

n = int(input().strip())  # Количество строк
m = int(input().strip())  # Количество столбцов

matrix = [list(map(int, input().strip().split())) for _ in range(n)]

transposed_matrix = transpose_matrix(matrix)

print("\n")

# Вывод транспонированной матрицы
for row in transposed_matrix:
    print(*row)
