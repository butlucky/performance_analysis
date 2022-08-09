1 soc_perf.sh脚本实现性能数据采样保存，默认按照cpu占用率排序
  1cps频率采样60秒top15的数据，可以根据实际情况修改。

  495M  157   6.6 com.example.android.ui
   44M 46.4   0.5 /vendor/bin/hw/android.hardware.media.c2@1.1-service
   31M 14.2   0.4 /vendor/bin/hw/android.hardware.camera.provider@2.4-service
   87M 10.7   1.1 /system/bin/surfaceflinger
  4.5M  7.1   0.0 top -b -o RES,%CPU,%MEM,CMDLINE -s 2 -d 1 -m 15 -n 60 -q
   12M  7.1   0.1 /vendor/bin/hw/android.hardware.graphics.composer@2.1-service
     0  3.5   0.0 [kworker/u17:4-mali_kbase_csf_kcpu]
     0  3.5   0.0 [kworker/u17:6-mali_kbase_csf_kcpu]
     0  3.5   0.0 [kworker/3:1-events]
     0  3.5   0.0 [kworker/u17:5-mali_kbase_csf_sync_upd]
   28M  3.5   0.3 media.extractor aextractor
   29M  3.5   0.3 /system/bin/cameraserver
     0  3.5   0.0 [kworker/4:1H-events_highpri]
  3.0M  0.0   0.0 /system/bin/sh /data/soc_perf.sh
     0  0.0   0.0 [kworker/7:0-events]
     0  0.0   0.0 [kworker/4:1-events]
     0  0.0   0.0 [kworker/5:0H-events_highpri]
     0  0.0   0.0 [kworker/0:1H-events_highpri]
     0  0.0   0.0 [kworker/0:1-pm]
     0  0.0   0.0 [kworker/6:1H-events_highpri]

2 在process.txt中配置保存需要采样分析性能的进程，具有唯一性即可，支持匹配查询。

  com.example.android.ui
  android.hardware.camera.provider
  android.hardware.media.c
  surfaceflinger
  android.hardware.graphics.composer
  cameraserver

3 在include.py中配置保存折线图相关参数

  # capture range 60s
  x_axis_limit = 60
  x_axis_step = 2
  x_axis_label = "time: sencond"
  # perf file
  plt_cpu_perf_file = "rockchip/cpu.log"
  plt_gpu_perf_file = "rockchip/gpu.log"
  plt_process_file="process.txt"
  # cpu line graph config
  plt_cpu_title = "cpu comsumption statisitics"
  plt_cpu_ylabel = "cpu usage percent: %"
  plt_cpu_y_axis_limit = 800
  plt_cpu_y_axis_step = 30
  # memory line graph config
  plt_mem_title = "memory comsumption statisitics"
  plt_mem_ylabel = "mem rss usage: M"
  plt_mem_y_axis_limit = 1024
  plt_mem_y_axis_step = 50
  # gpu line graph config
  plt_gpu_title = "gpu comsumption statisitics"
  plt_gpu_ylabel = "gpu usage percent: %"
  plt_gpu_y_axis_limit = 100
  plt_gpu_y_axis_step = 10

4 one_key_check.sh脚本为工具入口，在mac、linux的terminal上直接运行即可
  one_key_check.bat脚本为windows平台工具入口

  ./one_key_check.sh
  自动完成当下adb连接的android设备相关性能数据的抓取和分析并生成文件报告

5 output目录为最终输出的折线图文件，可直接双击查看

  ~/github/performence_analysis> ll output 
  -rw-r--r--  1 bytedance  staff  55002 Aug  5 16:40 20220805-16:39:59-cpu_usage.png
  -rw-r--r--  1 bytedance  staff  37019 Aug  5 16:40 20220805-16:39:59-memory_usage.png
  -rw-r--r--  1 bytedance  staff  33323 Aug  5 16:40 20220805-16:40:01-gpu_usage.png
  -rw-r--r--  1 bytedance  staff  52328 Aug  5 16:43 20220805-16:43:05-cpu_usage.png
  -rw-r--r--  1 bytedance  staff  36638 Aug  5 16:43 20220805-16:43:05-memory_usage.png
  -rw-r--r--  1 bytedance  staff  27477 Aug  5 16:43 20220805-16:43:06-gpu_usage.png
