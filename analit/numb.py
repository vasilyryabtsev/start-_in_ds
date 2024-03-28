import numpy as np
import matplotlib.pyplot as plt

numbers = np.loadtxt("numbers.csv", delimiter=",")

print(np.var(numbers, dtype=int, ddof=1))

plt.hist(numbers, bins=10, color='skyblue', edgecolor='black')

# Добавление заголовка и меток осей
plt.title('Гистограмма списка чисел')
plt.xlabel('Значения')
plt.ylabel('Частота')

# Отображение гистограммы
plt.show()

plt.savefig('plot.png')