# пишем функцию простейшего калькулятора
# ввод чисел и операции с клавиатуры

a = int(input("Введите первое число: ")) # вводим первое число с преобразованием в нужный формат
b = int(input("Введите второе число: ")) # вводим второе число с преобразованием в нужный формат
op = input("Введите желаемую операцию: ") # вводим нужную операцию +,-,*,/
def calc(a,b,op): # определяем функцию
    if op == "+": # сложение
        return a + b
    elif op == "-": # вычитание
        return a - b
    elif op == "*": # умножение
        return a * b
    elif op == "/": # деление
        return a / b
    else: # в случае неправильного определения операции
        return "Введена неправильная операция"
print(calc(a,b,op)) # выводим результат на печать с вызовом функции