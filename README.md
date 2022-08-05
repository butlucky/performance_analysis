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
