#########################################################################
# File Name: collect_data.sh
# Author: Wenwen He
# Email:  butlucky@gmail.com
# Created Time: Tue Aug  2 17:47:42 2022
#########################################################################
#!/bin/bash

:<<!
	< gpu_util >
	  [0] rockchip : /sys/devices/platform/*gpu/utilisation
	  [1] amlogic  : /sys/class/*gpu/utilization
	  [2] qualcomm : /sys/class/kgsl/kgsl-3d0/gpubusy
	  [3] mtk      : /d/ged/hal/gpu_utilization
	< script_path >
	  [0] non root : /sdcard/Android/data/
	  [1] root     : /data/
!

gpu_util="/sys/devices/platform/*gpu/utilisation"
script_path="/sdcard/Android/data/"
count=60
interval=1

usage()
{
	echo "Please running like this->"
	echo "    ./one_key_check.sh rockchip/amlogic/qualcomm/mtk..."
}

parse_by_cmd()
{
	echo "Android terminal do not support exec script directly, try exec command now !!!"
	adb shell "rm /sdcard/{cpu.log,gpu.log}"
	adb shell "top -b -o RES,%CPU,%MEM,CMDLINE -s 2 -d $interval -m 15 -n $count -q 1>/sdcard/cpu.log 2>/sdcard/cpu.log"
	adb shell "ls $gpu_util 1>/dev/null"
	if [ $? != 0 ];then
		adb shell "echo "gpu loading utilisation did not expose!" > /sdcard/gpu.log"
		return
	fi
	# default 1cps , total 60s , maybe need change here
	[ $1 == 'rockchip' ]  && adb shell 'for i in `seq 1 60`; do cat /sys/devices/platform/*gpu/utilisation >> /sdcard/gpu.log ; sleep 1 ; done'
	[ $1 == 'amlogic' ]  && adb shell 'for i in `seq 1 60`; do cat /sys/class/*gpu/utilization >> /sdcard/gpu.log ; sleep 1 ; done'
	[ $1 == 'qualcomm' ]  && adb shell 'for i in `seq 1 60`; do cat /sys/class/kgsl/kgsl-3d0/gpubusy >> /sdcard/gpu.log ; sleep 1 ; done'
	[ $1 == 'mtk' ]  && adb shell 'for i in `seq 1 60`; do cat /d/ged/hal/gpu_utilization >> /sdcard/gpu.log ; sleep 1 ; done'
}

[ $# != 1 ] && usage && exit
[ $1 == 'amlogic' ]  && gpu_util="/sys/class/*gpu/utilization"
[ $1 == 'qualcomm' ] && gpu_util="/sys/class/kgsl/kgsl-3d0/gpubusy"
[ $1 == 'mtk' ] && gpu_util="/d/ged/hal/gpu_utilization"

connect=`adb devices | grep device | wc -l`
if [ $connect != 2 ];then
	echo "!!! warning: plz confirm connect only one android device !!!"
	exit
fi
root=`adb root | grep "running as root" | wc -l`
if [ $root != 0 ];then
	echo "android device get root permission"
	script_path='/data/'
fi

adb push soc_perf.sh $script_path
echo "start to collect performance data !!"
adb shell "chmod a+x $script_path/soc_perf.sh"
adb shell "$script_path/soc_perf.sh"
if [ $? != 0 ];then
	parse_by_cmd $1
fi

rm -f ./{cpu.log,gpu.log}
adb pull /sdcard/{cpu.log,gpu.log} ./
echo "collect done !!"
echo "start to parse performance data for the following process:"
echo "------------------------------------------------"
cat process.txt
echo "------------------------------------------------"
python cpu_parse.py
python gpu_parse.py
echo "parse done !!"
