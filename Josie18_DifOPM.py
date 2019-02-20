import pandas as pd
import numpy as np
import re
import glob
import math
from math import log
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.offsetbox import AnchoredText

from Josie17_Functions import Calc_average_profile
from Josie17_Functions import Plot_compare_profile_plots
from Josie17_Functions import Plot_compare_profile_plots_updated
from Josie17_Functions import Calc_RDif
from Josie17_Functions import meanfunction
from Josie18_Functions import Calc_average_profile_PO3


df = pd.read_csv("/home/poyraden/Josie18/Josie18_Data.csv", low_memory=False)

#df = df.drop(df[(df.Tsim > 8000)].index)
#df = df.drop(df[(df.Sim == 196)].index)
df = df.drop(df[(df.PO3_OPM > 10)].index)


resol = 200
resolpo3 = 1
dimension = int(7000/resol)
dimensionpo3 = int(20/resolpo3)

ytitle = 'Elapsed Time (Sec)'
ytitlepo3 = 'Partial Pressure OPM (mPa)'

# profiles to be checked with ADX and noADX for each SST and Sonde type

# #ENSCI 2.0-0.1%B

profENSCI_201adx = df[(df.ENSCI == 1) & (df.Sol == 2) & (df.Buf == 0.1) & (df.ADX == 1)]
profENSCI_201noadx = df[(df.ENSCI == 1) & (df.Sol == 2) & (df.Buf == 0.1) & (df.ADX == 0)]

totO3ENSCI_201adx = profENSCI_201adx.drop_duplicates(['Sim', 'Team']).frac.mean()
totO3ENSCI_201noadx = profENSCI_201noadx.drop_duplicates(['Sim', 'Team']).frac.mean()

avgprofENSCI_201adx_X, avgprofENSCI_201adx_Xerr, Y = Calc_average_profile_PO3(profENSCI_201adx,resolpo3,'ADif_PO3S')
avgprofENSCI_201noadx_X, avgprofENSCI_201noadx_Xerr, Y = Calc_average_profile_PO3(profENSCI_201noadx,resolpo3,'ADif_PO3S')

avgprofENSCI_201adx_O3S_X, avgprofENSCI_201adx_O3S_Xerr, Y = Calc_average_profile_PO3(profENSCI_201adx,resolpo3,'PO3')
avgprofENSCI_201noadx_O3S_X, avgprofENSCI_201noadx_O3S_Xerr, Y = Calc_average_profile_PO3(profENSCI_201noadx,resolpo3,'PO3')
avgprofENSCI_201adx_OPM_X, avgprofENSCI_201adx_OPM_Xerr, Y = Calc_average_profile_PO3(profENSCI_201adx,resolpo3,'PO3_OPM')
avgprofENSCI_201noadx_OPM_X, avgprofENSCI_201noadx_OPM_Xerr, Y = Calc_average_profile_PO3(profENSCI_201noadx,resolpo3,'PO3_OPM')

RENSCI_201adx, RENSCI_201adxerr = Calc_RDif(avgprofENSCI_201adx_O3S_X, avgprofENSCI_201adx_OPM_X, avgprofENSCI_201adx_Xerr, dimensionpo3 )
RENSCI_201noadx, RENSCI_201noadxerr = Calc_RDif(avgprofENSCI_201noadx_O3S_X, avgprofENSCI_201noadx_OPM_X, avgprofENSCI_201noadx_Xerr, dimensionpo3 )

Plot_compare_profile_plots_updated(avgprofENSCI_201adx_X, avgprofENSCI_201adx_Xerr, avgprofENSCI_201noadx_X, avgprofENSCI_201noadx_Xerr, Y, [-5,5],'ENSCI2.0%+0.1B ADX and noADX', 'Sonde - OPM O3 Difference (mPa)', ytitlepo3, 'ENSCI2.0%+0.1B+ADX',  'ENSCI2.0%+0.1B', totO3ENSCI_201adx, totO3ENSCI_201noadx,profENSCI_201adx.drop_duplicates(['Sim', 'Team']) , profENSCI_201noadx.drop_duplicates(['Sim', 'Team']), 'ADif_ENSCI201_ADX_PO3')

Plot_compare_profile_plots_updated(RENSCI_201adx, RENSCI_201adxerr, RENSCI_201noadx, RENSCI_201noadxerr, Y, [-50,50],'ENSCI2.0%+0.1B ADX and noADX', 'Sonde - OPM O3 Difference (%)', ytitlepo3, 'ENSCI2.0%+0.1B+ADX',  'ENSCI2.0%+0.1B', totO3ENSCI_201adx, totO3ENSCI_201noadx, profENSCI_201adx.drop_duplicates(['Sim', 'Team']), profENSCI_201noadx.drop_duplicates(['Sim', 'Team']), 'RDif_ENSCI201_ADX_PO3')

