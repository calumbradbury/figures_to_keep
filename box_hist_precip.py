#precip 0.4 only. Hist and Box one plot.


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
        y_list = df['m_chi'].tolist()    
    return x_list,y_list


def getAxisBox(column,mins,maxs):

    x_list = []
    x_ticks = []
       
    with open(target+source,'r') as csvfile:
        
        df = pd.read_csv(csvfile,delimiter=',') 
        selectedDF = df[df['m_chi'] > 0]
                    
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
                  
    return x_list,x_ticks
    
fig = plt.figure(1, figsize=(20,10))

x_list,x_ticks = getAxisBox('secondary_',range(0,6000,500),range(500,6500,500))

names = ['0-500','500-1000','1000-1500','1500-2000','2000-2500','2500-3000','3000-3500','3500-4000','4000-4500','4500-5000','5000-5500','5500-6000']

ax = fig.add_subplot(121)   
names = [x.replace('-','\n') for x in names]                                                         
new_names = [x+'\n n:'+y for x,y in zip(names,x_ticks)]
   
ax.boxplot(x_list,labels=new_names)
ax.set_xticklabels(new_names,fontsize='small')
#plt.rc('xaxis', labelsize=20) 
plt.ylim(ymin=0,ymax=400)
plt.ylabel("Ksn",fontsize=18)
plt.xlabel("Precipitation in 5000 mm/year bins",fontsize=18)



x_list,y_list = getAxisHist('secondary_')
#print x_list,y_list

names = ['0-500','500-1000','1000-1500','1500-2000','2000-2500','2500-3000','3000-3500','3500-4000','4000-4500','4500-5000','5000-5500','5500-6000']
ax = fig.add_subplot(122)                                                       
h = ax.hist2d(x_list,y_list,bins=(100,100),range=((0,6000),(0,400)))
plt.colorbar(h[3], ax=ax)    
plt.ylabel("Ksn",fontsize=18)
plt.xlabel("Precipitation (mm/year)",fontsize=18)
ax.get_yaxis().set_visible(False)
    
fig.tight_layout()




fig.savefig('../precipiation_box_hist_0.4_removed.png', bbox_inches='tight')
