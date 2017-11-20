#!/bin/sh
python conv.py < in.txt > data.cnf
minisat data.cnf res.txt > /dev/null
cat in.txt res.txt > out.txt
python vis.py < out.txt
