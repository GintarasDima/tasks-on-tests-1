# Реализуйте алгоритм сортировки массива пузырьком.
import numpy as np
import random

arr = np.random.randint(1,100,15)
print("Сгенерированный массив: ", arr)

def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
    return arr
print("Отсортированный массив: ", bubble_sort(arr))
