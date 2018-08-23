#hist2d of concavity/distance from mountian front.

import matplotlib 
matplotlib.use("Agg")
from matplotlib import pyplot as plt
import pandas as pd           
import sys


target = '/exports/csce/datastore/geos/users/s1134744/LSDTopoTools/Topographic_projects/full_himalaya_5000/'

source_list = ['0_1_ex_MChiSegmented_burned.csv','0_15_ex_MChiSegmented_burned.csv','0_2_ex_MChiSegmented_burned.csv',
              '0_25_ex_MChiSegmented_burned.csv','0_3_ex_MChiSegmented_burned.csv','0_35_ex_MChiSegmented_burned.csv',
              '0_4_ex_MChiSegmented_burned.csv','0_45_ex_MChiSegmented_burned.csv','0_5_ex_MChiSegmented_burned.csv',
              '0_55_ex_MChiSegmented_burned.csv','0_6_ex_MChiSegmented_burned.csv','0_65_ex_MChiSegmented_burned.csv',
              '0_7_ex_MChiSegmented_burned.csv','0_75_ex_MChiSegmented_burned.csv','0_8_ex_MChiSegmented_burned.csv',
              '0_85_ex_MChiSegmented_burned.csv','0_9_ex_MChiSegmented_burned.csv','0_95_ex_MChiSegmented_burned.csv']

fig = plt.figure(1, figsize=(12,8))
ax = fig.add_subplot(111)              

x_list = []
y_list = []
y_ticks = []

for source in source_list:
    with open(target+source,'r') as csvfile:
        df = pd.read_csv(csvfile,delimiter=',')
        x_Series = df['segmented_elevation'].tolist()
        
        key = source.replace('_ex_MChiSegmented_burned.csv','')
        key = key.replace('_','.')
        key = float(key)
        y_ticks.append(key)
        length = len(x_Series)
        y_Series = [key]*length

        x_list = x_list + x_Series
        y_list = y_list + y_Series
        
        #ax.hist2d(x_Series,y_Series,bins=(100,18),range=((0,2),(0,1)))
        #plt.colorbar()
                                                 


h = ax.hist2d(x_list,y_list,bins=(100,[0.075,0.125,0.175,0.225,0.275,0.325,0.375,0.425,0.475,0.525,0.575,0.625,0.675,0.725,0.775,0.825,0.875,0.925,0.975]),range=((350,5000),(0.025,1)))
plt.yticks(y_ticks)
#plt.xticks([1,2,3,4],['Sub Himalaya','Lesser Himalaya','Greater Himalaya','Tethyan Himalaya'])
plt.ylabel("Concavity")
plt.xlabel("Elevation (m)")

plt.colorbar(h[3], ax=ax)


#ax.scatter(x_list,y_list,marker='.')

fig.savefig('../concavity-elevation.png', bbox_inches='tight')


        
