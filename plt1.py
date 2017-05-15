#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 22:50:16 2017

@author: changchao
"""

import matplotlib.pyplot as plt

labels = 'A', 'B', 'C', 'D'

sizes = [20, 30, 40, 10]

explode = (0, 0, 0.1, 0)

plt.pie(sizes, explode = explode, labels = labels, autopct = '%1.1f%%',
        shadow = True, startangle = 0)

plt.show()
