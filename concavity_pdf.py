import matplotlib 
matplotlib.use("Agg")
from matplotlib import pyplot as plt
import numpy as np

import pandas as pd
import matplotlib.patches as mpatches


target = '/exports/csce/datastore/geos/users/s1134744/LSDTopoTools/Topographic_projects/figures_to_keep/'

source_list = ['concavity_boot.csv','concavity_disorder.csv']

bootDF = pd.read_csv(target+source_list[0])
disorderDF = pd.read_csv(target+source_list[1])
pdf = True

fig = plt.figure(1, figsize=(15,8))
ax = fig.add_subplot(111)

x_Series = bootDF['concavity']
    
#plt.scatter(x_Series,bootDF['full'],marker='.', c='b')
#plt.scatter(x_Series,disorderDF['full'],marker='o', c='b')

#plt.scatter(x_Series,bootDF['full-clip'],marker='.', c='y')
#plt.scatter(x_Series,disorderDF['full-clip'],marker='o', c='y')

#plt.scatter(x_Series,bootDF['5000'],marker='.', c='r')
#plt.scatter(x_Series,disorderDF['5000'],marker='o', c='r')

#plt.scatter(x_Series,bootDF['5000-clip'],marker='.', c='k')
#plt.scatter(x_Series,disorderDF['5000-clip'],marker='o', c='k')

#plt.ylim(ymin=0,ymax=100)

#plt.scatter(x_Series,bootDF['reduction'],marker='.', c='b')
#plt.scatter(x_Series,disorderDF['reduction'],marker='o', c='b')

#plt.legend()

#fig.savefig(target+'concavity_reduction.png', bbox_inches='tight')

def seriesSum(Series):
    lister = Series.tolist()
    return sum(lister)
    
def getPDF(list,sum):
    pdf_list = []
    for x in list:
        x = float(x)
        sum = float(sum)
        pdf_list.append(x/sum)
    return pdf_list
    
def toSeries(data,name):
    new_series = pd.Series(data)
    new_series = new_series.rename(name)    
    return new_series

if pdf:
    full_sum = seriesSum(disorderDF['full'])
    full_glims_sum = seriesSum(disorderDF['full-clip'])
    five_sum = seriesSum(disorderDF['5000'])                                                
    five_glims_sum = seriesSum(disorderDF['5000-clip'])
    
    full_list = disorderDF['full'].tolist()
    full_glims_list = disorderDF['full-clip'].tolist()
    five_list = disorderDF['5000'].tolist()
    five_glims_list = disorderDF['5000-clip'].tolist()
    
    full_pdf = getPDF(full_list,full_sum)
    full_clip_pdf = getPDF(full_glims_list,full_glims_sum)
    five_pdf = getPDF(five_list,five_sum)
    five_clip_pdf = getPDF(five_glims_list,five_glims_sum)
    
    print full_pdf,full_clip_pdf,five_pdf,five_clip_pdf
    
    #plt.scatter(x_Series,bootDF['full'],marker='.', c='b')
    
    
    full_pdf_series = toSeries(full_pdf,"full")
    print full_pdf_series
    full_clip_pdf_series = toSeries(full_clip_pdf,"full_clip")
    five_pdf_series = toSeries(five_pdf,"five")
    five_clip_pdf_series = toSeries(five_clip_pdf,"five_clip")
    
    
    plt.scatter(x_Series,full_pdf_series,marker='o', c='b')

    #plt.scatter(x_Series,bootDF['full-clip'],marker='.', c='y')
    plt.scatter(x_Series,full_clip_pdf_series,marker='o', c='y')

    #plt.scatter(x_Series,bootDF['5000'],marker='.', c='r')
    plt.scatter(x_Series,five_pdf_series,marker='o', c='r')

    #plt.scatter(x_Series,bootDF['5000-clip'],marker='.', c='k')
    plt.scatter(x_Series,five_clip_pdf_series,marker='o', c='k')
    
    plt.xticks(x_Series)
        
    plt.ylabel("PDF (number of basins/total sample size)", fontsize=16)
    plt.xlabel("Concavity",fontsize=16)   
    
legends = []
    
for colour,name in zip(['b','y','r','k'],['350m-unlimited elevation','350m-unlimited elevation GLIMS glaciation removed','350-5000m elevation','350-5000m elevation GLIMS glaciation removed']):
    legend = mpatches.Patch(color=colour, label=name)
    legends.append(legend)
    
plt.legend(handles=legends,title='Data Processing Levels')

fig.savefig('../concavity_pdf.png', bbox_inches='tight')