#ENSCI 1.0-0.1%B

profENSCI_101adx = df[(df.ENSCI == 1) & (df.Sol == 1) & (df.Buf == 0.1) & (df.ADX == 1)]
profENSCI_101noadx = df[(df.ENSCI == 1) & (df.Sol == 1) & (df.Buf == 0.1) & (df.ADX == 0)]

totO3ENSCI_101adx = profENSCI_101adx.drop_duplicates(['Sim', 'Team']).frac.mean()
totO3ENSCI_101noadx = profENSCI_101noadx.drop_duplicates(['Sim', 'Team']).frac.mean()

avgprofENSCI_101adx_X, avgprofENSCI_101adx_Xerr, Y = Calc_average_profile_PO3(profENSCI_101adx,resolpo3,'ADif_PO3S')
avgprofENSCI_101noadx_X, avgprofENSCI_101noadx_Xerr, Y = Calc_average_profile_PO3(profENSCI_101noadx,resolpo3,'ADif_PO3S')

avgprofENSCI_101adx_O3S_X, avgprofENSCI_101adx_O3S_Xerr, Y = Calc_average_profile_PO3(profENSCI_101adx,resolpo3,'PO3')
avgprofENSCI_101noadx_O3S_X, avgprofENSCI_101noadx_O3S_Xerr, Y = Calc_average_profile_PO3(profENSCI_101noadx,resolpo3,'PO3')
avgprofENSCI_101adx_OPM_X, avgprofENSCI_101adx_OPM_Xerr, Y = Calc_average_profile_PO3(profENSCI_101adx,resolpo3,'PO3_OPM')
avgprofENSCI_101noadx_OPM_X, avgprofENSCI_101noadx_OPM_Xerr, Y = Calc_average_profile_PO3(profENSCI_101noadx,resolpo3,'PO3_OPM')

RENSCI_101adx, RENSCI_101adxerr = Calc_RDif(avgprofENSCI_101adx_O3S_X, avgprofENSCI_101adx_OPM_X, avgprofENSCI_101adx_Xerr, dimensionpo3 )
RENSCI_101noadx, RENSCI_101noadxerr = Calc_RDif(avgprofENSCI_101noadx_O3S_X, avgprofENSCI_101noadx_OPM_X, avgprofENSCI_101noadx_Xerr, dimensionpo3 )

Plot_compare_profile_plots_updated(avgprofENSCI_101adx_X, avgprofENSCI_101adx_Xerr, avgprofENSCI_101noadx_X, avgprofENSCI_101noadx_Xerr, Y, [-5,5],'ENSCI1.0%+0.1B ADX and noADX', 'Sonde - OPM O3 Difference (mPa)', ytitlepo3, 'ENSCI1.0%+0.1B+ADX',  'ENSCI1.0%+0.1B', totO3ENSCI_101adx, totO3ENSCI_101noadx,profENSCI_101adx.drop_duplicates(['Sim', 'Team']) , profENSCI_101noadx.drop_duplicates(['Sim', 'Team']), 'ADif_ENSCI101_ADX_PO3')

Plot_compare_profile_plots_updated(RENSCI_101adx, RENSCI_101adxerr, RENSCI_101noadx, RENSCI_101noadxerr, Y, [-50,50],'ENSCI1.0%+0.1B ADX and noADX', 'Sonde - OPM O3 Difference (%)', ytitlepo3, 'ENSCI1.0%+0.1B+ADX',  'ENSCI1.0%+0.1B', totO3ENSCI_101adx, totO3ENSCI_101noadx, profENSCI_101adx.drop_duplicates(['Sim', 'Team']), profENSCI_101noadx.drop_duplicates(['Sim', 'Team']), 'RDif_ENSCI101_ADX_PO3')



#ENSCI 1.0% - 1.0B

profENSCI_11adx = df[(df.ENSCI == 1) & (df.Sol == 1) & (df.Buf == 1.0) & (df.ADX == 1)]
profENSCI_11noadx = df[(df.ENSCI == 1) & (df.Sol == 1) & (df.Buf == 1.0) & (df.ADX == 0)]

totO3ENSCI_11adx = profENSCI_11adx.drop_duplicates(['Sim', 'Team']).frac.mean()
totO3ENSCI_11noadx = profENSCI_11noadx.drop_duplicates(['Sim', 'Team']).frac.mean()

