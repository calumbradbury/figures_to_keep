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
import joyplot
joyplot.plt.switch_backend('agg')

target = '/exports/csce/datastore/geos/users/s1134744/LSDTopoTools/Topographic_projects/full_himalaya_5000/'

source= '0_4_ex_MChiSegmented_burned_outlier_removed.csv'

def getAxis(column):
    
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
        
        
        for x,y in zip(range(0,2000,500),range(500,2500,500)):   
            selectedDF = df[df["distance_a"] >= x]
            selectedDF = selectedDF[selectedDF["distance_a"] < y]
            series = selectedDF[column].tolist()
            distance.append(series)  
                               
    return distance
    

data = getAxis("segmented_")
print data[0]

x_series = range(375,5025,50)

fig = plt.figure(1, figsize=(18,9))

legends = []

x = np.arange(len(range(0,2000,500)))
ys = [i+x+(i*x)**2 for i in range(len(range(0,2500,500)))]
colours = cm.rainbow(np.linspace(0, 1, len(ys)))
new_colour = []
new_colour.append('k')
for x in colours:
    new_colour.append(x)
print len(new_colour[:5])

bins = [str(y)+'-'+str(z) for y,z in zip(range(0,2000,500),range(500,2500,500))]

plt.hist(data,stacked=True,bins=x_series,color=new_colour[:5])

#for item,colour,name in zip(data[1:],colours,bins):
    
     #plt.hist(item,bins=x_series)#,marker=',',s=5,c=colour)
     #fig,axes=joyplot.joyplot(df,figsize=(100,100),title='Lithology')
     #legend = mpatches.Patch(color=colour, label=name)
     #legends.append(legend)

#plt.scatter(x_series,data[0],marker='o',c='k')
#legend = mpatches.Patch(color='k', label='Full Dataset')
#legend = mpatches.Circle((0.5, 0.5), 1, facecolor='k', linewidth=3)
#
#legends.append(legend)

#leg = plt.legend(handles=legends, title='Distance along mountain front (500km bins)',ncol=6,loc='upper center', bbox_to_anchor=(0.5, 1.05)) 
#plt.ylabel(r"Median $K_{sn}$")
#plt.xlabel("Elevation (50m bins)")                                                                                                         

#leg.get_frame().set_alpha(1)
    
fig.savefig('../elevation_hist.png', bbox_inches='tight')    
    
    
#