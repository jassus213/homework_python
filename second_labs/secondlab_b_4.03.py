# Создаем словарь для хранения учеников по классам
students_by_class = {9: [], 10: [], 11: []}

# Ввод данных с клавиатуры
print("Введите данные в формате 'класс фамилия' (для завершения ввода введите пустую строку):")
while True:
    input_data = input().strip()
    if not input_data:
        break

    class_number, name = input_data.split()
    students_by_class[int(class_number)].append(name)

# Выводим учеников в нужном порядке
for class_number in [9, 10, 11]:
    for name in students_by_class[class_number]:
        print(f"{class_number} {name}")