avgprofENSCI_11adx_X, avgprofENSCI_11adx_Xerr, Y = Calc_average_profile_PO3(profENSCI_11adx,resolpo3,'ADif_PO3S')
avgprofENSCI_11noadx_X, avgprofENSCI_11noadx_Xerr, Y = Calc_average_profile_PO3(profENSCI_11noadx,resolpo3,'ADif_PO3S')

avgprofENSCI_11adx_O3S_X, avgprofENSCI_11adx_O3S_Xerr, Y = Calc_average_profile_PO3(profENSCI_11adx,resolpo3,'PO3')
avgprofENSCI_11noadx_O3S_X, avgprofENSCI_11noadx_O3S_Xerr, Y = Calc_average_profile_PO3(profENSCI_11noadx,resolpo3,'PO3')
avgprofENSCI_11adx_OPM_X, avgprofENSCI_11adx_OPM_Xerr, Y = Calc_average_profile_PO3(profENSCI_11adx,resolpo3,'PO3_OPM')
avgprofENSCI_11noadx_OPM_X, avgprofENSCI_11noadx_OPM_Xerr, Y = Calc_average_profile_PO3(profENSCI_11noadx,resolpo3,'PO3_OPM')

RENSCI_11adx, RENSCI_11adxerr = Calc_RDif(avgprofENSCI_11adx_O3S_X, avgprofENSCI_11adx_OPM_X, avgprofENSCI_11adx_Xerr, dimensionpo3 )
RENSCI_11noadx, RENSCI_11noadxerr = Calc_RDif(avgprofENSCI_11noadx_O3S_X, avgprofENSCI_11noadx_OPM_X, avgprofENSCI_11noadx_Xerr, dimensionpo3 )

Plot_compare_profile_plots_updated(avgprofENSCI_11adx_X, avgprofENSCI_11adx_Xerr, avgprofENSCI_11noadx_X, avgprofENSCI_11noadx_Xerr, Y, [-5,5],'ENSCI1.0%+1.0B ADX and noADX', 'Sonde - OPM O3 Difference (mPa)', ytitlepo3, 'ENSCI1.0%+1.0B+ADX',  'ENSCI1.0%+1.0B', totO3ENSCI_11adx, totO3ENSCI_11noadx,profENSCI_11adx.drop_duplicates(['Sim', 'Team']) , profENSCI_11noadx.drop_duplicates(['Sim', 'Team']), 'ADif_ENSCI11_ADX_PO3')

Plot_compare_profile_plots_updated(RENSCI_11adx, RENSCI_11adxerr, RENSCI_11noadx, RENSCI_11noadxerr, Y, [-50,50],'ENSCI1.0%+1.0B ADX and noADX', 'Sonde - OPM O3 Difference (%)', ytitlepo3, 'ENSCI1.0%+1.0B+ADX',  'ENSCI1.0%+1.0B', totO3ENSCI_11adx, totO3ENSCI_11noadx, profENSCI_11adx.drop_duplicates(['Sim', 'Team']), profENSCI_11noadx.drop_duplicates(['Sim', 'Team']), 'RDif_ENSCI11_ADX_PO3')

#ENSCI 0.5% - 0.5B

print('ENSCI 0.5 0.5')

profENSCI_0505adx = df[(df.ENSCI == 1) & (df.Sol == 0.5) & (df.Buf == 0.5) & (df.ADX == 1)]
profENSCI_0505noadx = df[(df.ENSCI == 1) & (df.Sol == 0.5) & (df.Buf == 0.5) & (df.ADX == 0)]

totO3ENSCI_0505adx = profENSCI_0505adx.drop_duplicates(['Sim', 'Team']).frac.mean()
totO3ENSCI_0505noadx = profENSCI_0505noadx.drop_duplicates(['Sim', 'Team']).frac.mean()

avgprofENSCI_0505adx_X, avgprofENSCI_0505adx_Xerr, Y = Calc_average_profile_PO3(profENSCI_0505adx,resolpo3,'ADif_PO3S')
avgprofENSCI_0505noadx_X, avgprofENSCI_0505noadx_Xerr, Y = Calc_average_profile_PO3(profENSCI_0505noadx,resolpo3,'ADif_PO3S')

avgprofENSCI_0505adx_O3S_X, avgprofENSCI_0505adx_O3S_Xerr, Y = Calc_average_profile_PO3(profENSCI_0505adx,resolpo3,'PO3')
avgprofENSCI_0505noadx_O3S_X, avgprofENSCI_0505noadx_O3S_Xerr, Y = Calc_average_profile_PO3(profENSCI_0505noadx,resolpo3,'PO3')
avgprofENSCI_0505adx_OPM_X, avgprofENSCI_0505adx_OPM_Xerr, Y = Calc_average_profile_PO3(profENSCI_0505adx,resolpo3,'PO3_OPM')
avgprofENSCI_0505noadx_OPM_X, avgprofENSCI_0505noadx_OPM_Xerr, Y = Calc_average_profile_PO3(profENSCI_0505noadx,resolpo3,'PO3_OPM')

