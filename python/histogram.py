import randoms as rnd
import numpy as np
import platform as os
from datetime import datetime
import time
import sys
import socket  # for IP
import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib
matplotlib.use('Agg')


N1 = 1000
N2 = 100000

# data1_1 = rnd.clhistogram(N1, params1[0][0], params1[0][1])[0]
# data1_2 = rnd.clhistogram(N1, params1[1][0], params1[1][1])[0]
# data1_3 = rnd.clhistogram(N1, params1[2][0], params1[2][1])[0]
# data1_4 = rnd.clhistogram(N1, params1[3][0], params1[3][1])[0]
# data2_1 = rnd.clhistogram(N2, params2[0][0], params2[0][1])[0]
# data2_2 = rnd.clhistogram(N2, params2[1][0], params2[1][1])[0]
# data2_3 = rnd.clhistogram(N2, params2[2][0], params2[2][1])[0]
# data2_4 = rnd.clhistogram(N2, params2[3][0], params2[3][1])[0]

params1 = [[0, 10], [0, 15], [0, 25], [0, 35]]
params2 = [[0, 50], [0, 75], [0, 85], [0, 120]]

data_1 = [rnd.clhistogram(N1, params1[0][0], params1[0][1])[0], rnd.clhistogram(N1, params1[1][0], params1[1][1])[
    0], rnd.clhistogram(N1, params1[2][0], params1[2][1])[0], rnd.clhistogram(N1, params1[3][0], params1[3][1])[0]]

data_2 = [rnd.clhistogram(N2, params2[0][0], params2[0][1])[0], rnd.clhistogram(N2, params2[1][0], params2[1][1])[
    0], rnd.clhistogram(N2, params2[2][0], params2[2][1])[0], rnd.clhistogram(N2, params2[3][0], params2[3][1])[0]]

bins1 = 45
bins2 = 55


def CreateHistogram(N1, N2, data1, params1, bins1, data2, params2,  bins2, filename_dens, filename_counts, seeds):
    # preparing the data
    data1_1 = data1[0]
    data1_2 = data1[1]
    data1_3 = data1[2]
    data1_4 = data1[3]
    data2_1 = data2[0]
    data2_2 = data2[1]
    data2_3 = data2[2]
    data2_4 = data2[3]

    plt.rcParams["font.family"] = "serif"
    plt.rcParams["font.serif"] = "Times New Roman"
    plt.rcParams["font.size"] = 10

    fig1, ((ax1_1, ax1_2), (ax2_1, ax2_2)) = plt.subplots(
        2, 2)
    fig1.subplots_adjust(left=0.1, right=0.95, bottom=0.15)
    fig1.text(0.5, 0.03, 'x', ha='center')

    title_label = 'Histogram - Density'+' | ' + \
        'rd='+str(seeds[0])+' ; '+'mt='+str(seeds[1])
    fig1.text(0.5, 1, title_label, ha='center')
    fig1.text(-0.02, 0.5, 'Probability', va='center', rotation='vertical')

    # seed_label = 'rd='+str(seeds[0])+'\n'+'mt='+str(seeds[1])
    # fig1.text(0.5, 0.1, seed_label, fontsize=7, style='italic',
    #           bbox={'facecolor': 'red', 'alpha': 0.1, 'pad': 10})

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

    plt.savefig(filename_dens, bbox_inches='tight')
    plt.close()

    plt.rcParams["font.family"] = "serif"
    plt.rcParams["font.serif"] = "Times New Roman"
    plt.rcParams["font.size"] = 10
    fig1, ((ax1_1, ax1_2), (ax2_1, ax2_2)) = plt.subplots(
        2, 2)
    fig1.subplots_adjust(left=0.1, right=0.95, bottom=0.15)
    fig1.text(0.5, 0.03, 'x', ha='center')

    title_label = 'Histogram - Counts'+' | ' + \
        'rd='+str(seeds[0])+' ; '+'mt='+str(seeds[1])
    fig1.text(0.5, 1, title_label, ha='center')
    fig1.text(-0.02, 0.5, 'Counts', va='center', rotation='vertical')

    # seed_label = 'rd='+str(seeds[0])+'\n'+'mt='+str(seeds[1])

    # fig1.text(0.5, 1, seed_label, fontsize=7, style='italic',
    #           bbox={'facecolor': 'red', 'alpha': 0.1, 'pad': 10})

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

    plt.savefig(filename_counts, bbox_inches='tight')
    plt.close()


