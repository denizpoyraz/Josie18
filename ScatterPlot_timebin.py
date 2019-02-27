import pandas as pd
import numpy as np
import re
import glob
import math
from math import log
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.offsetbox import AnchoredText
from sklearn.linear_model import LinearRegression
from scipy import stats

from Josie17_Functions import Calc_average_profile
from Josie17_Functions import Plot_compare_profile_plots
from Josie17_Functions import Plot_compare_profile_plots_updated
from Josie17_Functions import Calc_RDif
from Josie17_Functions import meanfunction
from Josie18_Functions import Calc_average_profile_PO3


def plotfunction(x,y,title, lcolor):
    #plt.xlim(0.1,2)
    plt.ylim(0,7000)
    plt.ylabel('Time')
    plt.xlabel('Slope')
    plt.title(title)
    plt.grid(True)
    plt.plot(x, y, 'ro-',color = lcolor)



#df = pd.read_csv("/home/poyraden/Josie18/Josie18_Data.csv", low_memory=False)
#dfmd = pd.read_csv("/home/poyraden/Josie18/Josie18_MetaData.csv", low_memory=False)

df = pd.read_csv("/Volumes/HD3/KMI/Josie18/Josie18_Data.csv", low_memory=False)
dfmd = pd.read_csv("/Volumes/HD3/KMI/Josie18/Josie18_MetaData.csv", low_memory=False)


minOPM = 0.5; minPO3 = 0.5; maxOPM = 20; maxPO3 = 20; minT = 0; maxT = 7000;


tmin = 0; tmax = 7000; bin = 500; nt = int(tmax/bin);
minTbin = [0] * (nt)
maxTbin = [0] * (nt)


size = nt
slope = [0]*size; intercept = [0]*size; r_value = [0]*size; p_value = [0]*size;  std_err = [0]*size

opm_sim = [0]*size; po3_sim = [0]*size


timelist = [0]*size


for t in range(nt):
    minTbin[t] = bin * (t)
    maxTbin[t] = bin * (t+1)
    timelist[t] = (minTbin[t] + maxTbin[t])/2
    if( (minTbin[t] == 0) & (maxTbin[t] == 500) ): timelist[t] =0
    if( (minTbin[t] == 1500) & (maxTbin[t] == 2000) ): timelist[t] =0
    #print(minTbin[t], maxTbin[t])
    
    
timelist.remove(0)
timelist.remove(0)


df = df[(df.PO3_OPM > minOPM) & (df.PO3 > minPO3) & (df.PO3_OPM < maxOPM ) & (df.Tsim < maxT)]

dfENSCI_201 = df[(df.ENSCI == 1) & (df.Sol == 2) & (df.Buf == 0.1)]
dfENSCI_201adx = df[(df.ENSCI == 1) & (df.Sol == 2) & (df.Buf == 0.1) & (df.ADX == 1)]
dfENSCI_201noadx = df[(df.ENSCI == 1) & (df.Sol == 2) & (df.Buf == 0.1) & (df.ADX == 0)]

dfENSCI_201_tbin = {}
dfENSCI_201adx_tbin = {}
dfENSCI_201noadx_tbin = {}

for tt in range(0,nt):
    if( (minTbin[tt] == 0) & (maxTbin[tt] == 500) ): continue
    if( (minTbin[tt] == 1500) & (maxTbin[tt] == 2000) ): continue
    filttime = (dfENSCI_201.Tsim > minTbin[tt]) & (dfENSCI_201.Tsim <= maxTbin[tt])
    dfENSCI_201_tbin[tt] = dfENSCI_201[filttime]

    opm_sim[tt] = np.asarray(dfENSCI_201_tbin[tt].PO3_OPM)
    po3_sim[tt] = np.asarray(dfENSCI_201_tbin[tt].PO3)
    #print(tt, minTbin[tt], maxTbin[tt], opm_sim[tt].mean())

    slope[tt], intercept[tt], r_value[tt], p_value[tt], std_err[tt] = stats.linregress(opm_sim[tt],po3_sim[tt])
    #po3_fit[tt] = slope[tt] * opm_sim[tt] + intercept[tt]
    #print('tt', minTbin[tt], maxTbin[tt], slope[tt])

#for ss in slope: 
    
slope.remove(0)
slope.remove(0)


fig1,ax1 = plt.subplots()
plotfunction(slope,timelist, ' ENSCI 2.0%-0.1B ', 'green')
#plt.show()

# ENSCI 2.0%-0.1B ADX
slope = [0]*size; intercept = [0]*size; r_value = [0]*size; p_value = [0]*size;  std_err = [0]*size

for tt2 in range(0,nt):
    if( (minTbin[tt2] == 0) & (maxTbin[tt2] == 500) ): continue
    if( (minTbin[tt2] == 1500) & (maxTbin[tt2] == 2000) ): continue

    filttime = (dfENSCI_201adx.Tsim > minTbin[tt2]) & (dfENSCI_201adx.Tsim <= maxTbin[tt2])
    dfENSCI_201adx_tbin[tt2] = dfENSCI_201adx[filttime]

    opm_sim[tt2] = np.asarray(dfENSCI_201adx_tbin[tt2].PO3_OPM)
    po3_sim[tt2] = np.asarray(dfENSCI_201adx_tbin[tt2].PO3)
    #print('tt2', tt2, minTbin[tt2], maxTbin[tt2], opm_sim[tt].mean(), po3_sim[tt2].mean())

    slope[tt2], intercept[tt2], r_value[tt2], p_value[tt2], std_err[tt2] = stats.linregress(opm_sim[tt2],po3_sim[tt2])
    #po3_fit[tt2] = slope[tt2] * opm_sim[tt2] + intercept[tt2]

slope.remove(0)
slope.remove(0)

fig2,ax2 = plt.subplots()
plotfunction(slope,timelist, ' ENSCI 2.0%-0.1B ADX', 'red')
#plt.show()


# ENSCI 2.0%-0.1B noADX
slope = [0]*size; intercept = [0]*size; r_value = [0]*size; p_value = [0]*size;  std_err = [0]*size

for tt3 in range(0,nt):
    if( (minTbin[tt3] == 0) & (maxTbin[tt3] == 500) ): continue
    if( (minTbin[tt3] == 1500) & (maxTbin[tt3] == 2000) ): continue

    filttime = (dfENSCI_201noadx.Tsim > minTbin[tt3]) & (dfENSCI_201noadx.Tsim <= maxTbin[tt3])
    dfENSCI_201noadx_tbin[tt3] = dfENSCI_201noadx[filttime]

    opm_sim[tt3] = np.asarray(dfENSCI_201noadx_tbin[tt3].PO3_OPM)
    po3_sim[tt3] = np.asarray(dfENSCI_201noadx_tbin[tt3].PO3)
    #print('tt3', tt3, minTbin[tt3], maxTbin[tt3], opm_sim[tt].mean(), po3_sim[tt3].mean())

    slope[tt3], intercept[tt3], r_value[tt3], p_value[tt3], std_err[tt3] = stats.linregress(opm_sim[tt3],po3_sim[tt3])
    #po3_fit[tt2] = slope[tt2] * opm_sim[tt2] + intercept[tt2]

slope.remove(0)
slope.remove(0)

fig3,ax3 = plt.subplots()
plotfunction(slope,timelist, ' ENSCI 2.0%-0.1B noADX', 'red')
plt.show()







