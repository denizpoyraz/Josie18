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

df = pd.read_csv("/home/poyraden/Josie18/Josie18_Data.csv", low_memory=False)

# ENSCI 1.0%+0.1B Sim 198:3,4 and 197 1
df_e101adx1 = df[(df.Year == 2018) & (df.ENSCI ==1) & (df.Sol == 1.0) & (df.Buf == 0.1) & (df.ADX == 1 ) & (df.Sim == 198) &  (df.Team == 3) & (df.PO3 >0.5) & (df.PO3_OPM > 0.5) & (df.PO3_OPM < 21) & (df.Tsim < 7000) ]
df_e101adx2 = df[(df.Year == 2018) & (df.ENSCI ==1) & (df.Sol == 1.0) & (df.Buf == 0.1) & (df.ADX == 1 ) & (df.Sim == 198) & (df.Team == 4) & (df.PO3 >0.5) & (df.PO3_OPM > 0.5) & (df.PO3_OPM < 21)  & (df.Tsim < 7000)]
#df_e101noadx = df[(df.Year == 2018) & (df.ENSCI ==1) & (df.Sol == 1.0) & (df.Buf == 0.1) & (df.ADX == 0 ) & (df.Sim == 197) & (df.Team == 3)]
df_e101noadx = df[(df.Year == 2018) & (df.ENSCI ==1) & (df.Sol == 1.0) & (df.Buf == 0.1) & (df.ADX == 0 ) & (df.Sim == 197) & (df.Team == 3)& (df.PO3 >0.5) & (df.PO3_OPM > 0.5) & (df.PO3_OPM < 21)  & (df.Tsim < 7000)]

df_e101noadx_asc = df_e101noadx[((df_e101noadx.Tsim > 575 )&( df_e101noadx.Tsim < 1200)) |  ((df_e101noadx.Tsim > 2400) & (df_e101noadx.Tsim < 3000)) | ((df_e101noadx.Tsim > 4800) & (df_e101noadx.Tsim < 6800)) ]
df_e101noadx_dec = df_e101noadx[((df_e101noadx.Tsim > 1200 ) & (df_e101noadx.Tsim < 1400 )) | ( (df_e101noadx.Tsim > 3000) & (df_e101noadx.Tsim < 4800))]

df_rest = df_e101noadx[((df_e101noadx.Tsim > 1400 )&( df_e101noadx.Tsim < 2400)) | (df_e101noadx.Tsim > 6800)]


legend_e101adx1 = 'Sim 198 ENSCI-1 1.0%+0.1B+ADX '
legend_e101adx2 = 'Sim 198 ENSCI-2 1.0%+0.1B+ADX '
legend_e101noadx = 'Sim 197 ENSCI-1 1.0%+0.1B '

PO3_e101adx1, PO3_e101adx1_err, OPM_e101adx1  = Calc_average_profile_PO3(df_e101adx1, 1, 'PO3')
PO3_e101adx2, PO3_e101adx2_err, OPM_e101adx2  = Calc_average_profile_PO3(df_e101adx2, 1, 'PO3')
PO3_e101noadx, PO3_e101noadx_err, OPM_e101noadx  = Calc_average_profile_PO3(df_e101noadx, 1, 'PO3')

OPM_e101adx1 = np.asarray(df_e101adx1.PO3_OPM)
PO3_e101adx1 = np.asarray(df_e101adx1.PO3)

OPM_e101adx2 = np.asarray(df_e101adx2.PO3_OPM)
PO3_e101adx2 = np.asarray(df_e101adx2.PO3)

OPM_e101noadx = np.asarray(df_e101noadx.PO3_OPM) #.reshape(-1,1)
PO3_e101noadx = np.asarray(df_e101noadx.PO3) #.reshape(-1,1)

OPM_e101noadx_asc = np.asarray(df_e101noadx_asc.PO3_OPM) #.reshape(-1,1)
PO3_e101noadx_asc = np.asarray(df_e101noadx_asc.PO3) #.reshape(-1,1)

OPM_e101noadx_dec = np.asarray(df_e101noadx_dec.PO3_OPM) #.reshape(-1,1)
PO3_e101noadx_dec = np.asarray(df_e101noadx_dec.PO3) #.reshape(-1,1)

OPM_rest =  np.asarray(df_rest.PO3_OPM)
PO3_rest =  np.asarray(df_rest.PO3)