path_plots = '../output/'
path_logs = '../logs/'

counts_filename = 'counts-hist'
density_filename = 'dens-hist'

extension = '.pdf'
log_ext = '.log'
which_os = os.system()


def generate_log_line(info):
    message = 'Plot'


NPLOTS = 50

log_name = path_logs+'log-file-'+str(os.platform())+log_ext

# SAFETY FOR DARWIN issue with IP
IP = socket.gethostbyname('localhost')
HOSTNAME = socket.gethostname()
current_os = str(os.system())
if(current_os != 'Darwin'):
    IP = socket.gethostbyname(HOSTNAME)

# IP = socket.gethostbyname('localhost') # changed to localhost since there is an issue with macOS VMs on Azure
pyM = sys.version_info.major
pym = sys.version_info.minor
AARCH = str(os.processor())+'_'+str(os.architecture()[0])
nl = '\n'


log_file = open(log_name, 'w')

for plot_id in range(15):
    print(f'Generating plot no-{plot_id+1}...')
    filename1 = path_plots+density_filename + \
        '-'+str(plot_id+1)+'-'+which_os+extension
    filename2 = path_plots+counts_filename + \
        '-'+str(plot_id+1)+'-'+which_os+extension
    N1 = 1000
    N2 = 100000
    params1 = [[0, 10], [0, 15], [0, 25], [0, 35]]
    params2 = [[0, 50], [0, 75], [0, 85], [0, 120]]
    seeds = rnd.clhistogram(N2, params2[0][0], params2[0][1])[3]

    data_1 = [rnd.clhistogram(N1, params1[0][0], params1[0][1])[0], rnd.clhistogram(N1, params1[1][0], params1[1][1])[
        0], rnd.clhistogram(N1, params1[2][0], params1[2][1])[0], rnd.clhistogram(N1, params1[3][0], params1[3][1])[0]]

    data_2 = [rnd.clhistogram(N2, params2[0][0], params2[0][1])[0], rnd.clhistogram(N2, params2[1][0], params2[1][1])[
        0], rnd.clhistogram(N2, params2[2][0], params2[2][1])[0], rnd.clhistogram(N2, params2[3][0], params2[3][1])[0]]

    bins1 = 45
    bins2 = 55
    CreateHistogram(N1, N2, data_1, params1, bins1,
                    data_2, params2, bins2, filename1, filename2, seeds)
    print(f'Finished plot no-{plot_id+1}!')
    print(f'\n')
    status = 1
    now = str(datetime.utcnow())
    s0 = f'HIST_ID={plot_id} STATUS={status} GEN_TIME @{now} IP={IP} HSTNM={HOSTNAME} PLTFM={current_os} AARCH={AARCH} PY_V={pyM}.{pym}'
    log_file.write(s0+nl)

log_file.close()

# print(data1_1)
# print(data1_2)
# print(data1_3)
# print(data1_4)

# # PLOT  THE HISTOGRAM FOR DATA

# # DATA1

# bins1 = 45
# bins2 = 55

# plt.rcParams["font.family"] = "serif"
# plt.rcParams["font.serif"] = "Times New Roman"
# plt.rcParams["font.size"] = 10
# fig1, ((ax1_1, ax1_2), (ax2_1, ax2_2)) = plt.subplots(
#     2, 2)
# fig1.subplots_adjust(left=0.1, right=0.95, bottom=0.15)
# fig1.text(0.5, 0.03, 'x', ha='center')
# fig1.text(-0.02, 0.5, 'Probability', va='center', rotation='vertical')

# # plt.suptitle(f'Histogram for the normally distributed data \n N={N1}')
# # # plt.gca().set(title='Probability Histogram of Diamond Depths', ylabel='Probability')

# ax1_1.set(title=f'Histogram for N={N1} data points')
# ax1_1.hist(data1_1, bins=bins1, histtype='stepfilled',
#            alpha=0.9, density=True, stacked=True, label=f'$\mu$={params1[0][0]} , $\sigma$={params1[0][1]}')
# ax1_1.hist(data1_2, bins=bins1, histtype='stepfilled',
#            alpha=0.8, density=True, stacked=True, label=f'$\mu$={params1[1][0]} , $\sigma$={params1[1][1]}')
# ax1_1.legend(loc='best', fontsize=8)
# ax2_1.hist(data1_3, bins=bins1, histtype='stepfilled',
#            alpha=0.9, density=True, stacked=True, label=f'$\mu$={params1[2][0]} , $\sigma$={params1[2][1]}')
# ax2_1.hist(data1_4, bins=bins1, histtype='stepfilled',
#            alpha=0.8, density=True, stacked=True, label=f'$\mu$={params1[3][0]} , $\sigma$={params1[3][1]}')
# ax2_1.legend(loc='best', fontsize=8)

