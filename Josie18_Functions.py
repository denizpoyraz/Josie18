import pandas as pd
import numpy as np
import re
import glob
import math
from math import log
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.offsetbox import AnchoredText


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
        plt.plot(X1, Y1, label=label1, color='black', linewidth = 0.5)
        plt.plot(X2, Y2, label=label2, color='red', linewidth = 0.5)
        plt.plot(X3, Y3, label=label3, color='blue', linewidth = 0.5)
        plt.plot(X4, Y4, label=label4, color='green', linewidth = 0.5)
        plt.plot(X5, Y5, label=label5, color='cyan', linewidth = 1.0, linestyle = '--')
    if keylog ==1:
        plt.semilogy(X1, Y1, label=label1, color='black', linewidth = 0.5)
        plt.semilogy(X2, Y2, label=label2, color='red', linewidth = 0.5)
        plt.semilogy(X3, Y3, label=label3, color='blue', linewidth = 0.5)
        plt.semilogy(X4, Y4, label=label4, color='green', linewidth = 0.5)
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
   
