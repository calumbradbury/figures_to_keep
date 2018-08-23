import pandas as pd
import matplotlib
matplotlib.use("Agg")
from scipy import stats
import sys

from matplotlib import pyplot as plt

import numpy as np
import matplotlib.cm as cm
from numpy import median



target = '/exports/csce/datastore/geos/users/s1134744/LSDTopoTools/Topographic_projects/full_himalaya/raw/'
source = '0_35_ex_MChiSegmented_burned.csv'
source_list = ['0_1_ex_MChiSegmented_burned.csv','0_15_ex_MChiSegmented_burned.csv','0_2_ex_MChiSegmented_burned.csv',
              '0_25_ex_MChiSegmented_burned.csv','0_3_ex_MChiSegmented_burned.csv','0_35_ex_MChiSegmented_burned.csv',
              '0_4_ex_MChiSegmented_burned.csv','0_45_ex_MChiSegmented_burned.csv','0_5_ex_MChiSegmented_burned.csv',
              '0_55_ex_MChiSegmented_burned.csv','0_6_ex_MChiSegmented_burned.csv','0_65_ex_MChiSegmented_burned.csv',
              '0_7_ex_MChiSegmented_burned.csv','0_75_ex_MChiSegmented_burned.csv','0_8_ex_MChiSegmented_burned.csv',
              '0_85_ex_MChiSegmented_burned.csv','0_9_ex_MChiSegmented_burned.csv','0_95_ex_MChiSegmented_burned.csv']

def toSeries(DF,target,values,tectonics=False):
    if not tectonics:
        selectedDF = DF[DF[target].isin(range(values[0],values[1]))]
    if tectonics:
        selectedDF = DF[DF[target] == values]
    selectedDF = selectedDF[selectedDF['m_chi'] > 0]
    series = selectedDF['m_chi']
    if hist2d:
        return selectedDF
    return series

bin_range_lower = [10000,20000,30000,40000,50000,60000,70000,80000,90000,100000,110000,120000,130000,140000,150000,160000]
bin_range_upper = [20000,30000,40000,50000,60000,70000,80000,90000,100000,110000,120000,130000,140000,150000,160000,170000]

names = ["Evaporites","Ice \n and \n Glaciers","Metamorphics","NoData",
             "Acid \n Plutonic \n Rocks","Basin \n Plutonic \n Rocks",
             "Intermediate \n Plutonic \n Rocks","Pyroclastics","Carbonate \n Sedimentary \n Rocks",
             "Mixed \n Sedimentary \n Rocks","Siliciclastic \n Sedimentary \n Rocks",
             "Unconsolidated \n Sediments","Acid \n Volcanic \n Rocks","Basic \n Volcanic \n Rocks",
             "Intermediate \n Volcanic \n Rocks","Water \n Bodies"]
             
names = ['sub_Himalaya','Lesser Himalaya','Greater Himalaya', 'Tethyan Himalaya']

names_b = range(0,6000,200)

plot_within = False        
        
with open(target+'0_35_ex_MChiSegmented_burned.csv','r') as csvfile:
    
    pandasDF = pd.read_csv(csvfile,delimiter=',')
    #print pandasDF
    #selectedDF = pandasDF[pandasDF['m_chi'] > 0]
    medians_list = []
    x_i = 0
    medians_full = []
    for lat_lower,lat_upper in zip(range(76,94,3),range(79,97,3)):        
    
    
        medians = []
        values = []
        weights = []
        list_of_series = []
        label_list = []
    
        
        
       
       
       #for y,z in zip(bin_range_lower,bin_range_upper):
        #for y,z,name in zip(bin_range_lower,bin_range_upper,names):
        #for y,name in zip([1,2,3,4],names):
        #for y,z,name in zip(range(0,150,25),range(25,175,25),range(0,150,25)):
        for y,z,name in zip(range(350,4950,50),range(400,5000,50),range(50,6000,50)):
                #    
            #print "where am i"
            print x_i
            if x_i <1:
                
                #print "I am here"
                print y,z
                selectedDF_b = pandasDF[pandasDF['segmented_elevation'] >= y]
                #print pandasDF['longitude']
                selectedDF_b = selectedDF_b[selectedDF_b['segmented_elevation'] < z] 
                series_b = selectedDF_b['m_chi']
                
                list_b = series_b.tolist()
                medians_full.append(median(list_b))
                
                print medians_full
                #sys.exit()
                
                
            
            #"i've passed here"            
            #selectedDF = selectedDF[selectedDF['second_inv'] <= 100]
            #selectedDF = selectedDF[selectedDF['burned_data'] > y]
            #selectedDF = selectedDF[selectedDF['burned_data'] < z]
            #selectedDF = selectedDF[selectedDF['quaternary_burned_data'] == y]
            #selectedDF = selectedDF[selectedDF['tectonics'] == y]
            
            selectedDF = pandasDF[pandasDF['longitude'] > lat_lower]
            selectedDF = selectedDF[selectedDF['longitude'] < lat_upper]       
            #print medians_full
        
            selectedDF = selectedDF[selectedDF['segmented_elevation'] >= y]
                                                                      
            selectedDF = selectedDF[selectedDF['segmented_elevation'] < z]            
                          
                    

            series = selectedDF['m_chi']
            #series = selectedDF['secondary_burned_data']
                    
            lister = series.tolist()
            medians.append(median(lister))
        
        
            data_count = len(lister)
            new_label = str(name)+'n: %s'%(data_count)
            label_list.append(new_label)
            list_of_series.append(lister)
        
        x_i+=1
        #"hmmm, now where am I?"
        fig = plt.figure(1, figsize=(24,9))
        ax = fig.add_subplot(111)
        #plt.yscale('log')
        #plt.xlabel("segmented elevation in 50m bins")
        #plt.ylabel("median Ksn - log scale")        
            
        plt.ylabel("Ksn")
        plt.xlabel("Elevation binned 50")
        #plt.scatter(values,medians,c=weights,cmap=cm.Blues)
        #plt.colorbar()
        plt.boxplot(list_of_series,labels=label_list)
        plt.ylim(ymin=0,ymax=150)
        plt.xticks(rotation=90)
        
        lat_lower = str(lat_lower)
        lat_upper = str(lat_upper)
            
        fig.savefig('../full_0.35_mchi_elevation_lat_%s_%s_box.png'%(lat_lower,lat_upper), bbox_inches='tight')
        plt.cla()
        medians_list.append(medians)
        
    fig = plt.figure(1, figsize=(24,9))
    ax = fig.add_subplot(111)

    x_axis = range(350,4950,50)
    
    length = len(range(76,94,3))
    
    x = np.arange(length)
    ys = [i+x+(i*x)**2 for i in range(length)]

    colors = cm.Blues(np.linspace(0, 1, len(ys)))
                                                                      
    
    for scatter,colour in zip(medians_list,colors):
        plt.scatter(x_axis,scatter,marker='.',c=colour)    
    
    
    print len(x_axis),len(medians_full)
    print medians_full
    
    plt.scatter(x_axis,medians_full,marker = 'o', c='k')
    
    plt.ylabel("Ksn")
    plt.xlabel("Elevation binned 50")   
    plt.ylim(ymin=0,ymax=150)     
    fig.savefig('../full_0.35_mchi_elevation_lat_scatter_box.png', bbox_inches='tight')