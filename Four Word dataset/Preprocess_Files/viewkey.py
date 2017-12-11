#!/usr/bin/python
import sys
r = open("./Temp/tmpkey", "r").read().split()
p = list(set(r))
for i in range(0,len(p)):
    print(sys.argv[1] + p[i] + "="+ str(r.count(p[i])))