RENSCI_0505adx, RENSCI_0505adxerr = Calc_RDif(avgprofENSCI_0505adx_O3S_X, avgprofENSCI_0505adx_OPM_X, avgprofENSCI_0505adx_Xerr, dimensionpo3 )
RENSCI_0505noadx, RENSCI_0505noadxerr = Calc_RDif(avgprofENSCI_0505noadx_O3S_X, avgprofENSCI_0505noadx_OPM_X, avgprofENSCI_0505noadx_Xerr, dimensionpo3 )

Plot_compare_profile_plots_updated(avgprofENSCI_0505adx_X, avgprofENSCI_0505adx_Xerr, avgprofENSCI_0505noadx_X, avgprofENSCI_0505noadx_Xerr, Y, [-5,5],'ENSCI0.5%+0.5B ADX and noADX', 'Sonde - OPM O3 Difference (mPa)', ytitlepo3, 'ENSCI0.5%+0.5B+ADX',  'ENSCI0.5%+0.5B', totO3ENSCI_0505adx, totO3ENSCI_0505noadx,profENSCI_0505adx.drop_duplicates(['Sim', 'Team']) , profENSCI_0505noadx.drop_duplicates(['Sim', 'Team']), 'ADif_ENSCI0505_ADX_PO3')

Plot_compare_profile_plots_updated(RENSCI_0505adx, RENSCI_0505adxerr, RENSCI_0505noadx, RENSCI_0505noadxerr, Y, [-50,50],'ENSCI0.5%+0.5B ADX and noADX', 'Sonde - OPM O3 Difference (%)', ytitlepo3, 'ENSCI0.5%+0.5B+ADX',  'ENSCI0.5%+0.5B', totO3ENSCI_0505adx, totO3ENSCI_0505noadx, profENSCI_0505adx.drop_duplicates(['Sim', 'Team']), profENSCI_0505noadx.drop_duplicates(['Sim', 'Team']), 'RDif_ENSCI0505_ADX_PO3')

#### SPC ######

##SPC 2.0-0.1%B

print('SPC 2.0-0.1B')

profSPC_201adx = df[(df.ENSCI == 0) & (df.Sol == 2) & (df.Buf == 0.1) & (df.ADX == 1)]
profSPC_201noadx = df[(df.ENSCI == 0) & (df.Sol == 2) & (df.Buf == 0.1) & (df.ADX == 0)]

totO3SPC_201adx = profSPC_201adx.drop_duplicates(['Sim', 'Team']).frac.mean()
totO3SPC_201noadx = profSPC_201noadx.drop_duplicates(['Sim', 'Team']).frac.mean()

avgprofSPC_201adx_X, avgprofSPC_201adx_Xerr, Y = Calc_average_profile_PO3(profSPC_201adx,resolpo3,'ADif_PO3S')
avgprofSPC_201noadx_X, avgprofSPC_201noadx_Xerr, Y = Calc_average_profile_PO3(profSPC_201noadx,resolpo3,'ADif_PO3S')

avgprofSPC_201adx_O3S_X, avgprofSPC_201adx_O3S_Xerr, Y = Calc_average_profile_PO3(profSPC_201adx,resolpo3,'PO3')
avgprofSPC_201noadx_O3S_X, avgprofSPC_201noadx_O3S_Xerr, Y = Calc_average_profile_PO3(profSPC_201noadx,resolpo3,'PO3')
avgprofSPC_201adx_OPM_X, avgprofSPC_201adx_OPM_Xerr, Y = Calc_average_profile_PO3(profSPC_201adx,resolpo3,'PO3_OPM')
avgprofSPC_201noadx_OPM_X, avgprofSPC_201noadx_OPM_Xerr, Y = Calc_average_profile_PO3(profSPC_201noadx,resolpo3,'PO3_OPM')

RSPC_201adx, RSPC_201adxerr = Calc_RDif(avgprofSPC_201adx_O3S_X, avgprofSPC_201adx_OPM_X, avgprofSPC_201adx_Xerr, dimensionpo3 )
RSPC_201noadx, RSPC_201noadxerr = Calc_RDif(avgprofSPC_201noadx_O3S_X, avgprofSPC_201noadx_OPM_X, avgprofSPC_201noadx_Xerr, dimensionpo3 )

