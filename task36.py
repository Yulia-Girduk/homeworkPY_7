# Задача 36: Напишите функцию 
# print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по 
# номеру строки и столбца. Аргументы num_rows и num_columns указывают число 
# строк и столбцов таблицы, которые должны быть распечатаны. Нумерация 
# строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание:
# бинарной операцией называется любая операция, у которой ровно 
# два аргумента, как, например, у операции умножения.
# *Пример:*
# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

def PrintOperationTable(operation, numRows, numColumns):
   
    for i in range(1, numRows+1):
        result = []
        for j in range(1, numColumns+1):
            result.append(str(operation(i, j)))
        print(" ".join(result))
    

numRows = int(input('Введите количество строк таблицы: '))   
numColumns = int(input('Введите количество столбцов таблицы: ')) 
symbol = input('Введите знак для бинарной опрерации (+, -, *, /): ')

if symbol == '+':
    PrintOperationTable(lambda x, y: x + y, numRows, numColumns)
elif symbol == '-':
    PrintOperationTable(lambda x, y: x - y, numRows, numColumns)
elif symbol == '*':
    PrintOperationTable(lambda x, y: x * y, numRows, numColumns)
elif symbol == '/':
    PrintOperationTable(lambda x, y: x / y, numRows, numColumns)
else:
    print('Такого знака я незнаю(')
