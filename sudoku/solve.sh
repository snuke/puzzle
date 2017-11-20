#!/bin/sh
python conv.py < in.txt > a.cnf
minisat a.cnf out.txt > /dev/null
python vis.py < out.txt