Plot_compare_profile_plots_updated(avgprofSPC_201adx_X, avgprofSPC_201adx_Xerr, avgprofSPC_201noadx_X, avgprofSPC_201noadx_Xerr, Y, [-5,5],'SPC2.0%+0.1B ADX and noADX', 'Sonde - OPM O3 Difference (mPa)', ytitlepo3, 'SPC2.0%+0.1B+ADX',  'SPC2.0%+0.1B', totO3SPC_201adx, totO3SPC_201noadx,profSPC_201adx.drop_duplicates(['Sim', 'Team']) , profSPC_201noadx.drop_duplicates(['Sim', 'Team']), 'ADif_SPC201_ADX_PO3')

Plot_compare_profile_plots_updated(RSPC_201adx, RSPC_201adxerr, RSPC_201noadx, RSPC_201noadxerr, Y, [-50,50],'SPC2.0%+0.1B ADX and noADX', 'Sonde - OPM O3 Difference (%)', ytitlepo3, 'SPC2.0%+0.1B+ADX',  'SPC2.0%+0.1B', totO3SPC_201adx, totO3SPC_201noadx, profSPC_201adx.drop_duplicates(['Sim', 'Team']), profSPC_201noadx.drop_duplicates(['Sim', 'Team']), 'RDif_SPC201_ADX_PO3')

print("SPC 1.0-0.1%B")

profSPC_101adx = df[(df.ENSCI == 0) & (df.Sol == 1) & (df.Buf == 0.1) & (df.ADX == 1)]
profSPC_101noadx = df[(df.ENSCI == 0) & (df.Sol == 1) & (df.Buf == 0.1) & (df.ADX == 0)]

totO3SPC_101adx = profSPC_101adx.drop_duplicates(['Sim', 'Team']).frac.mean()
totO3SPC_101noadx = profSPC_101noadx.drop_duplicates(['Sim', 'Team']).frac.mean()

avgprofSPC_101adx_X, avgprofSPC_101adx_Xerr, Y = Calc_average_profile_PO3(profSPC_101adx,resolpo3,'ADif_PO3S')
avgprofSPC_101noadx_X, avgprofSPC_101noadx_Xerr, Y = Calc_average_profile_PO3(profSPC_101noadx,resolpo3,'ADif_PO3S')

avgprofSPC_101adx_O3S_X, avgprofSPC_101adx_O3S_Xerr, Y = Calc_average_profile_PO3(profSPC_101adx,resolpo3,'PO3')
avgprofSPC_101noadx_O3S_X, avgprofSPC_101noadx_O3S_Xerr, Y = Calc_average_profile_PO3(profSPC_101noadx,resolpo3,'PO3')
avgprofSPC_101adx_OPM_X, avgprofSPC_101adx_OPM_Xerr, Y = Calc_average_profile_PO3(profSPC_101adx,resolpo3,'PO3_OPM')
avgprofSPC_101noadx_OPM_X, avgprofSPC_101noadx_OPM_Xerr, Y = Calc_average_profile_PO3(profSPC_101noadx,resolpo3,'PO3_OPM')

RSPC_101adx, RSPC_101adxerr = Calc_RDif(avgprofSPC_101adx_O3S_X, avgprofSPC_101adx_OPM_X, avgprofSPC_101adx_Xerr, dimensionpo3 )
RSPC_101noadx, RSPC_101noadxerr = Calc_RDif(avgprofSPC_101noadx_O3S_X, avgprofSPC_101noadx_OPM_X, avgprofSPC_101noadx_Xerr, dimensionpo3 )

Plot_compare_profile_plots_updated(avgprofSPC_101adx_X, avgprofSPC_101adx_Xerr, avgprofSPC_101noadx_X, avgprofSPC_101noadx_Xerr, Y, [-5,5],'SPC1.0%+0.1B ADX and noADX', 'Sonde - OPM O3 Difference (mPa)', ytitlepo3, 'SPC1.0%+0.1B+ADX',  'SPC1.0%+0.1B', totO3SPC_101adx, totO3SPC_101noadx,profSPC_101adx.drop_duplicates(['Sim', 'Team']) , profSPC_101noadx.drop_duplicates(['Sim', 'Team']), 'ADif_SPC101_ADX_PO3')

Plot_compare_profile_plots_updated(RSPC_101adx, RSPC_101adxerr, RSPC_101noadx, RSPC_101noadxerr, Y, [-50,50],'SPC1.0%+0.1B ADX and noADX', 'Sonde - OPM O3 Difference (%)', ytitlepo3, 'SPC1.0%+0.1B+ADX',  'SPC1.0%+0.1B', totO3SPC_101adx, totO3SPC_101noadx, profSPC_101adx.drop_duplicates(['Sim', 'Team']), profSPC_101noadx.drop_duplicates(['Sim', 'Team']), 'RDif_SPC101_ADX_PO3')



