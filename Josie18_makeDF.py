import pandas as pd
import numpy as np
import re
import glob
import math
from math import log

# Read the metadata file
dfmeta = pd.read_csv("/home/poyraden/Josie18/Josie18_MetaData.csv")

# Path to all Josie18 simulation files

allFiles = glob.glob("/home/poyraden/Josie18/Files/Si*/*.O3R")
list_data = []

#Some declarations

columnString = "Tact Tsim Pair Tair Tinlet IM TPint TPext PFcor I_Pump PO3 VMRO3 PO3_OPM VMRO3_OPM ADif_PO3S RDif_PO3S Z"
columnStr = columnString.split(" ")


column_metaString = "Year Sim ENSCI Team Code Flow IB1 Cor Sol Buf ADX"
columnMeta = column_metaString.split(" ")

#**********************************************
# Main loop to merge all data sets
#**********************************************
for filename in allFiles:
    file = open(filename,'r')
    # Get the participant information from the name of the file
    tmp_team = filename.split("/")[6]
    header_team =( tmp_team.split("_")[2]).split(".")[0]
    file.readline()
    file.readline()
    header_part = int(header_team)
    header_sim = int(file.readline().split()[2])
    file.readline()
    file.readline()
    header_PFunc = float(file.readline().split()[1])
    header_PFcor = float(file.readline().split()[1])
    file.readline()
    header_IB1 = float(file.readline().split()[1])
    
    df = pd.read_csv(filename, sep = "\t", engine="python", skiprows=12, names=columnStr)

     # Add the header information to the main df
    
    df = df.join(pd.DataFrame(
        [[header_part,  header_sim, header_PFunc, header_PFcor, header_IB1 ]], 
        index=df.index, 
        columns=['Header_Team', 'Header_Sim', 'Header_PFunc', 'Header_PFcor', 'Header_IB1']
    ))
 # Get the index of the metadata that corresponds to this Simulation Number and Participant (Team)
    
    select_indicesTeam = list(np.where(dfmeta["Team"] == df['Header_Team'][0]))[0]
    select_indicesSim = list(np.where(dfmeta["Sim"] == df['Header_Sim'][0]))[0]
    common = [i for i in select_indicesTeam if i in select_indicesSim]
    index_common = common[0]  

     ## The index of the metadata that has the information of this simulation = index_common
    #  assign this row into a list
    
    list_md = dfmeta.iloc[index_common,:].tolist()
    #print(list_md)
    
    ## Add  metadata to the main df
    df = df.join(pd.DataFrame(
        [list_md],
        index = df.index,
        columns=columnMeta
    ))
    
    # I think I need to add the total profile calculation 
    # Calc total O3 
    
    dfpair_tmp = df.sort_values(by = 'Pair', ascending=False)
    dfpo3_tmp = df.sort_values(by = 'PO3', ascending=False)
    dfpo3opm_tmp = df.sort_values(by = 'PO3_OPM', ascending=False)
    
    dfpair = dfpair_tmp[dfpair_tmp.Pair >= 0 ]
    dfpair = dfpair_tmp[dfpair_tmp.PO3 > 0]
    dfpo3 = dfpo3_tmp[dfpo3_tmp.Pair >= 0 ]
    dfpo3 = dfpo3_tmp[dfpo3_tmp.PO3 > 0 ]
    dfpo3opm = dfpo3opm_tmp[dfpo3opm_tmp.Pair >= 0 ]
    dfpo3opm = dfpo3opm_tmp[dfpo3opm_tmp.PO3 > 0 ]
    
   
    ## the for loop is very slow :/
    O3_tot = 0.0
    O3_tot_opm = 0.0
    #idx=where(pres ge 0 and oz gt 0)
    for i in range(len(dfpair)-2):
        O3_tot = O3_tot + 3.9449 * (dfpo3.iloc[i]['PO3'] + dfpo3.iloc[i+1]['PO3'])* np.log(dfpair.iloc[i]['Pair']/dfpair.iloc[i+1]['Pair'])
        O3_tot_opm = O3_tot_opm + 3.9449 *(dfpo3opm.iloc[i]['PO3_OPM'] + dfpo3opm.iloc[i+1]['PO3_OPM'])* np.log(dfpair.iloc[i]['Pair']/dfpair.iloc[i+1]['Pair'])
    
    Adif = O3_tot - O3_tot_opm
    Rdif = 100.0 * (O3_tot - O3_tot_opm)/O3_tot_opm
    frac = O3_tot/O3_tot_opm
    
    ## now add these to the df
    print("tot O3 is")
    print(O3_tot)
    df = df.join(pd.DataFrame(
        [[O3_tot,  O3_tot_opm ,Adif , Rdif, frac ]], 
        index=df.index, 
        columns=['O3S', 'OPM', 'ADif', 'RDif', 'frac']
    ))
    
    
    
    list_data.append(df) 
    #  end of the allfiles loop    #
     
# Merging all the data files to df

df = pd.concat(list_data,ignore_index=True)
df.to_csv("/home/poyraden/Josie18/Josie18_Data.csv")
    
    





