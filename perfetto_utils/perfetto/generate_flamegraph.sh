#!/bin/bash

# 确保已安装 FlameGraph 工具（https://github.com/brendangregg/FlameGraph）
# 下载地址：git clone https://github.com/brendangregg/FlameGraph.git
FLAMEGRAPH_DIR=~/tools/perfetto/FlameGraph  # 根据实际路径修改

# 1. 用 simpleperf 导出带调用栈的文本数据（需包含符号信息）
./simplepf/simpleperf report -i perf.data > ~/perf.callgraph

# 2. 处理输出数据，转换为火焰图所需的栈格式（每行："计数 函数1;函数2;...;函数N"）
# 示例输入（simpleperf report 输出可能包含地址等无关信息，需过滤）：
# [0.01%] [kernel]  [k] __schedule
#         [0.01%] [user]  [k] main
# 转换为：1 main;__schedule

# 过滤并格式化（假设每行以百分比开头，符号在最后一列）
awk '
BEGIN { OFS=";" }
/^\s*\[.*%\]/ { 
    # 提取符号列（假设最后一个方括号后的内容为符号）
    symbol = $NF
    # 去除方括号和地址
    gsub(/\[|\]/, "", symbol)
    # 计数设为 1（或根据实际情况统计频率）
    print "1", symbol
}' ~/perf.callgraph > ~/perf.stacks

# 3. 折叠相同栈（使用 FlameGraph 的 stackcollapse 脚本）
perl $FLAMEGRAPH_DIR/stackcollapse-perf.pl ~/perf.stacks > ~/perf.folded

# 4. 生成火焰图（可选：--color=java 或 --color=cpp 根据语言调整）
perl $FLAMEGRAPH_DIR/flamegraph.pl --title="CPU Flame Graph" ~/perf.folded > ~/flamegraph.svg
