# Functions used for the analysis of Josie17 simulation data
# 16/01/2019

import pandas as pd
import numpy as np
import re
import glob
import math
from math import log
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.offsetbox import AnchoredText

# function to calculate the mean of a column ignoring the -99 values
def meanfunction(dff,Xf):

    #dft = dff
    #dft.X = dff.
    tmp1 = dff.drop_duplicates(['Sim', 'Team'])
    tmp2 = tmp1[tmp1[Xf] != -99.99]
    fmean = tmp2[Xf].mean()
    fstd = tmp2[Xf].std()

    return (str(round(fmean,2)) +' ± '+ str(round(fstd,2)))
    
    

# the function implemented from Roeland's code
def Calc_average_profile(dataframe, ybin, xcolumn):
    dft = dataframe

    if xcolumn == 'ADif_PO3S' :
        dft.PFcor = dataframe.ADif_PO3S
        xra = [-3,3]
        xtitle = 'Sonde - OPM O!D3!N Difference (mPa)'
    if xcolumn == 'RDif_PO3S' :
        dft['PFcor'] = dataframe['RDif_PO3S'].astype('float')
        xra = [-3,3]
        xtitle='Sonde - OPM O!D3!N Difference (%)'
    if xcolumn == 'PO3' :
        dft.PFcor = dataframe.PO3
        xra=[-1,30]
        xtitle='Ozone partial pressure (mPa)'
    if  xcolumn == 'PO3_OPM' :
        dft.PFcor = dataframe.PO3_OPM
        xra=[-1,30]
        xtitle='Ozone partial pressure (mPa)'

    ybin0 = ybin
    ymax = 7000.0
    ymin = 0.0
    fac = 1.0
    n = math.floor(ymax/ybin0)
    ystart = 0.0
    Xgrid = [-9999.0] * n
    Xsigma = [-9999.0] * n
    Ygrid = [-9999.0] * n
    Ysigma = [-9999.0] * n
    m = len(dataframe)
    Xarray = []
    Xarray2 = []

    for i in range(n):
        dftmp1 = pd.DataFrame()
        dfgrid = pd.DataFrame()

        grid_min = ystart + fac *float(ybin0) * float(i)
        grid_max = ystart + fac *float(ybin0) * float(i+1)
        Ygrid[i] = (grid_min + grid_max)/ 2.0
        #print(i, ' gridmin: ', grid_min, ' gridmax: ', grid_max )

        filta = dft.Tsim >= grid_min
        filtb = dft.Tsim < grid_max
        filter1 = filta & filtb
        dftmp1['X'] = dft[filter1].PFcor
        #print(i, 'len of dftmp1 ', len(dftmp1))

        filtnull = dftmp1.X > -9999.0
        filtfin = np.isfinite(dftmp1.X)
        filterall = filtnull & filtfin
        dfgrid['X'] = dftmp1[filterall].X

        #print('len of dfgrid ', len(dfgrid))
        #print(i, dfgrid.X)
        Xgrid[i] = np.mean(dfgrid.X)
        Xsigma[i] = np.std(dfgrid.X)
        #print(i , ' X ' ,Xgrid[i], " Xerr ", Xsigma[i])

    return Xgrid, Xsigma, Ygrid


# Calculate the relative difference between sonde and OPM

def Calc_RDif(profO3X, profOPMX, profO3Xerr, dimension):

    R1v = [-9999.9] * dimension
    R1verr = [-9999.9] * dimension

    for i in range(dimension):
        R1v[i] = 100 * (profO3X[i] - profOPMX[i])/ profOPMX[i]
        R1verr[i] =  100 * (profO3Xerr[i]/profOPMX[i])

    return R1v, R1verr


# Plots the two pllots of 2 different data profiles using the absolute difference and relative difference

def Plot_4profile_plots(prof1_X, prof1_Xerr, prof2_X,  prof2_Xerr, prof3_X, prof3_Xerr, prof4_X,  prof4_Xerr, Y,  xra, yra, xtit, ytit, mtitle,  plotname, keyword ):

    fig,ax = plt.subplots()
    plt.xlim(xra)
    plt.ylim(yra)
    plt.xlabel(xtit)
    plt.ylabel(ytit)
    plt.title(mtitle)

    plt.yticks(np.arange(0, 7001, 1000))
    ax.tick_params(axis='both', which='both', direction='in')
    ax.yaxis.set_ticks_position('both')
    ax.xaxis.set_ticks_position('both')

    ax.yaxis.set_minor_locator(AutoMinorLocator(10))
    ax.xaxis.set_minor_locator(AutoMinorLocator(10))

    if(keyword == '1234'):
    	ax.errorbar(prof1_X, Y,  xerr = prof1_Xerr, label="Participant 1",   color='red', linewidth = 1.5, elinewidth = 0.5, capsize = 1, capthick=0.5, linestyle='--')
    	ax.errorbar(prof2_X, Y,  xerr = prof2_Xerr, label="Participant 2",   color='green', linewidth = 1.5, elinewidth = 0.5, capsize = 1, capthick=0.5, linestyle='--')
    	ax.errorbar(prof3_X, Y,  xerr = prof3_Xerr, label="Participant 3",   color='blue', linewidth = 1.5, elinewidth = 0.5, capsize = 1, capthick=0.5, linestyle='--')
    	ax.errorbar(prof4_X, Y,  xerr = prof4_Xerr, label="Participant 4",   color='goldenrod', linewidth = 1.5, elinewidth = 0.5, capsize = 1, capthick=0.5, linestyle='--')

    if(keyword == '5678'):
    	ax.errorbar(prof1_X, Y,  xerr = prof1_Xerr, label="Participant 5",   color='crimson', linewidth = 1.5, elinewidth = 0.5, capsize = 1, capthick=0.5, linestyle='--')
    	ax.errorbar(prof2_X, Y,  xerr = prof2_Xerr, label="Participant 6",   color='limegreen', linewidth = 1.5, elinewidth = 0.5, capsize = 1, capthick=0.5, linestyle='--')
    	ax.errorbar(prof3_X, Y,  xerr = prof3_Xerr, label="Participant 7",   color='dodgerblue', linewidth = 1.5, elinewidth = 0.5, capsize = 1, capthick=0.5, linestyle='--')
    	ax.errorbar(prof4_X, Y,  xerr = prof4_Xerr, label="Participant 8",   color='darkorange', linewidth = 1.5, elinewidth = 0.5, capsize = 1, capthick=0.5, linestyle='--')

    #ax.plot(prof1_X, Y, label="Participant 1", color = 'green')
    #ax.plot(prof2_X, Y, label="Participant 2", color = 'cyan')
    #ax.plot(prof3_X, Y, label="Participant 3", color = 'tomato')
    #ax.plot(prof4_X, Y, label="Participant 4", color = 'blue')
    ax.legend(loc='lower right', frameon=True, fontsize = 'small')

    plt.savefig('/home/poyraden/Josie18/Plots/'+ plotname +'.pdf')
    plt.savefig('/home/poyraden/Josie18/Plots/'+ plotname +'.eps')


