import pandas as pd
import matplotlib
matplotlib.use("Agg")
from scipy import stats

from matplotlib import pyplot as plt

import numpy as np
import matplotlib.cm as cm



target = '/exports/csce/datastore/geos/users/s1134744/LSDTopoTools/Topographic_projects/full_himalaya_5000/'
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

plot_within = True        
        
with open(target+'0_35_ex_MChiSegmented_burned.csv','r') as csvfile:
    medians = []
    values = []
    weights = []
    list_of_series = []
    label_list = []
    pandasDF = pd.read_csv(csvfile,delimiter=',')
                
   
    
    #for y,z in zip(bin_range_lower,bin_range_upper):
    #for y,z,name in zip(bin_range_lower,bin_range_upper,names):
    #for y,name in zip([1,2,3,4],names):
    for y,z,name in zip(range(0,150,25),range(25,175,25),range(0,150,25)):
    #for y,z,name in zip(range(350,4950,50),range(400,5000,50),range(50,6000,50)):
                #    
        selectedDF = pandasDF[pandasDF['m_chi'] > 0]
        #selectedDF = selectedDF[selectedDF['second_inv'] <= 100]
        #selectedDF = selectedDF[selectedDF['burned_data'] > y]
        #selectedDF = selectedDF[selectedDF['burned_data'] < z]
        #selectedDF = selectedDF[selectedDF['quaternary_burned_data'] == y]
        #selectedDF = selectedDF[selectedDF['tectonics'] == y]
        
        selectedDF = selectedDF[selectedDF['second_inv'] > y]
        selectedDF = selectedDF[selectedDF['second_inv'] < z]
        
        #selectedDF = selectedDF[selectedDF['segmented_elevation'] >= y]
                    
        #selectedDF = selectedDF[selectedDF['segmented_elevation'] < z]                          
                    

        series = selectedDF['m_chi']
        #series = selectedDF['secondary_burned_data']
                    
        lister = series.tolist()
        
        
        data_count = len(lister)
        new_label = str(name)+'n: %s'%(data_count)
        label_list.append(new_label)
        list_of_series.append(lister)
        
        if plot_within:
            try:
                list_of_series_within = []
                label_list_within = []
            
                for lower,upper,name_b in zip(range(0,6000,500),range(500,5500,500),names_b):
                

                    within_selectedDF = selectedDF[selectedDF['secondary_burned_data'] > lower]
                    within_selectedDF = within_selectedDF[within_selectedDF['secondary_burned_data'] < upper]

                    #selectedDF = selectedDF[selectedDF['tectonics'] == y]
                    #selectedDF = selectedDF[selectedDF['strain_ezz'] >= y]
                    
                    #selectedDF = selectedDF[selectedDF['strain_ezz'] < z]                          
                    

                    series_within = within_selectedDF['m_chi']
                    #series = selectedDF['secondary_burned_data']
                    
                    lister_within = series_within.tolist()
                    
        
                    data_count_within = len(lister_within)
                    new_label_within = str(name_b)+'\n'+'n: %s'%(data_count_within)
                    
                    print new_label_within
                    print lower,upper
                    label_list_within.append(new_label_within)
                    list_of_series_within.append(lister_within)                
        
                fig = plt.figure(1, figsize=(27,9))
                ax = fig.add_subplot(111)
                plt.ylabel("Ksn")
                plt.xlabel("Annual precipitation 500mm bins")
                plt.boxplot(list_of_series_within,labels=label_list_within)
                plt.ylim(ymin=0,ymax=200)             
                name = str(name)                    
                fig.savefig('../0.35_mchi_precip_%s_box.png'%(name[:2]), bbox_inches='tight')
                plt.cla()
            except Exception as e:
                print e
                print "error in %s"%(name)
               
fig = plt.figure(1, figsize=(24,9))
ax = fig.add_subplot(111)
#plt.yscale('log')
#plt.xlabel("segmented elevation in 50m bins")
#plt.ylabel("median Ksn - log scale")        
            
plt.ylabel("Ksn")
plt.xlabel("Strain binned 25")
#plt.scatter(values,medians,c=weights,cmap=cm.Blues)
#plt.colorbar()
plt.boxplot(list_of_series,labels=label_list)
plt.ylim(ymin=0,ymax=200)
#plt.xticks(rotation=90)
            
fig.savefig('../0.35_mchi_strain_box.png', bbox_inches='tight')
plt.cla()