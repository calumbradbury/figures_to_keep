#hist2d of concavity/distance from mountian front.

import matplotlib 
matplotlib.use("Agg")
from matplotlib import pyplot as plt
import pandas as pd           
import sys


target = '/exports/csce/datastore/geos/users/s1134744/LSDTopoTools/Topographic_projects/full_himalaya_5000/'

source_list = ['0_3_ex_MChiSegmented_burned.csv','0_35_ex_MChiSegmented_burned.csv','0_4_ex_MChiSegmented_burned.csv','0_45_ex_MChiSegmented_burned.csv','0_5_ex_MChiSegmented_burned.csv',]

sub_plots = [321,322,323,324,325]
limits = [100,200,400,800,1600]  

fig = plt.figure(1, figsize=(20,30))
     
def getAxis(column,mins,maxs):
    
    x_list_list = []
    x_ticks_ticks = []
    
    
    for source in source_list:
        
        with open(target+source,'r') as csvfile:
        
            df = pd.read_csv(csvfile,delimiter=',') 
            selectedDF = df[df['m_chi'] > 0]
            x_list = []
            x_ticks = []
            
            for lower,upper in zip(mins,maxs):
            
                selectedDF = df[df[column] >= lower]
                selectedDF = selectedDF[selectedDF[column] < upper]            
          
                series = selectedDF['m_chi']                   
                lister = series.tolist()
                data_count = len(lister)
            
                #for labeling x axis
                #label = str(lower)+'\n n:'+str(data_count) 
                x_ticks.append(str(data_count))
        
                x_list.append(lister)
            
            x_list_list.append(x_list)
            x_ticks_ticks.append(x_ticks)
            
                  
    return x_list_list,x_ticks_ticks


fig = plt.figure(1, figsize=(20,30))    
deep_x_list,deep_x_tick = getAxis('distance',[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9],[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0])

for x_list,x_ticks,location,limit,source in zip(deep_x_list,deep_x_tick,sub_plots,limits,source_list):
    ax = fig.add_subplot(location)                                                     
    plt.cla()
    new_names = [str(y)+'-'+str(z)+'\n n:'+x for x,y,z in zip(x_ticks,[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9],[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0])]
    ax.boxplot(x_list,labels=new_names)
    plt.ylim(ymin=0,ymax=limit)
    plt.ylabel("Ksn")
    plt.xlabel("Distance from Mountain Front (decimal degrees)")
    plt.xticks(rotation=45)
    title = source.replace('_ex_MChiSegmented_burned.csv','')
    plt.title(title)

fig.tight_layout()
fig.savefig('../ksn_box_distance.png', bbox_inches='tight')
plt.clf()
plt.cla()
plt.close()
#fig.close()


fig = plt.figure(1, figsize=(20,30))
deep_x_list,deep_x_tick = getAxis('segmented_elevation',range(350,4950,50),range(400,5000,50))

for x_list,x_ticks,location,limit,source in zip(deep_x_list,deep_x_tick,sub_plots,limits,source_list):
    ax = fig.add_subplot(location)                                                   
    plt.cla()
    ax.boxplot(x_list)
    plt.ylim(ymin=0,ymax=limit)
    plt.ylabel("Ksn")
    plt.xlabel("Elevation (m)")
    title = source.replace('_ex_MChiSegmented_burned.csv','')
    plt.title(title)

fig.tight_layout()
fig.savefig('../ksn_box_elevation.png', bbox_inches='tight')
plt.clf()
plt.cla()
plt.close()
#fig.close()



fig = plt.figure(1, figsize=(20,30))
deep_x_list,deep_x_tick = getAxis('secondary_burned_data',range(0,6000,500),range(500,6500,500))

