import pandas as pd
import numpy as np
import re
import glob
import math
from math import log
from scipy.stats import iqr
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.offsetbox import AnchoredText


def Make_6ProfilePlots(X1, X2, X3, X4,X5,X6, Y1, Y2, Y3, Y4, Y5,Y6, xra, yra, label1, label2, label3, label4,label5,  xtit, ytit, mtit, plottit,keylog):
    
    fig,ax = plt.subplots()
    plt.xlim(xra)
    plt.ylim(yra)
    plt.xlabel(xtit)
    plt.ylabel(ytit)
    plt.title(mtit)
    plt.grid(True)
    
    #plt.yticks(np.arange(0, 7001, 1000))
    ax.tick_params(axis='both', which='both', direction='in')
    ax.yaxis.set_ticks_position('both')
    ax.xaxis.set_ticks_position('both')

    ax.yaxis.set_minor_locator(AutoMinorLocator(10))
    ax.xaxis.set_minor_locator(AutoMinorLocator(10))
    if keylog == 0:
        plt.plot(X1, Y1, label=label1, color='green', linewidth = 1.0)
        plt.plot(X2, Y2, label=label2, color='red', linewidth = 1.0)
        plt.plot(X3, Y3, label=label3, color='blue', linewidth = 1.0)
        plt.plot(X4, Y4, label=label4, color='magenta', linewidth = 1.0,  linestyle = '--')
        plt.plot(X5, Y5, label=label5, color='cyan', linewidth = 1.0, linestyle = '--')
    if keylog ==1:
        plt.semilogy(X1, Y1, label=label1, color='green', linewidth = 1.0)
        plt.semilogy(X2, Y2, label=label2, color='red', linewidth = 1.0)
        plt.semilogy(X3, Y3, label=label3, color='blue', linewidth = 1.0)
        plt.semilogy(X4, Y4, label=label4, color='magenta', linewidth = 1.0,  linestyle = '--')
        plt.semilogy(X5, Y5, label=label5, color='cyan', linewidth = 1.0, linestyle = '--')
        
    
    ax.legend(loc='upper left', frameon=True, fontsize = 'small')
    #ax.legend( frameon=True, fontsize = 'small')
    plt.savefig('/home/poyraden/Josie18/Plots/'+ plottit +'.eps')
    plt.savefig('/home/poyraden/Josie18/Plots/'+ plottit +'.pdf')

    plt.show()

def Make_5ProfilePlots(X1, X2, X3, X4,X5, Y1, Y2, Y3, Y4, Y5, xra, yra, label1, label2, label3, label4,label5,  xtit, ytit, mtit, plottit,keylog):
    
    fig,ax = plt.subplots()
    plt.xlim(xra)
    plt.ylim(yra)
    plt.xlabel(xtit)
    plt.ylabel(ytit)
    plt.title(mtit)
    plt.grid(True)
    
    #plt.yticks(np.arange(0, 7001, 1000))
    ax.tick_params(axis='both', which='both', direction='in')
    ax.yaxis.set_ticks_position('both')
    ax.xaxis.set_ticks_position('both')

    ax.yaxis.set_minor_locator(AutoMinorLocator(10))
    ax.xaxis.set_minor_locator(AutoMinorLocator(10))
    if keylog == 0:
        plt.plot(X1, Y1, label=label1, color='green', linewidth = 1.0)
        plt.plot(X2, Y2, label=label2, color='red', linewidth = 1.0)
        plt.plot(X3, Y3, label=label3, color='blue', linewidth = 1.0)
        plt.plot(X4, Y4, label=label4, color='magenta', linewidth = 1.0,  linestyle = '--')
        plt.plot(X5, Y5, label=label5, color='cyan', linewidth = 1.0, linestyle = '--')
    if keylog ==1:
        plt.semilogy(X1, Y1, label=label1, color='green', linewidth = 1.0)
        plt.semilogy(X2, Y2, label=label2, color='red', linewidth = 1.0)
        plt.semilogy(X3, Y3, label=label3, color='blue', linewidth = 1.0)
        plt.semilogy(X4, Y4, label=label4, color='magenta', linewidth = 1.0,  linestyle = '--')
        plt.semilogy(X5, Y5, label=label5, color='cyan', linewidth = 1.0, linestyle = '--')
        
    
    ax.legend(loc='upper left', frameon=True, fontsize = 'small')
    #ax.legend( frameon=True, fontsize = 'small')
    plt.savefig('/home/poyraden/Josie18/Plots/'+ plottit +'.eps')
    plt.savefig('/home/poyraden/Josie18/Plots/'+ plottit +'.pdf')
   
    plt.show()

