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

def plotfunction(ik, pltitle):
    plt.xlim(0,25)
    plt.ylim(0,25)
    plt.xlabel('OPM (mPa)')
    plt.ylabel(r'PO3 (mPa)')
    plt.title(pltitle)
    plt.grid(True)
    plt.scatter(opm_sim[ik],po3_sim[ik], c = 'red', s=0.5)
    plt.plot( opm_sim[ik], po3_fit[ik],'-.',color = 'red',  label = label_sim[ik], linewidth = 2.0)
    plt.scatter(opm_sim[ik+1],po3_sim[ik+1], c = 'blue', s=0.5)
    plt.plot( opm_sim[ik+1], po3_fit[ik+1],'-.',color = 'blue',  label = label_sim[ik+1], linewidth = 2.0)
    plt.scatter(opm_sim[ik+2],po3_sim[ik+2], c = 'green', s=0.5)
    plt.plot( opm_sim[ik+2], po3_fit[ik+2],'-.',color = 'green',  label = label_sim[ik+2], linewidth = 2.0)
    plt.scatter(opm_sim[ik+3],po3_sim[ik+3], c = 'gold', s=0.5)
    plt.plot( opm_sim[ik+3], po3_fit[ik+3],'-.',color = 'gold',  label = label_sim[ik+3], linewidth = 2.0)
    plt.legend(loc='lower right', frameon=True, fontsize = 'small')
        



df = pd.read_csv("/home/poyraden/Josie18/Josie18_Data.csv", low_memory=False)
dfmd = pd.read_csv("/home/poyraden/Josie18/Josie18_MetaData.csv", low_memory=False)

minOPM = 0.5; minPO3 = 0.5; maxOPM = 30; maxPO3 = 30; minT = 0; maxT = 6400;


size =  len(dfmd)
#metadata
Year = []; Sim = []; Team = []; ENSCI = []; Sol = []; Buf = []; ADX = []
#data
PO3 = []; OPM = []; Tsim = []
keylist = []; filterlist = []
opm_sim = []; po3_sim = []
label_sim = []; title = []
slope = [0]*size; intercept = [0]*size; r_value = [0]*size; p_value = [0]*size;  std_err = [0]*size
po3_fit = [0]*size ; text_fit = [' '] * size; t_fit = [' ']*size

slope_0910 = []; intercept_0910 = []; std_err_0910 = []; 
slope_0910adx = []; intercept_0910adx = []; std_err_0910adx = []; 
slope_0910noadx = []; intercept_0910noadx = []; std_err_0910noadx = []; 
slope_18 = []; intercept_18 = []; std_err_18 = []; 
slope_18adx = []; intercept_18adx = []; std_err_18adx = [];  
slope_18noadx = []; intercept_18noadx = []; std_err_18noadx = [];
slope_all = []; intercept_all = []; std_err_all = [];  
slope_adx = []; intercept_adx = []; std_err_adx = [];  
slope_noadx = []; intercept_noadx = []; std_err_noadx = [];  



for i in range(len(dfmd)):
    #if (dfmd.iloc[i]['Sim'] != 196):
    Year.append(dfmd.iloc[i]['Year'])
    Sim.append(dfmd.iloc[i]['Sim'])
    Team .append(dfmd.iloc[i]['Team'])   
    ENSCI.append(dfmd.iloc[i]['ENSCI'])
    Sol.append(dfmd.iloc[i]['Sol'])
    Buf.append(dfmd.iloc[i]['Buf'])
    ADX.append(dfmd.iloc[i]['ADX'])
    
df_sim = {}

