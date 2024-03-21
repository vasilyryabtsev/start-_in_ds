import numpy as np
import matplotlib.pyplot as plt

#numbers = np.loadtxt("/home/vasily/start_in_ds/analit/numbers.csv", delimiter=",")
numbers = np.loadtxt("numbers.csv", delimiter=",")

print(np.var(numbers, dtype=int, ddof=1))

plt.hist(numbers)