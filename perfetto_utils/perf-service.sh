#!/bin/sh

adb shell getprop ro.hardware
adb shell getprop ro.board.platform
adb shell getprop ro.build.version.release

echo "Now simpleperf Graph ..."
adb shell simpleperf record --app com.ctsi.cloudmeeting --call-graph dwarf --duration 30 -m 4096 -f 200 -c 1000000 -o /data/perf.data
sleep 35
adb pull /data/perf.data ./output/
./simpleperf/simpleperf report -i ./output/perf.data --sort dso > ./output/perf.dso.log
./simpleperf/stackcollapse.py -i ./output/perf.data > ./output/perf.folded.data
./FlameGraph/flamegraph.pl ./output/perf.folded.data > ./output/flamegraph.svg

echo "Now perfetto perform ..."
adb push ./perfetto/perfetto-arm64 /data/perfetto 
cat ./perfetto/config.pbtx | adb shell /data/perfetto -c - --txt -o /data/trace.pftrace
sleep 35
adb pull /data/trace.pftrace ./output

