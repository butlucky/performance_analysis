import string
import time
import os
import matplotlib.pyplot as plt
import numpy as np

output_dir = "./output/"

def get_perf(filename):
    intfs = []
    with open(filename,'r',encoding='utf8') as log_file:
        lines = log_file.readlines()
        for line in lines:
            if len(line)>3:
                mem_rss,cpu_duty,mem_duty,*name = line.split()
                intf_data = {
                    'mem_rss':mem_rss,
                    'cpu_duty':cpu_duty,
                    'mem_duty':mem_duty,
                    'name':name,
                }
                intfs.append(intf_data)
    return intfs

def get_proc(filename):
    process = []
    with open(filename,'r',encoding='utf8') as log_file:
        lines = log_file.readlines()
        for line in lines:
            process.append(line)
    return process

def main():
    process = get_proc('process.txt')
    intfs   = get_perf('rockchip/cpu.log')

    cpu = [[] for j in range(len(process))]
    mem = [[] for j in range(len(process))]

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
                break

    if not os.path.exists(output_dir):
        os.makedirs(output_dir) 
    time_str = time.strftime('%Y%m%d-%H:%M:%S', time.localtime(time.time()))
# plot cpu usage
    plt.figure(0)
    plt.title("cpu comsumption statisitics")
    plt.xlabel("time: sencond")
    plt.ylabel("cpu usage percent: (Max 800%)")
    plt.xlim((0, 60))
    plt.ylim((0, 800))
    my_x_ticks = np.arange(0, 60, 2)
    my_y_ticks = np.arange(0, 800, 20)
    plt.xticks(my_x_ticks)
    plt.yticks(my_y_ticks)
    for i in range(0,len(process)):
        procname = ''.join(process[i])
        plt.plot(range(0,60),[float(x) for x in cpu[i]],label=procname)
    plt.legend(loc="best")
    plt.savefig(output_dir + time_str + "cpu_usage")
# plot memory usage
    plt.figure(1)
    plt.title("memory comsumption statisitics")
    plt.xlabel("time: sencond")
    plt.ylabel("mem rss usage: Max 7.5G")
    plt.xlim((0, 60))
    plt.ylim((0, 1000))
    my_x_ticks = np.arange(0, 60, 2)
    my_y_ticks = np.arange(0, 1000, 50)
    plt.xticks(my_x_ticks)
    plt.yticks(my_y_ticks)
    for i in range(0,len(process)):
        procname = ''.join(process[i])
        plt.plot(range(0,60),[int(x) for x in mem[i]],label=procname)
    plt.legend(loc="best")
    plt.savefig(output_dir + time_str + "memory_usage")

if __name__ == '__main__':
    main()

