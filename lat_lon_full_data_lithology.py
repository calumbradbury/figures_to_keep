import matplotlib 
matplotlib.use("Agg")
from matplotlib import pyplot as plt
import pandas as pd           
import matplotlib.patches as mpatches
import sys

target = '/exports/csce/datastore/geos/users/s1134744/LSDTopoTools/Topographic_projects/'

source_list = ['full_himalaya/raw/full_data.csv']#,'full_himalaya/full_data.csv','full_himalaya_5000/raw/full_data.csv','full_himalaya_5000/full_data.csv']

colours = ['b','g','r','y','c','m']
numbers_a = [30000,50000,90000,100000,110000,120000]
numbers_b = [40000,60000,100000,110000,120000,130000]
legends = []
names = ["Metamorphics","Acid Plutonic Rocks","Carbonate Sedimentary Rocks",
             "Mixed Sedimentary Rocks","Siliciclastic Sedimentary Rocks",
             "Unconsolidated Sediments"]

for x,y,z,name in zip(numbers_a,numbers_b,colours,names):
    with open(target+'full_himalaya/raw/full_data.csv','r') as csvfile:
        pandasDF = pd.read_csv(csvfile,delimiter=',')
        #pandasDF = pandasDF[pandasDF['quaternary_burned_data'] == x]
        pandasDF = pandasDF[pandasDF['burned_data'] >= x]
        pandasDF = pandasDF[pandasDF['burned_data'] < y]        
        
        #pandasDF = pandasDF[pandasDF['longitude'] > 85]
        #pandasDF = pandasDF[pandasDF['longitude'] < 90]
        #pandasDF = pandasDF[pandasDF['distance_along'] < 1000]
        #pandasDF = pandasDF[pandasDF['distance_along'] > 150]    
    
        x_Series = pandasDF['longitude']
        y_Series = pandasDF['latitude']
    
        fig = plt.figure(1, figsize=(18,6))
        ax = fig.add_subplot(111)
    
        plt.scatter(x_Series,y_Series,marker='.',s=0.1, c=z)
        
        legend = mpatches.Patch(color=z, label=name)
        legends.append(legend)
        
        #plt.legend(handles=[red_patch])        

        #plt.gca().invert_xaxis()
        #matplotlib.axes.Axes.invert_xaxis 
    
        #ax.hist2d(x_Series,y_Series,bins=(40,40),range=((150,1000),(0,3000)))
        #plt.ylim(0,200)                                                  
        #cb = plt.colorbar()


plt.axes().set_aspect('equal', 'datalim')    
plt.xticks(range(76,96,1))
plt.xlabel("Degrees Longitude")
plt.ylabel("Degrees Latitude")
     
leg = plt.legend(handles=legends,ncol=6,loc='upper center', bbox_to_anchor=(0.5, -0.1))   
leg.get_frame().set_alpha(1)

fig.savefig(target+'figures_to_keep/lat_lon_full_data_lithology.png', bbox_inches='tight')
 