import randoms as rnd

import matplotlib
import numpy as np
import matplotlib.pyplot as plt

y = rnd.clhistogram(1000, 0, 10)
y2 = rnd.clhistogram(1000, 0, 20)
y3 = rnd.clhistogram(1000, 0, 25)
y4 = rnd.clhistogram(1000, 0, 35)
# print('The generated normal distribution:')
# print(y[0])
# print(y2[0])

elements = y[1]
counters = y[2]
# print('Counted elements:')
# for x in range(len(elements)):
# print(elements[x], counters[x])

# PLOT PART
num_bins = 69
fig, (ax, ax2) = plt.subplots(2, sharex=True)
fig.subplots_adjust(left=0.1, right=0.95, bottom=0.15)

ax.set(title='Histogram for the normally distributed data')
ax2.set(xlabel='x')
ax.hist(y[0], bins=num_bins, histtype='stepfilled',
        alpha=1, density=True, label=r'$\mu={0}\ ;\ \sigma={10}$')
ax.hist(y2[0], bins=num_bins, histtype='stepfilled', alpha=0.8,
        density=True, label=r'$\mu={0}\ ;\ \sigma={20}$')
ax.hist(y3[0], bins=num_bins, histtype='stepfilled', alpha=0.6,
        density=True, label=r'$\mu={0}\ ;\ \sigma={25}$')
ax.hist(y4[0], bins=num_bins, histtype='stepfilled', alpha=0.6,
        density=True, label=r'$\mu={0}\ ;\ \sigma={35}$')
ax2.hist(y4[0], bins=num_bins, histtype='stepfilled', alpha=0.6,
         density=True, label=r'$\mu={0}\ ;\ \sigma={35}$')
# plt.title('Histogram for the normally distributed data')
ax.legend(loc='best')
ax2.legend(loc='best')
# ax.ylabel('')
plt.savefig('hist.pdf', bbox_inches='tight')
