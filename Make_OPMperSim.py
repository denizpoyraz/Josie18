import pandas as pd
import numpy as np
import re
import glob
import math
from math import log
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.offsetbox import AnchoredText

df = pd.read_csv("/home/poyraden/Josie18/Josie18_Data.csv", low_memory=False)

df_sim = df.drop_duplicates(['Sim']) 
listSim = df_sim['Sim'].tolist()

dft = df.drop_duplicates(['Sim','Team'])
dfmd = df_sim.reset_index(drop=True)

size = len(listSim)

OPM = [0]*size; Time = [0]*size

dataframe_collection = {}
labels = []
filterlist = []

filterlist0910 = []
filterlist18 = []


filter0910 = df.Year < 2018
filter18 = df.Year > 2010
filteropm = df.Team == 1
    
for s in listSim:
    filtersim = df.Sim == s
    filterlist.append(filtersim & filteropm)
    filterlist0910.append(filtersim & filteropm & filter0910)
    filterlist18.append(filtersim & filteropm & filter18)

df0910 = df[filter0910].drop_duplicates(['Sim']) 
df18 = df[filter18].drop_duplicates(['Sim'])

listSim0910 = df0910['Sim'].tolist()
listSim18 = df18['Sim'].tolist()



for simitem in range(0,size):
    dataframe_collection[simitem] = df[filterlist[simitem]]
    OPM[simitem] =  dataframe_collection[simitem].PO3_OPM.tolist()
    Time[simitem] = dataframe_collection[simitem].Tsim.tolist()
    #neede for the labels
    sim = dfmd.loc[simitem,'Sim']; year =  dfmd.loc[simitem,'Year'];
    labels.append('Sim.' + str(sim) +', Year ' + str(year))

#yearlist = {137:2009, 136:2009, 150:2010, 151:2010, 198:2018, 194:2018, 195:2018, 145:2009, 196:2018, 146:2009, 199:2018, 197:2018}
yearlist = {0:2009, 1:2009, 2:2010, 3:2010, 4:2018, 5:2018, 6:2018, 7:2009, 8:2018, 9:2009, 10:2018, 11:2018}



    
fig,ax = plt.subplots()
plt.xlim(0,10000)
plt.ylim(0,30)
plt.xlabel('Simulation Time (sec.)')
plt.ylabel(r'Partial Pressure OPM ($\mu$Pa)')
plt.title('PO3 OPM per Simulation')
plt.grid(True)

#plt.yticks(np.arange(0, 7001, 1000))
ax.tick_params(axis='both', which='both', direction='in')
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')

ax.yaxis.set_minor_locator(AutoMinorLocator(10))
ax.xaxis.set_minor_locator(AutoMinorLocator(10))

for y in yearlist:
    iy = yearlist[y]
    if yearlist[y] ==  2018:
    #    print(y, iy)
        plt.plot(Time[y], OPM[y], label=labels[y], linewidth = 0.5)
        #plt.plot(Time[0], OPM[0], label=label1, color='black', linewidth = 0.5)

ax.legend(loc='upper left', frameon=True, fontsize = 'small')
plt.savefig('/home/poyraden/Josie18/Plots/OPM_Sim18.eps')
plt.savefig('/home/poyraden/Josie18/Plots/OPM_Sim18.pdf')
plt.close()

