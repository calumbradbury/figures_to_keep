#distance along front#precip 0.4 only


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


def getAxisBox(column,mins,maxs):

    x_list = []
    x_ticks = []
       
    with open(target+source,'r') as csvfile:
        
        df = pd.read_csv(csvfile,delimiter=',') 
        selectedDF = df[df['m_chi'] > 0]
                    
        for lower,upper in zip(mins,maxs):           
            selectedDF = df[df[column] >= lower]
            selectedDF = selectedDF[selectedDF[column] < upper]            
          
            series = selectedDF['tectonics']                   
            lister = series.tolist()
            data_count = len(lister)
            
            #for labeling x axis
            #label = str(lower)+'\n n:'+str(data_count) 
            x_ticks.append(str(data_count))
        
            x_list.append(lister)        
                  
    return x_list,x_ticks
    
fig = plt.figure(1, figsize=(20,10))

x_list,x_ticks = getAxisBox('distance',[0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8],[0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0])
#x_list,x_ticks = getAxisBox('distance',[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9],[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0])


#names_a = [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9]
#names_b = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0]

names_a = [0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8]
names_b = [0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0]

ax = fig.add_subplot(221)   
names = [str(x)+'\n'+str(y) for x,y in zip(names_a,names_b)]                                           

new_names = [x+'\n n:'+y for x,y in zip(names,x_ticks)]
   
ax.boxplot(x_list)#,labels=new_names)
ax.set_xticklabels(new_names,fontsize='small')
#plt.rc('xaxis', labelsize=20) 
plt.ylim(ymin=0,ymax=5)
plt.ylabel("Precipitation (mm/year)",fontsize=18)
plt.xlabel("Distance from Mountain Front (decimal degrees)",fontsize=18)


x_list,x_ticks = getAxisBox('distance_a',range(0,2000,200),range(200,2200,200))

names_a = range(0,2000,200)
names_b = range(200,2200,200)

names = [str(x)+'\n'+str(y) for x,y in zip(names_a,names_b)]

ax = fig.add_subplot(222)   
#names = [x.replace('-','\n') for x in names]                                                         
new_names = [x+'\n n:'+y for x,y in zip(names,x_ticks)]
   
ax.boxplot(x_list)#,labels=new_names)
ax.set_xticklabels(new_names,fontsize='small')
#plt.rc('xaxis', labelsize=20) 
plt.ylim(ymin=0,ymax=5)
plt.ylabel("Precipitation (mm/year)",fontsize=18)
plt.xlabel("Distance along Mountain Front East to West (km)",fontsize=18)



x_list,x_ticks = getAxisBox('latitude',[26.75,27.25,27.75,28.25,28.75,29.25,29.75,30.25,30.75,31.25],[27.25,27.75,28.25,28.75,29.25,29.75,30.25,30.75,31.25,31.75])

#names = ['0-500','500-1000','1000-1500','1500-2000','2000-2500','2500-3000','3000-3500','3500-4000','4000-4500','4500-5000','5000-5500','5500-6000']

ax = fig.add_subplot(223)   

names_a = [26.75,27.25,27.75,28.25,28.75,29.25,29.75,30.25,30.75,31.25] 
names_b = [27.25,27.75,28.25,28.75,29.25,29.75,30.25,30.75,31.25,31.75]
names = [str(x)+'\n'+str(y) for x,y in zip(names_a,names_b)]
                                                    
new_names = [x+'\n n:'+y for x,y in zip(names,x_ticks)]
   
ax.boxplot(x_list)#,labels=new_names)
ax.set_xticklabels(new_names,fontsize='small')
#plt.rc('xaxis', labelsize=20) 
plt.ylim(ymin=0,ymax=5)
plt.ylabel("Precipitation (mm/year)",fontsize=18)
plt.xlabel("Latitude (0.5 degree bins)",fontsize=18)




x_list,x_ticks = getAxisBox('longitude',range(76,96,2),range(78,98,2))

#names = ['0-500','500-1000','1000-1500','1500-2000','2000-2500','2500-3000','3000-3500','3500-4000','4000-4500','4500-5000','5000-5500','5500-6000']

ax = fig.add_subplot(224)   
names_a = range(76,96,2) 
names_b = range(78,98,2)                                                  

names = [str(x)+'\n'+str(y) for x,y in zip(names_a,names_b)]
new_names = [x+'\n n:'+y for x,y in zip(names,x_ticks)]
   
ax.boxplot(x_list)#,labels=new_names)
ax.set_xticklabels(new_names,fontsize='small')
#plt.rc('xaxis', labelsize=20) 
plt.ylim(ymin=0,ymax=5)
plt.ylabel("Precipitation (mm/year)",fontsize=18)
plt.xlabel("Longitude (2 degree bins)",fontsize=18)





fig.tight_layout()




fig.savefig('../precipiation_box_hist_distance_0.4_removed.png', bbox_inches='tight')