def Make_4ProfilePlots(X1, X2, X3, X4, Y1, Y2, Y3, Y4, xra, yra, label1, label2, label3, label4, xtit, ytit, mtit, plottit,keylog):
    
    fig,ax = plt.subplots()
    plt.xlim(xra)
    plt.ylim(yra)
    plt.xlabel(xtit)
    plt.ylabel(ytit)
    plt.title(mtit)
    plt.grid(True)
    
    #plt.yticks(np.arange(0, 7001, 1000))
    ax.tick_params(axis='both', which='both', direction='in')
    ax.yaxis.set_ticks_position('both')
    ax.xaxis.set_ticks_position('both')

    ax.yaxis.set_minor_locator(AutoMinorLocator(10))
    ax.xaxis.set_minor_locator(AutoMinorLocator(10))
    if keylog == 0:
        plt.plot(X1, Y1, label=label1, color='black', linewidth = 0.5)
        plt.plot(X2, Y2, label=label2, color='red', linewidth = 0.5)
        plt.plot(X3, Y3, label=label3, color='blue', linewidth = 0.5)
        plt.plot(X4, Y4, label=label4, color='green', linewidth = 0.5)
        #plt.plot(Xopm, Yopm, label='OPM', color='cyan', linewidth = 1.0, linestyle = '--')
    if keylog ==1:
        plt.semilogy(X1, Y1, label=label1, color='black', linewidth = 0.5)
        plt.semilogy(X2, Y2, label=label2, color='red', linewidth = 0.5)
        plt.semilogy(X3, Y3, label=label3, color='blue', linewidth = 0.5)
        plt.semilogy(X4, Y4, label=label4, color='green', linewidth = 0.5)
        #plt.semilogy(Xopm, Yopm, label='OPM', color='cyan', linewidth = 1.0, linestyle = '--')
        
    
    ax.legend(loc='upper left', frameon=True, fontsize = 'small')
    #ax.legend( frameon=True, fontsize = 'small')
    plt.savefig('/home/poyraden/Josie18/Plots/'+ plottit +'.eps')
    plt.savefig('/home/poyraden/Josie18/Plots/'+ plottit +'.pdf')
   
def Make_3ProfilePlots(X1, X2, X3, Y1, Y2, Y3, xra, yra, label1, label2, label3, label4, xtit, ytit, mtit, plottit,keylog):
    
    fig,ax = plt.subplots()
    plt.xlim(xra)
    plt.ylim(yra)
    plt.xlabel(xtit)
    plt.ylabel(ytit)
    plt.title(mtit)
    plt.grid(True)
    
    #plt.yticks(np.arange(0, 7001, 1000))
    ax.tick_params(axis='both', which='both', direction='in')
    ax.yaxis.set_ticks_position('both')
    ax.xaxis.set_ticks_position('both')

    ax.yaxis.set_minor_locator(AutoMinorLocator(10))
    ax.xaxis.set_minor_locator(AutoMinorLocator(10))
    if keylog == 0:
        plt.plot(X1, Y1, label=label1, color='black', linewidth = 0.5)
        plt.plot(X2, Y2, label=label2, color='red', linewidth = 0.5)
        plt.plot(X3, Y3, label=label3, color='blue', linewidth = 0.5)
        #plt.plot(X4, Y4, label=label4, color='green', linewidth = 0.5)
        #plt.plot(Xopm, Yopm, label='OPM', color='cyan', linewidth = 1.0, linestyle = '--')
    if keylog ==1:
        plt.semilogy(X1, Y1, label=label1, color='black', linewidth = 0.5)
        plt.semilogy(X2, Y2, label=label2, color='red', linewidth = 0.5)
        plt.semilogy(X3, Y3, label=label3, color='blue', linewidth = 0.5)
        #plt.semilogy(X4, Y4, label=label4, color='green', linewidth = 0.5)
        #plt.semilogy(Xopm, Yopm, label='OPM', color='cyan', linewidth = 1.0, linestyle = '--')
        
    
    ax.legend(loc='upper left', frameon=True, fontsize = 'small')
    #ax.legend( frameon=True, fontsize = 'small')
    plt.savefig('/home/poyraden/Josie18/Plots/'+ plottit +'.eps')
    plt.savefig('/home/poyraden/Josie18/Plots/'+ plottit +'.pdf')
   

    # the function implemented from Roeland's code
def Calc_average_profile_PO3(dataframe, ybin, xcolumn):
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
        xra=[-1,20]
        xtitle='Ozone partial pressure (mPa)'
    if  xcolumn == 'PO3_OPM' :
        dft.PFcor = dataframe.PO3_OPM
        xra=[-1,20]
        xtitle='Ozone partial pressure (mPa)'

    # for OPM
    dft.OPM = dataframe.PO3_OPM
    dft.Tsim = dataframe.PO3_OPM
    
    ybin0 = ybin
    ymax = 20.0
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
    YgridOPM = [-9999.0] * n

    #print('n is ', n)
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
        dftmp1['OPM'] = dft[filter1].OPM
        #print(i, 'len of dftmp1 ', len(dftmp1))

        filtnull = dftmp1.X > -9999.0
        filtfin = np.isfinite(dftmp1.X)
        filterall = filtnull & filtfin
        dfgrid['X'] = dftmp1[filterall].X
        dfgrid['OPM'] = dftmp1[filterall].OPM

        # using mean and std
        Xgrid[i] = np.mean(dfgrid.X)
        Xsigma[i] = np.std(dfgrid.X)
        YgridOPM[i] = np.mean(dfgrid.OPM)
        
        # using median and interquantiles
        #Xgrid[i] = np.median(dfgrid.X)

        #q75, q25 = np.percentile(dfgrid.X, [75 ,25])
        #print(i, q75, q25)

        #if math.isnan(q75): q75 = 0.0
        #if math.isnan(q25): q25 = 0.0

        #iqr = q75 - q25
        #print(iqr, iqr(dfgrid.X))
        #if math.isnan(Xgrid[i]): Xgrid[i] = 0.0
        #if math.isnan(iqr): igr = 0.0
        
        #Xsigma[i] = iqr
        #YgridOPM[i] = np.mean(dfgrid.OPM)
        #print(i, " stdmean " , np.mean(dfgrid.X), " iqrmedian ", Xgrid[i] )

        #print(i, " std " , np.std(dfgrid.X), " iqr ", iqr )

    return Xgrid, Xsigma, YgridOPM

