1 按照cpu占用率排序采样,默认60秒top15的数据，可以根据实际情况修改。

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

2 根据实际情况将采样进程的名字修改保存在process.txt中，具有唯一性即可，支持匹配查询。

  com.example.android.ui
  android.hardware.camera.provider
  android.hardware.media.c
  surfaceflinger
  android.hardware.graphics.composer
  cameraserver

3 配置折线图相关参数保存在include.py中

  # capture range 60s
  x_axis_limit = 60
  x_axis_step  = 2
  x_axis_label = "time: sencond"
  # cpu line graph config
  plt_cpu_title = "cpu comsumption statisitics"
  plt_cpu_ylabel = "cpu usage percent"
  plt_cpu_y_axis_limit = 800
  plt_cpu_y_axis_step = 20
  # memory line graph config
  plt_mem_title = "memory comsumption statisitics"
  plt_mem_ylabel = "mem rss usage"
  plt_mem_y_axis_limit = 1024
  plt_mem_y_axis_step = 50
  # gpu line graph config
  plt_gpu_title = "gpu comsumption statisitics"
  plt_gpu_ylabel = "gpu usage percent"
  plt_gpu_y_axis_limit = 100
  plt_gpu_y_axis_step = 10

4 程序入口
  one_key_check.sh  // mac & linux
  one_key_check.bat // windows


