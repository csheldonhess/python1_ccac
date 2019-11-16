# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 18:57:23 2019

@author: coral
"""

fh = open("the_raven.txt", "r")
fw = open("raven_abbreviated.txt", "w")

raven_list = fh.readlines()

count = 0
for item in raven_list:
    line = item.rstrip("\n")
    if count % 3 == 0:
        fw.write(line + "\n")
    count += 1

fh.close()
fw.close()