# OPM_e101noadx = np.asarray(OPM_e101noadx)
# PO3_e101noadx = np.asarray(PO3_e101noadx) 


slope_e101adx1, intercept_e101adx1, r_value_e101adx1, p_value_e101adx1, std_err_e101adx1 = stats.linregress(OPM_e101adx1,PO3_e101adx1)
PO3_e101adx1fit = slope_e101adx1 * OPM_e101adx1 + intercept_e101adx1

slope_e101adx2, intercept_e101adx2, r_value_e101adx2, p_value_e101adx2, std_err_e101adx2 = stats.linregress(OPM_e101adx2,PO3_e101adx2)
PO3_e101adx2fit = slope_e101adx2 * OPM_e101adx2 + intercept_e101adx2

slope_e101noadx, intercept_e101noadx, r_value_e101noadx, p_value_e101noadx, std_err_e101noadx = stats.linregress(OPM_e101noadx,PO3_e101noadx)
PO3_e101noadxfit = slope_e101noadx * OPM_e101noadx + intercept_e101noadx

slope_e101noadx_asc, intercept_e101noadx_asc, r_value_e101noadx_asc, p_value_e101noadx_asc, std_err_e101noadx_asc = stats.linregress(OPM_e101noadx_asc,PO3_e101noadx_asc)
PO3_e101noadx_ascfit = slope_e101noadx_asc * OPM_e101noadx_asc + intercept_e101noadx_asc

slope_e101noadx_dec, intercept_e101noadx_dec, r_value_e101noadx_dec, p_value_e101noadx_dec, std_err_e101noadx_dec = stats.linregress(OPM_e101noadx_dec,PO3_e101noadx_dec)
PO3_e101noadx_decfit = slope_e101noadx_dec * OPM_e101noadx_dec + intercept_e101noadx_dec

slope_rest, intercept_rest, r_value_rest, p_value_rest, std_err_rest = stats.linregress(OPM_rest,PO3_rest)
PO3_restfit = (slope_rest * OPM_rest) + intercept_rest

# modelnoadx = LinearRegression()
# modelnoadx.fit(OPM_e101noadx,PO3_e101noadx)


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



# plt.plot(OPM_e101adx1,PO3_e101adx1,'+', color = 'green', label = legend_e101adx1)
# plt.plot( OPM_e101adx1, PO3_e101adx1fit,':', color = 'lime', linewidth = 1.0)

# plt.plot(OPM_e101adx2,PO3_e101adx2,'x', color = 'b', label = legend_e101adx2)
# plt.plot( OPM_e101adx2, PO3_e101adx2fit,':', color = 'cyan', linewidth = 1.0)

# plt.plot(OPM_e101noadx,PO3_e101noadx,'*', color = 'purple', label = legend_e101noadx)
# plt.plot( OPM_e101noadx, PO3_e101noadxfit,':', color = 'magenta', linewidth = 2.0)
#plt.plot( OPM_e101noadx, modelnoadx.predict(OPM_e101noadx),':', color = 'magenta', linewidth = 1.0)

plt.plot(OPM_e101noadx_dec,PO3_e101noadx_dec,'+', color = 'purple', label = legend_e101noadx)
plt.plot( OPM_e101noadx_dec, PO3_e101noadx_decfit,':', color = 'magenta', linewidth = 2.0)

plt.plot(OPM_e101noadx_asc,PO3_e101noadx_asc,'x', color = 'orange', label = legend_e101noadx)
plt.plot( OPM_e101noadx_asc, PO3_e101noadx_ascfit,':', color = 'red', linewidth = 2.0)



plt.plot(OPM_rest,PO3_rest,'+', color = 'yellow', label = legend_e101noadx)
#plt.plot( OPM_rest, PO3_restfit,':', color = 'cyan', linewidth = 2.0)

ax.legend(loc='upper left', frameon=True, fontsize = 'small')
# ax = plt.gca()
# fig = plt.gcf()

text_e101adx1 =  'Slope: ' + str(round(slope_e101adx1,2)) +', Intercept: '+ str(round(intercept_e101adx1,2))
text_e101adx2 =  'Slope: ' + str(round(slope_e101adx2,2)) +', Intercept: '+ str(round(intercept_e101adx2,2))
text_e101noadx =  'Slope: ' + str(round(slope_e101noadx,2)) +', Intercept: '+ str(round(intercept_e101noadx,2))


