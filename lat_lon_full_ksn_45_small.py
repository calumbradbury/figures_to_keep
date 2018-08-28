import matplotlib 
matplotlib.use("Agg")
from matplotlib import pyplot as plt
import pandas as pd           
import matplotlib.patches as mpatches
import matplotlib.cm as cm
import sys
from mpl_toolkits.axes_grid.inset_locator import inset_axes

target = '/exports/csce/datastore/geos/users/s1134744/LSDTopoTools/Topographic_projects/full_himalaya/raw/0_4/'

source_list = ['0_1_0.4_MChiSegmented_burned.csv','0_15_0.4_MChiSegmented_burned.csv','0_2_0.4_MChiSegmented_burned.csv',
              '0_25_0.4_MChiSegmented_burned.csv','0_3_0.4_MChiSegmented_burned.csv','0_35_0.4_MChiSegmented_burned.csv',
              '0_4_0.4_MChiSegmented_burned.csv','0_45_0.4_MChiSegmented_burned.csv','0_5_0.4_MChiSegmented_burned.csv',
              '0_55_0.4_MChiSegmented_burned.csv','0_6_0.4_MChiSegmented_burned.csv','0_65_0.4_MChiSegmented_burned.csv',
              '0_7_0.4_MChiSegmented_burned.csv','0_75_0.4_MChiSegmented_burned.csv','0_8_0.4_MChiSegmented_burned.csv',
              '0_85_0.4_MChiSegmented_burned.csv','0_9_0.4_MChiSegmented_burned.csv','0_95_0.4_MChiSegmented_burned.csv']

#def openPandas(source):
#    df = pd.read_csv(target+source)
#    return df 

#for source in source_list:
#    df = openPandas(source)
    #print pandasDF
#    df.to_csv(target+'full_data.csv',mode='a',index=False,header=False)



with open(target+'full_data.csv','r') as csvfile:
    pandasDF = pd.read_csv(csvfile,delimiter=',')
    #print pandasDF
    #pandasDF = pandasDF[pandasDF['burned_data'] > 0]
    #pandasDF = pandasDF[pandasDF[''] < 400]
    pandasDF = pandasDF[pandasDF['longitude'] > 86.5]
    pandasDF = pandasDF[pandasDF['longitude'] < 87]
    pandasDF = pandasDF[pandasDF['latitude'] > 28.5]
    pandasDF = pandasDF[pandasDF['latitude'] < 29]
    #pandasDF = pandasDF[pandasDF['distance_along'] < 1000]
    #pandasDF = pandasDF[pandasDF['distance_along'] > 150]    
    
    x_Series = pandasDF['longitude']
    y_Series = pandasDF['latitude']
    #print x_Series
    weight = pandasDF['m_chi']
    
    fig = plt.figure(1, figsize=(6,6))
    ax = fig.add_subplot(111)    
    plt.scatter(x_Series,y_Series,marker=',',s=1, c=weight, cmap = cm.terrain)
    plt.axes().set_aspect('equal', 'datalim')  
    plt.xlabel("Degrees Longitude")
    plt.ylabel("Degrees Latitude")
    
    #plt.xticks(range(76,96,1))
    h = plt.colorbar()
    h.set_label(r'$K_{sn}$')

    #plt.axes().set_aspect('equal', 'datalim')  
    
    
        
        #plt.gca().invert_xaxis()
        #matplotlib.axes.Axes.invert_xaxis 
    
        #ax.hist2d(x_Series,y_Series,bins=(40,40),range=((150,1000),(0,3000)))
        #plt.ylim(0,200)   
    #plt.axes().set_aspect('equal', 'datalim')                                               
    #plt.colorbar()
        
    fig.savefig(target+'/lat_lon_full_data_0.4_small_ksn_plot.png', bbox_inches='tight')
 