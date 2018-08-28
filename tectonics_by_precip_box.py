#precip by lithology

import matplotlib 
matplotlib.use("Agg")
from matplotlib import pyplot as plt
import pandas as pd           
import sys
import matplotlib.patches as mpatches


target = '/exports/csce/datastore/geos/users/s1134744/LSDTopoTools/Topographic_projects/full_himalaya_5000/'

source= '0_4_ex_MChiSegmented_burned_outlier_removed.csv'

numbers_a = [30000,50000,90000,100000,110000,120000]
numbers_b = [40000,60000,100000,110000,120000,130000]
names = ["Metamorphics","Acid \n Plutonic \n Rocks","Carbonate \n Sedimentary \n Rocks",
             "Mixed \n Sedimentary \n Rocks","Siliciclastic \n Sedimentary \n Rocks",
             "Unconsolidated \n Sediments"]
names_b = ['Sub Himalaya','Lesser Himalaya','Greater Himalaya','Tethyan Himalaya']

def getAxisHist(column):
    
    with open(target+source,'r') as csvfile:                                                                                            
        df = pd.read_csv(csvfile,delimiter=',')
        x_list = df[column].tolist()
        y_list = df['secondary_burned_data'].tolist()    
    return x_list,y_list

zones_min = range(0,5000,1000)
zones_max = range(1000,6000,1000)
titles = [str(x)+'-'+str(y)+' '+r"($mm\,yr^{-1}$)" for x,y in zip(zones_min,zones_max)]
location_list = [141,142,143,144]   

def getAxisBox(column,mins,maxs):

    x_list = []
    x_ticks = []
       
    with open(target+source,'r') as csvfile:
        
        df = pd.read_csv(csvfile,delimiter=',') 
        df_A = df[df['m_chi'] > 0]
        
        for x,y in zip(zones_min,zones_max):
            selectedDF_a = df_A[df_A['secondary_'] >= x] 
            selectedDF_a = selectedDF_a[selectedDF_a['secondary_'] < y]           
            
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
    
    
fig = plt.figure(1, figsize=(20,8))

x_list,x_ticks = getAxisBox('tectonics',[1,2,3,4],[2,3,4,5])


ax = fig.add_subplot(location_list[0])   

new_names = ['n:\n'+str(x) for x in x_ticks[0]]
   
box = ax.boxplot(x_list[0],labels=new_names,patch_artist=True,medianprops=dict(linestyle='-', linewidth=2.5, color='k'))

colours = ['b','r','c','y']

for patch, color in zip(box['boxes'], colours):
    patch.set_facecolor(color)



ax.set_xticklabels(new_names,fontsize='small')
    #plt.rc('xaxis', labelsize=20) 
plt.ylim(ymin=0,ymax=250)
plt.ylabel(r"$K_{sn}$",fontsize=18)
#plt.xlabel("Lithology")
#ax.axes.get_xaxis().set_visible(False)

plt.title(titles[0],fontsize=20)



for box,tick,location,name in zip(x_list[1:],x_ticks[1:],location_list[1:],titles[1:]):
    #print box
    ax = fig.add_subplot(location)   
    #names = [str(x)+'\n'+str(y) for x,y in zip(range(0,6000,500),range(500,6500,500))]     
                                     

    new_names = ['n:\n'+str(x) for x in tick]
   
    box = ax.boxplot(box,labels=new_names,patch_artist=True,medianprops=dict(linestyle='-', linewidth=2.5, color='k'))
    for patch, color in zip(box['boxes'], colours):
        patch.set_facecolor(color)
    #ax.set_xticklabels(new_names,fontsize='small')
    #plt.rc('xaxis', labelsize=20) 
    plt.ylim(ymin=0,ymax=250)
    #plt.ylabel(r"$K_{sn}$")
    #plt.xlabel("Tectonic Zone")
    ax.set_yticklabels([])
    #ax.axes.get_yaxis().set_visible(False)
    #ax.axes.get_xaxis().set_visible(False)
    plt.title(name,fontsize=20)


    plt.title(name,fontsize=20)


plt.subplots_adjust(wspace=0, hspace=0)

legends = []
for colour,name in zip(colours,names_b):
    legend = mpatches.Patch(color=colour, label=name)
    legends.append(legend)

leg = fig.legend(legends, names_b,'lower center',ncol=4,title='Tectonic Zone',borderaxespad=0.2) 



#fig.tight_layout()




fig.savefig('../tectonics_by_precip_0.4_removed.png', bbox_inches='tight')
