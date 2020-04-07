import numpy as np
import matplotlib.pyplot as plt

_ = plt.plot(x_vers, y_vers, '.')
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

_ = plt.plot(ptiles_vers, percentiles/100, marker='D', color='red',
         linestyle='none')
plt.show()

differences = versicolor_petal_length - np.mean(versicolor_petal_length)
diff_sq = differences**2
variance_explicit = np.mean(diff_sq)
variance_np = np.var(versicolor_petal_length)
print(variance_explicit, variance_np)

def pearson_r(x, y):
   
    corr_mat = np.corrcoef(x, y)
    return corr_mat[0,1]

r = pearson_r(versicolor_petal_length, versicolor_petal_width)

print(r)
