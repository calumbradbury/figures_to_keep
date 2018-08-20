import matplotlib 
matplotlib.use("Agg")
from matplotlib import pyplot as plt

import pandas as pd

target = '/exports/csce/datastore/geos/users/s1134744/LSDTopoTools/Topographic_projects/figures_to_keep/'

source_list = ['concavity_boot.csv','concavity_disorder.csv']

bootDF = pd.read_csv(target+source_list[0])
disorderDF = pd.read_csv(target+source_list[1])


fig = plt.figure(1, figsize=(24,12))
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

plt.ylim(ymin=0,ymax=100)

plt.scatter(x_Series,bootDF['reduction'],marker='.', c='b')
plt.scatter(x_Series,disorderDF['reduction'],marker='o', c='b')

plt.legend()

fig.savefig(target+'concavity_reduction.png', bbox_inches='tight')