for s in range(len(Year)):
    filt1 = (df.Sim == Sim[s]) & (df.Year == Year[s]) & (df.Team == Team[s]) & (df.ENSCI == ENSCI[s]) & (df.Sol == Sol[s]) & (df.Buf == Buf[s]) & (df.ADX == ADX[s])
    filt2 = (df.PO3_OPM > minOPM) & (df.PO3 > minPO3) & (df.PO3_OPM < maxOPM ) & (df.Tsim < maxT)
    filt = filt1 & filt2
    filterlist.append(filt)
    
    df_sim[s] = df[filterlist[s]] 
    opm_sim.append(np.asarray(df_sim[s].PO3_OPM))
    po3_sim.append(np.asarray(df_sim[s].PO3))
    
    ensci = 'ENSCI-' if ENSCI[s] == 1 else 'SPC-'
    adx = '+ADX' if ADX[s] ==1 else ''
    #label_sim.append('Sim' + str(Sim[s]) + ' ' + ensci + str(Team[s]) + ' ' + str(Sol[s]) + '%+' + str(Buf[s]) + 'B' + adx)
    
    slope[s], intercept[s], r_value[s], p_value[s], std_err[s] = stats.linregress(opm_sim[s],po3_sim[s])
    po3_fit[s] = slope[s] * opm_sim[s] + intercept[s]
    text_fit[s] =  'Slope: ' + str(round(slope[s],2)) +', Intercept: '+ str(round(intercept[s],2)) + ' err:' + str(round(std_err[s],4))
    label_sim.append(str(Sim[s]) + ' ' + ensci + str(Team[s]) + ' ' + str(Sol[s]) + '%+' + str(Buf[s]) + 'B' + adx + ' Slope:' + str(round(slope[s],2)))
                     #+','+ str(round(intercept[s],2)) + ',' + str(round(std_err[s],4))  )
    slope_all.append(slope[s]); intercept_all.append(intercept[s]); std_err_all.append(std_err[s])
    title.append('Sim' + str(Sim[s]))

    print(Sim[s], slope[s])
    
    if ADX[s] == 1:
            slope_adx.append(slope[s]); intercept_adx.append(intercept[s]); std_err_adx.append(std_err[s]) 
    if ADX[s] == 0:
            slope_noadx.append(slope[s]); intercept_noadx.append(intercept[s]); std_err_noadx.append(std_err[s]) 
    if (Year[s] == 2009) | (Year[s] == 2010):
        slope_0910.append(slope[s]); intercept_0910.append(intercept[s]); std_err_0910.append(std_err[s])
        if ADX[s] == 1:
            slope_0910adx.append(slope[s]); intercept_0910adx.append(intercept[s]); std_err_0910adx.append(std_err[s]) 
        if ADX[s] == 0:
            slope_0910noadx.append(slope[s]); intercept_0910noadx.append(intercept[s]); std_err_0910noadx.append(std_err[s]) 
    if (Year[s] == 2018):
        slope_18.append(slope[s]); intercept_18.append(intercept[s]); std_err_18.append(std_err[s])
        if ADX[s] == 1:
            slope_18adx.append(slope[s]); intercept_18adx.append(intercept[s]); std_err_18adx.append(std_err[s]) 
        if ADX[s] == 0:
            slope_18noadx.append(slope[s]); intercept_18noadx.append(intercept[s]); std_err_18noadx.append(std_err[s]) 


print('2009-2010: Slope = ' + str(round(np.mean(slope_0910),3)) + '±'+ str(round(np.std(slope_0910),3))+ ' Intercept: ' +  str(round(np.mean(intercept_0910),3)) + '±'+   str(round(np.std(intercept_0910),3)) + ' Err: ' +  str(round(np.mean(std_err_0910),4)) + '±'+  str(round(np.std(std_err_0910),4)) + ' Size ' + str(len(slope_0910)) )
print('2009-2010 ADX : Slope = ' + str(round(np.mean(slope_0910adx),3)) + '±'+ str(round(np.std(slope_0910adx),3))+ ' Intercept: ' +  str(round(np.mean(intercept_0910adx),3)) + '±'+   str(round(np.std(intercept_0910adx),3)) + ' Err: ' +  str(round(np.mean(std_err_0910adx),4)) + '±'+  str(round(np.std(std_err_0910adx),4))+ ' Size ' + str(len(slope_0910adx)) )
print('2009-2010 noADX : Slope = ' + str(round(np.mean(slope_0910noadx),3)) + '±'+ str(round(np.std(slope_0910noadx),3))+ ' Intercept: ' +  str(round(np.mean(intercept_0910noadx),3)) + '±'+   str(round(np.std(intercept_0910noadx),3)) + ' Err: ' +  str(round(np.mean(std_err_0910noadx),4)) + '±'+  str(round(np.std(std_err_0910noadx),4))+ ' Size ' + str(len(slope_0910noadx)) )

