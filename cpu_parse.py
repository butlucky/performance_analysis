import string
import time
import os
import matplotlib.pyplot as plt
import numpy as np
from include import *

output_dir = "./output/"

def get_perf(filename):
    intfs = []
    wc = 0

    with open(filename,'r',encoding='utf8') as log_file:
        lines = log_file.readlines()
        for line in lines:
            wc += 1
            if len(line)>3:
                mem_rss,cpu_duty,mem_duty,*name = line.split()
                intf_data = {
                    'mem_rss':mem_rss,
                    'cpu_duty':cpu_duty,
                    'mem_duty':mem_duty,
                    'name':name,
                }
                intfs.append(intf_data)
        if wc < 8:
            print("!!! warning: can not capture cpu loading,please confirm !!!")
            os._exit(0)

    return intfs

def get_proc(filename):
    process = []
    with open(filename,'r',encoding='utf8') as log_file:
        lines = log_file.readlines()
        for line in lines:
            process.append(line)
    return process

def main():
    process = get_proc(plt_process_file)
    intfs   = get_perf(plt_cpu_perf_file)

    cpu = [[] for j in range(len(process))]
    mem = [[] for j in range(len(process))]
    val = [ 0 for j in range(len(process))]
    eout = 0

    for i in range(0,len(intfs)):
        strname = ''.join(intfs[i]['name'])
        for j in range(0,len(process)):
            procname = ''.join(process[j])
            procname = procname.strip()
            if strname.find(procname)>=0:
                cpu[j].append(intfs[i]['cpu_duty'])
                mem_rss = ''.join(intfs[i]['mem_rss'])
                mem_rss = mem_rss.strip('M')
                mem[j].append(mem_rss)
                val[j] +=1
                break
    for i in range(0,len(process)):
        if val[i] != x_axis_limit:
            print("!!!waring: process data missing, process name->",process[i])
            print("we need ->",x_axis_limit,"capture ->",val[i],"fill it")
            for j in range(val[i],x_axis_limit):
                cpu[i].append(cpu[i][j-1])
                mem[i].append(mem[i][j-1])

    if not os.path.exists(output_dir):
        os.makedirs(output_dir) 
    time_str = time.strftime('%Y%m%d-%H:%M:%S', time.localtime(time.time()))

# plot cpu usage
    plt.figure(0)
    plt.figure(figsize=(16,4))
    plt.tick_params(axis='x',labelsize=8)
    plt.title(plt_cpu_title)
    plt.xlabel(x_axis_label)
    plt.xlim((0, x_axis_limit))
    my_x_ticks = np.arange(0, x_axis_limit, x_axis_step)
    plt.xticks(my_x_ticks)
    plt.xticks(rotation=-25)
    plt.ylabel(plt_cpu_ylabel)
    plt.ylim((0, plt_cpu_y_axis_limit))
    my_y_ticks = np.arange(0, plt_cpu_y_axis_limit, plt_cpu_y_axis_step)
    plt.yticks(my_y_ticks)
    for i in range(0,len(process)):
        procname = ''.join(process[i])
        plt.plot(range(0,x_axis_limit),[float(x) for x in cpu[i]],label=procname)
    plt.legend(loc="best",fontsize = 'x-small')
    plt.savefig(output_dir + time_str + "-cpu_usage")

# plot memory usage
    plt.figure(1)
    plt.figure(figsize=(16,4))
    plt.tick_params(axis='x',labelsize=8)
    plt.title(plt_mem_title)
    plt.xlabel(x_axis_label)
    plt.xlim((0, x_axis_limit))
    my_x_ticks = np.arange(0, x_axis_limit, x_axis_step)
    plt.xticks(my_x_ticks)
    plt.xticks(rotation=-25)
    plt.ylabel(plt_mem_ylabel)
    plt.ylim((0, plt_mem_y_axis_limit))
    my_y_ticks = np.arange(0, plt_mem_y_axis_limit, plt_mem_y_axis_step)
    plt.yticks(my_y_ticks)
    for i in range(0,len(process)):
        procname = ''.join(process[i])
        plt.plot(range(0,x_axis_limit),[float(x) for x in mem[i]],label=procname)
    plt.legend(loc="best",fontsize = 'x-small')
    plt.savefig(output_dir + time_str + "-memory_usage")

if __name__ == '__main__':
    main()

