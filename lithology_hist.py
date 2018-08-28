                                                                                                                                                           #precip 0.4 only. Hist and Box one plot.


import matplotlib 
matplotlib.use("Agg")
from matplotlib import pyplot as plt
import pandas as pd           
import sys
import matplotlib.patches as mpatches

target = '/exports/csce/datastore/geos/users/s1134744/LSDTopoTools/Topographic_projects/full_himalaya_5000/'

source= '0_4_ex_MChiSegmented_burned_outlier_removed.csv'



def getAxisHist(column):
    
    with open(target+source,'r') as csvfile:
        df_a = pd.read_csv(csvfile,delimiter=',')
        for_hist = []
        for x in [1,2,3,4]:
            df = df_a[df_a['tectonics'] == x]
            
            x_list = df[column].tolist()
            y_list = df['m_chi'].tolist()    
            for_hist.append(x_list)
    
    return for_hist


def getAxisBox(column,mins,maxs):

    x_list = []
    x_ticks = []
       
    with open(target+source,'r') as csvfile:
        
        df = pd.read_csv(csvfile,delimiter=',') 
        selectedDF = df[df['m_chi'] > 0]
        selectedDF = selectedDF[selectedDF['quaternary_burned_data'] == 1]
                    
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
    
colours = ['b','g','r','y','c','m']
numbers_a = [30000,50000,90000,100000,110000,120000]
numbers_b = [40000,60000,100000,110000,120000,130000]
bin_names = ["Metamorphics","Acid Plutonic Rocks","Carbonate Sedimentary Rocks",
             "Mixed Sedimentary Rocks","Siliciclastic Sedimentary Rocks",
             "Unconsolidated Sediments"]


fig = plt.figure(1, figsize=(15,9))

#x_list,y_list = getAxisBox('burned_dat',range(10000,170000,10000),range(20000,180000,10000))
x_list = getAxisHist('burned_dat')
#print x_list,y_list
names = ["Evaporites","Ice \n and \n Glaciers","Metamorphics","NoData",
             "Acid \n Plutonic \n Rocks","Basin \n Plutonic \n Rocks",
             "Intermediate \n Plutonic \n Rocks","Pyroclastics","Carbonate \n Sedimentary \n Rocks",
             "Mixed \n Sedimentary \n Rocks","Siliciclastic \n Sedimentary \n Rocks",
             "Unconsolidated \n Sediments","Acid \n Volcanic \n Rocks","Basic \n Volcanic \n Rocks",
             "Intermediate \n Volcanic \n Rocks","Water \n Bodies"]
#names = ['0-500','500-1000','1000-1500','1500-2000','2000-2500','2500-3000','3000-3500','3500-4000','4000-4500','4500-5000','5000-5500','5500-6000']
#ax = fig.add_subplot(111)

legends = []
titles = ['Sub Himalaya','Lesser Himalaya','Greater Himalaya','Tethyan Himalaya']
print x_list
locations = [221,222,223,224]
for x,location,title in zip(x_list,locations,titles):                                                       
    ax = fig.add_subplot(location)
    N,bins,patches = ax.hist(x,bins=range(10000,170000,10000),stacked=False)
    i = 2
    patches[i].set_facecolor('b')
    i = 4
    patches[i].set_facecolor('g')
    i = 8
    patches[i].set_facecolor('r')
    i = 9
    patches[i].set_facecolor('y')
    i = 10
    patches[i].set_facecolor('c')
    i = 11
    patches[i].set_facecolor('m')
    
    #plt.xticks([35000,55000,95000,105000,115000,125000],bin_names)
    plt.ylabel("Frequency",fontsize=18)
    #plt.xlabel("GLIM Lithology Class",fontsize=18)
    plt.title(title)
    ax.get_xaxis().set_visible(False)

for colour,name in zip(colours,bin_names):
    legend = mpatches.Patch(color=colour, label=name)
    legends.append(legend)

leg = fig.legend(legends, bin_names,'lower center',ncol=3,title='GLIM Lithology Class') 


#N,bins,patches = ax.hist(x,bins=range(10000,170000,10000),stacked=False)

i = 2
#patches[i].set_facecolor('b')


i = 4
#patches[i].set_facecolor('r')

i = 8
#patches[i].set_facecolor('c')

i = 9
#patches[i].set_facecolor('y')

i = 10
#patches[i].set_facecolor('m')




#plt.xticks(range(15000,185000,10000),names)
#plt.ylabel("Frequency",fontsize=18)
#plt.xlabel("GLIM Lithology Class",fontsize=18)    
#fig.tight_layout()

fig.savefig('../lithology_sub_hist_5000.png', bbox_inches='tight')