print("#SPC 1.0% - 1.0B")

profSPC_11adx = df[(df.ENSCI == 0) & (df.Sol == 1) & (df.Buf == 1.0) & (df.ADX == 1)]
profSPC_11noadx = df[(df.ENSCI == 0) & (df.Sol == 1) & (df.Buf == 1.0) & (df.ADX == 0)]

totO3SPC_11adx = profSPC_11adx.drop_duplicates(['Sim', 'Team']).frac.mean()
totO3SPC_11noadx = profSPC_11noadx.drop_duplicates(['Sim', 'Team']).frac.mean()

avgprofSPC_11adx_X, avgprofSPC_11adx_Xerr, Y = Calc_average_profile_PO3(profSPC_11adx,resolpo3,'ADif_PO3S')
avgprofSPC_11noadx_X, avgprofSPC_11noadx_Xerr, Y = Calc_average_profile_PO3(profSPC_11noadx,resolpo3,'ADif_PO3S')

avgprofSPC_11adx_O3S_X, avgprofSPC_11adx_O3S_Xerr, Y = Calc_average_profile_PO3(profSPC_11adx,resolpo3,'PO3')
avgprofSPC_11noadx_O3S_X, avgprofSPC_11noadx_O3S_Xerr, Y = Calc_average_profile_PO3(profSPC_11noadx,resolpo3,'PO3')
avgprofSPC_11adx_OPM_X, avgprofSPC_11adx_OPM_Xerr, Y = Calc_average_profile_PO3(profSPC_11adx,resolpo3,'PO3_OPM')
avgprofSPC_11noadx_OPM_X, avgprofSPC_11noadx_OPM_Xerr, Y = Calc_average_profile_PO3(profSPC_11noadx,resolpo3,'PO3_OPM')

RSPC_11adx, RSPC_11adxerr = Calc_RDif(avgprofSPC_11adx_O3S_X, avgprofSPC_11adx_OPM_X, avgprofSPC_11adx_Xerr, dimensionpo3 )
RSPC_11noadx, RSPC_11noadxerr = Calc_RDif(avgprofSPC_11noadx_O3S_X, avgprofSPC_11noadx_OPM_X, avgprofSPC_11noadx_Xerr, dimensionpo3 )

Plot_compare_profile_plots_updated(avgprofSPC_11adx_X, avgprofSPC_11adx_Xerr, avgprofSPC_11noadx_X, avgprofSPC_11noadx_Xerr, Y, [-5,5],'SPC1.0%+1.0B ADX and noADX', 'Sonde - OPM O3 Difference (mPa)', ytitlepo3, 'SPC1.0%+1.0B+ADX',  'SPC1.0%+1.0B', totO3SPC_11adx, totO3SPC_11noadx,profSPC_11adx.drop_duplicates(['Sim', 'Team']) , profSPC_11noadx.drop_duplicates(['Sim', 'Team']), 'ADif_SPC11_ADX_PO3')

Plot_compare_profile_plots_updated(RSPC_11adx, RSPC_11adxerr, RSPC_11noadx, RSPC_11noadxerr, Y, [-50,50],'SPC1.0%+1.0B ADX and noADX', 'Sonde - OPM O3 Difference (%)', ytitlepo3, 'SPC1.0%+1.0B+ADX',  'SPC1.0%+1.0B', totO3SPC_11adx, totO3SPC_11noadx, profSPC_11adx.drop_duplicates(['Sim', 'Team']), profSPC_11noadx.drop_duplicates(['Sim', 'Team']), 'RDif_SPC11_ADX_PO3')

print('SPC 0.5% - 0.5B')

profSPC_0505adx = df[(df.ENSCI == 0) & (df.Sol == 0.5) & (df.Buf == 0.5) & (df.ADX == 1)]
profSPC_0505noadx = df[(df.ENSCI == 0) & (df.Sol == 0.5) & (df.Buf == 0.5) & (df.ADX == 0)]

totO3SPC_0505adx = profSPC_0505adx.drop_duplicates(['Sim', 'Team']).frac.mean()
totO3SPC_0505noadx = profSPC_0505noadx.drop_duplicates(['Sim', 'Team']).frac.mean()

avgprofSPC_0505adx_X, avgprofSPC_0505adx_Xerr, Y = Calc_average_profile_PO3(profSPC_0505adx,resolpo3,'ADif_PO3S')
avgprofSPC_0505noadx_X, avgprofSPC_0505noadx_Xerr, Y = Calc_average_profile_PO3(profSPC_0505noadx,resolpo3,'ADif_PO3S')

