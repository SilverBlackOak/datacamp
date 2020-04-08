import numpy as np
import matplotlib.pyplot as plt

def successive_poisson(tau1, tau2, size=1):
    t1 = np.random.exponential(tau1, size)
    t2 = np.random.exponential(tau2, size)
    return t1 + t2

waiting_times = successive_poisson(764,715, size=100000)

_ = plt.hist(waiting_times, bins=100, normed=True, histtype='step')

_ = plt.xlabel('Mean waiting time for a no-hitter')
_ = plt.ylabel('Mean waiting time for hitting the cycle')

plt.show()
