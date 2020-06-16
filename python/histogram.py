import matplotlib.pyplot as plt
from matplotlib import rc
import randoms as rnd
import numpy as np

import matplotlib
matplotlib.use('Agg')

N1 = 1000
N2 = 100000
params1 = [[0, 10], [0, 15], [0, 25], [0, 35]]
params2 = [[0, 50], [0, 75], [0, 85], [0, 120]]

data1_1 = rnd.clhistogram(N1, params1[0][0], params1[0][1])[0]
data1_2 = rnd.clhistogram(N1, params1[1][0], params1[1][1])[0]
data1_3 = rnd.clhistogram(N1, params1[2][0], params1[2][1])[0]
data1_4 = rnd.clhistogram(N1, params1[3][0], params1[3][1])[0]

data2_1 = rnd.clhistogram(N2, params2[0][0], params2[0][1])[0]
data2_2 = rnd.clhistogram(N2, params2[1][0], params2[1][1])[0]
data2_3 = rnd.clhistogram(N2, params2[2][0], params2[2][1])[0]
data2_4 = rnd.clhistogram(N2, params2[3][0], params2[3][1])[0]

# print(data1_1)
# print(data1_2)
# print(data1_3)
# print(data1_4)

# PLOT  THE HISTOGRAM FOR DATA

# DATA1

bins1 = 45
bins2 = 55

plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = "Times New Roman"
plt.rcParams["font.size"] = 10
fig1, ((ax1_1, ax1_2), (ax2_1, ax2_2)) = plt.subplots(
    2, 2)
fig1.subplots_adjust(left=0.1, right=0.95, bottom=0.15)
fig1.text(0.5, 0.03, 'x', ha='center')
fig1.text(-0.02, 0.5, 'Probability', va='center', rotation='vertical')

# plt.suptitle(f'Histogram for the normally distributed data \n N={N1}')
# # plt.gca().set(title='Probability Histogram of Diamond Depths', ylabel='Probability')

ax1_1.set(title=f'Histogram for N={N1} data points')
ax1_1.hist(data1_1, bins=bins1, histtype='stepfilled',
           alpha=0.9, density=True, stacked=True, label=f'$\mu$={params1[0][0]} , $\sigma$={params1[0][1]}')
ax1_1.hist(data1_2, bins=bins1, histtype='stepfilled',
           alpha=0.8, density=True, stacked=True, label=f'$\mu$={params1[1][0]} , $\sigma$={params1[1][1]}')
ax1_1.legend(loc='best', fontsize=8)
ax2_1.hist(data1_3, bins=bins1, histtype='stepfilled',
           alpha=0.9, density=True, stacked=True, label=f'$\mu$={params1[2][0]} , $\sigma$={params1[2][1]}')
ax2_1.hist(data1_4, bins=bins1, histtype='stepfilled',
           alpha=0.8, density=True, stacked=True, label=f'$\mu$={params1[3][0]} , $\sigma$={params1[3][1]}')
ax2_1.legend(loc='best', fontsize=8)

ax1_2.set(title=f'Histogram for N={N2} data points')
ax1_2.hist(data2_1, bins=bins2, histtype='stepfilled',
           alpha=0.9, density=True, stacked=True, label=f'$\mu$={params2[0][0]} , $\sigma$={params2[0][1]}')
ax1_2.hist(data2_2, bins=bins2, histtype='stepfilled',
           alpha=0.8, density=True, stacked=True, label=f'$\mu$={params2[1][0]} , $\sigma$={params2[1][1]}')
ax1_2.legend(loc='best', fontsize=8)
ax2_2.hist(data2_3, bins=bins2, histtype='stepfilled',
           alpha=0.9, density=True, stacked=True, label=f'$\mu$={params2[2][0]} , $\sigma$={params2[2][1]}')
ax2_2.hist(data2_4, bins=bins2, histtype='stepfilled',
           alpha=0.8, density=True, stacked=True, label=f'$\mu$={params2[3][0]} , $\sigma$={params2[3][1]}')
ax2_2.legend(loc='best', fontsize=8)

plt.savefig('histogram-data-density.pdf', bbox_inches='tight')
plt.close()
##

plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = "Times New Roman"
plt.rcParams["font.size"] = 10
fig1, ((ax1_1, ax1_2), (ax2_1, ax2_2)) = plt.subplots(
    2, 2)
fig1.subplots_adjust(left=0.1, right=0.95, bottom=0.15)
fig1.text(0.5, 0.03, 'x', ha='center')
fig1.text(-0.02, 0.5, 'Counts', va='center', rotation='vertical')

# plt.suptitle(f'Histogram for the normally distributed data \n N={N1}')
# # plt.gca().set(title='Probability Histogram of Diamond Depths', ylabel='Probability')

ax1_1.set(title=f'Histogram for N={N1} data points')
ax1_1.hist(data1_1, bins=bins1, histtype='stepfilled',
           alpha=0.9,  label=f'$\mu$={params1[0][0]} , $\sigma$={params1[0][1]}')
ax1_1.hist(data1_2, bins=bins1, histtype='stepfilled',
           alpha=0.8,  label=f'$\mu$={params1[1][0]} , $\sigma$={params1[1][1]}')
ax1_1.legend(loc='best', fontsize=8)
ax2_1.hist(data1_3, bins=bins1, histtype='stepfilled',
           alpha=0.9,  label=f'$\mu$={params1[2][0]} , $\sigma$={params1[2][1]}')
ax2_1.hist(data1_4, bins=bins1, histtype='stepfilled',
           alpha=0.8,  label=f'$\mu$={params1[3][0]} , $\sigma$={params1[3][1]}')
ax2_1.legend(loc='best', fontsize=8)

ax1_2.set(title=f'Histogram for N={N2} data points')
ax1_2.hist(data2_1, bins=bins2, histtype='stepfilled',
           alpha=1,  label=f'$\mu$={params2[0][0]} , $\sigma$={params2[0][1]}')
ax1_2.hist(data2_2, bins=bins2, histtype='stepfilled',
           alpha=0.7,  label=f'$\mu$={params2[1][0]} , $\sigma$={params2[1][1]}')
ax1_2.legend(loc='best', fontsize=8)
ax2_2.hist(data2_3, bins=bins2,  histtype='barstacked',
           alpha=1,  label=f'$\mu$={params2[2][0]} , $\sigma$={params2[2][1]}')
ax2_2.hist(data2_4, bins=bins2, histtype='barstacked',
           alpha=0.7, label=f'$\mu$={params2[3][0]} , $\sigma$={params2[3][1]}')
ax2_2.legend(loc='best', fontsize=8)

plt.savefig('histogram-data-counts.pdf', bbox_inches='tight')
plt.close()
