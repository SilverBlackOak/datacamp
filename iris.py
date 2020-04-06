import matplotlib.pyplot as plt
import numpy as np

def ecdf(data):
    n = len(data)
    x = np.sort(data)
    y = np.arange(1, n+1)/n
    return x, y
    
x_vers, y_vers = ecdf(versicolor_petal_length)
x_set, y_set = ecdf(setosa_petal_length)
x_virg, y_virg = ecdf(virginica_petal_length)

plt.plot(x_vers, y_vers, marker='.', linestyle='none')
plt.plot(x_set, y_set, marker='.', linestyle='none')
plt.plot(x_virg, y_virg, marker='.', linestyle='none')

plt.legend(('setosa', 'versicolor', 'virginica'), loc='lower right')
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

plt.show()