avgprofSPC_0505adx_O3S_X, avgprofSPC_0505adx_O3S_Xerr, Y = Calc_average_profile_PO3(profSPC_0505adx,resolpo3,'PO3')
avgprofSPC_0505noadx_O3S_X, avgprofSPC_0505noadx_O3S_Xerr, Y = Calc_average_profile_PO3(profSPC_0505noadx,resolpo3,'PO3')
avgprofSPC_0505adx_OPM_X, avgprofSPC_0505adx_OPM_Xerr, Y = Calc_average_profile_PO3(profSPC_0505adx,resolpo3,'PO3_OPM')
avgprofSPC_0505noadx_OPM_X, avgprofSPC_0505noadx_OPM_Xerr, Y = Calc_average_profile_PO3(profSPC_0505noadx,resolpo3,'PO3_OPM')

RSPC_0505adx, RSPC_0505adxerr = Calc_RDif(avgprofSPC_0505adx_O3S_X, avgprofSPC_0505adx_OPM_X, avgprofSPC_0505adx_Xerr, dimensionpo3 )
RSPC_0505noadx, RSPC_0505noadxerr = Calc_RDif(avgprofSPC_0505noadx_O3S_X, avgprofSPC_0505noadx_OPM_X, avgprofSPC_0505noadx_Xerr, dimensionpo3 )

Plot_compare_profile_plots_updated(avgprofSPC_0505adx_X, avgprofSPC_0505adx_Xerr, avgprofSPC_0505noadx_X, avgprofSPC_0505noadx_Xerr, Y, [-5,5],'SPC0.5%+0.5B ADX and noADX', 'Sonde - OPM O3 Difference (mPa)', ytitlepo3, 'SPC0.5%+0.5B+ADX',  'SPC0.5%+0.5B', totO3SPC_0505adx, totO3SPC_0505noadx,profSPC_0505adx.drop_duplicates(['Sim', 'Team']) , profSPC_0505noadx.drop_duplicates(['Sim', 'Team']), 'ADif_SPC0505_ADX_PO3')

Plot_compare_profile_plots_updated(RSPC_0505adx, RSPC_0505adxerr, RSPC_0505noadx, RSPC_0505noadxerr, Y, [-50,50],'SPC0.5%+0.5B ADX and noADX', 'Sonde - OPM O3 Difference (%)', ytitlepo3, 'SPC0.5%+0.5B+ADX',  'SPC0.5%+0.5B', totO3SPC_0505adx, totO3SPC_0505noadx, profSPC_0505adx.drop_duplicates(['Sim', 'Team']), profSPC_0505noadx.drop_duplicates(['Sim', 'Team']), 'RDif_SPC0505_ADX_PO3')



print(' Standard Sonde Operation Merging: SPC 1.0% 1.0B and ENSCI 0.5% - 0.5B')



profSTadx = df[((df.ENSCI == 1) & (df.Sol == 0.5) & (df.Buf == 0.5) & (df.ADX == 1)) | ((df.ENSCI == 0) & (df.Sol == 1.0) & (df.Buf == 1.0) & (df.ADX == 1))]
profSTnoadx = df[((df.ENSCI == 1) & (df.Sol == 0.5) & (df.Buf == 0.5) & (df.ADX == 0)) | ((df.ENSCI == 0) & (df.Sol == 1.0) & (df.Buf == 1.0) & (df.ADX == 0))]

totO3STadx = profSTadx.drop_duplicates(['Sim', 'Team']).frac.mean()
totO3STnoadx = profSTnoadx.drop_duplicates(['Sim', 'Team']).frac.mean()

avgprofSTadx_X, avgprofSTadx_Xerr, Y = Calc_average_profile_PO3(profSTadx,resolpo3,'ADif_PO3S')
avgprofSTnoadx_X, avgprofSTnoadx_Xerr, Y = Calc_average_profile_PO3(profSTnoadx,resolpo3,'ADif_PO3S')

avgprofSTadx_O3S_X, avgprofSTadx_O3S_Xerr, Y = Calc_average_profile_PO3(profSTadx,resolpo3,'PO3')
avgprofSTnoadx_O3S_X, avgprofSTnoadx_O3S_Xerr, Y = Calc_average_profile_PO3(profSTnoadx,resolpo3,'PO3')
avgprofSTadx_OPM_X, avgprofSTadx_OPM_Xerr, Y = Calc_average_profile_PO3(profSTadx,resolpo3,'PO3_OPM')
avgprofSTnoadx_OPM_X, avgprofSTnoadx_OPM_Xerr, Y = Calc_average_profile_PO3(profSTnoadx,resolpo3,'PO3_OPM')

