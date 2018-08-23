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

source_list = ['0_5_ex_MChiSegmented_burned.csv']

fig = plt.figure(1, figsize=(18,20))
        



def getAxis(column):
    
    x_list = []
    y_list = []
    y_ticks = []
    
    for source in source_list:
        with open(target+source,'r') as csvfile:
            df = pd.read_csv(csvfile,delimiter=',')
            x_Series = df[column].tolist()
            y_Series = df['m_chi'].tolist()
            print y_Series
        
            #key = source.replace('_ex_MChiSegmented_burned.csv','')
            #key = key.replace('_','.')
            #key = float(key)
            #y_ticks.append(key)
            #length = len(x_Series)
            #y_Series = [key]*length

            #x_list = x_list + x_Series
            #y_list = y_list + y_Series
    
    
    return x_Series,y_Series#,y_ticks    


ax = fig.add_subplot(321)                                                 
x_list,y_list = getAxis('distance')      
h = ax.hist2d(x_list,y_list,bins=(100,100),range=((0,2),(0,800)))
#plt.yticks(y_ticks)
plt.colorbar(h[3], ax=ax)
plt.ylabel("Ksn")
plt.xlabel("Distance from Mountain Front (decimal degrees)")

ax = fig.add_subplot(322)                                                 
x_list,y_list = getAxis('segmented_elevation')   
h = ax.hist2d(x_list,y_list,bins=(100,100),range=((350,5000),(0,800)))
#plt.yticks(y_ticks)
plt.colorbar(h[3], ax=ax)
plt.ylabel("Ksn")
plt.xlabel("Elevation (m)")

ax = fig.add_subplot(323)                                                 
x_list,y_list = getAxis('secondary_burned_data')      
h = ax.hist2d(x_list,y_list,bins=(100,100),range=((0,6000),(0,800)))
#plt.yticks(y_ticks)
plt.colorbar(h[3], ax=ax)
plt.ylabel("Ksn")
plt.xlabel("Precipitation (mm/year)")

ax = fig.add_subplot(324)                                                 
x_list,y_list = getAxis('second_inv')   
h = ax.hist2d(x_list,y_list,bins=(100,100),range=((0,200),(0,800)))
#plt.yticks(y_ticks)
plt.colorbar(h[3], ax=ax)
plt.ylabel("Ksn")
plt.xlabel("Strain")

ax = fig.add_subplot(325)                                                 
x_list,y_list  = getAxis('burned_data')      
h = ax.hist2d(x_list,y_list,bins=(16,100),range=((0,170000),(0,800)))
#plt.yticks(y_ticks)
plt.colorbar(h[3], ax=ax)
plt.ylabel("Ksn")
plt.xlabel("Lithology")

ax = fig.add_subplot(326)                                                 
x_list,y_list = getAxis('tectonics')   
h = ax.hist2d(x_list,y_list,bins=([0.5,1.5,2.5,3.5,4.5],100),range=((0,5),(0,800)))
#plt.yticks(y_ticks)
plt.colorbar(h[3], ax=ax)
plt.ylabel("Ksn")
plt.xlabel("Tectonic Zone")
plt.xticks([1,2,3,4],['Sub Himalaya','Lesser Himalaya','Greater Himalaya','Tethyan Himalaya'])


#plt.ylabel("Concavity")
#plt.xlabel("Elevation (m)")

#plt.colorbar(h[3], ax=ax)


#ax.scatter(x_list,y_list,marker='.')

fig.savefig('../ksn_0.5.png', bbox_inches='tight')


        
