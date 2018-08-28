#Ksn by elevation

import matplotlib 
matplotlib.use("Agg")
from matplotlib import pyplot as plt
import pandas as pd           
import sys
import numpy as np
from numpy import median
import matplotlib.cm as cm
import matplotlib.patches as mpatches
from mpl_toolkits.axes_grid.inset_locator import inset_axes

target = '/exports/csce/datastore/geos/users/s1134744/LSDTopoTools/Topographic_projects/full_himalaya_5000/'

source= '0_4_ex_MChiSegmented_burned_outlier_removed.csv'


colours = ['b','g','r','y','c','m']
numbers_a = [30000,50000,90000,100000,110000,120000]
numbers_b = [40000,60000,100000,110000,120000,130000]
bins = ["Metamorphics","Acid Plutonic Rocks","Carbonate Sedimentary Rocks",
             "Mixed Sedimentary Rocks","Siliciclastic Sedimentary Rocks",
             "Unconsolidated Sediments"]


def getAxis(column):
    
    with open(target+source,'r') as csvfile:
        df = pd.read_csv(csvfile,delimiter=',')
        
        distance = []
        full_data = []
        
        for lower,upper in zip(range(350,5000,50),range(400,5050,50)): 
            selectedDF_c = df[df[column] >= lower]
            selectedDF_c = selectedDF_c[selectedDF_c[column] < upper]                     
            series = selectedDF_c["m_chi"].tolist()
            value = median(series)
            full_data.append(value)  
              
        distance.append(full_data)
        
        
        for x,y in zip(numbers_a,numbers_b):   
            selectedDF = df[df["burned_dat"] >= x]
            selectedDF = selectedDF[selectedDF["burned_dat"] < y]
            elevation = []

            for lower,upper in zip(range(350,5000,50),range(400,5050,50)): 
                selectedDF_b = selectedDF[selectedDF[column] >= lower]
                selectedDF_b = selectedDF_b[selectedDF_b[column] < upper]                     
                series = selectedDF_b["m_chi"].tolist()
                value = median(series)
                #print value
                elevation.append(value)

                    
            distance.append(elevation)
                   
    return distance
    
    
def getAxisHist(column):
    
    with open(target+source,'r') as csvfile:
        df = pd.read_csv(csvfile,delimiter=',')
        
        distance = []
        full_data = []
        
        #for lower,upper in zip(range(350,5000,50),range(400,5050,50)): 
        #    selectedDF_c = df[df[column] >= lower]
        #    selectedDF_c = selectedDF_c[selectedDF_c[column] < upper]                     
        series = df[column].tolist()
            #value = median(series)
        distance.append(series)  
              
        #distance.append(full_data)
        
        
        for x,y in zip(numbers_a,numbers_b):   
            selectedDF = df[df["burned_dat"] >= x]
            selectedDF = selectedDF[selectedDF["burned_dat"] < y]
            series = selectedDF[column].tolist()
            distance.append(series)  
                               
    return distance
    

data = getAxis("segmented_")

x_series = range(375,5025,50)

fig = plt.figure(1, figsize=(18,9))

legends = []

#x = np.arange(len(numbers_a))
#ys = [i+x+(i*x)**2 for i in range(len(numbers_a))]
#colours = cm.rainbow(np.linspace(0, 1, len(ys)))

#bins = [str(y)+'-'+str(z) for y,z in zip(range(0,5000,1000),range(1000,6000,1000))]

ax = fig.add_subplot(111)

for item,colour,name in zip(data[1:],colours,bins):
    
    ax.scatter(x_series,item,marker=',',s=5,c=colour)
    legend = mpatches.Patch(color=colour, label=name)
    legends.append(legend)

ax.scatter(x_series,data[0],marker='o',c='k')
legend = mpatches.Patch(color='k', label='Full Dataset')
#legend = mpatches.Circle((0.5, 0.5), 1, facecolor='k', linewidth=3)

legends.append(legend)

leg = plt.legend(handles=legends, title='Lithology',ncol=7,loc='upper center', bbox_to_anchor=(0.5, 1.05)) 
plt.ylabel(r"Median $K_{sn}$")
plt.xlabel("Elevation (50m bins)")                                                                                                         
leg.get_frame().set_alpha(1)

x_i = len(numbers_a)

#adding inset histogram
new_axes = inset_axes(ax, width="40%",height="40%",bbox_to_anchor=(-400,400,1200,300))
#new_axes = inset_axes(ax, width="40%",height="40%",bbox_to_anchor=(0.5,0.5,800,700))
data_2 = getAxisHist("segmented_")                     
new_colour = []
new_colour.append('k')
for x in colours:
    new_colour.append(x)
print len(data),len(new_colour)
plt.hist(data_2,bins=x_series,stacked=True,color=new_colour)
plt.title("Histogram of Data Points in Elevation Bins")
plt.ylabel("Frequency")
plt.xlabel("Elevation (50m bins)") 


leg.get_frame().set_alpha(1)
    
fig.savefig('../elevation_scatter_lithology.png', bbox_inches='tight')    
    
    
