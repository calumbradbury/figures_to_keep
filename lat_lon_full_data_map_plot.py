import matplotlib 
matplotlib.use("Agg")
from matplotlib import pyplot as plt
import pandas as pd           
import matplotlib.patches as mpatches
import sys

target = '/exports/csce/datastore/geos/users/s1134744/LSDTopoTools/Topographic_projects/'

source_list = ['full_himalaya/raw/full_data.csv','full_himalaya/full_data.csv','full_himalaya_5000/raw/full_data.csv','full_himalaya_5000/full_data.csv']

colours = ['b','g','r','c']
legends = []

for x,y in zip(source_list,colours):
    with open(target+x,'r') as csvfile:
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
    
        plt.scatter(x_Series,y_Series,marker='.', c=y)
        
        name = x.replace('full_data.csv','')

        legend = mpatches.Patch(color=y, label=name)
        legends.append(legend)
        
        #plt.legend(handles=[red_patch])        

        #plt.gca().invert_xaxis()
        #matplotlib.axes.Axes.invert_xaxis 
    
        #ax.hist2d(x_Series,y_Series,bins=(40,40),range=((150,1000),(0,3000)))
        #plt.ylim(0,200)                                                  
        #cb = plt.colorbar()
        
plt.legend(handles=legends)   

fig.savefig(target+'figures_to_keep/lat_lon_full_data_map_plot.png', bbox_inches='tight')
 