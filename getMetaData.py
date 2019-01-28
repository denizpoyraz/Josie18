#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import re
import glob
import math
from math import log
import re

files = glob.glob("/home/poyraden/Josie18/Files/Si*/*.ntb")

Sim = []
Team = []
Code = []
Flow = []
IB1 = []
Cor = []
Sol = []
Buf = []
ADX = []
Year = []

for filename in files:
    if filename.find('PR') != -1:
        continue
    nm = filename.split("/")[6]
    nm2 = nm.split(".")[0]
    #print('nm2',nm2)
    simd = nm2.replace('SI','')
    #print('filename', filename, simd)
    fb = open(filename,'rb')
    yeard = int(str(fb.readline().split()[3],'utf-8'))
    fb.close()

    fb = open(filename,'rb')

    linenum = []
    linetext = []

    for cnt in enumerate(fb):
        linenum.append(cnt[0])
        linetext.append(cnt[1])
    
    
    for il in range(3,22,5):
        tmp = str(linetext[il],'utf-8')
        tstr = re.search('(?<=O)(.*)(?=-)',tmp.split()[0])
        teamd = int(tstr.group())
        coded = str(tmp.split()[1])
        flowd = float(linetext[il+1].split()[1])
        ib1d = float(linetext[il+2].split()[1])
        cord = str(linetext[il+3].split()[1],'utf-8')
        par = str(linetext[il+4],'utf-8') 
        m = re.search('(?<==)(.*)(?=%)', par)
        sold = float(m.group())
        n = re.search('(?<=\+)(.*)(?=B)', par)
        bufd = float(n.group(0))
        o = re.search('(?<=B)(.*)(?=ADX\s)', par)
        ad = str(o.group(0)).lstrip().rstrip()
        adxd = str(ad)
        if(adxd =='NO'):
            adxdbool = 0
        if(adxd =='+'): 
            adxdbool = 1
        Sim.append(simd)
        Team.append(teamd)
        Code.append(coded)
        Flow.append(flowd)
        IB1.append(ib1d)
        Cor.append(cord)
        Sol.append(sold)
        Buf.append(bufd)
        ADX.append(adxdbool)
        Year.append(yeard)

dfMD = pd.DataFrame(list(zip(Year, Sim, Team, Code, Flow, IB1, Cor, Sol, Buf, ADX)), 
               columns =['Year', 'Sim', 'Team', 'Code', 'Flow', 'IB1', 'Cor', 'Sol', 'Buf', 'ADX'])         


#print(dfMD)
df = dfMD.sort_values(by = 'Sim', ascending=True)
#print(df)
df.to_csv("/home/poyraden/Josie18/Josie18_MetaData.csv", index=False)

