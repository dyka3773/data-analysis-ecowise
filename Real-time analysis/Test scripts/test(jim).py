# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 23:42:51 2021

@author: Herck
"""
import pandas as pd
from matplotlib import pyplot as plt

data1 = pd.read_excel('./Bexus 24 PTU data.xlsx')
Temp_out = data1['Temp out']
Air_Press = data1['Air press']
Altitude = data1['Altitude']

plt.scatter(Air_Press, Altitude, c=Temp_out, cmap='jet',s=20, marker='.')

cbar = plt.colorbar()
cbar.set_label('Measured Temperature (?)')

plt.title('Temperature & Pressure Measurements')
plt.xlabel('Pressure (mbar)')
plt.ylabel('Altitude (?)')
plt.rcParams['axes.facecolor'] = '#ccccff'
plt.grid(linewidth = 0.5, linestyle = '--', color = '#262626', alpha=0.2)


plt.tight_layout()
plt.show()