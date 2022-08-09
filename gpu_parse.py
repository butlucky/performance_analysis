import string
import time
import os
import matplotlib.pyplot as plt
import numpy as np
from include import *

output_dir = "./output/"

def main():
    gpu = []
    wc = 0

    with open(plt_gpu_perf_file,'r',encoding='utf8') as log_file:
        lines = log_file.readlines()
        for line in lines:
            wc += 1
            gpu.append(line)

    if wc == 1:
        print("!!! warning: can not capture gpu loading,please confirm !!!")
        os._exit(0)
    if wc != x_axis_limit:
        print("!!! error: gpu cature data error, we need->",x_axis_limit,"but capture->",wc)
        os._exit(0)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir) 
    time_str = time.strftime('%Y%m%d-%H:%M:%S', time.localtime(time.time()))

# plot gpu usage
    plt.figure(0)
    plt.title(plt_gpu_title)
    plt.xlabel(x_axis_label)
    plt.ylabel(plt_gpu_ylabel)
    plt.xlim((0, x_axis_limit))
    plt.ylim((0, plt_gpu_y_axis_limit))
    my_x_ticks = np.arange(0, x_axis_limit, x_axis_step)
    my_y_ticks = np.arange(0, plt_gpu_y_axis_limit, plt_gpu_y_axis_step)
    plt.xticks(my_x_ticks)
    plt.yticks(my_y_ticks)
    plt.plot(range(0,x_axis_limit),[int(x) for x in gpu],label='Mali-G610')
    plt.savefig(output_dir + time_str + "-gpu_usage")

if __name__ == '__main__':
    main()

