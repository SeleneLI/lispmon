# -*- coding: utf-8 -*-
__author__ = 'yueli'
'''In this python script, we plan to define some globl variables'''


import os
from pylab import *
import matplotlib.pyplot as plt
import urllib2  # the lib that handles the url stuff
import csv
import matplotlib as mpl



# 读取 环境变量 Atlas 目录下的各个文件夹
# 上述 环境变量 定义在 工作目录下 .profile中 (也有可能定义在 .bashprofile中)
try:
    # $HOME/Documents/Codes/lispmon/analyze_traces
    LISPMON_ANALYZE_TRACES = '/Users/yueli/Documents/Codes/lispmon/analyze_traces'
    # $HOME/Documents/Codes/lispmon/figures_and_tables
    LISPMON_FIGURES_AND_TABLES = '/Users/yueli/Documents/Codes/lispmon/figures_and_tables'
    # $HOME/Documents/Codes/lispmon/plot
    LISPMON_PLOT = '/Users/yueli/Documents/Codes/lispmon/plot'
    # $HOME/Documents/Codes/lispmon/traces
    LISPMON_TRACES = '/Users/yueli/Documents/Codes/lispmon/traces'


except KeyError:

    print "Environment variable is not properly defined or " \
          "the definition about this variable is not taken into account."
    print "If every environment variable is well defined, restart Pycharm to try again!"




# Plot part

font = {
    'fontname'   : 'Times New Roman',
    'color'      : 'k',
    'fontsize'   : 40
       }

fontText = {
    'fontname'   : 'Times New Roman',
    'color'      : 'k',
    'fontsize'   : 40
       }

font3D = {
    'fontname'   : 'Times New Roman',
    'color'      : 'k',
    'fontsize'   : 52
       }