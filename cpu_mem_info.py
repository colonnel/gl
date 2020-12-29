#!/usr/bin/env python
import psutil
from sys import argv


def get_cpu_metrics():
    all_cpu_metrics = psutil.cpu_times_percent(interval=1)
    print('system.cpu.user: ' + str(all_cpu_metrics[0]))
    print('system.cpu.system: ' + str(all_cpu_metrics[2]))
    print('system.cpu.idle: ' + str(all_cpu_metrics[3]))
    print('system.cpu.iowait: ' + str(all_cpu_metrics[4]))
    print('system.cpu.steal: ' + str(all_cpu_metrics[7]))
    print('system.cpu.guest: ' + str(all_cpu_metrics[8]))


def get_mem_metrics():
    virt_mem_metrics = psutil.virtual_memory()
    swap_mem_metrics = psutil.swap_memory()
    print('virtual total: ' + str(virt_mem_metrics[0]))
    print('virtual used: ' + str(virt_mem_metrics[3]))
    print('virtual free: ' + str(virt_mem_metrics[4]))
    print('virtual shared: ' + str(virt_mem_metrics[9]))
    print('swap total: ' + str(swap_mem_metrics[0]))
    print('swap used: ' + str(swap_mem_metrics[1]))
    print('swap free: ' + str(swap_mem_metrics[2]))


def usage():
    print('Get CPU metrics: ' + argv[0] + ' cpu')
    print('Get Memory metrics: ' + argv[0] + ' mem')


def run_script():
    try:
        key = argv[1]
    except IndexError as e:
        key = ''
    if key == 'cpu':
        get_cpu_metrics()
    elif key == 'mem':
        get_mem_metrics()
    else:
        usage()

run_script()