RSTadx, RSTadxerr = Calc_RDif(avgprofSTadx_O3S_X, avgprofSTadx_OPM_X, avgprofSTadx_Xerr, dimensionpo3 )
RSTnoadx, RSTnoadxerr = Calc_RDif(avgprofSTnoadx_O3S_X, avgprofSTnoadx_OPM_X, avgprofSTnoadx_Xerr, dimensionpo3 )

Plot_compare_profile_plots_updated(avgprofSTadx_X, avgprofSTadx_Xerr, avgprofSTnoadx_X, avgprofSTnoadx_Xerr, Y, [-5,5],'Standard Sonde Sol.  ADX and noADX', 'Sonde - OPM O3 Difference (mPa)', ytitlepo3, 'Standard Sonde Sol.+ADX',  'Standard Sonde Sol.', totO3STadx, totO3STnoadx,profSTadx.drop_duplicates(['Sim', 'Team']) , profSTnoadx.drop_duplicates(['Sim', 'Team']), 'ADif_StandardSolutions_ADX_PO3')

Plot_compare_profile_plots_updated(RSTadx, RSTadxerr, RSTnoadx, RSTnoadxerr, Y, [-50,50],'Standard Sonde Sol. ADX and noADX', 'Sonde - OPM O3 Difference (%)', ytitlepo3, 'Standard Sonde Sol.+ADX',  'Standard Sonde Sol.', totO3STadx, totO3STnoadx, profSTadx.drop_duplicates(['Sim', 'Team']), profSTnoadx.drop_duplicates(['Sim', 'Team']), 'RDif_StandardSolutions_ADX_PO3')







# avgprofENSCI_201adx_X, avgprofENSCI_201adx_Xerr, Y = Calc_average_profile(profENSCI_201adx,resol,'ADif_PO3S')
# avgprofENSCI_201noadx_X, avgprofENSCI_201noadx_Xerr, Y = Calc_average_profile(profENSCI_201noadx,resol,'ADif_PO3S')

# avgprofENSCI_201adx_O3S_X, avgprofENSCI_201adx_O3S_Xerr, Y = Calc_average_profile(profENSCI_201adx,resol,'PO3')
# avgprofENSCI_201noadx_O3S_X, avgprofENSCI_201noadx_O3S_Xerr, Y = Calc_average_profile(profENSCI_201noadx,resol,'PO3')
# avgprofENSCI_201adx_OPM_X, avgprofENSCI_201adx_OPM_Xerr, Y = Calc_average_profile(profENSCI_201adx,resol,'PO3_OPM')
# avgprofENSCI_201noadx_OPM_X, avgprofENSCI_201noadx_OPM_Xerr, Y = Calc_average_profile(profENSCI_201noadx,resol,'PO3_OPM')

# RENSCI_201adx, RENSCI_201adxerr = Calc_RDif(avgprofENSCI_201adx_O3S_X, avgprofENSCI_201adx_OPM_X, avgprofENSCI_201adx_Xerr, dimension )
# RENSCI_201noadx, RENSCI_201noadxerr = Calc_RDif(avgprofENSCI_201noadx_O3S_X, avgprofENSCI_201noadx_OPM_X, avgprofENSCI_201noadx_Xerr, dimension )

# Plot_compare_profile_plots_updated(avgprofENSCI_201adx_X, avgprofENSCI_201adx_Xerr, avgprofENSCI_201noadx_X, avgprofENSCI_201noadx_Xerr, Y, [-3,3],'ENSCI2.0%+0.1B ADX and noADX', 'Sonde - OPM O3 Difference (mPa)', ytitle, 'ENSCI2.0%+0.1B+ADX',  'ENSCI2.0%+0.1B', totO3ENSCI_201adx, totO3ENSCI_201noadx,profENSCI_201adx.drop_duplicates(['Sim', 'Team']) , profENSCI_201noadx.drop_duplicates(['Sim', 'Team']), 'ADif_ENSCI201_ADX')

# Plot_compare_profile_plots_updated(RENSCI_201adx, RENSCI_201adxerr, RENSCI_201noadx, RENSCI_201noadxerr, Y, [-40,40],'ENSCI2.0%+0.1B ADX and noADX', 'Sonde - OPM O3 Difference (%)', ytitle, 'ENSCI2.0%+0.1B+ADX',  'ENSCI2.0%+0.1B', totO3ENSCI_201adx, totO3ENSCI_201noadx, profENSCI_201adx.drop_duplicates(['Sim', 'Team']), profENSCI_201noadx.drop_duplicates(['Sim', 'Team']), 'RDif_ENSCI201_ADX')
