# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 14:53:27 2017

@author: ankyt
"""
from math import sqrt

plot1 = [1,3]
plot2 = [2,5]

eucledian_distance = sqrt( (plot1[0]-plot2[0])**2 + (plot1[1]-plot2[1])**2 )

print(eucledian_distance)