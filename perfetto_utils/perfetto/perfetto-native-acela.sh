#########################################################################
# File Name: perfetto-native-acela.sh
# Author: Wenwen He
# Email:  butlucky@gmail.com
# Created Time: Fri May  9 10:16:37 2025
#########################################################################
#!/bin/bash
[ $# -ne 1 ] && echo "Usage: $0 <trace_file>" && exit 1
./trace_processor_shell --httpd $1 