print('2018: Slope = ' + str(round(np.mean(slope_18),3)) + '±'+ str(round(np.std(slope_18),3))+ ' Intercept: ' +  str(round(np.mean(intercept_18),3)) + '±'+   str(round(np.std(intercept_18),3)) + ' Err: ' +  str(round(np.mean(std_err_18),4)) + '±'+  str(round(np.std(std_err_18),4)) + ' Size ' + str(len(slope_18)) )
print('2018 ADX : Slope = ' + str(round(np.mean(slope_18adx),3)) + '±'+ str(round(np.std(slope_18adx),3))+ ' Intercept: ' +  str(round(np.mean(intercept_18adx),3)) + '±'+   str(round(np.std(intercept_18adx),3)) + ' Err: ' +  str(round(np.mean(std_err_18adx),4)) + '±'+  str(round(np.std(std_err_18adx),4)) +  ' Size ' + str(len(slope_18adx)) )
print('2018 noADX : Slope = ' + str(round(np.mean(slope_18noadx),3)) + '±'+ str(round(np.std(slope_18noadx),3))+ ' Intercept: ' +  str(round(np.mean(intercept_18noadx),3)) + '±'+   str(round(np.std(intercept_18noadx),3)) + ' Err: ' +  str(round(np.mean(std_err_18noadx),4)) + '±'+  str(round(np.std(std_err_18noadx),4))+ ' Size ' + str(len(slope_18noadx)) )

print('All: Slope = ' + str(round(np.mean(slope_all),3)) + '±'+ str(round(np.std(slope_all),3))+ ' Intercept: ' +  str(round(np.mean(intercept_all),3)) + '±'+   str(round(np.std(intercept_all),3)) + ' Err: ' +  str(round(np.mean(std_err_all),4)) + '±'+  str(round(np.std(std_err_all),4)) + ' Size ' + str(len(slope_all)) )
print('All ADX : Slope = ' + str(round(np.mean(slope_adx),3)) + '±'+ str(round(np.std(slope_adx),3))+ ' Intercept: ' +  str(round(np.mean(intercept_adx),3)) + '±'+   str(round(np.std(intercept_adx),3)) + ' Err: ' +  str(round(np.mean(std_err_adx),4)) + '±'+  str(round(np.std(std_err_adx),4)) +  ' Size ' + str(len(slope_adx)) )
print('All noADX : Slope = ' + str(round(np.mean(slope_noadx),3)) + '±'+ str(round(np.std(slope_noadx),3))+ ' Intercept: ' +  str(round(np.mean(intercept_noadx),3)) + '±'+   str(round(np.std(intercept_noadx),3)) + ' Err: ' +  str(round(np.mean(std_err_noadx),4)) + '±'+  str(round(np.std(std_err_noadx),4))+ ' Size ' + str(len(slope_noadx)) )


colorlist = ['dodgerblue', 'blue', 'cyan', 'orange' , 'orangered', 'red', 'maroon',  'darkcyan', 'green', 'lime',  'greenyellow', 'seagreen', 'orchid', 'purple', 'magenta', 'grey', 'olive','pink', 'navy', 'salmon',  'palegreen','brown','teal','chocolate']

fig,ax = plt.subplots()
plt.xlim(0,30)
plt.ylim(0,30)
plt.xlabel('OPM (mPa)')
plt.ylabel(r'PO3 (mPa)')
plt.title('PO3 vs  OPM ')
plt.grid(True)

#plt.yticks(np.arange(0, 7001, 1000))
ax.tick_params(axis='both', which='both', direction='in')
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')

ax.yaxis.set_minor_locator(AutoMinorLocator(10))
ax.xaxis.set_minor_locator(AutoMinorLocator(10))