t1 = ax.text(0.55,0.25, text_e101adx1 ,  color='green', transform=ax.transAxes)
t2 = ax.text(0.55,0.175, text_e101adx2 ,  color='blue', transform=ax.transAxes)
t3 = ax.text(0.55,0.10, text_e101noadx ,  color='magenta', transform=ax.transAxes)

#xt2 = ax.text(0.05,0.02, text2,  color='red', transform=ax.transAxes)

    
#plt.plot(xfit, yfit, color='red')
#plt.plot(OPM_e101adx1, PO3_e101adx1, linewidth = 0.5)
#plt.show()



# SPC  1.0%+0.1B Sim 198:1,2 and 197 1,2 
df_s101adx1 = df[(df.Year == 2018) & (df.ENSCI ==0) & (df.Sol == 1.0) & (df.Buf == 0.1) & (df.ADX == 1 ) & (df.Sim == 198) &  (df.Team == 1) & (df.PO3 >0.5) & (df.PO3_OPM > 0.5) & (df.PO3_OPM < 21)  & (df.Tsim < 7000)]
df_s101adx2 = df[(df.Year == 2018) & (df.ENSCI ==0) & (df.Sol == 1.0) & (df.Buf == 0.1) & (df.ADX == 1 ) & (df.Sim == 198) & (df.Team == 2) & (df.PO3 >0.5) & (df.PO3_OPM > 0.5) & (df.PO3_OPM < 21) ]
df_s101noadx1 = df[(df.Year == 2018) & (df.ENSCI ==0) & (df.Sol == 1.0) & (df.Buf == 0.1) & (df.ADX == 0 ) & (df.Sim == 197) & (df.Team == 1) & (df.PO3 >0.5) & (df.PO3_OPM > 0.5) & (df.PO3_OPM < 21)  & (df.Tsim < 7000) ]
df_s101noadx2 = df[(df.Year == 2018) & (df.ENSCI ==0) & (df.Sol == 1.0) & (df.Buf == 0.1) & (df.ADX == 0 ) & (df.Sim == 197) & (df.Team == 2) & (df.PO3 >0.5) & (df.PO3_OPM > 0.5) & (df.PO3_OPM < 21)]


legend_s101adx1 = 'Sim 198 SPC-1 1.0%+0.1B+ADX '
legend_s101adx2 = 'Sim 198 SPC-2 1.0%+0.1B+ADX '
legend_s101noadx1 = 'Sim 197 SPC-1 1.0%+0.1B '
legend_s101noadx2 = 'Sim 197 SPC-2 1.0%+0.1B '


PO3_s101adx1, PO3_s101adx1_err, OPM_s101adx1  = Calc_average_profile_PO3(df_s101adx1, 1, 'PO3')
PO3_s101adx2, PO3_s101adx2_err, OPM_s101adx2  = Calc_average_profile_PO3(df_s101adx2, 1, 'PO3')
PO3_s101noadx1, PO3_s101noadx1_err, OPM_s101noadx1  = Calc_average_profile_PO3(df_s101noadx1, 1, 'PO3')
PO3_s101noadx2, PO3_s101noadx2_err, OPM_s101noadx2  = Calc_average_profile_PO3(df_s101noadx2, 1, 'PO3')


OPM_s101adx1 = np.asarray(df_s101adx1.PO3_OPM)
PO3_s101adx1 = np.asarray(df_s101adx1.PO3)

OPM_s101adx2 = np.asarray(df_s101adx2.PO3_OPM)
PO3_s101adx2 = np.asarray(df_s101adx2.PO3)

OPM_s101noadx1 = np.asarray(df_s101noadx1.PO3_OPM)
PO3_s101noadx1 = np.asarray(df_s101noadx1.PO3)

OPM_s101noadx2 = np.asarray(df_s101noadx2.PO3_OPM)
PO3_s101noadx2 = np.asarray(df_s101noadx2.PO3)

slope_s101adx1, intercept_s101adx1, r_value_s101adx1, p_value_s101adx1, std_err_s101adx1 = stats.linregress(OPM_s101adx1,PO3_s101adx1)
PO3_s101adx1fit = slope_s101adx1 * OPM_s101adx1 + intercept_s101adx1

slope_s101adx2, intercept_s101adx2, r_value_s101adx2, p_value_s101adx2, std_err_s101adx2 = stats.linregress(OPM_s101adx2,PO3_s101adx2)
PO3_s101adx2fit = slope_s101adx2 * OPM_s101adx2 + intercept_s101adx2

