#########################################################################
# File Name: collect_data.sh
# Author: Wenwen He
# Email:  butlucky@gmail.com
# Created Time: Tue Aug  2 17:47:42 2022
#########################################################################
#!/bin/bash
[ $# != 1 ] && echo "need more args, eg: ./one_key_check.sh rockchip" && exit
adb root
adb remount
if [ $1 == rockchip ];then
    adb push rockchip/soc_perf.sh /data/
    echo "start to collect performance data ->"
    adb shell /data/soc_perf.sh
    rm -f ./rockchip/{cpu.log,gpu.log}
    adb pull /data/{cpu.log,gpu.log} ./rockchip/
    echo "collect already done!"
fi
echo "start to parse performance data"
python cpu_parse.py
python gpu_parse.py
echo "parse already done"
