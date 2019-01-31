import pandas as pd
import numpy as np
import re
import glob
import math
from math import log
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.offsetbox import AnchoredText

from Josie18_Functions import Make_5ProfilePlots
from Josie18_Functions import Make_4ProfilePlots

df = pd.read_csv("/home/poyraden/Josie18/Josie18_Data.csv", low_memory=False)

df_sim = df.drop_duplicates(['Sim']) 
listSim = df_sim['Sim'].tolist()

df_team = df.drop_duplicates(['Team']) 
listTeam = df_team['Team'].tolist()

size = len(listTeam) * len(listSim)

PO3 = [0]*size; IM = [0]*size; OPM = [0]*size;   Time = [0]*size; Tinlet = [0]*size;  

dataframe_collection = {}
opm_collection = {}
keylist = []
filterlist = []
#plotstr = []
filtsim = []
labels = []
#titlestr = []

dft = df.drop_duplicates(['Sim','Team'])
dfmd = dft.reset_index(drop=True)


for s in listSim:
    #filts = dfsim.Sim == s
    
    #print(s)
    #filtsim.append(filts)
    for t in range(0,4):
        #plotstr.append("Plot_Sim" + str(s))
        filta = df.Sim == s
        filtb = df.Team == t+1
        filterlist.append(filta & filtb)



for simitem in range(0,size):
    dataframe_collection[simitem] = df[filterlist[simitem]]
    PO3[simitem] = dataframe_collection[simitem].PO3.tolist()
    IM[simitem] = dataframe_collection[simitem].IM.tolist()
    Tinlet[simitem] = round((dataframe_collection[simitem].Tinlet - 273.15),3).tolist()
    Time[simitem] = dataframe_collection[simitem].Tsim.tolist()
    OPM[simitem] =  dataframe_collection[simitem].PO3_OPM.tolist()
    print(simitem, len(Time[simitem]), len(OPM[simitem]))

    #print(dfmd.loc[simitem,'Sim'])
    sim = dfmd.loc[simitem,'Sim']; team =  dfmd.loc[simitem,'Team']; boolensci =  dfmd.loc[simitem,'ENSCI']; sol =  dfmd.loc[simitem,'Sol']
    buf =  dfmd.loc[simitem,'Buf'];  booladx = dfmd.loc[simitem,'ADX']
    ensci = 'ENSCI' if boolensci == 1 else 'SPC'
    adx = 'ADX' if booladx ==1 else 'NoADX'
    #titlestr.append('Simulation '+str(s))
    labels.append(ensci + str(sol) + ' %+ ' + str(buf) + 'B + ' + adx)


plotlist = {137:0, 136:4, 150:8, 151:12, 198:16, 194:20, 195:24, 145:28, 196:32, 146:36, 199:40, 197:44}

for s in plotlist:
    titlestr = 'Simulation ' + str(s)
    plotstrpo3 = 'Simulation_PO3_' + str(s)
    plotstrim = 'Simulation_IM_' + str(s)

    i = plotlist[s]
    #print(plotstr[i])
    print(s, plotlist[s], i)
    
    Make_5ProfilePlots(Time[i], Time[i+1], Time[i+2], Time[i+3], Time[i], PO3[i], PO3[i+1], PO3[i+2], PO3[i+3], OPM[i], [0,10000], [0,30], labels[i],labels[i+1],labels[i+2],labels[i+3],'OPM', 'Simulation Time(sec.)', 'O3 Partial Pressure', titlestr, plotstrpo3, 0)
    Make_4ProfilePlots(Time[i], Time[i+1], Time[i+2], Time[i+3], IM[i], IM[i+1], IM[i+2], IM[i+3], [0,10000], [0.01,10], labels[i],labels[i+1],labels[i+2],labels[i+3], 'Simulation Time(sec.)', r'ECC Current ($\mu$A)', titlestr, plotstrim,1)
  
