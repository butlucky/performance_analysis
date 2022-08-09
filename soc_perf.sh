#########################################################################
# File Name: soc_perf.sh
# Author: Wenwen He
# Email:  butlucky@gmail.com
# Created Time: Tue Aug  2 15:30:40 2022
#########################################################################
#!/system/bin/sh
:<<!
    < gpu_util >
      [0] rockchip : /sys/devices/platform/*gpu/utilisation
      [1] amlogic  : /sys/class/*gpu/utilization
      [2] qualcomm : /sys/class/kgsl/kgsl-3d0/gpubusy
      [3] mtk      : /d/ged/hal/gpu_utilization
!

count=60
interval=1
[ -e /sys/devices/platform/*gpu/utilisation ] && gpu_util="/sys/devices/platform/*gpu/utilisation"
[ -e /sys/class/*gpu/utilization ]            && gpu_util="/sys/class/*gpu/utilization"
[ -e /sys/class/kgsl/kgsl-3d0/gpubusy ]       && gpu_util="/sys/class/kgsl/kgsl-3d0/gpubusy"
[ -e /d/ged/hal/gpu_utilization ]             && gpu_util="/d/ged/hal/gpu_utilization"

rm -f /sdcard/{cpu.log,gpu.log}
top -b -o RES,%CPU,%MEM,CMDLINE -s 2 -d $interval -m 15 -n $count -q 1>/sdcard/cpu.log 2>/sdcard/cpu.log
[ ! -e $gpu_util ] && echo "gpu loading utilisation didn't expose!" > /sdcard/gpu.log && exit
for i in `seq 1 $count`
do
    cat $gpu_util >> /sdcard/gpu.log
    sleep $interval
done

