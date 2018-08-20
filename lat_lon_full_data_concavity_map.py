import matplotlib 
matplotlib.use("Agg")
from matplotlib import pyplot as plt
import pandas as pd           
import matplotlib.patches as mpatches
import sys
import matplotlib.cm as cm
import numpy as np

target = '/exports/csce/datastore/geos/users/s1134744/LSDTopoTools/Topographic_projects/'

#source_list = ['full_himalaya/raw/full_data.csv','full_himalaya/full_data.csv','full_himalaya_5000/raw/full_data.csv','full_himalaya_5000/full_data.csv']

source_list = ['0_1_ex_MChiSegmented_burned.csv','0_15_ex_MChiSegmented_burned.csv','0_2_ex_MChiSegmented_burned.csv',
              '0_25_ex_MChiSegmented_burned.csv','0_3_ex_MChiSegmented_burned.csv','0_35_ex_MChiSegmented_burned.csv',
              '0_4_ex_MChiSegmented_burned.csv','0_45_ex_MChiSegmented_burned.csv','0_5_ex_MChiSegmented_burned.csv',
              '0_55_ex_MChiSegmented_burned.csv','0_6_ex_MChiSegmented_burned.csv','0_65_ex_MChiSegmented_burned.csv',
              '0_7_ex_MChiSegmented_burned.csv','0_75_ex_MChiSegmented_burned.csv','0_8_ex_MChiSegmented_burned.csv',
              '0_85_ex_MChiSegmented_burned.csv','0_9_ex_MChiSegmented_burned.csv','0_95_ex_MChiSegmented_burned.csv']


z = np.arange(18)
ys = [i+z+(i*z)**2 for i in range(18)]

colors = cm.Reds(np.linspace(0, 1, len(ys)))
legends = []

for x,y in zip(source_list,colors):
    with open(target+'full_himalaya/raw/'+x,'r') as csvfile:
        pandasDF = pd.read_csv(csvfile,delimiter=',')
        #pandasDF = pandasDF[pandasDF['m_chi'] > 0]
        #pandasDF = pandasDF[pandasDF['longitude'] > 85]
        #pandasDF = pandasDF[pandasDF['longitude'] < 90]
        #pandasDF = pandasDF[pandasDF['distance_along'] < 1000]
        #pandasDF = pandasDF[pandasDF['distance_along'] > 150]    
    
        x_Series = pandasDF['longitude']
        y_Series = pandasDF['latitude']
    
        fig = plt.figure(1, figsize=(36,12))
        ax = fig.add_subplot(111)
    
        plt.scatter(x_Series,y_Series,marker='.', c=y, cmap = cm.Reds)
        
        name = x.replace('_ex_MChiSegmented_burned.csv','')

        legend = mpatches.Patch(color=y, label=name)
        legends.append(legend)
        
        #plt.legend(handles=[red_patch])        

        #plt.gca().invert_xaxis()
        #matplotlib.axes.Axes.invert_xaxis 
    
        #ax.hist2d(x_Series,y_Series,bins=(40,40),range=((150,1000),(0,3000)))
        #plt.ylim(0,200)                                                  
        #cb = plt.colorbar()
        
plt.legend(handles=legends)   

fig.savefig(target+'figures_to_keep/lat_lon_full_data_concavity_map.png', bbox_inches='tight')
 