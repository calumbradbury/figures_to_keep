#precip 0.4 only. Hist and Box one plot.


import matplotlib 
matplotlib.use("Agg")
from matplotlib import pyplot as plt
import pandas as pd           
import sys


target = '/exports/csce/datastore/geos/users/s1134744/LSDTopoTools/Topographic_projects/full_himalaya_5000/'

source= '0_4_ex_MChiSegmented_burned_outlier_removed.csv'


colours = ['b','g','r','y','c','m']
numbers_a = [30000,50000,90000,100000,110000,120000]
numbers_b = [40000,60000,100000,110000,120000,130000]
legends = []
names = ["Metamorphics","Acid \n Plutonic \n Rocks","Carbonate \n Sedimentary \n Rocks",
             "Mixed \n Sedimentary \n Rocks","Siliciclastic \n Sedimentary \n Rocks",
             "Unconsolidated \n Sediments"]
names_b = ['Sub Himalaya','Lesser Himalaya','Greater Himalaya','Tethyan Himalaya']

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

x_list,x_ticks = getAxisBox('burned_dat',numbers_a,numbers_b)

#names = ['0-500','500-1000','1000-1500','1500-2000','2000-2500','2500-3000','3000-3500','3500-4000','4000-4500','4500-5000','5000-5500','5500-6000']



ax = fig.add_subplot(121)   
#names = [x.replace('-','\n') for x in names]                                                         
new_names = [x+'\n n:'+y for x,y in zip(names,x_ticks)]
   
ax.boxplot(x_list,labels=new_names)
ax.set_xticklabels(new_names)
plt.xticks(rotation=60)
#plt.rc('xaxis', labelsize=20) 
plt.ylim(ymin=0,ymax=250)
plt.ylabel(r"$K_{sn}$",fontsize=18)
plt.xlabel("Lithology",fontsize=18)



x_list,y_list = getAxisHist('burned_dat')
#print x_list,y_list

ax = fig.add_subplot(122)                                                       
h = ax.hist2d(x_list,y_list,bins=(range(30000,140000,10000),100),range=((30000,140000),(0,400)))
plt.xticks([35000,55000,95000,105000,115000,125000],names,rotation=60)
plt.colorbar(h[3], ax=ax)    
plt.ylabel(r"$K_{sn}$",fontsize=18)
plt.xlabel("Lithology",fontsize=18)
ax.get_yaxis().set_visible(False)
    
fig.tight_layout()




fig.savefig('../lithology_box_hist_0.4_removed.png', bbox_inches='tight')