# ax1_2.set(title=f'Histogram for N={N2} data points')
# ax1_2.hist(data2_1, bins=bins2, histtype='stepfilled',
#            alpha=0.9, density=True, stacked=True, label=f'$\mu$={params2[0][0]} , $\sigma$={params2[0][1]}')
# ax1_2.hist(data2_2, bins=bins2, histtype='stepfilled',
#            alpha=0.8, density=True, stacked=True, label=f'$\mu$={params2[1][0]} , $\sigma$={params2[1][1]}')
# ax1_2.legend(loc='best', fontsize=8)
# ax2_2.hist(data2_3, bins=bins2, histtype='stepfilled',
#            alpha=0.9, density=True, stacked=True, label=f'$\mu$={params2[2][0]} , $\sigma$={params2[2][1]}')
# ax2_2.hist(data2_4, bins=bins2, histtype='stepfilled',
#            alpha=0.8, density=True, stacked=True, label=f'$\mu$={params2[3][0]} , $\sigma$={params2[3][1]}')
# ax2_2.legend(loc='best', fontsize=8)

# plt.savefig('histogram-data-density.pdf', bbox_inches='tight')
# plt.close()
# ##

# plt.rcParams["font.family"] = "serif"
# plt.rcParams["font.serif"] = "Times New Roman"
# plt.rcParams["font.size"] = 10
# fig1, ((ax1_1, ax1_2), (ax2_1, ax2_2)) = plt.subplots(
#     2, 2)
# fig1.subplots_adjust(left=0.1, right=0.95, bottom=0.15)
# fig1.text(0.5, 0.03, 'x', ha='center')
# fig1.text(-0.02, 0.5, 'Counts', va='center', rotation='vertical')

# # plt.suptitle(f'Histogram for the normally distributed data \n N={N1}')
# # # plt.gca().set(title='Probability Histogram of Diamond Depths', ylabel='Probability')

# ax1_1.set(title=f'Histogram for N={N1} data points')
# ax1_1.hist(data1_1, bins=bins1, histtype='stepfilled',
#            alpha=0.9,  label=f'$\mu$={params1[0][0]} , $\sigma$={params1[0][1]}')
# ax1_1.hist(data1_2, bins=bins1, histtype='stepfilled',
#            alpha=0.8,  label=f'$\mu$={params1[1][0]} , $\sigma$={params1[1][1]}')
# ax1_1.legend(loc='best', fontsize=8)
# ax2_1.hist(data1_3, bins=bins1, histtype='stepfilled',
#            alpha=0.9,  label=f'$\mu$={params1[2][0]} , $\sigma$={params1[2][1]}')
# ax2_1.hist(data1_4, bins=bins1, histtype='stepfilled',
#            alpha=0.8,  label=f'$\mu$={params1[3][0]} , $\sigma$={params1[3][1]}')
# ax2_1.legend(loc='best', fontsize=8)

# ax1_2.set(title=f'Histogram for N={N2} data points')
# ax1_2.hist(data2_1, bins=bins2, histtype='stepfilled',
#            alpha=1,  label=f'$\mu$={params2[0][0]} , $\sigma$={params2[0][1]}')
# ax1_2.hist(data2_2, bins=bins2, histtype='stepfilled',
#            alpha=0.7,  label=f'$\mu$={params2[1][0]} , $\sigma$={params2[1][1]}')
# ax1_2.legend(loc='best', fontsize=8)
# ax2_2.hist(data2_3, bins=bins2,  histtype='barstacked',
#            alpha=1,  label=f'$\mu$={params2[2][0]} , $\sigma$={params2[2][1]}')
# ax2_2.hist(data2_4, bins=bins2, histtype='barstacked',
#            alpha=0.7, label=f'$\mu$={params2[3][0]} , $\sigma$={params2[3][1]}')
# ax2_2.legend(loc='best', fontsize=8)

# plt.savefig('histogram-data-counts.pdf', bbox_inches='tight')
# plt.close()
