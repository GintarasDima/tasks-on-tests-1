# Создайте двумерный массив размерностью 3 на 4, состоящий из случайных
# целых чисел от 15 до 37.
# Требуется создать новый массив той же размерности (3,4), значения которого будут
# зависеть от значений исходного массива и могут принимать одно из трех возможных значений:
# "small", для значений исходного массива меньше 20;
# "medium", для значений исходного массива в промежутке [20, 30];
# "large", для значений исходного массива больше 30.
import numpy as np
import random
a = np.random.randint(15,38,12).reshape(3,4)
print(a)

def convert(x):
    if x < 20:
        return "small"
    elif x <= 30:
        return "medium"
    else:
        return "large"

b = np.vectorize(convert)(a)
print(b)