slope_s101noadx1, intercept_s101noadx1, r_value_s101noadx1, p_value_s101noadx1, std_err_s101noadx1 = stats.linregress(OPM_s101noadx1,PO3_s101noadx1)
PO3_s101noadx1fit = slope_s101noadx1 * OPM_s101noadx1 + intercept_s101noadx1

slope_s101noadx2, intercept_s101noadx2, r_value_s101noadx2, p_value_s101noadx2, std_err_s101noadx2 = stats.linregress(OPM_s101noadx2,PO3_s101noadx2)
PO3_s101noadx2fit = slope_s101noadx2 * OPM_s101noadx2 + intercept_s101noadx2


fig2,ax2 = plt.subplots()
plt.xlim(0,30)
plt.ylim(0,30)
plt.xlabel('OPM (mPa)')
plt.ylabel(r'PO3 (mPa)')
plt.title('PO3 vs  OPM ')
plt.grid(True)

ax2.tick_params(axis='both', which='both', direction='in')
ax2.yaxis.set_ticks_position('both')
ax2.xaxis.set_ticks_position('both')

ax2.yaxis.set_minor_locator(AutoMinorLocator(10))
ax2.xaxis.set_minor_locator(AutoMinorLocator(10))


plt.plot(OPM_s101adx2,PO3_s101adx2,'x', color = 'b', label = legend_s101adx2)
plt.plot( OPM_s101adx2, PO3_s101adx2fit,':', color = 'cyan', linewidth = 1.0)

plt.plot(OPM_s101adx1,PO3_s101adx1,'+', color = 'green', label = legend_s101adx1)
plt.plot( OPM_s101adx1, PO3_s101adx1fit,':', color = 'lime', linewidth = 1.0)

plt.plot(OPM_s101noadx1,PO3_s101noadx1,'*', color = 'purple', label = legend_s101noadx1)
plt.plot(OPM_s101noadx1, PO3_s101noadx1fit,':', color = 'magenta', linewidth = 1.0)

plt.plot(OPM_s101noadx2,PO3_s101noadx2,'.', color = 'red', label = legend_s101noadx2)
plt.plot(OPM_s101noadx2, PO3_s101noadx2fit,':', color = 'darkred', linewidth = 1.0)

ax2.legend(loc='upper left', frameon=True, fontsize = 'small')

print( r_value_s101noadx1, p_value_s101noadx1, std_err_s101noadx1)
#print('err ', std_err_s101adx1)
text_s101adx1 =  'Slope: ' + str(round(slope_s101adx1,2)) +', Intercept: '+ str(round(intercept_s101adx1,2)) + ' err:' + str(round(std_err_s101adx1,4))
text_s101adx2 =  'Slope: ' + str(round(slope_s101adx2,2)) +', Intercept: '+ str(round(intercept_s101adx2,2)) + ' err:' + str(round(std_err_s101adx2,4))
text_s101noadx1 =  'Slope: ' + str(round(slope_s101noadx1,2)) +', Intercept: '+ str(round(intercept_s101noadx1,2)) + ' err:' + str(round(std_err_s101noadx1,4))
text_s101noadx2 =  'Slope: ' + str(round(slope_s101noadx2,2)) +', Intercept: '+ str(round(intercept_s101noadx2,2)) + ' err:' + str(round(std_err_s101noadx2,4))


t1 = ax2.text(0.45,0.25, text_s101adx1 ,  color='green', transform=ax2.transAxes)
t2 = ax2.text(0.45,0.175, text_s101adx2 ,  color='blue', transform=ax2.transAxes)
t3 = ax2.text(0.45,0.10, text_s101noadx1 ,  color='magenta', transform=ax2.transAxes)
t4 = ax2.text(0.45,0.05, text_s101noadx2 ,  color='red', transform=ax2.transAxes)
    
plt.show()

#################
# OPM_e101adx1 = np.asarray(OPM_e101adx1)
# PO3_e101adx1 = np.asarray(PO3_e101adx1)

# OPM_e101adx2 = np.asarray(OPM_e101adx2)
# PO3_e101adx2 = np.asarray(PO3_e101adx2)

# OPM_e101noadx = np.asarray(OPM_e101noadx)
# PO3_e101noadx = np.asarray(PO3_e101noadx)
