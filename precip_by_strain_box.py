#precip by lithology

import matplotlib 
matplotlib.use("Agg")
from matplotlib import pyplot as plt
import pandas as pd           
import sys


target = '/exports/csce/datastore/geos/users/s1134744/LSDTopoTools/Topographic_projects/full_himalaya_5000/'

source= '0_4_ex_MChiSegmented_burned_outlier_removed.csv'



def getAxisHist(column):
    
    with open(target+source,'r') as csvfile:
        df = pd.read_csv(csvfile,delimiter=',')
        x_list = df[column].tolist()
        y_list = df['secondary_burned_data'].tolist()    
    return x_list,y_list

zones_min = range(25,125,25)
zones_max = range(50,150,25)
titles = ["25-50", "50-75", "75-100", "100-125"]
location_list = [221,222,223,224]     

def getAxisBox(column,mins,maxs):

    x_list = []
    x_ticks = []
       
    with open(target+source,'r') as csvfile:
        
        df = pd.read_csv(csvfile,delimiter=',') 
        df_A = df[df['m_chi'] > 0]
        
        for x,y in zip(zones_min,zones_max):
            selectedDF_a = df_A[df_A['second_inv'] >= x] 
            selectedDF_a = selectedDF_a[selectedDF_a['second_inv'] < y]           
            
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
    
fig = plt.figure(1, figsize=(15,15))

x_list,x_ticks = getAxisBox('secondary_',range(0,6000,500),range(500,6500,500))
#print x_list

for box,tick,location,name in zip(x_list,x_ticks,location_list,titles):
    #print box
    ax = fig.add_subplot(location)   
    names = [str(x)+'\n'+str(y) for x,y in zip(range(0,6000,500),range(500,6500,500))]     
                                     

    new_names = [str(x)+'\n n:'+str(y) for x,y in zip(names,tick)]
   
    ax.boxplot(box,labels=new_names)
    ax.set_xticklabels(new_names,fontsize='small')
    #plt.rc('xaxis', labelsize=20) 
    plt.ylim(ymin=0,ymax=400)
    plt.ylabel("Ksn")
    plt.xlabel("Precipitation in 500 mm/year bins")

    plt.title(name,fontsize=20)






fig.tight_layout()




fig.savefig('../precip_by_strain_0.4_removed.png', bbox_inches='tight')