for x_list,x_ticks,location,limit,source in zip(deep_x_list,deep_x_tick,sub_plots,limits,source_list):
    names = ['0-500','500-1000','1000-1500','1500-2000','2000-2500','2500-3000','3000-3500','3500-4000','4000-4500','4500-5000','5000-5500','5500-6000']
    ax = fig.add_subplot(location)                                                         
    plt.cla()
    new_names = [x+'\n n:'+y for x,y in zip(names,x_ticks)]
    ax.boxplot(x_list,labels=new_names)
    plt.ylim(ymin=0,ymax=limit)
    plt.ylabel("Ksn")
    plt.xlabel("Precipitation (mm/year)")
    title = source.replace('_ex_MChiSegmented_burned.csv','')
    plt.title(title)

    
fig.tight_layout()
fig.savefig('../ksn_box_precipiation.png', bbox_inches='tight')
plt.clf()
plt.cla()
plt.close()
#fig.close()



fig = plt.figure(1, figsize=(20,30))
deep_x_list,deep_x_tick = getAxis('second_inv',range(0,175,25),range(25,200,25))

for x_list,x_ticks,location,limit,source in zip(deep_x_list,deep_x_tick,sub_plots,limits,source_list):
    names = ['0-25','25-50','50-75','75-100','100-125','125-150','150-175']
    ax = fig.add_subplot(location)                                                    
    new_names = [x+'\n n:'+y for x,y in zip(names,x_ticks)]
    ax.boxplot(x_list,labels=new_names)
    plt.ylim(ymin=0,ymax=limit)
    plt.ylabel("Ksn")
    plt.xlabel("Strain")
    title = source.replace('_ex_MChiSegmented_burned.csv','')
    plt.title(title)
    
fig.tight_layout()
fig.savefig('../ksn_box_strain.png', bbox_inches='tight')
plt.clf()
plt.cla()
plt.close()
#fig.close()



fig = plt.figure(1, figsize=(20,30))
deep_x_list,deep_x_tick = getAxis('burned_data',range(10000,170000,10000),range(20000,180000,10000))

for x_list,x_ticks,location,limit,source in zip(deep_x_list,deep_x_tick,sub_plots,limits,source_list):
    names = ["Evaporites","Ice and Glaciers","Metamorphics","NoData",
                 "Acid Plutonic Rocks","Basic Plutonic Rocks",
                 "Intermediate Plutonic Rocks","Pyroclastics","Carbonate Sedimentary Rocks",
                 "Mixed Sedimentary Rocks","Siliciclastic Sedimentary Rocks",
                 "Unconsolidated Sediments","Acid Volcanic Rocks","Basic Volcanic Rocks",
                 "Intermediate Volcanic Rocks","Water Bodies"]
    ax = fig.add_subplot(location)                                                      
    plt.cla()
    new_names = [x+'\n n:'+y for x,y in zip(names,x_ticks)]
    ax.boxplot(x_list,labels=new_names)
    plt.ylim(ymin=0,ymax=limit)
    plt.ylabel("Ksn")
    plt.xlabel("Lithology")
    plt.xticks(rotation=90)
    title = source.replace('_ex_MChiSegmented_burned.csv','')
    plt.title(title)

    
fig.tight_layout()
fig.savefig('../ksn_box_lithology.png', bbox_inches='tight')
plt.clf()
plt.cla()
plt.close()
#fig.close()



fig = plt.figure(1, figsize=(20,30))
deep_x_list,deep_x_tick = getAxis('tectonics',[0.5,1.5,2.5,3.5],[1.5,2.5,3.5,4.5])

for x_list,x_ticks,location,limit,source in zip(deep_x_list,deep_x_tick,sub_plots,limits,source_list):
    names = ['Sub Himalaya','Lesser Himalaya','Greater Himalaya','Tethyan Himalaya']
    ax = fig.add_subplot(location)                                                  
    plt.cla()
    new_names = [x+'\n n:'+y for x,y in zip(names,x_ticks)]
    ax.boxplot(x_list,labels=new_names)
    plt.ylim(ymin=0,ymax=limit)
    plt.ylabel("Ksn")
    plt.xlabel("Tectonic Zone")
    title = source.replace('_ex_MChiSegmented_burned.csv','')
    plt.title(title)
    
fig.tight_layout()
fig.savefig('../ksn_box_tectonics.png', bbox_inches='tight')
plt.clf()
plt.cla()
plt.close()
#fig.close()



