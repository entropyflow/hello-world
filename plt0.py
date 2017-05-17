#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 21:54:20 2017

@author: changchao
"""

from pylab import mpl

import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams['font.sans-serif'] = ['STHeiti'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题


a = np.arange(0.0, 5.0, 0.1)
                    
plt.xlabel('横轴：时间',fontproperties = 'STHeiti', fontsize = 15)
plt.ylabel('纵轴：振幅',fontproperties = 'STHeiti', fontsize = 15)

plt.plot(a, np.cos(2*np.pi*a), 'r--')
# plt.plot(a, a*1.5, 'go-', a, a*2.5,
#         'rx', a, a*3.5, '*', a, a*4.5, 'b-.')
# plt.savefig("pltfig1",dpi = 500)
plt.show()