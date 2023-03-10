# Даны два списка x и y
# Постройте два графика: plot(x,y) и scatter(x,y) на разных координатных плоскостях.
# Постройте еще один график plot(x,y) размером (6, 3) со следущими элементами:
# линиями сетки;
# подписями осей х и y;
# названием графика "Самолет".

import matplotlib.pyplot as plt

x = [-7, -5, 7, 9, 10, 10, 9, -7, 0, 5, 7, 4, 0, 6, 8, 4, 0]
y = [0, 2, 2, 5, 5, 1, 0, 0, 2, 6, 6, 2, 1, -3, -3, 1, 1]

plt.plot(x, y)
plt.title("Самолет")
plt.xlabel('Переменная X')
plt.ylabel('Переменная Y')
plt.grid()
plt.show()

plt.scatter(x, y)
plt.title("Самолет")
plt.xlabel('Переменная X')
plt.ylabel('Переменная Y')
plt.grid()
plt.show()

plt.figure(figsize=(6, 3))
plt.plot(x, y)
plt.title("Самолет")
plt.xlabel('Переменная X')
plt.ylabel('Переменная Y')
plt.grid()
plt.show()