def Plot_compare_profile_plots(prof1_X, prof1_Xerr, prof2_X,  prof2_Xerr, Y, xra, xtit, ytit, filtx, filty,  totO31value, totO32value, prof1_nodup, prof2_nodup, plotname):   

    n1 = len(prof1_nodup)
    n2 = len(prof2_nodup)

    yra = [0,7000]
    labelx = filtx + ' ( n =' + str(n1) + ')'
    labely = filty + '( n =' + str(n2) + ')'

    text1 = 'tot O3 ratio: ' + str(round(totO31value,2))
    text2 = 'tot O3 ratio: ' + str(round(totO32value, 2))

    fig,ax = plt.subplots()
    plt.xlim(xra)
    plt.ylim(yra)
    plt.xlabel(xtit)
    plt.ylabel(ytit)

	# reference line
    ax.axvline(x=0, color='grey', linestyle='--')

    ax.errorbar(prof1_X, Y, xerr = prof1_Xerr, label = labelx,  color='black', linewidth = 1, elinewidth = 0.5, capsize = 1, capthick=0.5)
    ax.errorbar(prof2_X, Y, xerr = prof2_Xerr, label = labely, color='red', linewidth = 1, elinewidth = 0.5, capsize = 1, capthick=0.5)

    plt.yticks(np.arange(0, 7001, 1000))
    ax.tick_params(axis='both', which='both', direction='in')
    ax.yaxis.set_ticks_position('both')
    ax.xaxis.set_ticks_position('both')

    ax.yaxis.set_minor_locator(AutoMinorLocator(10))
    ax.xaxis.set_minor_locator(AutoMinorLocator(10))
    ax.legend(loc='lower right', frameon=True, fontsize = 'small')


    t1 = ax.text(0.05,0.09, text1,  color='black', transform=ax.transAxes)
    t2 = ax.text(0.05,0.02, text2,  color='red', transform=ax.transAxes)


    plt.savefig('/home/poyraden/Josie18/Plots/'+ plotname +'.pdf')
    plt.savefig('/home/poyraden/Josie18/Plots/'+ plotname +'.eps')


################

def Plot_compare_profile_plots_updated(prof1_X, prof1_Xerr, prof2_X,  prof2_Xerr, Y, xra, mtit, xtit, ytit, filtx, filty,  totO31value, totO32value, prof1_nodup, prof2_nodup, plotname):   

    n1 = len(prof1_nodup)
    n2 = len(prof2_nodup)
    yra = [0,20]

#    if keyword == 'PO3'
#    yra = [0,30]
    labelx = filtx + ' ( n =' + str(n1) + ')'
    labely = filty + '( n =' + str(n2) + ')'

    text1 = 'tot O3 ratio: ' + str(round(totO31value,2))
    text2 = 'tot O3 ratio: ' + str(round(totO32value, 2))

    fig,ax = plt.subplots()
    plt.xlim(xra)
    plt.ylim(yra)
    plt.title(mtit)
    plt.xlabel(xtit)
    plt.ylabel(ytit)
    plt.grid(True)

	# reference line
    ax.axvline(x=0, color='grey', linestyle='--')

    ax.errorbar(prof1_X, Y, xerr = prof1_Xerr, label = labelx,  color='black', linewidth = 1, elinewidth = 0.5, capsize = 1, capthick=0.5)
    ax.errorbar(prof2_X, Y, xerr = prof2_Xerr, label = labely, color='red', linewidth = 1, elinewidth = 0.5, capsize = 1, capthick=0.5)

    #plt.yticks(np.arange(0, 7001, 1000))
    ax.tick_params(axis='both', which='both', direction='in')
    ax.yaxis.set_ticks_position('both')
    ax.xaxis.set_ticks_position('both')

    ax.yaxis.set_minor_locator(AutoMinorLocator(10))
    ax.xaxis.set_minor_locator(AutoMinorLocator(10))
    ax.legend(loc='lower right', frameon=True, fontsize = 'small')


    t1 = ax.text(0.05,0.09, text1,  color='black', transform=ax.transAxes)
    t2 = ax.text(0.05,0.02, text2,  color='red', transform=ax.transAxes)


    plt.savefig('/home/poyraden/Josie18/Plots/ADif_RDif/TestTest/'+ plotname +'.pdf')
    plt.savefig('/home/poyraden/Josie18/Plots/ADif_RDif/TestTest/'+ plotname +'.eps')
