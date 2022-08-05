#########################################################################
# File Name: soc_perf.sh
# Author: Wenwen He
# Email:  butlucky@gmail.com
# Created Time: Tue Aug  2 15:30:40 2022
#########################################################################
#!/system/bin/sh
count=60
interval=1

rm -f /data/{cpu.log,gpu.log}

top -b -o RES,%CPU,%MEM,CMDLINE -s 2 -d $interval -m 15 -n $count -q 1>/data/cpu.log
for i in `seq 1 $count`
do
    cat /sys/devices/platform/fb000000.gpu/utilisation >> /data/gpu.log
    sleep $interval
done

