#! /usr/bin/env python
#-*- coding: utf8 -*-

'''
 > File Name: analyze.py
 > Author: Wenwen He
 > Email:  butlucky@gmail.com
 > Created Time: Mon Mar 31 16:06:06 2025
'''

import re
import argparse

def parse_systrace(file_path, threshold):
    timestamps = []
    lines = []
    
    with open(file_path, 'r') as file:
        for line in file:
            match = re.search(r'\s*(\d+\.\d+):', line)  # 提取时间戳
            if match:
                timestamp = float(match.group(1))
                timestamps.append(timestamp)
                lines.append(line.strip())

    # 计算时间差
    for i in range(1, len(timestamps)):
        delta = timestamps[i] - timestamps[i - 1]
        if delta > threshold:
            print(f"Time Difference: {delta:.6f} s\n{lines[i-1]}\n{lines[i]}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze systrace file for large timestamp gaps.")
    parser.add_argument("file", type=str, help="Path to the systrace file")
    parser.add_argument("threshold", type=float, help="Threshold for timestamp difference in seconds")
    args = parser.parse_args()
    
    parse_systrace(args.file, args.threshold)

