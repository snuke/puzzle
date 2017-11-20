#!/bin/sh
python converter.py < in.txt > data.cnf
minisat data.cnf out.txt > /dev/null
python visualizer.py in.txt out.txt
