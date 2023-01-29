# Нарисуйте график рассеяния со случайным распределением по осям X и Y.

import numpy as np
import matplotlib.pyplot as plt

X = np.random.rand(500)
Y = np.random.rand(500)

figure, axes = plt.subplots()
axes.scatter(X,Y,c='deeppink')
figure.set_facecolor('violet')
axes.set_facecolor('lightyellow')
axes.set_title('График рассеяния')
figure.set_figwidth(8)
figure.set_figheight(8)

plt.show()
