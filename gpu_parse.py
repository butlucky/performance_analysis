import string
import time
import os
import matplotlib.pyplot as plt
import numpy as np

output_dir = "./output/"

def main():
    gpu = []

    with open('rockchip/gpu.log','r',encoding='utf8') as log_file:
        lines = log_file.readlines()
        for line in lines:
            gpu.append(line)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir) 
    time_str = time.strftime('%Y%m%d-%H:%M:%S', time.localtime(time.time()))

# plot gpu usage
    plt.figure(0)
    plt.title("gpu comsumption statisitics")
    plt.xlabel("time: sencond")
    plt.ylabel("gpu usage percent: Max 100%")
    plt.xlim((0, 60))
    plt.ylim((0, 100))
    my_x_ticks = np.arange(0, 60, 2)
    my_y_ticks = np.arange(0, 100, 10)
    plt.xticks(my_x_ticks)
    plt.yticks(my_y_ticks)
    plt.plot(range(0,60),[int(x) for x in gpu],label='Mali-G610')
    plt.savefig(output_dir + time_str + "gpu_usage")

if __name__ == '__main__':
    main()

