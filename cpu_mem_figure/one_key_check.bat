adb root
adb remount
adb push rockchip/soc_perf.sh /data/
adb shell /data/soc_perf.sh
adb pull /data/{cpu.log,gpu.log} ./rockchip/
python cpu_parse.py
python gpu_parse.py
