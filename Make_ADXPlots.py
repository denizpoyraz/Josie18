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


df = pd.read_csv("/home/poyraden/Josie18/Josie18_Data.csv")
dfnp = df.drop_duplicates(['Sim','Team'])

#ENSCI Plots:
# 1.0-0.1B:
# 2 plots  Sim 151: 3-4 ADX and 197-3 noADX, Sim 198:3-4 ADX and 197-3 no ADX

df_en1011_1513 = df[(df.ENSCI == 1) & (df.Sol ==1) & (df.Buf == 0.1) & (df.ADX == 1) & (df.Sim == 151) & (df.Team == 3)]
df_en1011_1514 = df[(df.ENSCI == 1) & (df.Sol ==1) & (df.Buf == 0.1) & (df.ADX == 1) & (df.Sim == 151) & (df.Team == 4)]
df_en1011_1983 = df[(df.ENSCI == 1) & (df.Sol ==1) & (df.Buf == 0.1) & (df.ADX == 1) & (df.Sim == 198) & (df.Team == 3)]
df_en1011_1984 = df[(df.ENSCI == 1) & (df.Sol ==1) & (df.Buf == 0.1) & (df.ADX == 1) & (df.Sim == 198) & (df.Team == 4)]
df_en1010_1973 = df[(df.ENSCI == 1) & (df.Sol ==1) & (df.Buf == 0.1) & (df.ADX == 0) & (df.Sim == 197) & (df.Team == 3)]

PO3_en1011_1513 = df_en1011_1513['PO3'].tolist()
PO3_en1011_1514 = df_en1011_1514['PO3'].tolist()
OPM_151 = df_en1011_1514['PO3_OPM'].tolist()
Time_151 = df_en1011_1513['Tsim'].tolist()
PO3_en1011_1983 = df_en1011_1983['PO3'].tolist()
PO3_en1011_1984 = df_en1011_1984['PO3'].tolist()
Time_198 = df_en1011_1983['Tsim'].tolist()
PO3_en1010_1973 = df_en1010_1973['PO3'].tolist()
OPM_197 = df_en1010_1973['PO3_OPM'].tolist()
Time_197 = df_en1010_1973['Tsim'].tolist()
print(len(PO3_en1011_1513), len(PO3_en1011_1514), len(Time_151))

xtitle = 'Simulation Time(sec.)'
ytitle = 'Partial O3 Pressure (mPa)'
Make_5ProfilePlots(Time_151, Time_151,Time_197, Time_151, Time_197,  PO3_en1011_1513, PO3_en1011_1514, PO3_en1010_1973, OPM_151, OPM_197, [0,10000], [0,30],'Sim. 151 ENSCI 1  1.0%+0.1B+ADX' , 'Sim. 151 ENSCI 2 1.0%+0.1B+ADX', 'Sim. 197 ENSCI 1.0%+0.1B+noADX', 'OPM Sim 151','OPM Sim 197', xtitle, ytitle, 'Comparison of ENSCI 1.0%-0.1B ADX vs noADX', 'ENSCI101_Sim151_Sim197',0)


