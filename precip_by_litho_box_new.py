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



def getAxisHist(column):
    
    with open(target+source,'r') as csvfile:
        df = pd.read_csv(csvfile,delimiter=',')
        x_list = df[column].tolist()
        y_list = df['secondary_burned_data'].tolist()    
    return x_list,y_list

litho_mins = [30000,50000,90000,100000,110000]
litho_maxs = [40000,60000,100000,1110000,120000]
titles = ["Metamorphics","Acid Plutonic Rocks","Carbonate Sedimentary Rocks",
          "Mixed Sedimentary Rocks","Siliciclastic Sedimentary Rocks"]
names_c = [str(x)+'-'+str(y) for x,y in zip(range(0,6000,500),range(500,6500,500))]          
          
location_list = [151,152,153,154,155]     

def getAxisBox(column,mins,maxs):

    x_list = []
    x_ticks = []
       
    with open(target+source,'r') as csvfile:
        
        df = pd.read_csv(csvfile,delimiter=',') 
        df_A = df[df['m_chi'] > 0]
        
        for x,y in zip(litho_mins,litho_maxs):
            selectedDF_a = df_A[df_A['burned_dat'] >= x]
            selectedDF_a = selectedDF_a[selectedDF_a['burned_dat'] < y]            
            
            x_list_b = []
            x_tick_b = []
            
            for lower,upper in zip(mins,maxs):           
                selectedDF = selectedDF_a[selectedDF_a[column] >= lower]
                selectedDF = selectedDF[selectedDF[column] < upper]            
          
                series = selectedDF['m_chi']                   
                print selectedDF
                lister = series.tolist()
                data_count = len(lister)
                x_list_b.append(lister)
                x_tick_b.append(data_count)
        
            x_ticks.append(x_tick_b)
            x_list.append(x_list_b)        
                  
    return x_list,x_ticks
    
fig = plt.figure(1, figsize=(22,10))

x_list,x_ticks = getAxisBox('secondary_',range(0,6000,500),range(500,6500,500))
#print x_list



ax = fig.add_subplot(location_list[0])   

new_names = ['n:'+str(x) for x in x_ticks[0]]
   
box = ax.boxplot(x_list[0],labels=new_names,patch_artist=True,medianprops=dict(linestyle='-', linewidth=2.5, color='k'))

x = np.arange(len(range(0,6000,500)))
ys = [i+x+(i*x)**2 for i in range(len(range(0,6000,500)))]
colours = cm.Blues(np.linspace(0, 1, len(ys)))


for patch, color in zip(box['boxes'], colours):
    patch.set_facecolor(color)



ax.set_xticklabels(new_names,rotation=90)
    #plt.rc('xaxis', labelsize=20) 
plt.ylim(ymin=0,ymax=250)
plt.ylabel(r"$K_{sn}$",fontsize=18)
#plt.xlabel("Lithology")
#ax.axes.get_xaxis().set_visible(False)

plt.title(titles[0],fontsize=14)




for box,tick,location,name in zip(x_list[1:],x_ticks[1:],location_list[1:],titles[1:]):
    #print box
    ax = fig.add_subplot(location)   
    names = [str(x)+'\n'+str(y) for x,y in zip(range(0,6000,500),range(500,6500,500))]                                           

    new_names = ['n:'+str(x) for x in tick]
   
    box = ax.boxplot(box,labels=new_names,patch_artist=True,medianprops=dict(linestyle='-', linewidth=2.5, color='k'))
    
    for patch, color in zip(box['boxes'], colours):
        patch.set_facecolor(color)
    ax.set_xticklabels(new_names,rotation=90)
    ax.set_yticklabels([])
    #plt.rc('xaxis', labelsize=20) 
    plt.ylim(ymin=0,ymax=250)
    #plt.ylabel("Ksn")
    #plt.xlabel("Precipitation in 500 mm/year bins")
    plt.title(name,fontsize=14)





plt.subplots_adjust(wspace=0, hspace=0,bottom=0.13)
#fig.tight_layout()

legends = []
for colour,name in zip(colours,names_c):
    legend = mpatches.Patch(edgecolor='k',facecolor=colour, label=name)
    legends.append(legend)

leg = fig.legend(legends, names_c,'lower center',ncol=12,title=r'Precipitation ($mm\,yr^{-1}$)') 


fig.savefig('../precip_by_litho_0.4_removed.png', bbox_inches='tight')
