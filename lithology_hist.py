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
    
fig = plt.figure(1, figsize=(18,8))

#x_list,y_list = getAxisBox('burned_dat',range(10000,170000,10000),range(20000,180000,10000))
x_list,y_list = getAxisHist('burned_dat')
#print x_list,y_list
names = ["Evaporites","Ice \n and \n Glaciers","Metamorphics","NoData",
             "Acid \n Plutonic \n Rocks","Basin \n Plutonic \n Rocks",
             "Intermediate \n Plutonic \n Rocks","Pyroclastics","Carbonate \n Sedimentary \n Rocks",
             "Mixed \n Sedimentary \n Rocks","Siliciclastic \n Sedimentary \n Rocks",
             "Unconsolidated \n Sediments","Acid \n Volcanic \n Rocks","Basic \n Volcanic \n Rocks",
             "Intermediate \n Volcanic \n Rocks","Water \n Bodies"]
#names = ['0-500','500-1000','1000-1500','1500-2000','2000-2500','2500-3000','3000-3500','3500-4000','4000-4500','4500-5000','5000-5500','5500-6000']
ax = fig.add_subplot(111)
print x_list
                                                       
N,bins,patches = ax.hist(x_list,bins=range(10000,170000,10000))

i = 2
patches[i].set_facecolor('b')


i = 4
patches[i].set_facecolor('r')

i = 8
patches[i].set_facecolor('c')

i = 9
patches[i].set_facecolor('y')

i = 10
patches[i].set_facecolor('m')

plt.xticks(range(15000,185000,10000),names)
plt.ylabel("Frequency",fontsize=18)
plt.xlabel("GLIM Lithology Class",fontsize=18)
#ax.get_yaxis().set_visible(False)
    
fig.tight_layout()

fig.savefig('../lithology_hist_0.4_removed.png', bbox_inches='tight')