y_range = [0.25, 0.175, 0.10, 0.05]

ini = 44;
for p in range(24):
    plt.scatter(opm_sim[p],po3_sim[p], c = colorlist[p], s=0.5)
    plt.plot( opm_sim[p], po3_fit[p],'-.',color = colorlist[p],  label = label_sim[p], linewidth = 2.0)
    # plt.scatter(opm_sim[p],po3_sim[p], s=0.5)
    # plt.plot( opm_sim[p], po3_fit[p],'-.',  label = label_sim[p], linewidth = 2.0)
    
    ax.legend(loc='lower right', frameon=True, fontsize = 'small')
    #print(ini, p)
    # plt.savefig('/home/poyraden/Josie18/Plots/Sonde_OPM_wTimeCut/' + str(Sim[p]) + '.pdf')
    # plt.savefig('/home/poyraden/Josie18/Plots/Sonde_OPM_wTimeCut/' + str(Sim[p]) + '.eps')


    
#plt.savefig('/home/poyraden/Josie18/Plots/Sonde_OPM_wTimeCut/Sim0910_opmless13.pdf')
#plt.savefig('/home/poyraden/Josie18/Plots/Sonde_OPM_wTimeCut/Sim0910_opmless13.eps')


fig2,ax2 = plt.subplots()
plt.xlim(0,30)
plt.ylim(0,30)
plt.xlabel('OPM (mPa)')
plt.ylabel(r'PO3 (mPa)')
plt.title('PO3 vs  OPM ')
plt.grid(True)

#plt.yticks(np.arange(0, 7001, 1000))
ax2.tick_params(axis='both', which='both', direction='in')
ax2.yaxis.set_ticks_position('both')
ax2.xaxis.set_ticks_position('both')

ax2.yaxis.set_minor_locator(AutoMinorLocator(10))
ax2.xaxis.set_minor_locator(AutoMinorLocator(10))

for p in range(24,48):
    plt.scatter(opm_sim[p],po3_sim[p],c = colorlist[p-24], s=0.5)
    plt.plot( opm_sim[p], po3_fit[p],'-.', color= colorlist[p-24], label = label_sim[p], linewidth = 2.0)
    ax2.legend(loc='lower right', frameon=True, fontsize = 'small')
    #t_fit[p] =  ax.text(0.45,y_range[p], text_fit[p] , transform=ax.transAxes)
    #print(Sim[p], text_fit[p])
    
#plt.savefig('/home/poyraden/Josie18/Plots/Sonde_OPM_wTimeCut/Sim18_opmless13.pdf')
#plt.savefig('/home/poyraden/Josie18/Plots/Sonde_OPM_wTimeCut/Sim18.eps')

plt.show()

############
## array of plots test

figs,axs = plt.subplots(2,3)

y_range = [0.25, 0.175, 0.10, 0.05]

ini = 44;
for p in range(0,28,4):
    print('p', p)
    if (p == 0):
        plt.subplot(231)
        plotfunction(p, title[p])
    if (p == 4):
        plt.subplot(232)
        plotfunction(p, title[p])
    if (p == 8):
        plt.subplot(233)
        plotfunction(p, title[p])
    if (p == 12):
        plt.subplot(234)
        plotfunction(p, title[p])
    if (p == 16):
        plt.subplot(235)
        plotfunction(p, title[p])       
    if (p == 20):
        plt.subplot(236)
        plotfunction(p, title[p])    

plt.show()

figs2,axs2 = plt.subplots(2,3)


for p in range(24,48,4):
    print('p', p)
    if (p == 24):
        plt.subplot(231)
        plotfunction(p, title[p])
    if (p == 28):
        plt.subplot(232)
        plotfunction(p, title[p])
    if (p == 32):
        plt.subplot(233)
        plotfunction(p, title[p])
    if (p == 36):
        plt.subplot(234)
        plotfunction(p, title[p])
    if (p == 40):
        plt.subplot(235)
        plotfunction(p, title[p])       
    if (p == 44):
        plt.subplot(236)
        plotfunction(p, title[p]) 

plt.show()
