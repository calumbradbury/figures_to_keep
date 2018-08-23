#hist2d of concavity/distance from mountian front.

import matplotlib 
matplotlib.use("Agg")
from matplotlib import pyplot as plt
import pandas as pd           
import sys


target = '/exports/csce/datastore/geos/users/s1134744/LSDTopoTools/Topographic_projects/full_himalaya_5000/'

source_list = ['0_3_ex_MChiSegmented_burned.csv','0_35_ex_MChiSegmented_burned.csv','0_4_ex_MChiSegmented_burned.csv','0_45_ex_MChiSegmented_burned.csv','0_5_ex_MChiSegmented_burned.csv',]

sub_plots = [231,232,233,234,235]
limits = [50,100,200,400,800]  

fig = plt.figure(1, figsize=(30,20))
     
    
def getAxis(column):
    
    x_list = []
    y_list = []
    
    for source in source_list:
        with open(target+source,'r') as csvfile:
            df = pd.read_csv(csvfile,delimiter=',')
            x_Series = df[column].tolist()
            y_Series = df['m_chi'].tolist()    
            x_list.append(x_Series)
            y_list.append(y_Series)    
    return x_list,y_list


fig = plt.figure(1, figsize=(30,20))    
x_list,y_list = getAxis('distance')

for x,y,location,limit,source in zip(x_list,y_list,sub_plots,limits,source_list):
    ax = fig.add_subplot(location)                                                     
    plt.cla()
    h = ax.hist2d(x,y,bins=(100,100),range=((0,2),(0,limit)))
    plt.colorbar(h[3], ax=ax)    
    plt.ylabel("Ksn")
    plt.xlabel("Distance from Mountain Front (decimal degrees)")
    title = source.replace('_ex_MChiSegmented_burned.csv','')
    plt.title(title)

fig.tight_layout()
fig.savefig('../ksn_hist_distance.png', bbox_inches='tight')
plt.clf()
plt.cla()
plt.close()
#fig.close()



fig = plt.figure(1, figsize=(30,20))
x_list,y_list = getAxis('segmented_elevation')

for x,y,location,limit,source in zip(x_list,y_list,sub_plots,limits,source_list):
    ax = fig.add_subplot(location)                                                   
    plt.cla()
    h = ax.hist2d(x,y,bins=(100,100),range=((350,5000),(0,limit)))
    plt.colorbar(h[3], ax=ax)    
    plt.ylabel("Ksn")
    plt.xlabel("Elevation (m)")
    title = source.replace('_ex_MChiSegmented_burned.csv','')
    plt.title(title)

fig.tight_layout()
fig.savefig('../ksn_hist_elevation.png', bbox_inches='tight')
plt.clf()
plt.cla()
plt.close()
#fig.close()



fig = plt.figure(1, figsize=(30,20))
x_list,y_list = getAxis('secondary_burned_data')

for x,y,location,limit,source in zip(x_list,y_list,sub_plots,limits,source_list):
    names = ['0-500','500-1000','1000-1500','1500-2000','2000-2500','2500-3000','3000-3500','3500-4000','4000-4500','4500-5000','5000-5500','5500-6000']
    ax = fig.add_subplot(location)                                                         
    plt.cla()
    h = ax.hist2d(x,y,bins=(100,100),range=((0,6000),(0,limit)))
    plt.colorbar(h[3], ax=ax)    
    plt.ylabel("Ksn")
    plt.xlabel("Precipitation (mm/year)")
    title = source.replace('_ex_MChiSegmented_burned.csv','')
    plt.title(title)

    
fig.tight_layout()
fig.savefig('../ksn_hist_precipiation.png', bbox_inches='tight')
plt.clf()
plt.cla()
plt.close()
#fig.close()



fig = plt.figure(1, figsize=(30,20))
x_list,y_list = getAxis('second_inv')

for x,y,location,limit,source in zip(x_list,y_list,sub_plots,limits,source_list):
    names = ['0-25','25-50','50-75','75-100','100-125','125-150','150-175']
    ax = fig.add_subplot(location)                                                    
    h = ax.hist2d(x,y,bins=(100,100),range=((0,200),(0,limit)))
    plt.colorbar(h[3], ax=ax)    
    plt.ylabel("Ksn")
    plt.xlabel("Strain")
    title = source.replace('_ex_MChiSegmented_burned.csv','')
    plt.title(title)
    
fig.tight_layout()
fig.savefig('../ksn_hist_strain.png', bbox_inches='tight')
plt.clf()
plt.cla()
plt.close()
#fig.close()



fig = plt.figure(1, figsize=(30,20))
x_list,y_list = getAxis('burned_data')

for x,y,location,limit,source in zip(x_list,y_list,sub_plots,limits,source_list):
    names = ["Evaporites","Ice \n and \n Glaciers","Metamorphics","NoData",
                 "Acid \n Plutonic \n Rocks","Basic \n Plutonic \n Rocks",
                 "Intermediate \n Plutonic \n Rocks","Pyroclastics","Carbonate \n Sedimentary \n Rocks",
                 "Mixed \n Sedimentary \n Rocks","Siliciclastic \n Sedimentary \n Rocks",
                 "Unconsolidated \n Sediments","Acid \n Volcanic \n Rocks","Basic \n Volcanic \n Rocks",
                 "Intermediate \n Volcanic \n Rocks","Water \n Bodies"]
    ax = fig.add_subplot(location)                                                      
    plt.cla()
    h = ax.hist2d(x,y,bins=([5000,15000,25000,35000,45000,55000,65000,75000,85000,95000,105000,115000,125000,135000,145000,155000,165000],100),range=((0,170000),(0,limit)))
    plt.colorbar(h[3], ax=ax)    
    plt.ylabel("Ksn")
    plt.xlabel("Lithology")
    
    title = source.replace('_ex_MChiSegmented_burned.csv','')
    plt.xticks([10000,20000,30000,40000,50000,60000,70000,80000,90000,100000,110000,120000,130000,140000,150000,160000],names)
    plt.xticks(rotation=45)
    plt.title(title)

    
fig.tight_layout()
fig.savefig('../ksn_hist_lithology.png', bbox_inches='tight')
plt.clf()
plt.cla()
plt.close()
#fig.close()



fig = plt.figure(1, figsize=(30,20))
x_list,y_list = getAxis('tectonics')

for x,y,location,limit,source in zip(x_list,y_list,sub_plots,limits,source_list):
    names = ['Sub Himalaya','Lesser Himalaya','Greater Himalaya','Tethyan Himalaya']
    ax = fig.add_subplot(location)                                                  
    plt.cla()
    h = ax.hist2d(x,y,bins=([0.5,1.5,2.5,3.5,4.5],100),range=((0,5),(0,limit)))
    plt.colorbar(h[3], ax=ax)    
    plt.ylabel("Ksn")
    plt.xlabel("Tectonic Zone")
    title = source.replace('_ex_MChiSegmented_burned.csv','')
    plt.xticks([1,2,3,4],['Sub Himalaya','Lesser Himalaya','Greater Himalaya','Tethyan Himalaya'])
    plt.title(title)
    
fig.tight_layout()
fig.savefig('../ksn_hist_tectonics.png', bbox_inches='tight')
plt.clf()
plt.cla()
plt.close()
#fig.close()



